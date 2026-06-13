import json
import argparse
import logging
from pathlib import Path
from build_middleware import build_file

# Configure logging
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
        help="Markdown files to build"
    )

    args = parser.parse_args()

    DOCS_FOLDER = Path("docs").resolve()

    for f in args.input:
        file_path = Path(f).resolve()

        if file_path.suffix not in [".md", ".mdx"]:
            raise ValueError(f"Invalid file type: {file_path.suffix}, only .md/.mdx allowed")

        try:
            file_path.relative_to(DOCS_FOLDER)
        except ValueError:
            raise ValueError(f"Invalid input: {file_path} is not under docs/")

    # build_middleware_base = "i18n_middleware"
    build_middleware_base = "i18n"
    build_cache_base = ".build_cache"
    lang_list = ["en"]

    logger.info("Starting build process...")

    for current_lang in lang_list:
        logger.info(f"build {current_lang}")

        build_cache = f"{build_cache_base}/cache_{current_lang}.json"
        # build_middleware = f"{build_middleware_base}/{current_lang}"
        build_middleware = f"{build_middleware_base}/{current_lang}/docusaurus-plugin-content-docs/current"

        cache_data = {}

        if Path(build_cache).exists():
            try:
                cache_data = json.loads(Path(build_cache).read_text())
                logger.info(f"Loaded cache with {len(cache_data)} entries")
            except Exception:
                logger.error("Failed to read cache; performing full build")

        Path(build_middleware).mkdir(parents=True, exist_ok=True)

        md_files = [
            Path(f)
            for f in args.input
            if f.endswith((".md", ".mdx"))
        ]

        logger.info(f"Building {len(md_files)} files")

        for md_file in md_files:
            if not md_file.exists():
                logger.warning(f"Skip missing file: {md_file}")
                continue

            build_file(md_file, build_middleware, cache_data)

        try:
            Path(build_cache_base).mkdir(parents=True, exist_ok=True)
            Path(build_cache).write_text(json.dumps(cache_data, indent=2))
            logger.info("Build complete. Cache updated.")
        except Exception as e:
            logger.error(f"Failed to save cache file: {e}")

if __name__ == "__main__":
    main()
