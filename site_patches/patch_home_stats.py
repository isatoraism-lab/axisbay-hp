from pathlib import Path

ROOT = Path("dist")


def main() -> None:
    path = ROOT / "index.html"
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")

    # ホームの実績表示を更新。HTML構造やCSSは変更せず、表示テキストだけ差し替えます。
    replacements = {
        "約30": "34",
        "約３０": "34",
        "３０": "34",
        "30": "34",
        "犯罪ルート": "犯罪コンテンツ",
    }
    for before, after in replacements.items():
        text = text.replace(before, after)

    # 念のため、全角数字指定にも対応します。
    text = text.replace("３４", "34")

    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
