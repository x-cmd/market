# market

**A manual for writing a market and marketing report.** Every figure is an [x-cmd draw](https://github.com/x-cmd/draw) URL: the data lives in the link, server-rendered as SVG. Open any chart and you see its full parameters; paste it anywhere markdown images work.

> The full outline — every page's title, its sections and what each section covers — is in **[OUTLINE.yml](OUTLINE.yml)**.

## The idea

You are writing a report: how big this market is, who is in it, what people buy, where the money goes, what came back, where the next dollar should go. The hard part is not a lack of data. It is that the numbers in each section do not agree with the numbers in the next one. Market share uses one denominator, campaign performance uses another. Brand search volume gets treated as consideration. Store sales get counted as online incrementality.

Each section says which fields to fill, where the numbers come from, and how to know they are right.

## The sections

The site follows the table of contents of the report itself.

| Series | What it covers | Pages |
|---|---|---|
| `1-overview` | The five charts a market report has to deliver, and how to make each one right | 5 |
| `2-market` | How big this market is, and whether the number you have can be trusted | 7 |
| `3-competitor` | Who you are competing with, and how big they are | 2 |
| `4-user` | Who is buying, and whether your survey tells you anything | 3 |
| `5-ad` | The numbers of this campaign or promotion | 5 |
| `6-result` | What the money you spent actually brought back | 9 |
| `7-budget` | How to split the money across channels | 3 |
| `8-brand` | Where your brand shows up, and how people talk about it | 9 |
| `9-glossary` | Eight tools, one page each | 9 |
| | **Total** | **52** |

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
- **Add one public series** to the data source list, and the whole site gains one more number it can look up.

Changing one field changes the whole report. That is the difference between this and a pile of articles.

## Data sources

| Data | How to fetch it |
|---|---|
| EU retail and e-commerce turnover | `x dbnomics data Eurostat/isoc_ec_evaln2/…` |
| US industry gross output and concentration | `x dbnomics data BEA/GDPbyIndustry-26/…` |
| US consumer sentiment | `x dbnomics data SCSMICH/MICS/…` |
| US prices, unemployment | `x dbnomics data bls.cpi` / `bls.unemployment` |
| Advertising measurement, published experiments | cited by paper and journal in the page's data line |

## 中文页

正文目前只有中文版。**全站 52 页的标题、章节与每节装什么，在 [OUTLINE.yml](OUTLINE.yml)**。

### 你今天卡在哪，从这儿进

| 你卡在哪 | 从这一页开始 |
|---|---|
| 平台给我的数和我自己算的对不上 | [没有广告，这些单会成交吗](docs/1-overview/05-incrementality-chart/cn.md) → 投放效果 → 客户 |
| 市场份额到底怎么算 | 市场规模 → 你的份额和别人比之前，先说清分母 |
| 对手有多大 | 竞争对手 → 市场规模 |
| 客户到底怎么想的 | 客户 → 投放效果 |
| 这次活动值不值 | 广告投放 → 投放效果 |
| 下个月的钱往哪放 | 预算分配 → 投放效果 |
| 品牌现在什么位置 | 品牌 → 竞争对手 |
| 这个词到底指什么 | 名词解释 |


### 1-overview · 你要交的那几张图

- 你的市场份额，别人是按哪个分母在算  
  <sub>`docs/1-overview/01-market-share-chart/` · 待写</sub>
- 这门生意还值不值得进  
  <sub>`docs/1-overview/02-growth-chart/` · 待写</sub>
- 你的价格，在品类里站得住吗  
  <sub>`docs/1-overview/03-price-band-chart/` · 待写</sub>
- 再花一块钱，能多换回多少  
  <sub>`docs/1-overview/04-ad-spend-chart/` · 待写</sub>
- **[没有广告，这些单会成交吗](docs/1-overview/05-incrementality-chart/cn.md)**  
  <sub>`docs/1-overview/05-incrementality-chart/`</sub>

### 2-market · 市场规模，以及你手上的数能不能信

- 进这行之前，先看这三个数  
  <sub>`docs/2-market/11-industry-entry-scale-growth-concentration/` · 待写</sub>
- **[你的份额和别人比之前，先说清分母](docs/2-market/01-share-denominator/cn.md)**  
  <sub>`docs/2-market/01-share-denominator/`</sub>
- 调研数据和官方数据，哪个更可信  
  <sub>`docs/2-market/02-panel-vs-census-bias/` · 待写</sub>
- 一个数敢不敢用，先找第二个来源对一遍  
  <sub>`docs/2-market/03-cross-source-triangulation/` · 待写</sub>
- 这个数漏了谁，用之前先看一眼  
  <sub>`docs/2-market/04-coverage-gaps/` · 待写</sub>
- 季调数和不季调数，别混着用  
  <sub>`docs/2-market/05-seasonal-vs-nsa/` · 待写</sub>
- 这个品类，价格怎么排，促销打多狠  
  <sub>`docs/2-market/12-category-entry-price-bands-promo-cadence/` · 待写</sub>

### 3-competitor · 对手是谁、有多大

- 写竞品，别人才核得了你的数  
  <sub>`docs/3-competitor/06-competitor-entry-schema/` · 待写</sub>
- 两家公司怎么比，才不算比错  
  <sub>`docs/3-competitor/07-head-to-head-share-and-growth/` · 待写</sub>

### 4-user · 谁在买，你的调研说明不了什么

- 问卷结果可信不可信，先看样本怎么抽的  
  <sub>`docs/4-user/08-survey-sampling/` · 待写</sub>
- 问卷、访谈、后台数据，哪个更接近真相  
  <sub>`docs/4-user/09-survey-interview-behavior-bias/` · 待写</sub>
- 五个卖点只能做一个，按什么排  
  <sub>`docs/4-user/10-demand-intensity-ranking/` · 待写</sub>

### 5-ad · 这一笔投放、这次促销本身的数

- 渠道报的 CPM，和你谈下来的，为什么不一样  
  <sub>`docs/5-ad/01-reported-cpm-vs-negotiated-cpm/` · 待写</sub>
- 促销带来的增长，有多少是真的  
  <sub>`docs/5-ad/02-promotion-pulls-demand-forward/` · 待写</sub>
- 素材什么时候该换  
  <sub>`docs/5-ad/03-creative-fatigue-ctr-decay/` · 待写</sub>
- 不同地区投广告，贵的贵在哪  
  <sub>`docs/5-ad/04-geo-targeting-cost-map/` · 待写</sub>
- 同样的钱，每天花和周末花不一样  
  <sub>`docs/5-ad/05-budget-pacing-even-vs-weekend/` · 待写</sub>

### 6-result · 花出去的钱到底换回了什么

- 收入减广告费，不等于赚  
  <sub>`docs/6-result/01-spend-and-revenue-together/` · 待写</sub>
- ROI 最高的渠道，不该加最多钱  
  <sub>`docs/6-result/02-roi-ranking-vs-budget-allocation/` · 待写</sub>
- 平台报的数字，和真实效果不是一回事  
  <sub>`docs/6-result/03-platform-metrics-vs-incremental-metrics/` · 待写</sub>
- 加预算之前，先看边际回报  
  <sub>`docs/6-result/04-marginal-roi-decay/` · 待写</sub>
- 效果多久才出来，别急着下结论  
  <sub>`docs/6-result/05-did-it-work-three-weeks-later/` · 待写</sub>
- 对照组该怎么定  
  <sub>`docs/6-result/01-what-a-control-group-is/` · 待写</sub>
- 样本太少，结论会反着  
  <sub>`docs/6-result/02-sample-size-and-power/` · 待写</sub>
- 测的组合太多，会看到假效果  
  <sub>`docs/6-result/03-multiple-testing/` · 待写</sub>
- 一个数，要配一个区间  
  <sub>`docs/6-result/04-confidence-intervals/` · 待写</sub>

### 7-budget · 几个渠道之间，钱怎么分

- 钱怎么分，才不会白花  
  <sub>`docs/7-budget/01-equal-marginal-returns/` · 待写</sub>
- 算最优之前，先把限制列出来  
  <sub>`docs/7-budget/02-state-constraints-first/` · 待写</sub>
- 挪完预算，要复查两件事  
  <sub>`docs/7-budget/03-after-the-shift-what-goes-wrong/` · 待写</sub>

### 8-brand · 品牌在哪儿出现，人们怎么议论它

- 你的牌子现在什么位置，能查到的公开信号都在这儿  
  <sub>`docs/8-brand/13-brand-entry-public-signals/` · 待写</sub>
- 品牌有多响，用三把尺子量  
  <sub>`docs/8-brand/01-visibility-three-measures/` · 待写</sub>
- 搜索里和 AI 回答里，各占多少  
  <sub>`docs/8-brand/02-share-of-voice-seo-and-geo/` · 待写</sub>
- 问 AI 同一个问题，答案会变  
  <sub>`docs/8-brand/03-same-question-two-answers/` · 待写</sub>
- 提到你的次数，和说的是好话坏话  
  <sub>`docs/8-brand/04-volume-without-sentiment-is-blind/` · 待写</sub>
- 品牌词和品类词，看的是两件事  
  <sub>`docs/8-brand/05-brand-terms-vs-category-terms/` · 待写</sub>
- 词表排对，后面的数才对  
  <sub>`docs/8-brand/06-keyword-list-triage/` · 待写</sub>
- 交过来的表，要看哪几列  
  <sub>`docs/8-brand/07-the-five-column-table/` · 待写</sub>
- 把四个数放一起看，才知道哪个在动  
  <sub>`docs/8-brand/08-four-lines-side-by-side/` · 待写</sub>

### 9-glossary · 八个工具，各一页

- 八个工具，一张表  
  <sub>`docs/9-glossary/00-toolbox-overview/` · 待写</sub>
- 归因：把功劳分给各个接触点  
  <sub>`docs/9-glossary/01-attribution/` · 待写</sub>
- 增量实验：拿一块地方做对照  
  <sub>`docs/9-glossary/02-incrementality-testing/` · 待写</sub>
- MMM 贡献分解：把长期贡献拆开  
  <sub>`docs/9-glossary/03-mmm-contribution/` · 待写</sub>
- Adstock 衰减：广告的效果会拖多久  
  <sub>`docs/9-glossary/04-adstock-decay/` · 待写</sub>
- Hill 饱和曲线：效果怎么撞天花板  
  <sub>`docs/9-glossary/05-hill-saturation-curve/` · 待写</sub>
- 边际 ROI 和平均 ROI：两个不同的数  
  <sub>`docs/9-glossary/06-marginal-vs-average-roi/` · 待写</sub>
- 等边际原则：最优分配的判据  
  <sub>`docs/9-glossary/07-equal-marginal-returns-principle/` · 待写</sub>
- 置信区间和拟合度：模型能信几分  
  <sub>`docs/9-glossary/08-confidence-intervals-and-fit/` · 待写</sub>

---

**规划与讨论**：<https://github.com/edwinjhlee/ai/issues/52>
