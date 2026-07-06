const SITE = {
  discordUrl: "#",
  xUrl: "#",
  crimeQuickReferenceUrl: "#",
  videoUrl: "https://www.youtube.com/embed/bWjh5AaDpJE"
};

const citySections = [
  { tag: "暮らし", title: "仕事と店舗経営", text: "飲食店、販売店、メカニックなど、接客や商品提供を通じた職業RPを楽しめます。住民との交流が街の中心になります。" },
  { tag: "公務員", title: "警察", text: "事件対応、捜査、交通対応を通して街の治安を守ります。勝敗だけでなく、相手のRPを尊重した対応が重要です。" },
  { tag: "医療", title: "救急隊・個人医", text: "救命、治療、搬送、医療相談を通して住民を支えます。救急隊と個人医は、それぞれのルールに沿って活動します。" },
  { tag: "車両", title: "メカニック", text: "修理、整備、カスタムを通して住民のカーライフを支えます。車両を通じた交流や職業RPを楽しめます。" },
  { tag: "住まい", title: "不動産", text: "不動産の購入は運営が対応します。希望する場合は、六法のチケットからお問い合わせください。" },
  { tag: "組織", title: "ギャング・組織RP", text: "縄張り、外交、抗争、イベントを通して、組織同士の濃いRPを作れます。事前協議と相手への配慮を重視します。" },
  { tag: "イベント", title: "島取り", text: "ギャングがエリアの所有権を巡って争う定期犯罪イベントです。", schedule: "7月：第2水曜日 22:00開始" },
  { tag: "イベント", title: "エアドロップ", text: "物資の確保と防衛を巡る定期イベントです。島取りとは別イベントとして扱います。", schedule: "毎週土曜日 22:00開始" },
  { tag: "初心者", title: "初心者支援", text: "初めてFiveM RPに参加する方も、案内と初心者マークを活用しながら街に慣れられます。" }
];

const rules = [
  {
    category: "基本・安全",
    title: "全体ルール",
    summary: "すべての住民が共通して守る基本ルールです。",
    keywords: "全体 基本 初心者 ジョブ フリージョブ 不動産 白市民カード ホワイトジョブコイン 売買 譲渡",
    body: `
      <h4>基本方針</h4>
      <ul><li>AXIS BAYでは、相手を尊重したロールプレイと住民同士の交流を重視します。</li><li>迷惑行為、誹謗中傷、荒らし行為、外部情報を利用した行動は禁止します。</li></ul>
      <h4>ジョブ・フリージョブ</h4>
      <ul><li>市民は最大2つのジョブに就くことができます。</li><li>ギャング所属も1ジョブとして数えます。</li><li>ギャングが兼務として認められるのは、フロント企業のみです。</li></ul>
      <h4>初心者マーク</h4>
      <ul><li>初心者マークが付いている間は、病院で初心者向けの優遇を受けられます。</li><li>初心者マークを付けたまま犯罪を行うことは禁止です。</li><li>初心者マークを早期解除する場合は、F1 → 一般 → ネームタグ →「初心者マークを早期解除する」から操作します。</li></ul>
      <h4>不動産の購入</h4>
      <p>不動産の購入については運営が対応いたしますので、六法のチケットからお問い合わせください。</p>
      <h4>白市民カード</h4>
      <ul><li>公務員職に就く場合は、白市民カードの所持が必須です。</li><li>白市民カードの譲渡・貸与は禁止です。</li><li>白市民価格を利用した代理購入や譲渡は禁止です。</li></ul>
      <h4>ホワイトジョブコイン</h4>
      <p>白市民カードを携帯している状態でホワイトジョブに従事していると、給与と同時に「ホワイトジョブコイン」が付与されます。これは限定の車やアイテムと交換できるアイテムです。</p>
      <div class="alert danger"><strong>禁止事項：</strong>ホワイトジョブコインの売買・譲渡は一切禁止します。</div>`
  },
  { category: "基本・安全", title: "配信ルール", summary: "配信・動画投稿時の情報管理と周囲への配慮です。", keywords: "配信 動画 メタ 個人情報", body: `<ul><li>他者の個人情報、運営情報、未公開情報を公開しないでください。</li><li>配信外で得た情報をゲーム内で利用する行為は禁止です。</li><li>トラブル時は当事者間で拡大させず、必要に応じて六法のチケットで運営へ連絡してください。</li></ul>` },
  { category: "基本・安全", title: "荒らし対応ルール", summary: "荒らしや重大な迷惑行為へ遭遇した場合の対応です。", keywords: "荒らし 通報 証拠 録画 チケット", body: `<ul><li>個人で過度に反応せず、可能な範囲で動画やスクリーンショットなどの記録を残してください。</li><li>相手への報復や公開の場での晒し行為は禁止です。</li><li>六法のチケットから運営へ報告してください。</li></ul>` },
  { category: "企業・職業", title: "企業共通ルール", summary: "店舗や企業を運営する際の共通ルールです。", keywords: "企業 店舗 経営 従業員 廃業 休業", body: `<ul><li>企業は接客や商品提供を通じたRPを大切にしてください。</li><li>価格設定、在庫、従業員管理、イベント運営について責任を持ってください。</li><li>他企業への妨害、システムの悪用、従業員権限の不正利用は禁止です。</li></ul>` },
  { category: "企業・職業", title: "販売店ルール", summary: "車両や商品の販売を行う店舗向けのルールです。", keywords: "販売店 車両 販売 割引 在庫 価格", body: `<ul><li>販売価格、割引、支払い方法、限定商品などは店舗に認められた範囲で運用してください。</li><li>権限や在庫を利用した不正な自己購入、無償譲渡、価格操作は禁止です。</li><li>購入者へ必要な説明を行い、販売記録や店舗内の手続きを適切に管理してください。</li></ul>` },
  { category: "企業・職業", title: "メカニックルール", summary: "修理・整備・車両カスタムを行う際のルールです。", keywords: "メカニック 修理 整備 カスタム 車両", body: `<ul><li>修理やカスタムは、料金と施工内容を確認してから行ってください。</li><li>職務権限、専用設備、材料を私的に不正利用することは禁止です。</li><li>ほかの車両システムや店舗運営を妨げないよう、作業場所と周囲の安全へ配慮してください。</li></ul>` },
  { category: "公務員・医療", title: "警察ルール", summary: "警察官の捜査、逮捕、押収、犯罪対応に関するルールです。", keywords: "警察 逮捕 捜査 押収 公務員 必要人数", body: `<ul><li>警察は街の治安を守る立場として、公平で相手のRPを尊重した対応を行ってください。</li><li>権限の私的利用、理由のない拘束や押収、職務情報の漏えいは禁止です。</li><li>犯罪ごとの必要人数や対応条件は犯罪ルールと犯罪早見表を確認してください。</li></ul>` },
  { category: "公務員・医療", title: "救急隊ルール", summary: "救命・治療・搬送を行う救急隊向けのルールです。", keywords: "救急隊 EMS 治療 蘇生 搬送 医療", body: `<ul><li>救急隊は負傷者の救命を優先し、現場の安全と状況を確認して対応してください。</li><li>職務上知り得た情報を犯罪や私的利益へ利用することは禁止です。</li><li>治療中や搬送中は、負傷者と周囲のRPを尊重してください。</li></ul>` },
  { category: "公務員・医療", title: "個人医ルール", summary: "個人医として治療を行う場合の活動条件と禁止事項です。", keywords: "個人医 治療 医療 救急隊 犯罪", body: `<ul><li>個人医は認められた範囲で治療を行い、救急隊や警察の活動を妨害しないでください。</li><li>犯罪への加担、医療権限の悪用、治療を利用した不当な利益獲得は禁止です。</li></ul>` },
  { category: "犯罪・ギャング", title: "犯罪ルール", summary: "犯罪の開始条件、警察人数、進行、禁止事項に関するルールです。", keywords: "犯罪 警察人数 クールタイム 装備 参加人数 禁止", body: `<ul><li>犯罪を開始する前に、必要警察人数、クールタイム、使用可能な装備、参加人数などを確認してください。</li><li>システムの不具合や同期ずれを利用して利益を得る行為は禁止です。</li><li>犯罪終了後も相手を尊重し、過度な煽り、死体撃ち、RPを壊す行動を行わないでください。</li></ul>` },
  {
    category: "犯罪・ギャング",
    title: "犯罪イベントルール",
    summary: "島取りとエアドロップの開催日時・進行・禁止事項です。",
    keywords: "犯罪イベント 島取り 第2水曜日 22時 エアドロップ 土曜日 エリア 抗争 賠償 薬",
    body: `<div class="part"><h4>PART A 島取りルール</h4><p><strong>7月は第2水曜日 22:00開始</strong>です。</p><ul><li>島取り期間外も、所有エリアで薬を販売し、島の維持に努めてください。</li><li>所有エリア外で誤って薬を販売した場合は、そのエリアを所有するギャングと対応を協議してください。</li><li>対応方法は、話し合い、抗争、または抗争を拒否する場合の賠償金支払いです。</li></ul></div><div class="part"><h4>PART B 定期イベント「エアドロップ」</h4><p><strong>毎週土曜日 22:00開始</strong>です。</p><ul><li>島取りとは別のイベントとして扱います。</li><li>イベントの流れ、参加条件、禁止事項を確認してから参加してください。</li><li>物資の確保と防衛を巡る定期犯罪イベントです。</li></ul></div>`
  },
  { category: "犯罪・ギャング", title: "ギャングルール", summary: "ギャングの設立、縄張り、抗争、フロント企業に関するルールです。", keywords: "ギャング 抗争 縄張り フロント企業 兼務", body: `<ul><li>ギャングは組織としてのRPを重視し、縄張り、抗争、外交を当事者間の協議に基づいて行ってください。</li><li>抗争条件や勝敗の扱いは事前に確認し、終了後の報復や過度な煽りは禁止です。</li><li>ギャングが兼務として認められるのはフロント企業のみです。</li></ul>` }
];

function card(section) {
  return `<article class="card"><span class="tag">${section.tag}</span><h3>${section.title}</h3><p>${section.text}</p>${section.schedule ? `<div class="schedule">${section.schedule}</div>` : ""}</article>`;
}

function renderCity() {
  document.getElementById("cityGrid").innerHTML = citySections.map(card).join("");
}

function renderRules(list = rules) {
  const ruleList = document.getElementById("ruleList");
  ruleList.innerHTML = list.map((rule, index) => `
    <details class="rule-card" ${index === 0 || rule.title === "犯罪イベントルール" ? "open" : ""} data-keywords="${rule.keywords}">
      <summary><div><span class="tag">${rule.category}</span><h3>${rule.title}</h3><p>${rule.summary}</p></div></summary>
      <div class="rule-body">${rule.body}</div>
    </details>`).join("");
  document.getElementById("ruleCount").textContent = `${list.length}件`;
}

function setupSearch() {
  const input = document.getElementById("ruleSearch");
  input.addEventListener("input", () => {
    const q = input.value.trim().toLowerCase();
    const filtered = !q ? rules : rules.filter(rule => `${rule.category} ${rule.title} ${rule.summary} ${rule.keywords} ${rule.body}`.toLowerCase().includes(q));
    renderRules(filtered);
  });
}

function setupNav() {
  const menu = document.querySelector(".menu");
  const links = document.querySelector(".links");
  menu.addEventListener("click", () => links.classList.toggle("open"));
  document.querySelectorAll(".links a").forEach(a => a.addEventListener("click", () => links.classList.remove("open")));
}

renderCity();
renderRules();
setupSearch();
setupNav();
