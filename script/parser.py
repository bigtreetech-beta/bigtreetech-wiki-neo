import re
import hashlib

def normalize(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def get_block_key(content: str) -> str:
    return hashlib.md5(normalize(content).encode("utf-8")).hexdigest()[:16]

def parse_blocks(md_text: str):
    lines = md_text.splitlines(keepends=True)
    blocks = []
    i = 0

    block_config = [
        (lambda line: line.strip().startswith("<div"), lambda line: "</div>" in line),
        (lambda line: line.strip().startswith("<Tabs"), lambda line: "</Tabs>" in line),
        (lambda line: line.strip().startswith("<ImageView"), lambda line: "/>" in line),
        (lambda line: line.strip().startswith(":::"),  lambda line: line.strip() == ":::"),
        (lambda line: line.strip().startswith("```"),  lambda line: line.strip() == "```")
    ]
    
    while i < len(lines):
        line = lines[i]
        
        is_range_matched = False
        for start_cond, end_cond in block_config:
            if start_cond(line):
                # inline read
                buf = [line]
                if end_cond(line):
                    blocks.append(line)
                    i += 1
                    is_range_matched = True
                    break

                i += 1

                while i < len(lines):
                    buf.append(lines[i])
                    if end_cond(lines[i]):
                        break
                    i += 1
                blocks.append("".join(buf))
                i += 1
                is_range_matched = True
                break
                
        if is_range_matched:
            continue

        # html block
        if re.match(r'^\s*<[a-zA-Z]', line):
            buf = [line]
            if "/>" in line or (re.search(r'</\w+>', line)):
                blocks.append(line)
                i += 1
                continue
            i += 1
            while i < len(lines):
                buf.append(lines[i])
                if ">" in lines[i]:
                    break
                i += 1
            blocks.append("".join(buf))
            i += 1
            continue

        # table
        if line.strip().startswith("|"):
            buf = []
            while i < len(lines) and (lines[i].strip().startswith("|") or lines[i].strip() == ""):
                if lines[i].strip() == "": break
                buf.append(lines[i])
                i += 1
            blocks.append("".join(buf))
            continue

        # title
        if line.startswith("#"):
            blocks.append(line)
            i += 1
            continue

        # empty line
        if line.strip() == "":
            i += 1
            continue

        # normal block
        buf = []
        while i < len(lines):
            is_special_start = (
                line.startswith("#") or 
                line.startswith("|") or 
                re.match(r'^\s*<[a-zA-Z]', line) or 
                any(start_cond(line) for start_cond, _ in block_config)
            )
            
            if line.strip() == "" or is_special_start:
                break
                
            buf.append(lines[i])
            i += 1
            if i < len(lines): 
                line = lines[i]
        
        if buf:
            blocks.append("".join(buf))

    return [b for b in blocks if b.strip()]
