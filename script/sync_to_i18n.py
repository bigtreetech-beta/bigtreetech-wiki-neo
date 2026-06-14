import tomlkit
import shutil
import logging
from pathlib import Path
from parser import parse_blocks, get_block_key

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def load_translation_map(toml_path: Path):
    mapping = {}
    if toml_path.exists():
        try:
            data = tomlkit.parse(toml_path.read_text(encoding="utf-8"))
            for block in data.get("block", []):
                if "key" in block and "translate" in block:
                    # Clean up common TOML string artifacts if necessary
                    content = str(block["translate"])
                    mapping[str(block["key"])] = content
        except Exception as e:
            logger.error(f"Failed to parse TOML {toml_path}: {e}")
    return mapping

def rebuild_file(md_path: Path, toml_path: Path, output_path: Path):
    if not toml_path.exists():
        logger.warning(f"No translation found for {md_path}, copying original.")
        shutil.copy(md_path, output_path)
        return

    translations = load_translation_map(toml_path)
    raw_content = md_path.read_text(encoding="utf-8")
    
    blocks = parse_blocks(raw_content)
    
    translated_md = raw_content

    for block in reversed(blocks):
        key = get_block_key(block)
        if key in translations:
            translated_text = translations[key]
            translated_md = translated_md.replace(block, translated_text)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(translated_md, encoding="utf-8")
    logger.info(f"Reconstructed: {output_path}")

def main():
    # Configuration
    DOCS_FOLDER = Path("docs")
    I18N_FOLDER = Path("i18n")
    build_middleware_base = Path("i18n_middleware")
    lang_list = ["en"]
    
    for current_lang in list(lang_list):

        output_root = Path(I18N_FOLDER / current_lang / "docusaurus-plugin-content-docs" / "current")
        
        md_files = list(DOCS_FOLDER.rglob("*.md")) + list(DOCS_FOLDER.rglob("*.mdx"))

        for md_file in md_files:
            rel_path = md_file.relative_to(DOCS_FOLDER)
            toml_file = build_middleware_base / current_lang / rel_path.with_suffix(".toml")
            target_md = output_root / rel_path

            try:
                rebuild_file(md_file, toml_file, target_md)
            except Exception as e:
                logger.error(f"Error rebuilding {md_file}: {e}")

if __name__ == "__main__":
    main()
