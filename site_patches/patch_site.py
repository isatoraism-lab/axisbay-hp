from pathlib import Path

DISCORD_URL = "https://discord.gg/dCHCAY6DbZ"
X_URL = "https://x.com/AxisBay89986"
ROOT = Path("dist")


def apply_public_links() -> None:
    config = ROOT / "assets/js/config.js"
    if config.exists():
        text = config.read_text(encoding="utf-8")
        for old in [
            'discordUrl: "DISCORD_INVITE_URL_HERE"',
            'discordUrl: "https://disboard.org/ja/server/1216271639952752691"',
            'discordUrl: "https://discord.gg/Mt4EVcdEDQ"',
            'discordUrl: "https://discord.com/invite/Mt4EVcdEDQ"',
            'discordUrl: "https://discord.gg/dCHCAY6DbZ"',
        ]:
            text = text.replace(old, f'discordUrl: "{DISCORD_URL}"')
        text = text.replace('xUrl: "X_URL_HERE"', f'xUrl: "{X_URL}"')
        text = text.replace('xUrl: "https://x.com/AxisBay89986"', f'xUrl: "{X_URL}"')
        config.write_text(text, encoding="utf-8")

    replacements = {
        "AXIS BAYへの参加方法、最低限のルール、Disboard経由でDiscordへ参加する流れ。": "AXIS BAYへの参加方法、最低限のルール、Discord参加申請の流れ。",
        "AXIS BAYへの参加方法、最低限のルール、Discord申請の流れ。": "AXIS BAYへの参加方法、最低限のルール、Discord参加申請の流れ。",
        "参加条件と最低限のルールを確認して、DisboardページからDiscordへ参加し、申請してください。": "参加条件と最低限のルールを確認して、Discordから申請してください。",
        "最低限の確認を終えたら、DisboardページからDiscordへ参加し、参加申請へ進めます。": "最低限の確認を終えたら、Discordから参加申請へ進めます。",
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
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for before, after in replacements.items():
            text = text.replace(before, after)
        path.write_text(text, encoding="utf-8")


SHOP_RULE_HTML = r'''<!DOCTYPE html>
<html lang="ja"><head>
<meta charset="utf-8"/><meta content="width=device-width,initial-scale=1" name="viewport"/>
<meta content="飲食店・販売店・サービス店の開業、営業、販売に関する共通ルール" name="description"/><meta content="#061522" name="theme-color"/>
<meta content="website" property="og:type"/><meta content="販売店ルール｜AXIS BAY" property="og:title"/>
<meta content="飲食店・販売店・サービス店の開業、営業、販売に関する共通ルール" property="og:description"/>
<meta content="https://static.wixstatic.com/media/075481_a6ae8d96b2eb4c4aaa4a0a34a9059718~mv2.png/v1/crop/x_468%2Cy_0%2Cw_980%2Ch_729%2Cq_90%2Cenc_avif%2Cquality_auto/075481_a6ae8d96b2eb4c4aaa4a0a34a9059718~mv2.png" property="og:image"/>
<title>販売店ルール｜AXIS BAY</title><link href="../assets/css/site.css" rel="stylesheet"/>
</head><body><a class="skip-link" href="#main">本文へ移動</a>
<header class="site-header"><div class="container nav"><a class="brand" href="../index.html"><img alt="AXIS BAY" class="brand-logo" src="https://static.wixstatic.com/media/32c055_d798a13c90e2468c919cc934ce696f19~mv2.png/v1/fill/w_583%2Ch_439%2Cal_c%2Cq_85%2Cenc_avif%2Cquality_auto/icon.png"/><span class="brand-copy"><strong>AXIS BAY</strong><small>ROLEPLAY SERVER</small></span></a><button aria-expanded="false" aria-label="メニュー" class="menu-button" type="button">☰</button><nav class="nav-links"><a href="../index.html">ホーム</a><a href="../about.html">街紹介</a><a aria-current="page" href="../rules.html">ルール</a><a href="../join.html">参加へ</a></nav></div></header>
<main id="main"><section class="page-hero" style="--page-image:url('https://static.wixstatic.com/media/075481_a6ae8d96b2eb4c4aaa4a0a34a9059718~mv2.png/v1/crop/x_468%2Cy_0%2Cw_980%2Ch_729%2Cq_90%2Cenc_avif%2Cquality_auto/075481_a6ae8d96b2eb4c4aaa4a0a34a9059718~mv2.png')"><div class="container">
<div class="breadcrumbs"><a href="../index.html">ホーム</a><span>/</span><a href="../rules.html">ルールセンター</a><span>/</span><span>販売店ルール</span></div><span class="eyebrow">RULES</span><h1>販売店ルール</h1><p class="lead">飲食店・販売店・サービス店の開業、営業、販売に関する共通ルール</p>
<div class="page-meta"><span class="pill">事業・職業</span><span class="pill">ページ内検索</span><span class="pill">9項目</span></div></div></section>
<section class="section-sm"><div class="container"><div class="notice" data-rule-notice=""></div></div></section>
<section class="section rule-detail"><div class="container rule-detail-layout">
<aside class="rule-toc"><div class="rule-toc-title">このページの目次</div><a href="#section-1">1．起業・開業の条件</a><a href="#section-2">2．廃業となる可能性がある条件</a><a href="#section-3">3．営業時の基本ルール</a><a href="#section-4">4．販売できる商品の区分</a><a href="#section-5">5．販売価格一覧</a><a href="#section-6">6．販売数と商品の説明</a><a href="#section-7">7．商品の追加・開発</a><a href="#section-8">8．禁止事項</a><a href="#section-9">9．追加物・スクリプト・ライセンスの扱い</a><a class="toc-back" href="../rules.html">← ルール一覧へ</a></aside>
<div class="rule-document">
<div class="rule-page-tools"><div><span class="eyebrow">SEARCH THIS RULE</span><h2>販売店ルール</h2><p class="muted">飲食店・販売店・サービス店の開業、営業、販売に関する共通ルール</p></div>
<div class="rule-search-box"><input class="search-input" data-rule-page-search="" placeholder="このルール内を検索" type="search"/><span data-rule-page-count=""></span></div></div>
<div class="rule-filter-empty" data-rule-filter-empty="" hidden="">一致する項目がありません。</div>
<aside class="rule-callout info"><p>適用範囲：運営が認めた例外を除き、店舗を構えてサービスを提供するすべての飲食店・販売店・サービス店に適用します。</p></aside>
<section class="rule-content-section" data-rule-section="" id="section-1"><h2>1．起業・開業の条件</h2><p>販売店を起業する場合は、次の条件を満たす必要があります。</p><ul class="rule-source-list"><li><span class="rule-marker">□</span><span>オーナー1名、店員1名以上の合計2名以上で名簿を提出すること。</span></li><li><span class="rule-marker">□</span><span>開業資金を、許可後すぐに支払えること。</span></li><li><span class="rule-marker">□</span><span>オーナーが白市民パスを所持していること。</span></li><li><span class="rule-marker">□</span><span>オーナーが、すでに2つのジョブに就いていないこと。</span></li><li><span class="rule-marker">□</span><span>起業後も継続して店舗を経営できると運営が判断できること。</span></li><li><span class="rule-marker">□</span><span>過去に経営していた店舗を廃業している場合は、別途面談を受けること。</span></li></ul><aside class="rule-callout info"><p>申請手続きや開業までの流れは「AXIS BAY 起業ルール」を確認してください。</p></aside></section>
<section class="rule-content-section" data-rule-section="" id="section-2"><h2>2．廃業となる可能性がある条件</h2><ul class="rule-source-list"><li><span class="rule-marker">●</span><span>営業時間が、街で定める週4時間に満たない場合。</span></li><li><span class="rule-marker">●</span><span>オーナーが、特別な理由なく2週間以上出勤することが難しい場合。</span></li><li><span class="rule-marker">●</span><span>オーナーに犯罪歴が付いた場合（聞き取りを行ったうえで判断します）。</span></li><li><span class="rule-marker">●</span><span>オーナーから自己都合による廃業申請が提出された場合。</span></li><li><span class="rule-marker">●</span><span>運営からの改善命令に従わないなど、廃業が必要であると運営が判断した場合。</span></li></ul></section>
<section class="rule-content-section" data-rule-section="" id="section-3"><h2>3．営業時の基本ルール</h2><ul class="rule-source-list"><li><span class="rule-marker">●</span><span>社員は原則として自店舗での購入を控え、ほかの店舗を利用してください。</span></li><li><span class="rule-marker">●</span><span>1週間の営業時間は、合計4時間以上を目安としてください。</span></li><li><span class="rule-marker">●</span><span>1回の開店につき、30分以上営業してください。</span></li><li><span class="rule-marker">●</span><span>営業時間が週4時間に達しない見込みの場合は、事前に市役所へ連絡してください。</span></li><li><span class="rule-marker">●</span><span>開店時と閉店時には、birdieへ投稿してください。</span></li><li><span class="rule-marker">●</span><span>勤務中は、店舗で定められた制服を着用してください。</span></li><li><span class="rule-marker">●</span><span>ネームタグには「名前」と「店舗名」を明示してください。</span></li></ul></section>
<section class="rule-content-section" data-rule-section="" id="section-4"><h2>4．販売できる商品の区分</h2><p>店舗は、申請時に決めた「メイン区分」を中心に商品を販売してください。</p><div class="table-scroll"><table class="rule-table"><tr><th><p>店舗区分</p></th><th><p>メイン商品</p></th><th><p>メインではない商品の販売条件</p></th></tr><tr><td><p>飲食メイン店</p></td><td><p>食べ物・飲み物</p></td><td><p>ストレス回復メイン店が営業していない場合に限り、ストレス回復商品を販売できます。</p></td></tr><tr><td><p>ストレス回復メイン店</p></td><td><p>ストレス回復商品</p></td><td><p>飲食メイン店が営業していない場合に限り、食べ物・飲み物を販売できます。</p></td></tr></table></div><p>メインではない商品の回復量は、最大20％までです。グッズなど、回復効果を持たない商品の販売は可能です。</p></section>
<section class="rule-content-section" data-rule-section="" id="section-5"><h2>5．販売価格一覧</h2><p class="rule-note-text">※以下は、各店舗区分で販売する商品の価格一覧です。</p><h3>飲食メイン店</h3><div class="table-scroll"><table class="rule-table"><tr><th><p>商品区分</p></th><th><p>効果</p></th><th><p>価格</p></th></tr><tr><td><p>飲食</p></td><td><p>10％</p></td><td><p>20,000</p></td></tr><tr><td><p>飲食</p></td><td><p>20％</p></td><td><p>60,000</p></td></tr><tr><td><p>飲食</p></td><td><p>30％</p></td><td><p>100,000</p></td></tr><tr><td><p>イートイン（1）</p></td><td><p>－</p></td><td><p>150,000</p></td></tr><tr><td><p>イートイン（2）</p></td><td><p>－</p></td><td><p>200,000</p></td></tr><tr><td><p>ストレス回復</p></td><td><p>10％</p></td><td><p>35,000</p></td></tr><tr><td><p>ストレス回復</p></td><td><p>20％</p></td><td><p>65,000</p></td></tr></table></div><h3>ストレス回復メイン店</h3><div class="table-scroll"><table class="rule-table"><tr><th><p>商品区分</p></th><th><p>効果</p></th><th><p>価格</p></th></tr><tr><td><p>ストレス回復</p></td><td><p>10％</p></td><td><p>30,000</p></td></tr><tr><td><p>ストレス回復</p></td><td><p>20％</p></td><td><p>50,000</p></td></tr><tr><td><p>ストレス回復</p></td><td><p>30％</p></td><td><p>70,000</p></td></tr><tr><td><p>イートイン（1）</p></td><td><p>－</p></td><td><p>95,000</p></td></tr><tr><td><p>飲食</p></td><td><p>10％</p></td><td><p>30,000</p></td></tr><tr><td><p>飲食</p></td><td><p>20％</p></td><td><p>90,000</p></td></tr></table></div></section>
<section class="rule-content-section" data-rule-section="" id="section-6"><h2>6．販売数と商品の説明</h2><ul class="rule-source-list"><li><span class="rule-marker">●</span><span>販売できる個数に、街全体で定める上限はありません。</span></li><li><span class="rule-marker">●</span><span>店舗ごとに独自の販売数上限を設けることは可能です。</span></li><li><span class="rule-marker">●</span><span>商品は時間の経過によって効果を失うため、初めて購入する方には必ず説明してください。</span></li></ul></section>
<section class="rule-content-section" data-rule-section="" id="section-7"><h2>7．商品の追加・開発</h2><ul class="rule-source-list"><li><span class="rule-marker">●</span><span>商品開発数には、制限はありません。</span></li><li><span class="rule-marker">●</span><span>商品開発や追加方法について不明点がある場合は、運営へ相談してください。</span></li></ul></section>
<section class="rule-content-section" data-rule-section="" id="section-8"><h2>8．禁止事項</h2><aside class="rule-callout info"><ul class="rule-source-list"><li><span class="rule-marker danger">×</span><span>過度な押し売りをすること。</span></li><li><span class="rule-marker danger">×</span><span>相手の同意なく、インベントリへ商品を入れて売りつけること。</span></li><li><span class="rule-marker danger">×</span><span>価格を明示せずに販売すること。</span></li><li><span class="rule-marker danger">×</span><span>店員ではない人が、店舗の商品を代理販売すること。</span></li><li><span class="rule-marker danger">×</span><span>キッチンカー以外で、店舗外に出勤状態で販売すること（困っている方への譲渡は除きます）。</span></li><li><span class="rule-marker danger">×</span><span>店舗販売の請求書を、店舗ではなく個人名義で発行すること。</span></li></ul></aside></section>
<section class="rule-content-section" data-rule-section="" id="section-9"><h2>9．追加物・スクリプト・ライセンスの扱い</h2><ul class="rule-source-list"><li><span class="rule-marker">●</span><span>購入して追加したMLO・スクリプト・ライセンス・ファイルは、実装後にAXIS BAYへ帰属します。</span></li><li><span class="rule-marker">●</span><span>店舗が廃業した場合でも、購入費用の返金は行いません。</span></li><li><span class="rule-marker">●</span><span>サーバーとの相性などにより実装できなかった場合でも、返金は行いません。</span></li><li><span class="rule-marker">●</span><span>廃業後、別のオーナーが同じMLOや追加物を利用して新しい店舗を経営する場合があります。</span></li><li><span class="rule-marker">●</span><span>追加を行った本人がサーバーを離れた場合でも、実装物の削除・返還は行いません。</span></li></ul><aside class="rule-callout info"><p>同意について：追加物・スクリプトなどの導入を依頼した時点で、上記の取り扱いに同意したものとみなします。</p></aside><p>利用者が安心して店舗を利用できるよう、価格・営業時間・販売方法を明確にして営業してください。</p></section>
<div class="rule-end-actions"><a class="button button-secondary" href="../rules.html">ルール一覧へ戻る</a><a class="button button-primary" data-config-link="discord" href="#">不明点はチケットへ</a></div>
</div></div></section>
<section class="section section-alt"><div class="container"><span class="eyebrow">RELATED RULES</span><h2>関連するルール</h2><div class="rule-card-grid"><article class="rule-card" data-rule-card="" data-search-text="企業共通ルール 起業 営業時間 廃業 申請"><div class="rule-card-top"><span class="rule-card-icon">起</span><span class="rule-card-group">事業・職業</span></div><h3>企業共通ルール</h3><p>起業、共通営業、廃業、開店までの流れ</p><a class="card-link" href="../rules/business.html">全文を見る →</a></article><article class="rule-card" data-rule-card="" data-search-text="メカニックルール 勤務資格、営業、カスタム記録"><div class="rule-card-top"><span class="rule-card-icon">整</span><span class="rule-card-group">事業・職業</span></div><h3>メカニックルール</h3><p>勤務資格、営業、カスタム記録</p><a class="card-link" href="../rules/mechanic.html">全文を見る →</a></article><article class="rule-card" data-rule-card="" data-search-text="警察ルール 勤務、装備、事件対応、守秘義務"><div class="rule-card-top"><span class="rule-card-icon">警</span><span class="rule-card-group">事業・職業</span></div><h3>警察ルール</h3><p>勤務、装備、事件対応、守秘義務</p><a class="card-link" href="../rules/police.html">全文を見る →</a></article></div></div></section></main>
<footer class="site-footer"><div class="container footer-row"><div class="footer-brand"><img alt="" src="https://static.wixstatic.com/media/32c055_d798a13c90e2468c919cc934ce696f19~mv2.png/v1/fill/w_583%2Ch_439%2Cal_c%2Cq_85%2Cenc_avif%2Cquality_auto/icon.png"/><span>© <span data-current-year=""></span> AXIS BAY</span></div><div class="footer-links"><a href="../index.html">ホーム</a><a href="../about.html">街紹介</a><a href="../rules.html">ルール</a><a href="../join.html">参加へ</a><a data-config-link="x" href="#">X</a></div></div></footer><script src="../assets/js/config.js"></script><script src="../assets/js/site.js"></script></body></html>'''


def apply_shops_rule() -> None:
    path = ROOT / "rules/shops.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(SHOP_RULE_HTML, encoding="utf-8")


if __name__ == "__main__":
    apply_public_links()
    apply_shops_rule()
