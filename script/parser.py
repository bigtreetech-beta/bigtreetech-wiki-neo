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
    
    while i < len(lines):
        line = lines[i]
        
        if line.strip().startswith(":::"):
            buf = [line]
            i += 1
            while i < len(lines):
                buf.append(lines[i])
                if lines[i].strip() == ":::":
                    break
                i += 1
            blocks.append("".join(buf))
            i += 1
            continue

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

        if line.strip().startswith("|"):
            buf = []
            while i < len(lines) and (lines[i].strip().startswith("|") or lines[i].strip() == ""):
                if lines[i].strip() == "": break
                buf.append(lines[i])
                i += 1

            blocks.append("".join(buf))
            continue

        if line.startswith("#"):

            blocks.append(line)
            i += 1
            continue

        if line.strip() == "":
            i += 1
            continue

        buf = []
        while i < len(lines) and line.strip() != "" and not line.startswith("#") and not line.startswith("|") and not line.strip().startswith(":::"):
            buf.append(lines[i])
            i += 1
            if i < len(lines): line = lines[i]
        
        if buf:
            blocks.append("".join(buf))

    return [b for b in blocks if b.strip()]
