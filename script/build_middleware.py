import json
import re
import tomlkit
import hashlib
import logging
from pathlib import Path, PurePosixPath
from parser import parse_blocks, get_block_key

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def get_file_sha256(path: Path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_existing_toml(toml_path: Path):
    mapping = {}
    if toml_path.exists():
        try:
            with open(toml_path, "r", encoding="utf-8") as f:
                data = tomlkit.parse(f.read())
                for block in data.get("block", []):
                    if "key" in block and "translate" in block:
                        mapping[str(block["key"])] = str(block["translate"])
            logger.debug(f"Loaded {len(mapping)} existing translations from {toml_path.name}")
        except Exception as e:
            logger.warning(f"Could not read existing file {toml_path}: {e}")
    return mapping

def process_jsx_paths(text: str, md_path: Path):
    try:
        # get file .md or .mdx relative directory to docs
        md_rel_dir = PurePosixPath(md_path.relative_to("docs").parent)
    except ValueError:
        md_rel_dir = PurePosixPath(".")

    def replace(match):
        img_path = match.group(1)

        # skip
        if img_path.startswith(("http", "@site", "/")):
            return match.group(0)

        full_path = (md_rel_dir / img_path).as_posix()
        
        normalized = full_path.replace('./', '')

        return f"require('@site/docs/{normalized}').default"

    return re.sub(
        r"require\(['\"](.+?)['\"]\)(?:\.default)?",
        replace,
        text
    )

def process_svg_import_paths(text: str, md_path: Path):
    try:
        # docs relative directory 
        md_rel_dir = PurePosixPath(md_path.relative_to("docs").parent)
    except ValueError:
        md_rel_dir = PurePosixPath(".")

    def replace(match):
        prefix = match.group(1)   # import xxx from
        quote = match.group(2)    # " or '
        img_path = match.group(3) # ./img/xxx.svg

        # only relative path
        if img_path.startswith(("http", "@site", "/")):
            return match.group(0)

        full_path = (md_rel_dir / img_path).as_posix()

        # remove ./ prefix
        normalized = full_path.replace("./", "")

        return f'{prefix}"@site/docs/{normalized}"'

    return re.sub(
        r'(import\s+[\w{}\s,*]+\s+from\s+)(["\'])(.+?)\2',
        replace,
        text
    )

def process_markdown_image_paths(text: str, md_path: Path):
    try:
        md_rel_dir = PurePosixPath(md_path.relative_to("docs").parent)
    except ValueError:
        md_rel_dir = PurePosixPath(".")

    def replace(match):
        alt_text = match.group(1)
        img_path = match.group(2)

        if img_path.startswith(("http", "@site", "/")):
            return match.group(0)

        full_path = (md_rel_dir / img_path).as_posix()

        normalized = full_path.replace("./", "")

        return f"![{alt_text}](@site/docs/{normalized})"

    return re.sub(
        r"!\[(.*?)\]\((.+?)\)",
        replace,
        text
    )

def block_control(text, md_path, is_jsx=False):
    
    front_matter_pattern = r"^---\s*\n[\s\S]*?\n---\s*"
    if re.match(front_matter_pattern, text.strip()):
        return f"{text}"
    
    # import lib
    external_import_re = r"^import\s+.*?\s+from\s+['\"]([^.'].*?)['\"];?$"
    lines = text.strip().splitlines()
    if lines and all(re.match(external_import_re, line.strip()) or not line.strip() for line in lines):
        return text
    
    comment_block_re = r"^\{\/\*\s*.*?\s*\*\/\s*\}$"
    if lines and all(re.match(comment_block_re, line.strip()) or not line.strip() for line in lines):
        return text

    # svg improt
    svg_import = r'^import\s+[A-Za-z_$][\w$]*\s+from\s+["\']\.\/img\/[^"\']+\.svg["\'];?$'
    if any(re.match(svg_import, line.strip()) for line in lines):
        return process_svg_import_paths(text, md_path)
    
    # image
    if is_jsx or ("<" in text and "require(" in text):
        return process_jsx_paths(text, md_path)

    if "<" in text and ("src=" in text or "img=" in text):
        return process_jsx_paths(text, md_path)
    
    image_path_pattern = r"!\[.*?\]\((.*?)\)"
    if re.findall(image_path_pattern, text):
        return process_markdown_image_paths(text, md_path)
    
    # text block can be translate
    # if text.endswith('\n'):
    #     return f"{text.rstrip()} [translated]\n"
    
    # fail back return text
    return f"{text}"

def build_toml(blocks, existing_translations, md_path):
    doc = tomlkit.document()
    doc.add("metadata", {}) 
    blocks_array = tomlkit.aot() 
    
    for b in blocks:
        key = get_block_key(b)
        if key in existing_translations:
            translated = existing_translations[key]
        else:
            # use block control to the post process
            translated = block_control(b, md_path)

        table = tomlkit.table()
        table.add("key", key)
        for field, content in [("origin", b), ("translate", translated)]:
            if "\n" in content:
                table.add(field, tomlkit.string(f"\n{content}", multiline=True, literal=True))
            else:
                table.add(field, f"\n{content}")
        blocks_array.append(table)

    doc.add("block", blocks_array)
    return tomlkit.dumps(doc)


def build_file(md_path: Path, local_root: str, cache: dict):
    rel_path = str(md_path)
    new_file_hash = get_file_sha256(md_path)
    
    # Hash check for incremental builds
    if cache.get(rel_path) == new_file_hash:
        logger.info(f"Skipping (unchanged): {md_path.name}")
        return

    logger.info(f"Processing: {rel_path}")
    
    out_path = Path(local_root) / md_path.relative_to("docs").with_suffix(".toml")
    existing_translations = load_existing_toml(out_path)
    
    try:
        raw_content = md_path.read_text(encoding="utf-8")
        blocks = parse_blocks(raw_content)
        
        toml_string = build_toml(blocks, existing_translations, md_path)
        
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(toml_string, encoding="utf-8")
        logger.info(f"Successfully wrote -> {out_path}")
        
        cache[rel_path] = new_file_hash
    except Exception as e:
        logger.error(f"Error processing {rel_path}: {e}")

def main():
    build_middleware_base = "i18n_middleware"
    build_cache_base = ".build_cache"
    lang_list = ["en"]

    logger.info("Starting build process...")
    
    for current_lang in list(lang_list):
        logger.info(f"build {current_lang}")
        build_cache = f"{build_cache_base}/cache_{current_lang}.json"
        build_middleware = f"{build_middleware_base}/{current_lang}"

        cache_data = {}
        if Path(build_cache).exists():
            try:
                cache_data = json.loads(Path(build_cache).read_text())
                logger.info(f"Loaded cache with {len(cache_data)} entries")
            except Exception:
                logger.error("Failed to read cache; performing full build")

        Path(build_middleware).mkdir(parents=True, exist_ok=True)

        md_files = list(Path("docs").rglob("*.md"))
        logger.info(f"Found {len(md_files)} Markdown files")

        for md_file in md_files:
            build_file(md_file, build_middleware, cache_data)
            
        try:
            Path(build_cache_base).mkdir(parents=True, exist_ok=True)
            Path(build_cache).write_text(json.dumps(cache_data, indent=2))
            logger.info("Build complete. Cache updated.")
        except Exception as e:
            logger.error(f"Failed to save cache file: {e}")

if __name__ == "__main__":
    main()
