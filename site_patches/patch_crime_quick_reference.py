from pathlib import Path
import re

ROOT = Path("dist")
CRIME_QUICK_REFERENCE_URL = "https://docs.google.com/document/d/1ri9PRzSva2BWucBmw-S4gyxwFa3CJ0I_PoTCZbKqnXk/edit?pli=1&tab=t.5vrw1uc9rehi"
LINK_TEXT = "犯罪早見表を開く"


def clean_anchor_attrs(attrs: str) -> str:
    attrs = re.sub(r'\s+href=("[^"]*"|\'[^\']*\'|[^\s>]+)', '', attrs)
    attrs = re.sub(r'\s+target=("[^"]*"|\'[^\']*\'|[^\s>]+)', '', attrs)
    attrs = re.sub(r'\s+rel=("[^"]*"|\'[^\']*\'|[^\s>]+)', '', attrs)
    attrs = re.sub(r'\s+', ' ', attrs).strip()
    return f" {attrs}" if attrs else ""


def patch_file(path: Path) -> bool:
    if not path.exists():
        return False

    text = path.read_text(encoding="utf-8")
    original = text

    # 既存の「犯罪早見表を開く」ボタン/リンクの見た目は維持し、リンク先だけをGoogleドキュメントへ変更します。
    def replace_anchor(match: re.Match) -> str:
        attrs = clean_anchor_attrs(match.group(1))
        inner = match.group(2)
        return f'<a{attrs} href="{CRIME_QUICK_REFERENCE_URL}" target="_blank" rel="noopener noreferrer">{inner}</a>'

    text = re.sub(
        r'<a\b([^>]*)>([^<]*犯罪早見表を開く[^<]*)</a>',
        replace_anchor,
        text,
        flags=re.IGNORECASE,
    )

    # 念のため、リンク先がプレースホルダーや古いURLで残っている場合も置換します。
    text = text.replace("CRIME_QUICK_REFERENCE_URL_HERE", CRIME_QUICK_REFERENCE_URL)
    text = text.replace("犯罪早見表_URL_HERE", CRIME_QUICK_REFERENCE_URL)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> None:
    # ルールセンター下部の「犯罪早見表を開く」を主対象にします。
    patch_file(ROOT / "rules.html")


if __name__ == "__main__":
    main()
