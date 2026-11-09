# market

**A manual for writing a market and marketing report.** Every figure is an [x-cmd draw](https://github.com/x-cmd/draw) URL: the data lives in the link, server-rendered as SVG. Open any chart and you see its full parameters; paste it anywhere markdown images work.

> The full outline — every stage, every page's title in both languages, what it gives you, its sections and what each section covers — is in **[OUTLINE.yml](OUTLINE.yml)**. The machine-readable metric definitions an agent needs are in **[spec/metric-cards.yml](spec/metric-cards.yml)**.

## The idea

You are writing a report: how big this market is, who is in it, what people buy, where the money goes, what came back, where the next dollar should go. The hard part is not a lack of data. It is that the numbers in each section do not agree with the numbers in the next one. Market share uses one denominator, campaign performance uses another. Brand search volume gets treated as consideration. Store sales get counted as online incrementality.

Each section says which fields to fill, where the numbers come from, and how to know they are right.

## The flow

The site is a sequence of stages, not a pile of topics. Each stage answers the question you are stuck on at that moment, and each page in it is one solution.


数从哪来 → 怎么扰动 → 怎么读 → 怎么投 → 怎么挪 → 看得见吗 → 查字典


| Stage | Series | You are stuck because | Pages |
|---|---|---|---|

| 入口 | `1-report-overview` — The five charts a market report has to deliver, and how to make each one right | 要交一份报告，先弄清楚交哪几张图 | 7 |
| 数从哪来 | `2-market-research` — Where the numbers come from — how to measure them, and who is in this market | 手上一堆数，不确定能不能信 | 14 |
| 怎么扰动 | `3-experiment-design` — How to perturb the world without designing a broken test | 想知道是不是广告干的，一测就出问题 | 4 |
| 怎么读 | `4-performance-analysis` — How to read what the platforms tell you | 数字到手了，读不出意思 | 5 |
| 怎么投 | `5-campaign-analysis` — The numbers of this campaign or promotion | 这一笔投放本身的数不对劲 | 5 |
| 怎么挪 | `6-budget-optimization` — How to move the money between channels | 几个渠道之间，不知道钱往哪放 | 3 |
| 看得见吗 | `7-brand-visibility` — How many people see you, in search, on social, and inside AI answers | 想知道品牌被多少人看见、被怎么评价 | 9 |
| 查字典 | `8-analysis-toolbox` — Eight tools, one page each | 遇到一个不认识的词 | 8 |

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
| US company revenue, gross profit, marketing spend | `https://data.sec.gov/api/xbrl/companyconcept/CIK<cik>/us-gaap/<tag>.json` |
| Advertising measurement, published experiments | cited by paper and journal in the page's data line |

## 中文页

正文目前中英双语的 55 页都在 `docs/` 下，**每篇一个目录，里面是 `cn.md` 与 `en.md`**，图与数字中英共用。

### 你今天卡在哪，从这儿进

| 你卡在哪 | 从这一页开始 |
|---|---|
| 平台给我的数和我自己算的对不上 | 怎么读 · 效果分析 |
| 这个数到底怎么算出来的 | 数从哪来 · 市场调研 |
| 对手是谁、有多大 | 数从哪来 · 市场调研 → 竞品分析 |
| 客户到底怎么想的 | 数从哪来 · 市场调研 → 用户调研 |
| 这次活动值不值 | 怎么投 · 投放分析 → 怎么读 · 效果分析 |
| 下个月的钱往哪放 | 怎么挪 · 预算优化 |
| 品牌现在什么位置 | 看得见吗 · 品牌可见度 |
| 这个词到底指什么 | 查字典 · 工具箱 |


### 入口 · 你要交的那几张图

- [一份市场报告怎么跑出来](docs/1-report-overview/01-report-runbook/cn.md) · [Eight steps turn a market question into a report you can defend](docs/1-report-overview/01-report-runbook/en.md)  
  <sub>`docs/1-report-overview/01-report-runbook/`</sub>
- [你说的 23%，跟别人说的 23%，是一回事吗](docs/1-report-overview/02-market-share-chart/cn.md) · [Two Numbers Called 23% May Not Be the Same Number](docs/1-report-overview/02-market-share-chart/en.md)  
  <sub>`docs/1-report-overview/02-market-share-chart/`</sub>
- [这门生意还值不值得进](docs/1-report-overview/03-growth-chart/cn.md) · [Is This Market Still Worth Entering](docs/1-report-overview/03-growth-chart/en.md)  
  <sub>`docs/1-report-overview/03-growth-chart/`</sub>
- [你的价格，在品类里站得住吗](docs/1-report-overview/04-price-band-chart/cn.md) · [Your price only holds up if the category agrees](docs/1-report-overview/04-price-band-chart/en.md)  
  <sub>`docs/1-report-overview/04-price-band-chart/`</sub>
- [再花一块钱，能多换回多少](docs/1-report-overview/05-ad-spend-chart/cn.md) · [How much does one more dollar of ad spend buy back](docs/1-report-overview/05-ad-spend-chart/en.md)  
  <sub>`docs/1-report-overview/05-ad-spend-chart/`</sub>
- [没有广告，这些单会成交吗](docs/1-report-overview/06-incrementality-chart/cn.md) · [The ROAS on your dashboard is not the return on your next dollar](docs/1-report-overview/06-incrementality-chart/en.md)  
  <sub>`docs/1-report-overview/06-incrementality-chart/`</sub>
- [八个工具，一张表](docs/1-report-overview/07-eight-tools-in-one-table/cn.md) · [Eight tools, one table: pick by the question, not by the number](docs/1-report-overview/07-eight-tools-in-one-table/en.md)  
  <sub>`docs/1-report-overview/07-eight-tools-in-one-table/`</sub>

### 数从哪来 · 数从哪来：怎么量才准，市场里都有谁

- [进这行之前，先看这三个数](docs/2-market-research/01-industry-entry-scale-growth-concentration/cn.md) · [Three numbers decide whether an industry is worth entering](docs/2-market-research/01-industry-entry-scale-growth-concentration/en.md)  
  <sub>`docs/2-market-research/01-industry-entry-scale-growth-concentration/`</sub>
- [这个品类，价格怎么排，促销打多狠](docs/2-market-research/02-category-entry-price-bands-promo-cadence/cn.md) · [The cheapest beef sells 45% of the volume and the priciest sells 26%](docs/2-market-research/02-category-entry-price-bands-promo-cadence/en.md)  
  <sub>`docs/2-market-research/02-category-entry-price-bands-promo-cadence/`</sub>
- [对手的资料，要经得起别人查](docs/2-market-research/03-competitor-entry-schema/cn.md) · [A competitor profile nobody can check is worth nothing](docs/2-market-research/03-competitor-entry-schema/en.md)  
  <sub>`docs/2-market-research/03-competitor-entry-schema/`</sub>
- [两家公司怎么比，才不算比错](docs/2-market-research/04-head-to-head-share-and-growth/cn.md) · [Two companies cannot be compared until their numbers mean the same thing](docs/2-market-research/04-head-to-head-share-and-growth/en.md)  
  <sub>`docs/2-market-research/04-head-to-head-share-and-growth/`</sub>
- [问卷结果可信不可信，先看样本怎么抽的](docs/2-market-research/05-survey-sampling/cn.md) · [A survey's credibility is decided by how the sample was drawn](docs/2-market-research/05-survey-sampling/en.md)  
  <sub>`docs/2-market-research/05-survey-sampling/`</sub>
- [问卷、访谈、后台数据，哪个更接近真相](docs/2-market-research/06-survey-interview-behavior-bias/cn.md) · [Surveys, interviews, and logs each measure something different](docs/2-market-research/06-survey-interview-behavior-bias/en.md)  
  <sub>`docs/2-market-research/06-survey-interview-behavior-bias/`</sub>
- [五个卖点只能做一个，按什么排](docs/2-market-research/07-demand-intensity-ranking/cn.md) · [Five selling points, one priority: the yardstick decides the winner](docs/2-market-research/07-demand-intensity-ranking/en.md)  
  <sub>`docs/2-market-research/07-demand-intensity-ranking/`</sub>
- [同样一个占比，能有四种算法](docs/2-market-research/08-share-denominator/cn.md) · [One percentage, four different numbers](docs/2-market-research/08-share-denominator/en.md)  
  <sub>`docs/2-market-research/08-share-denominator/`</sub>
- [调研数据和官方数据，哪个更可信](docs/2-market-research/09-panel-vs-census-bias/cn.md) · [A survey and an official statistic each miss a different half of the market](docs/2-market-research/09-panel-vs-census-bias/en.md)  
  <sub>`docs/2-market-research/09-panel-vs-census-bias/`</sub>
- [一个数敢不敢用，先找第二个来源对一遍](docs/2-market-research/10-cross-source-triangulation/cn.md) · [A number is worth nothing until a second source has tried to break it](docs/2-market-research/10-cross-source-triangulation/en.md)  
  <sub>`docs/2-market-research/10-cross-source-triangulation/`</sub>
- [这个数漏了谁，用之前先看一眼](docs/2-market-research/11-coverage-gaps/cn.md) · [Every percentage comes from a frame, and the frame is not everything](docs/2-market-research/11-coverage-gaps/en.md)  
  <sub>`docs/2-market-research/11-coverage-gaps/`</sub>
- [季调数和不季调数，别混着用](docs/2-market-research/12-seasonal-vs-nsa/cn.md) · [One month, two numbers, opposite stories](docs/2-market-research/12-seasonal-vs-nsa/en.md)  
  <sub>`docs/2-market-research/12-seasonal-vs-nsa/`</sub>
- [跑鞋这行，Nike 的营收三年没长，Hoka 的母公司五年翻了一倍](docs/2-market-research/13-running-shoes-competitors/cn.md) · [Nike's revenue has not grown in three years. HOKA's parent doubled in five](docs/2-market-research/13-running-shoes-competitors/en.md)  
  <sub>`docs/2-market-research/13-running-shoes-competitors/`</sub>
- [网站分析开源项目里，umami 的 fork 数排第一，star 排第二](docs/2-market-research/14-analytics-tools-competitors/cn.md) · [Umami leads on forks among open-source web analytics tools, and sits second on stars](docs/2-market-research/14-analytics-tools-competitors/en.md)  
  <sub>`docs/2-market-research/14-analytics-tools-competitors/`</sub>

### 怎么扰动 · 怎么扰动：设计一个不出错的实验

- [对照组该怎么定](docs/3-experiment-design/01-what-a-control-group-is/cn.md) · [A bad control group is worse than no control group](docs/3-experiment-design/01-what-a-control-group-is/en.md)  
  <sub>`docs/3-experiment-design/01-what-a-control-group-is/`</sub>
- [样本太少，结论会反着](docs/3-experiment-design/02-sample-size-and-power/cn.md) · [A small sample can invert the answer, not only blur it](docs/3-experiment-design/02-sample-size-and-power/en.md)  
  <sub>`docs/3-experiment-design/02-sample-size-and-power/`</sub>
- [测的组合太多，会看到假效果](docs/3-experiment-design/03-multiple-testing/cn.md) · [Twenty combinations tested, and three of them are noise](docs/3-experiment-design/03-multiple-testing/en.md)  
  <sub>`docs/3-experiment-design/03-multiple-testing/`</sub>
- [一个数，要配一个区间](docs/3-experiment-design/04-confidence-intervals/cn.md) · [A number without its interval is half an answer](docs/3-experiment-design/04-confidence-intervals/en.md)  
  <sub>`docs/3-experiment-design/04-confidence-intervals/`</sub>

### 怎么读 · 怎么读：这类数到底说明了什么

- [收入减广告费，不等于赚](docs/4-performance-analysis/01-spend-and-revenue-together/cn.md) · [Revenue minus ad spend is not profit](docs/4-performance-analysis/01-spend-and-revenue-together/en.md)  
  <sub>`docs/4-performance-analysis/01-spend-and-revenue-together/`</sub>
- [ROI 最高的渠道，不该加最多钱](docs/4-performance-analysis/02-roi-ranking-vs-budget-allocation/cn.md) · [The highest-ROI channel is not the one that deserves the next dollar](docs/4-performance-analysis/02-roi-ranking-vs-budget-allocation/en.md)  
  <sub>`docs/4-performance-analysis/02-roi-ranking-vs-budget-allocation/`</sub>
- [平台报的数字，和真实效果不是一回事](docs/4-performance-analysis/03-platform-metrics-vs-incremental-metrics/cn.md) · [Two numbers on the same ad spend answer two different questions](docs/4-performance-analysis/03-platform-metrics-vs-incremental-metrics/en.md)  
  <sub>`docs/4-performance-analysis/03-platform-metrics-vs-incremental-metrics/`</sub>
- [再多加一块钱，还赚得回来吗](docs/4-performance-analysis/04-marginal-roi-decay/cn.md) · [One more dollar on that channel, will it still earn its keep](docs/4-performance-analysis/04-marginal-roi-decay/en.md)  
  <sub>`docs/4-performance-analysis/04-marginal-roi-decay/`</sub>
- [效果多久才出来，别急着下结论](docs/4-performance-analysis/05-did-it-work-three-weeks-later/cn.md) · [A 1% lift three weeks in is not a verdict](docs/4-performance-analysis/05-did-it-work-three-weeks-later/en.md)  
  <sub>`docs/4-performance-analysis/05-did-it-work-three-weeks-later/`</sub>

### 怎么投 · 怎么投：这一笔投放本身的数

- [渠道报的 CPM，和你谈下来的，为什么不一样](docs/5-campaign-analysis/01-reported-cpm-vs-negotiated-cpm/cn.md) · [Two CPM numbers, one budget, and no one is cheating](docs/5-campaign-analysis/01-reported-cpm-vs-negotiated-cpm/en.md)  
  <sub>`docs/5-campaign-analysis/01-reported-cpm-vs-negotiated-cpm/`</sub>
- [促销带来的增长，有多少是真的](docs/5-campaign-analysis/02-promotion-pulls-demand-forward/cn.md) · [A promotion that lifts the report by 40% may have added nothing at all](docs/5-campaign-analysis/02-promotion-pulls-demand-forward/en.md)  
  <sub>`docs/5-campaign-analysis/02-promotion-pulls-demand-forward/`</sub>
- [素材什么时候该换](docs/5-campaign-analysis/03-creative-fatigue-ctr-decay/cn.md) · [Your creative is not getting worse. Your audience is getting tired of it.](docs/5-campaign-analysis/03-creative-fatigue-ctr-decay/en.md)  
  <sub>`docs/5-campaign-analysis/03-creative-fatigue-ctr-decay/`</sub>
- [不同地区投广告，贵的贵在哪](docs/5-campaign-analysis/04-geo-targeting-cost-map/cn.md) · [The same budget buys three times as many impressions in Germany as in the United States](docs/5-campaign-analysis/04-geo-targeting-cost-map/en.md)  
  <sub>`docs/5-campaign-analysis/04-geo-targeting-cost-map/`</sub>
- [同样的钱，每天花和周末花不一样](docs/5-campaign-analysis/05-budget-pacing-even-vs-weekend/cn.md) · [The same budget buys 14,286 more impressions when you spread it out](docs/5-campaign-analysis/05-budget-pacing-even-vs-weekend/en.md)  
  <sub>`docs/5-campaign-analysis/05-budget-pacing-even-vs-weekend/`</sub>

### 怎么挪 · 怎么挪：几个渠道之间钱怎么分

- [钱怎么分，才不会白花](docs/6-budget-optimization/01-equal-marginal-returns/cn.md) · [The best split is the one where every channel's last dollar earns the same](docs/6-budget-optimization/01-equal-marginal-returns/en.md)  
  <sub>`docs/6-budget-optimization/01-equal-marginal-returns/`</sub>
- [算最优之前，先把限制列出来](docs/6-budget-optimization/02-state-constraints-first/cn.md) · [A solver cannot check reality for you](docs/6-budget-optimization/02-state-constraints-first/en.md)  
  <sub>`docs/6-budget-optimization/02-state-constraints-first/`</sub>
- [挪完预算，要复查两件事](docs/6-budget-optimization/03-after-the-shift-what-goes-wrong/cn.md) · [A flat report after a budget shift usually means you read it too early](docs/6-budget-optimization/03-after-the-shift-what-goes-wrong/en.md)  
  <sub>`docs/6-budget-optimization/03-after-the-shift-what-goes-wrong/`</sub>

### 看得见吗 · 看得见吗：在搜索、社媒、AI 里被看见多少

- [查一个品牌，能查到些什么](docs/7-brand-visibility/01-brand-entry-public-signals/cn.md) · [Every brand number comes with a receipt, or it does not count](docs/7-brand-visibility/01-brand-entry-public-signals/en.md)  
  <sub>`docs/7-brand-visibility/01-brand-entry-public-signals/`</sub>
- [品牌有多响，用三把尺子量](docs/7-brand-visibility/02-visibility-three-measures/cn.md) · [Three numbers decide how visible a brand is, and none of them covers the others](docs/7-brand-visibility/02-visibility-three-measures/en.md)  
  <sub>`docs/7-brand-visibility/02-visibility-three-measures/`</sub>
- [搜索里和 AI 回答里，各占多少](docs/7-brand-visibility/03-share-of-voice-seo-and-geo/cn.md) · [On leads search and disappears from AI; Saucony does the reverse](docs/7-brand-visibility/03-share-of-voice-seo-and-geo/en.md)  
  <sub>`docs/7-brand-visibility/03-share-of-voice-seo-and-geo/`</sub>
- [问 AI 同一个问题，答案会变](docs/7-brand-visibility/04-same-question-two-answers/cn.md) · [Ask the same question twice and the model gives two different answers](docs/7-brand-visibility/04-same-question-two-answers/en.md)  
  <sub>`docs/7-brand-visibility/04-same-question-two-answers/`</sub>
- [提到你的次数，和说的是好话坏话](docs/7-brand-visibility/05-volume-without-sentiment-is-blind/cn.md) · [Volume tells you how many people talked, not whether they were happy](docs/7-brand-visibility/05-volume-without-sentiment-is-blind/en.md)  
  <sub>`docs/7-brand-visibility/05-volume-without-sentiment-is-blind/`</sub>
- [品牌词和品类词，看的是两件事](docs/7-brand-visibility/06-brand-terms-vs-category-terms/cn.md) · [A brand term and a category term answer two different questions](docs/7-brand-visibility/06-brand-terms-vs-category-terms/en.md)  
  <sub>`docs/7-brand-visibility/06-brand-terms-vs-category-terms/`</sub>
- [词表排对，后面的数才对](docs/7-brand-visibility/07-keyword-list-triage/cn.md) · [A keyword list is only worth the rows you can defend](docs/7-brand-visibility/07-keyword-list-triage/en.md)  
  <sub>`docs/7-brand-visibility/07-keyword-list-triage/`</sub>
- [交过来的表，要看哪几列](docs/7-brand-visibility/08-the-five-column-table/cn.md) · [A table with one missing column will hand you the wrong answer](docs/7-brand-visibility/08-the-five-column-table/en.md)  
  <sub>`docs/7-brand-visibility/08-the-five-column-table/`</sub>
- [把四个数放一起看，才知道哪个在动](docs/7-brand-visibility/09-four-lines-side-by-side/cn.md) · [Four numbers, one brand, and only one of them moved](docs/7-brand-visibility/09-four-lines-side-by-side/en.md)  
  <sub>`docs/7-brand-visibility/09-four-lines-side-by-side/`</sub>

### 查字典 · 查字典：术语与方法

- [归因：把功劳分给各个接触点](docs/8-analysis-toolbox/01-attribution/cn.md) · [The 260 orders search ads "brought in" are a rule, not a finding](docs/8-analysis-toolbox/01-attribution/en.md)  
  <sub>`docs/8-analysis-toolbox/01-attribution/`</sub>
- [增量实验：拿一块地方做对照](docs/8-analysis-toolbox/02-incrementality-testing/cn.md) · [Incrementality is measured by withholding a slice of the map](docs/8-analysis-toolbox/02-incrementality-testing/en.md)  
  <sub>`docs/8-analysis-toolbox/02-incrementality-testing/`</sub>
- [MMM 贡献分解：把长期贡献拆开](docs/8-analysis-toolbox/03-mmm-contribution/cn.md) · [The 14% your TV ads "produced" is a setting, not a measurement](docs/8-analysis-toolbox/03-mmm-contribution/en.md)  
  <sub>`docs/8-analysis-toolbox/03-mmm-contribution/`</sub>
- [Adstock 衰减：广告的效果会拖多久](docs/8-analysis-toolbox/04-adstock-decay/cn.md) · [Your ads keep working after you stop paying for them](docs/8-analysis-toolbox/04-adstock-decay/en.md)  
  <sub>`docs/8-analysis-toolbox/04-adstock-decay/`</sub>
- [Hill 饱和曲线：效果怎么撞天花板](docs/8-analysis-toolbox/05-hill-saturation-curve/cn.md) · [The extra 100,000 buys you 0 orders, or 30, or 3. The Hill curve says which](docs/8-analysis-toolbox/05-hill-saturation-curve/en.md)  
  <sub>`docs/8-analysis-toolbox/05-hill-saturation-curve/`</sub>
- [边际 ROI 和平均 ROI：两个不同的数](docs/8-analysis-toolbox/06-marginal-vs-average-roi/cn.md) · [Your channel's ROI is 2.28x. That number cannot tell you whether to spend more](docs/8-analysis-toolbox/06-marginal-vs-average-roi/en.md)  
  <sub>`docs/8-analysis-toolbox/06-marginal-vs-average-roi/`</sub>
- [等边际原则：最优分配的判据](docs/8-analysis-toolbox/07-equal-marginal-returns-principle/cn.md) · [A budget split is only optimal when every channel's next dollar earns the same](docs/8-analysis-toolbox/07-equal-marginal-returns-principle/en.md)  
  <sub>`docs/8-analysis-toolbox/07-equal-marginal-returns-principle/`</sub>
- [置信区间和拟合度：模型能信几分](docs/8-analysis-toolbox/08-confidence-intervals-and-fit/cn.md) · [A good fit does not mean a trustworthy number](docs/8-analysis-toolbox/08-confidence-intervals-and-fit/en.md)  
  <sub>`docs/8-analysis-toolbox/08-confidence-intervals-and-fit/`</sub>

---

**规划与讨论**：<https://github.com/edwinjhlee/ai/issues/52>
