from pathlib import Path

ROOT = Path("dist")


def main() -> None:
    path = ROOT / "index.html"
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")

    # ホームのWHY AXIS BAY内にある犯罪数表示だけを更新します。
    # 文字サイズやHTML構造、CSSは変更しません。
    text = text.replace("<strong>約30</strong><span>犯罪ルート</span>", "<strong>34</strong><span>犯罪コンテンツ</span>")
    text = text.replace("<strong>約３０</strong><span>犯罪ルート</span>", "<strong>34</strong><span>犯罪コンテンツ</span>")
    text = text.replace("<strong>３０</strong><span>犯罪ルート</span>", "<strong>34</strong><span>犯罪コンテンツ</span>")
    text = text.replace("<strong>34</strong><span>犯罪ルート</span>", "<strong>34</strong><span>犯罪コンテンツ</span>")

    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
