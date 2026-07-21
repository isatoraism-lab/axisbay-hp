from pathlib import Path
import re

ROOT = Path("dist")
CRIME_QUICK_REFERENCE_URL = "https://docs.google.com/document/d/1ri9PRzSva2BWucBmw-S4gyxwFa3CJ0I_PoTCZbKqnXk/edit?pli=1&tab=t.5vrw1uc9rehi"


def main() -> None:
    config = ROOT / "assets/js/config.js"
    if not config.exists():
        return

    text = config.read_text(encoding="utf-8")
    original = text

    # site.js は data-config-link="crimequick" のクリック時に AXIS_BAY_CONFIG.crimequickUrl を参照するため、
    # href だけではなく config.js 側にもURLを必ず設定します。
    if "crimequickUrl" in text:
        text = re.sub(
            r'(crimequickUrl\s*:\s*)(["\'])(.*?)(["\'])',
            lambda m: f'{m.group(1)}"{CRIME_QUICK_REFERENCE_URL}"',
            text,
        )
    else:
        # 念のため、古いconfigに項目が存在しない場合は xUrl の直後へ追加します。
        inserted = re.sub(
            r'(xUrl\s*:\s*["\'][^"\']*["\']\s*,?)',
            lambda m: f'{m.group(1)}\n  crimequickUrl: "{CRIME_QUICK_REFERENCE_URL}",',
            text,
            count=1,
        )
        if inserted != text:
            text = inserted
        else:
            text = re.sub(
                r'(\{\s*)',
                lambda m: f'{m.group(1)}\n  crimequickUrl: "{CRIME_QUICK_REFERENCE_URL}",',
                text,
                count=1,
            )

    # プレースホルダーが文字列として残るパターンにも対応します。
    text = text.replace("CRIME_QUICK_URL_HERE", CRIME_QUICK_REFERENCE_URL)
    text = text.replace("CRIME_QUICK_REFERENCE_URL_HERE", CRIME_QUICK_REFERENCE_URL)
    text = text.replace("犯罪早見表_URL_HERE", CRIME_QUICK_REFERENCE_URL)

    if text != original:
        config.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
