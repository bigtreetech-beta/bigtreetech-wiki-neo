import os
import re
from pathlib import Path

def sync_docs(runner_src_dir, runner_i18n_base):
    if not runner_src_dir.exists():
        print(f"[err] {runner_src_dir}")
        return

    for md_file in runner_src_dir.rglob('*'):
        if md_file.suffix not in ['.md', '.mdx']:
            continue

        relative_path = md_file.relative_to(runner_src_dir)
        target_path = runner_i18n_base / relative_path

        # check file exist 
        if target_path.exists():
            print(f"[SKIPPED] {relative_path}")
            continue

        content = md_file.read_text(encoding='utf-8')

        # find @site path 
        file_dir = str(relative_path.parent).replace('\\', '/')
        # check if is root dir. avoid `@site/docs/.`
        path_suffix = f"/{file_dir}" if file_dir != "." else ""
        site_path_prefix = f"@site/docs{path_suffix}"

        # replace
        # jsx "require('./img/xxx.png') -> require('@site/docs/xxx/img/xxx.png')"
        new_content = re.sub(
            r"require\('\./img/(.*?)'\)", 
            f"require('{site_path_prefix}/img/\\1')", 
            content
        )
        
        # markdown "![](./img/xxx.png) -> ![](@site/docs/xxx/img/xxx.png)"
        new_content = re.sub(
            r"!\[(.*?)\]\(\./img/(.*?)\)", 
            f"![\\1]({site_path_prefix}/img/\\2)", 
            new_content
        )

        # write file 
        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(new_content, encoding='utf-8')
        print(f"[SYNCED] {relative_path}")

if __name__ == "__main__":

    lang_config = ["en"]
    src_docs = Path("docs")
    
    for current_lang in lang_config:
        src_i18n = Path(f"i18n/{current_lang}/docusaurus-plugin-content-docs/current")
        sync_docs(src_docs, src_i18n)
