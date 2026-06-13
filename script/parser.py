import re
import hashlib

def normalize(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def get_block_key(content: str) -> str:
    return hashlib.sha256(normalize(content).encode("utf-8")).hexdigest()[:16]

def parse_blocks(md_text: str):
    lines = md_text.splitlines(keepends=True)
    blocks = []
    i = 0

    block_config = [
        (lambda line: line.strip().startswith("<div"), lambda line: "</div>" in line, True),
        (lambda line: line.strip().startswith("<Tabs"), lambda line: "</Tabs>" in line, True),
        (lambda line: line.strip().startswith("<ImageView"), lambda line: "/>" in line, False),
        (lambda line: line.strip().startswith(":::"),  lambda line: line.strip() == ":::", False),
        (lambda line: line.strip().startswith("```"),  lambda line: line.strip() == "```", False)
    ]

    def handle_structured(i):
        line = lines[i]

        for start_cond, end_cond, *rest in block_config:
            is_nested = rest[0] if rest else False

            if start_cond(line):

                if is_nested:
                    buf = [line]
                    i += 1
                    depth = 1

                    while i < len(lines):
                        cur = lines[i]
                        buf.append(cur)

                        if start_cond(cur):
                            depth += 1

                        if end_cond(cur):
                            depth -= 1

                            if depth == 0:
                                i += 1
                                break

                        i += 1

                    blocks.append("".join(buf))
                    return i

                buf = [line]
                i += 1

                if end_cond(line):
                    blocks.append(line)
                    return i

                while i < len(lines):
                    buf.append(lines[i])

                    if end_cond(lines[i]):
                        i += 1
                        break

                    i += 1

                blocks.append("".join(buf))
                return i

        return None

    def handle_html(i):
        line = lines[i]
        if not re.match(r'^\s*<[a-zA-Z]', line):
            return None

        buf = [line]
        i += 1

        if "/>" in line or re.search(r'</\w+>', line):
            blocks.append(line)
            return i

        while i < len(lines):
            buf.append(lines[i])
            if ">" in lines[i]:
                i += 1
                break
            i += 1

        blocks.append("".join(buf))
        return i

    def handle_table(i):
        line = lines[i]
        if not line.strip().startswith("|"):
            return None

        buf = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            if lines[i].strip() == "":
                break
            buf.append(lines[i])
            i += 1

        blocks.append("".join(buf))
        return i

    def handle_title(i):
        if lines[i].startswith("#"):
            blocks.append(lines[i])
            return i + 1
        return None

    def handle_empty(i):
        if lines[i].strip() == "":
            return i + 1
        return None

    def handle_normal(i):
        buf = []

        while i < len(lines):
            line = lines[i]

            is_special = (
                line.startswith("#")
                or line.startswith("|")
                or re.match(r'^\s*<[a-zA-Z]', line)
                or any(start_cond(line) for start_cond, _, _ in block_config)
            )

            if line.strip() == "" or is_special:
                break

            buf.append(line)
            i += 1

        if buf:
            blocks.append("".join(buf))

        return i

    handlers = [
        handle_structured,
        handle_html,
        handle_table,
        handle_title,
        handle_empty,
        handle_normal,
    ]

    while i < len(lines):
        for h in handlers:
            new_i = h(i)
            if new_i is not None:
                i = new_i
                break

    return [b for b in blocks if b.strip()]
