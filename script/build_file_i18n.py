import argparse
import logging
from pathlib import Path
from sync_to_i18n import rebuild_file

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%H:%M:%S'
)
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i",
        "--input",
        nargs="+",
        required=True,
        help="markdown/mdx files under docs folder"
    )
    args = parser.parse_args()

    # Configuration
    DOCS_FOLDER = Path("docs").resolve()
    I18N_FOLDER = Path("i18n")
    # build_middleware_base = Path("i18n_middleware")
    build_middleware_base = Path("i18n")
    lang_list = ["en"]

    md_files = []

    for f in args.input:
        path = Path(f).resolve()
        
        if path.suffix not in [".md", ".mdx"]:
            raise ValueError(f"Invalid file type: {path.suffix}, only .md/.mdx allowed")

        try:
            rel = path.relative_to(DOCS_FOLDER)
        except ValueError:
            raise ValueError(f"Invalid input: {path} is not under docs/")

        md_files.append(path)

    for current_lang in lang_list:

        output_root = Path(
            I18N_FOLDER / current_lang / "docusaurus-plugin-content-docs" / "current"
        )

        for md_file in md_files:
            rel_path = md_file.relative_to(DOCS_FOLDER)

            # toml_file = build_middleware_base / current_lang / rel_path.with_suffix(".toml")
            toml_file = build_middleware_base / current_lang / "docusaurus-plugin-content-docs/current" / rel_path.with_suffix(".toml")
            target_md = output_root / rel_path
            
            if not md_file.exists():
                logger.warning(f"Skip missing file: {md_file}")
                continue

            try:
                rebuild_file(md_file, toml_file, target_md)
            except Exception as e:
                logger.error(f"Error rebuilding {md_file}: {e}")

if __name__ == "__main__":
    main()
