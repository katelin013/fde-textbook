"""textbook/ 章節同步到 docs/ 時的格式轉換工具。

用法：從 FDE_PROJECT 本地的 textbook/ 複製章節到本 repo 的 docs/ 後執行：
    python3 scripts/convert_details.py docs/ch*.md
把原始的 <details><summary> HTML 摺疊區塊轉成 MkDocs Material 的 ??? note 語法。
已轉換過的檔案不受影響（冪等）。
"""
import re
import sys
from pathlib import Path

def convert(text: str) -> str:
    pattern = re.compile(
        r'<details><summary>(.*?)</summary>\n(.*?)</details>',
        re.DOTALL,
    )
    def repl(m):
        title, body = m.group(1), m.group(2).strip('\n')
        indented = '\n'.join(
            ('    ' + line) if line.strip() else '' for line in body.split('\n')
        )
        return f'??? note "{title}"\n\n{indented}'
    return pattern.sub(repl, text)

for path in sys.argv[1:]:
    p = Path(path)
    original = p.read_text(encoding='utf-8')
    converted = convert(original)
    if converted != original:
        p.write_text(converted, encoding='utf-8')
        print(f'converted: {p.name}')
    else:
        print(f'no change: {p.name}')
