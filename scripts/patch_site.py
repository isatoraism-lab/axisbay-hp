from pathlib import Path
import re

DISCORD_URL = "https://discord.gg/dCHCAY6DbZ"
X_URL = "https://x.com/AxisBay89986"
ROOT = Path("dist")


def replace_all(text: str, replacements: dict[str, str]) -> str:
    for before, after in replacements.items():
        text = text.replace(before, after)
    return text


def patch_public_links() -> None:
    config = ROOT / "assets/js/config.js"
    if config.exists():
        text = config.read_text(encoding="utf-8")
        replacements = {
            'discordUrl: "DISCORD_INVITE_URL_HERE"': f'discordUrl: "{DISCORD_URL}"',
            'discordUrl: "https://disboard.org/ja/server/1216271639952752691"': f'discordUrl: "{DISCORD_URL}"',
            'discordUrl: "https://discord.gg/Mt4EVcdEDQ"': f'discordUrl: "{DISCORD_URL}"',
            'discordUrl: "https://discord.com/invite/Mt4EVcdEDQ"': f'discordUrl: "{DISCORD_URL}"',
            'discordUrl: "https://discord.gg/dCHCAY6DbZ"': f'discordUrl: "{DISCORD_URL}"',
            'xUrl: "X_URL_HERE"': f'xUrl: "{X_URL}"',
            'xUrl: "https://x.com/AxisBay89986"': f'xUrl: "{X_URL}"',
        }
        config.write_text(replace_all(text, replacements), encoding="utf-8")

    replacements = {
        "AXIS BAYへの参加方法、最低限のルール、Disboard経由でDiscordへ参加する流れ。": "AXIS BAYへの参加方法、最低限のルール、Discord参加申請の流れ。",
        "AXIS BAYへの参加方法、最低限のルール、Discord申請の流れ。": "AXIS BAYへの参加方法、最低限のルール、Discord参加申請の流れ。",
        "参加条件と最低限のルールを確認して、DisboardページからDiscordへ参加し、申請してください。": "参加条件と最低限のルールを確認して、Discordから申請してください。",
        "参加条件と最低限のルールを確認して、Discordから申請してください。": "参加条件と最低限のルールを確認して、Discordから申請してください。",
        "最低限の確認を終えたら、DisboardページからDiscordへ参加し、参加申請へ進めます。": "最低限の確認を終えたら、Discordから参加申請へ進めます。",
        "最低限の確認を終えたら、Discordから参加申請へ進めます。": "最低限の確認を終えたら、Discordから参加申請へ進めます。",
        "<h3>DisboardからDiscordへ参加</h3>": "<h3>Discordへ参加</h3>",
        "<h3>Discord内の案内と最低限ルールを確認</h3>": "<h3>Discordの案内と最低限ルールを確認</h3>",
        "APPLY VIA DISBOARD": "APPLY ON DISCORD",
        "DisboardからDiscord参加へ。": "Discordから参加申請へ。",
        "Disboardの掲載ページからDiscordへ参加し、Discord内で申請方法と募集状況を確認してください。": "申請方法と現在の募集状況はDiscordで案内しています。",
        "AXIS BAYをDisboardで見る": "AXIS BAY Discordへ参加",
        "https://disboard.org/ja/server/1216271639952752691": DISCORD_URL,
        "https://discord.gg/Mt4EVcdEDQ": DISCORD_URL,
        "https://discord.com/invite/Mt4EVcdEDQ": DISCORD_URL,
    }

    for path in [ROOT / "index.html", ROOT / "join.html"]:
        if path.exists():
            path.write_text(replace_all(path.read_text(encoding="utf-8"), replacements), encoding="utf-8")


def patch_shops_rule() -> None:
    path = ROOT / "rules/shops.html"
    if not path.exists():
        return

    text = path.read_text(encoding="utf-8")

    text = replace_all(text, {
        "営業、販売区分、価格、商品開発": "飲食店・販売店・サービス店の開業、営業、販売に関する共通ルール",
        "販売区分、価格、商品開発、販売方法に関する店舗固有ルール": "飲食店・販売店・サービス店の開業、営業、販売に関する共通ルール",
        '<span class="pill">6項目</span>': '<span class="pill">9項目</span>',
    })

    toc = '''<aside class="rule-toc"><div class="rule-toc-title">このページの目次</div><a href="#section-1">1．起業・開業の条件</a><a href="#section-2">2．廃業となる可能性がある条件</a><a href="#section-3">3．営業時の基本ルール</a><a href="#section-4">4．販売できる商品の区分</a><a href="#section-5">5．販売価格一覧</a><a href="#section-6">6．販売数と商品の説明</a><a href="#section-7">7．商品の追加・開発</a><a href="#section-8">8．禁止事項</a><a href="#section-9">9．追加物・スクリプト・ライセンスの扱い</a><a class="toc-back" href="../rules.html">← ルール一覧へ</a></aside>'''
    text = re.sub(r'<aside class="rule-toc">.*?</aside>\s*<div class="rule-document">', toc + '\n<div class="rule-document">', text, count=1, flags=re.S)
    text = re.sub(r'<aside class="rule-callout info common-rule-link">.*?</aside>', '', text, count=1, flags=re.S)

    text = replace_all(text, {
        'id="section-1"><h2>1．販売できる商品の区分</h2>': 'id="section-4"><h2>4．販売できる商品の区分</h2>',
        'id="section-2"><h2>2．販売価格一覧</h2>': 'id="section-5"><h2>5．販売価格一覧</h2>',
        'id="section-3"><h2>3．販売数と商品の説明</h2>': 'id="section-6"><h2>6．販売数と商品の説明</h2>',
        'id="section-4"><h2>4．商品の追加・開発</h2>': 'id="section-7"><h2>7．商品の追加・開発</h2>',
        'id="section-5"><h2>5．禁止事項</h2>': 'id="section-8"><h2>8．禁止事項</h2>',
        'id="section-6"><h2>6．追加物・スクリプト・ライセンスの扱い</h2>': 'id="section-9"><h2>9．追加物・スクリプト・ライセンスの扱い</h2>',
    })

    new_sections = '''<section class="rule-content-section" data-rule-section="" id="section-1"><h2>1．起業・開業の条件</h2><p>販売店を起業する場合は、次の条件を満たす必要があります。</p><ul class="rule-source-list"><li><span class="rule-marker">□</span><span>オーナー1名、店員1名以上の合計2名以上で名簿を提出すること。</span></li><li><span class="rule-marker">□</span><span>開業資金を、許可後すぐに支払えること。</span></li><li><span class="rule-marker">□</span><span>オーナーが白市民パスを所持していること。</span></li><li><span class="rule-marker">□</span><span>オーナーが、すでに2つのジョブに就いていないこと。</span></li><li><span class="rule-marker">□</span><span>起業後も継続して店舗を経営できると運営が判断できること。</span></li><li><span class="rule-marker">□</span><span>過去に経営していた店舗を廃業している場合は、別途面談を受けること。</span></li></ul><aside class="rule-callout info"><p>申請手続きや開業までの流れは「AXIS BAY 起業ルール」を確認してください。</p></aside></section><section class="rule-content-section" data-rule-section="" id="section-2"><h2>2．廃業となる可能性がある条件</h2><ul class="rule-source-list"><li><span class="rule-marker">●</span><span>営業時間が、街で定める週4時間に満たない場合。</span></li><li><span class="rule-marker">●</span><span>オーナーが、特別な理由なく2週間以上出勤することが難しい場合。</span></li><li><span class="rule-marker">●</span><span>オーナーに犯罪歴が付いた場合（聞き取りを行ったうえで判断します）。</span></li><li><span class="rule-marker">●</span><span>オーナーから自己都合による廃業申請が提出された場合。</span></li><li><span class="rule-marker">●</span><span>運営からの改善命令に従わないなど、廃業が必要であると運営が判断した場合。</span></li></ul></section><section class="rule-content-section" data-rule-section="" id="section-3"><h2>3．営業時の基本ルール</h2><ul class="rule-source-list"><li><span class="rule-marker">●</span><span>社員は原則として自店舗での購入を控え、ほかの店舗を利用してください。</span></li><li><span class="rule-marker">●</span><span>1週間の営業時間は、合計4時間以上を目安としてください。</span></li><li><span class="rule-marker">●</span><span>1回の開店につき、30分以上営業してください。</span></li><li><span class="rule-marker">●</span><span>営業時間が週4時間に達しない見込みの場合は、事前に市役所へ連絡してください。</span></li><li><span class="rule-marker">●</span><span>開店時と閉店時には、birdieへ投稿してください。</span></li><li><span class="rule-marker">●</span><span>勤務中は、店舗で定められた制服を着用してください。</span></li><li><span class="rule-marker">●</span><span>ネームタグには「名前」と「店舗名」を明示してください。</span></li></ul></section>'''
    marker = '<section class="rule-content-section" data-rule-section="" id="section-4"><h2>4．販売できる商品の区分</h2>'
    if 'id="section-1"><h2>1．起業・開業の条件</h2>' not in text and marker in text:
        text = text.replace(marker, new_sections + marker, 1)

    text = replace_all(text, {
        '<tr><td><p>ストレス回復</p></td><td><p>10％</p></td><td><p>15,000</p></td></tr>': '<tr><td><p>ストレス回復</p></td><td><p>10％</p></td><td><p>35,000</p></td></tr>',
        '<tr><td><p>ストレス回復</p></td><td><p>20％</p></td><td><p>45,000</p></td></tr>': '<tr><td><p>ストレス回復</p></td><td><p>20％</p></td><td><p>65,000</p></td></tr>',
        '<tr><td><p>ストレス回復</p></td><td><p>10％</p></td><td><p>10,000</p></td></tr>': '<tr><td><p>ストレス回復</p></td><td><p>10％</p></td><td><p>30,000</p></td></tr>',
        '<tr><td><p>ストレス回復</p></td><td><p>20％</p></td><td><p>30,000</p></td></tr>': '<tr><td><p>ストレス回復</p></td><td><p>20％</p></td><td><p>50,000</p></td></tr>',
        '<tr><td><p>ストレス回復</p></td><td><p>30％</p></td><td><p>50,000</p></td></tr>': '<tr><td><p>ストレス回復</p></td><td><p>30％</p></td><td><p>70,000</p></td></tr>',
        '<tr><td><p>イートイン（1）</p></td><td><p>－</p></td><td><p>75,000</p></td></tr>': '<tr><td><p>イートイン（1）</p></td><td><p>－</p></td><td><p>95,000</p></td></tr>',
        '商品開発は、1店舗につき月4商品までです。': '商品開発数には、制限はありません。',
    })

    text = replace_all(text, {
        '販売区分、価格、商品開発、販売方法に関する店舗固有ルール': '開業、営業、販売区分、価格、商品開発に関する店舗ルール',
        '営業、販売区分、価格、商品開発': '開業、営業、販売区分、価格、商品開発',
    })

    path.write_text(text, encoding="utf-8")


def main() -> None:
    patch_public_links()
    patch_shops_rule()


if __name__ == "__main__":
    main()
