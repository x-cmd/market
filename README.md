# market

**A manual for writing a market and marketing report.** Every figure is an [x-cmd draw](https://github.com/x-cmd/draw) URL: the data lives in the link, server-rendered as SVG. Open any chart and you see its full parameters; paste it anywhere markdown images work.

> The full outline — every stage, every page's title, what it gives you, its sections and what each section covers — is in **[OUTLINE.yml](OUTLINE.yml)**. The machine-readable metric definitions an agent needs are in **[spec/metric-cards.yml](spec/metric-cards.yml)**.

## The idea

You are writing a report: how big this market is, who is in it, what people buy, where the money goes, what came back, where the next dollar should go. The hard part is not a lack of data. It is that the numbers in each section do not agree with the numbers in the next one. Market share uses one denominator, campaign performance uses another. Brand search volume gets treated as consideration. Store sales get counted as online incrementality.

Each section says which fields to fill, where the numbers come from, and how to know they are right.

## The flow

The site is a sequence of stages, not a pile of topics. Each stage answers the question you are stuck on at that moment, and each page in it is one solution.


数从哪来 → 怎么扰动 → 怎么读 → 怎么投 → 怎么挪 → 看得见吗 → 查字典


| Stage | Series | You are stuck because | Pages |
|---|---|---|---|

| 入口 | `1-report-overview` — The five charts a market report has to deliver, and how to make each one right | 要交一份报告，先弄清楚交哪几张图 | 7 |
| 数从哪来 | `2-market-research` — Where the numbers come from — how to measure them, and who is in this market | 手上一堆数，不确定能不能信 | 12 |
| 怎么扰动 | `3-experiment-design` — How to perturb the world without designing a broken test | 想知道是不是广告干的，一测就出问题 | 4 |
| 怎么读 | `4-performance-analysis` — How to read what the platforms tell you | 数字到手了，读不出意思 | 5 |
| 怎么投 | `5-campaign-analysis` — The numbers of this campaign or promotion | 这一笔投放本身的数不对劲 | 5 |
| 怎么挪 | `6-budget-optimization` — How to move the money between channels | 几个渠道之间，不知道钱往哪放 | 3 |
| 看得见吗 | `7-brand-visibility` — How many people see you, in search, on social, and inside AI answers | 想知道品牌被多少人看见、被怎么评价 | 9 |
| 查字典 | `8-analysis-toolbox` — Eight tools, one page each | 遇到一个不认识的词 | 8 |

## Running a report

[docs/1-report-overview/01-report-runbook.md](docs/1-report-overview/01-report-runbook.md) is the runbook: eight steps from brief to delivery, each with who does it, what comes out, and how to check it. It also holds the ten-item QA checklist and the prompt shape to hand a step to an AI agent.

The division of labour is short: **a human decides the question, the scope, the definition and signs off; an agent fetches, computes, draws, drafts and cross-links.**

## How the charts work

A chart is a URL with the data in it:

```
https://x-cmd.com/draw/echarts?d=<url-encoded ECharts option>&w=760&h=420
```

Three templates are in use. `/draw/echarts` for data charts, `/draw/mindmap` for structure, `/draw/archmap` for architecture. Each renders SVG with the full data embedded in a `<metadata>` tag, so the chart can be parsed back into numbers.

To redraw a chart with your own data, change the numbers in the `d=` payload. To read a chart's parameters, open it.

## Contributing

Three ways, all small:

- **Fill in a missing field** on an entry page and send a pull request. Every page that links to that entry benefits at the same time.
- **Redraw a chart** with your own numbers — the data is in the URL.
- **Add one public series** to `spec/metric-cards.yml` and to the data source list, and the whole site gains one more number it can look up.

Changing one field changes the whole report. That is the difference between this and a pile of articles.

## Data sources

| Data | How to fetch it |
|---|---|
| EU retail and e-commerce turnover | `x dbnomics data Eurostat/isoc_ec_evaln2/…` |
| EU retail turnover index | `x dbnomics data Eurostat/sts_trtu_m/…` |
| US industry gross output | `x dbnomics data BEA/GDPbyIndustry-26/…` |
| US consumer sentiment | `x dbnomics data SCSMICH/MICS/…` |
| US prices, unemployment | `x dbnomics data bls.cpi` / `bls.unemployment` |
| Advertising measurement, published experiments | cited by paper and journal in the page's data line |

## 中文页

正文目前只有中文版。**全站 53 页的阶段、标题、价值、章节与每节装什么，在 [OUTLINE.yml](OUTLINE.yml)**。

### 你今天卡在哪，从这儿进

| 你卡在哪 | 从这一页开始 |
|---|---|
| 平台给我的数和我自己算的对不上 | 怎么读 · 效果分析 |
| 这个数到底怎么算出来的 | 数从哪来 · 市场调研 |
| 对手是谁、有多大 | 数从哪来 · 市场调研 → 竞品调研 |
| 客户到底怎么想的 | 数从哪来 · 市场调研 → 用户调研 |
| 这次活动值不值 | 怎么投 · 投放分析 → 怎么读 · 效果分析 |
| 下个月的钱往哪放 | 怎么挪 · 预算优化 |
| 品牌现在什么位置 | 看得见吗 · 品牌可见度 |
| 这个词到底指什么 | 查字典 · 工具箱 |


### 入口 · 概览

- 一份市场报告怎么跑出来 — 知道一份报告怎么从零跑出来，每步谁做、做完怎么验  
  <sub>`docs/1-report-overview/01-report-runbook/` · 待写</sub>
- 你说的 23%，跟别人说的 23%，是一回事吗 — 做出一张别人不会误读的市场份额图  
  <sub>`docs/1-report-overview/02-market-share-chart/` · 待写</sub>
- 这门生意还值不值得进 — 判断这门生意还值不值得进  
  <sub>`docs/1-report-overview/03-growth-chart/` · 待写</sub>
- 你的价格，在品类里站得住吗 — 看出自己的价格在品类里站不站得住  
  <sub>`docs/1-report-overview/04-price-band-chart/` · 待写</sub>
- 再花一块钱，能多换回多少 — 知道再花一块钱能多换回多少  
  <sub>`docs/1-report-overview/05-ad-spend-chart/` · 待写</sub>
- **[没有广告，这些单会成交吗](docs/1-report-overview/06-incrementality-chart/cn.md)** — 分清广告赚到的和本来就有的  
  <sub>`docs/1-report-overview/06-incrementality-chart/`</sub>
- 八个工具，一张表 — 知道八个工具各管什么、什么时候查哪个  
  <sub>`docs/1-report-overview/07-eight-tools-in-one-table/` · 待写</sub>

### 数从哪来 · 市场调研

- 进这行之前，先看这三个数 — 写出一份行业条目：四格数字加口径  
  <sub>`docs/2-market-research/01-industry-entry-scale-growth-concentration/` · 待写</sub>
- 这个品类，价格怎么排，促销打多狠 — 写出一份品类条目，画出价格带和促销节奏  
  <sub>`docs/2-market-research/02-category-entry-price-bands-promo-cadence/` · 待写</sub>
- 对手的资料，要经得起别人查 — 写出一份别人能核、也能更新的竞品条目  
  <sub>`docs/2-market-research/03-competitor-entry-schema/` · 待写</sub>
- 两家公司怎么比，才不算比错 — 把两家公司放进一张表比，而且比的是同一件事  
  <sub>`docs/2-market-research/04-head-to-head-share-and-growth/` · 待写</sub>
- 问卷结果可信不可信，先看样本怎么抽的 — 判断一份调研的样本能不能代表你想问的人  
  <sub>`docs/2-market-research/05-survey-sampling/` · 待写</sub>
- 问卷、访谈、后台数据，哪个更接近真相 — 知道三种数据各自偏哪边、怎么互补  
  <sub>`docs/2-market-research/06-survey-interview-behavior-bias/` · 待写</sub>
- 五个卖点只能做一个，按什么排 — 给需求排序时用对的方法，说得清依据  
  <sub>`docs/2-market-research/07-demand-intensity-ranking/` · 待写</sub>
- **[同样一个占比，能有四种算法](docs/2-market-research/08-share-denominator/cn.md)** — 报任何一个份额之前，能说清分母是谁、分子装了什么  
  <sub>`docs/2-market-research/08-share-denominator/`</sub>
- 调研数据和官方数据，哪个更可信 — 知道这两类数各自偏哪边，什么时候该信哪个  
  <sub>`docs/2-market-research/09-panel-vs-census-bias/` · 待写</sub>
- 一个数敢不敢用，先找第二个来源对一遍 — 会给关键数字配第二个来源，知道不一致时先查什么  
  <sub>`docs/2-market-research/10-cross-source-triangulation/` · 待写</sub>
- 这个数漏了谁，用之前先看一眼 — 看出一个数覆盖了谁、没覆盖谁，并在图上标出来  
  <sub>`docs/2-market-research/11-coverage-gaps/` · 待写</sub>
- 季调数和不季调数，别混着用 — 知道两个口径为什么对不上，一张图上该用哪个  
  <sub>`docs/2-market-research/12-seasonal-vs-nsa/` · 待写</sub>

### 怎么扰动 · 实验设计

- 对照组该怎么定 — 知道对照组该长什么样，以及几种常见的错法  
  <sub>`docs/3-experiment-design/01-what-a-control-group-is/` · 待写</sub>
- 样本太少，结论会反着 — 知道差多少算够，为什么小样本会把方向搞反  
  <sub>`docs/3-experiment-design/02-sample-size-and-power/` · 待写</sub>
- 测的组合太多，会看到假效果 — 知道测了一堆组合以后该怎么读结果  
  <sub>`docs/3-experiment-design/03-multiple-testing/` · 待写</sub>
- 一个数，要配一个区间 — 不再只报一个数，习惯带上区间  
  <sub>`docs/3-experiment-design/04-confidence-intervals/` · 待写</sub>

### 怎么读 · 效果分析

- 收入减广告费，不等于赚 — 能把花费和收入放进同一张表，算出自己的真实账  
  <sub>`docs/4-performance-analysis/01-spend-and-revenue-together/` · 待写</sub>
- ROI 最高的渠道，不该加最多钱 — 知道 ROI 排名和加钱顺序不是一回事  
  <sub>`docs/4-performance-analysis/02-roi-ranking-vs-budget-allocation/` · 待写</sub>
- 平台报的数字，和真实效果不是一回事 — 手里有两套数时，知道怎么并列而不混用  
  <sub>`docs/4-performance-analysis/03-platform-metrics-vs-incremental-metrics/` · 待写</sub>
- 再多加一块钱，还赚得回来吗 — 能画出自己渠道的边际曲线，读出拐点  
  <sub>`docs/4-performance-analysis/04-marginal-roi-decay/` · 待写</sub>
- 效果多久才出来，别急着下结论 — 知道效果什么时候才算完，以及怎么判断  
  <sub>`docs/4-performance-analysis/05-did-it-work-three-weeks-later/` · 待写</sub>

### 怎么投 · 投放分析

- 渠道报的 CPM，和你谈下来的，为什么不一样 — 能问对渠道报价里那个 CPM 是怎么算的  
  <sub>`docs/5-campaign-analysis/01-reported-cpm-vs-negotiated-cpm/` · 待写</sub>
- 促销带来的增长，有多少是真的 — 促销结束后能看出真实影响，而不是把提前的量算成增量  
  <sub>`docs/5-campaign-analysis/02-promotion-pulls-demand-forward/` · 待写</sub>
- 素材什么时候该换 — 知道素材的疲劳曲线，以及什么时候该换  
  <sub>`docs/5-campaign-analysis/03-creative-fatigue-ctr-decay/` · 待写</sub>
- 不同地区投广告，贵的贵在哪 — 能读一张地域成本图，知道贵在哪儿  
  <sub>`docs/5-campaign-analysis/04-geo-targeting-cost-map/` · 待写</sub>
- 同样的钱，每天花和周末花不一样 — 知道花钱的节奏本身会改结果  
  <sub>`docs/5-campaign-analysis/05-budget-pacing-even-vs-weekend/` · 待写</sub>

### 怎么挪 · 预算优化

- 钱怎么分，才不会白花 — 知道在什么条件下各渠道边际拉平就是最优  
  <sub>`docs/6-budget-optimization/01-equal-marginal-returns/` · 待写</sub>
- 算最优之前，先把限制列出来 — 动优化之前先把约束列全  
  <sub>`docs/6-budget-optimization/02-state-constraints-first/` · 待写</sub>
- 挪完预算，要复查两件事 — 挪完预算以后能自己查一遍  
  <sub>`docs/6-budget-optimization/03-after-the-shift-what-goes-wrong/` · 待写</sub>

### 看得见吗 · 品牌可见度

- 查一个品牌，能查到些什么 — 用公开信号查出一个品牌的位置  
  <sub>`docs/7-brand-visibility/01-brand-entry-public-signals/` · 待写</sub>
- 品牌有多响，用三把尺子量 — 知道品牌有多响该看哪三个数  
  <sub>`docs/7-brand-visibility/02-visibility-three-measures/` · 待写</sub>
- 搜索里和 AI 回答里，各占多少 — 分别算出搜索里和 AI 答案里的份额  
  <sub>`docs/7-brand-visibility/03-share-of-voice-seo-and-geo/` · 待写</sub>
- 问 AI 同一个问题，答案会变 — 知道 GEO 的数该怎么测才算数  
  <sub>`docs/7-brand-visibility/04-same-question-two-answers/` · 待写</sub>
- 提到你的次数，和说的是好话坏话 — 知道声量为什么要带情绪一起出  
  <sub>`docs/7-brand-visibility/05-volume-without-sentiment-is-blind/` · 待写</sub>
- 品牌词和品类词，看的是两件事 — 分清品牌词和品类词各自说明什么  
  <sub>`docs/7-brand-visibility/06-brand-terms-vs-category-terms/` · 待写</sub>
- 词表排对，后面的数才对 — 排出一张能用的关键词表  
  <sub>`docs/7-brand-visibility/07-keyword-list-triage/` · 待写</sub>
- 交过来的表，要看哪几列 — 知道交过来的表缺哪一列就不能用  
  <sub>`docs/7-brand-visibility/08-the-five-column-table/` · 待写</sub>
- 把四个数放一起看，才知道哪个在动 — 把四条线索并排着读  
  <sub>`docs/7-brand-visibility/09-four-lines-side-by-side/` · 待写</sub>

### 查字典 · 工具箱

- 归因：把功劳分给各个接触点 — 看懂归因在做什么，它什么时候会骗你  
  <sub>`docs/8-analysis-toolbox/01-attribution/` · 待写</sub>
- 增量实验：拿一块地方做对照 — 看懂增量实验的读法与代价  
  <sub>`docs/8-analysis-toolbox/02-incrementality-testing/` · 待写</sub>
- MMM 贡献分解：把长期贡献拆开 — 看懂 MMM 拆出来的贡献是怎么来的  
  <sub>`docs/8-analysis-toolbox/03-mmm-contribution/` · 待写</sub>
- Adstock 衰减：广告的效果会拖多久 — 看懂广告效果随时间衰减的形状  
  <sub>`docs/8-analysis-toolbox/04-adstock-decay/` · 待写</sub>
- Hill 饱和曲线：效果怎么撞天花板 — 看懂饱和曲线两个参数各管什么  
  <sub>`docs/8-analysis-toolbox/05-hill-saturation-curve/` · 待写</sub>
- 边际 ROI 和平均 ROI：两个不同的数 — 不会再把这两个数搞混  
  <sub>`docs/8-analysis-toolbox/06-marginal-vs-average-roi/` · 待写</sub>
- 等边际原则：最优分配的判据 — 知道这个原则说了什么、成立的条件是什么  
  <sub>`docs/8-analysis-toolbox/07-equal-marginal-returns-principle/` · 待写</sub>
- 置信区间和拟合度：模型能信几分 — 知道一个模型的两个可信度指标各管什么  
  <sub>`docs/8-analysis-toolbox/08-confidence-intervals-and-fit/` · 待写</sub>

---

**规划与讨论**：<https://github.com/edwinjhlee/ai/issues/52>
