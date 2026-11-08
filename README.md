# market

**A manual for writing a market and marketing report.** Every figure is an [x-cmd draw](https://github.com/x-cmd/draw) URL: the data lives in the link, server-rendered as SVG. Open any chart and you see its full parameters; paste it anywhere markdown images work.

> The site itself is a set of pages, not this README. The full table of contents — every page's title, outline, goal, case study and intended reader — is in **[docs/1-overview/00-site-outline/cn.md](docs/1-overview/00-site-outline/cn.md)**.

## The idea

You are writing a report: how big this market is, who is in it, what people buy, where the money goes, what came back, where the next dollar should go. The hard part is not a lack of data. It is that the numbers in each section do not agree with the numbers in the next one. Market share uses one denominator, campaign performance uses another. Brand search volume gets treated as consideration. Store sales get counted as online incrementality.

Each section on this site says which fields to fill, where the numbers come from, and how to know they are right.

## The sections

The site follows the table of contents of the report itself.

| Series | What it covers | Pages |
|---|---|---|
| [`1-overview`](docs/1-overview/) | What this site is, and five situations that expose the measurement problem | 6 |
| [`2-research`](docs/2-research/) | How to measure these numbers without fooling yourself — plus entries for competitors, industries, categories, brands and users | 13 |
| `3-experiment` | Designing the test that will actually answer your question | 4 |
| `4-analytics` | What the numbers the platforms give you actually say | 5 |
| `5-media` | The numbers of this particular campaign or promotion | 5 |
| `6-optimization` | How to split money across several channels | 3 |
| `7-visibility` | How many people see you in search, on social, and inside AI answers | 8 |
| `8-toolbox` | Eight tools, one page each — a dictionary, not a course | 9 |
| | **Total** | **53** |

## How the charts work

A chart is a URL with the data in it:

```
https://x-cmd.com/draw/echarts?d=<url-encoded ECharts option>&w=760&h=420
```

Three templates are in use. `/draw/echarts` for data charts, `/draw/mindmap` for structure, `/draw/archmap` for architecture. Each one renders SVG with the full data embedded in a `<metadata>` tag, so the chart can be parsed back into numbers.

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

正文目前只有中文版。**全站 53 页的标题、大纲、目标、案例、适合谁读，在 [docs/1-overview/00-site-outline/cn.md](docs/1-overview/00-site-outline/cn.md)**——那是这个站的总纲页。

### 1-overview · 这个站是什么，以及五个能戳中测量难题的场景

- **[这份报告长什么样：全站 55 页的目录、大纲和目标](docs/1-overview/00-site-outline/cn.md)** —— 知道这个站在写什么、每一节归谁管、自己要的东西在哪一页  
  <sub>适合谁读：S1 S2 S3 S4</sub>
- **[平台报你 ROI 4.0，实验测出来是 −63%](docs/1-overview/01-platform-roi-vs-incremental-roi/cn.md)** —— 分清平台报表上的数和你自己测出来的数，看出两者差多少  
  <sub>适合谁读：S1 S2 S4</sub>
- 美国电商 2025 占零售 16.4%，比 2024 高 0.3 个百分点 —— 读懂任何一个「线上占比 X%」，知道它的分母站在哪一边  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 钱花到这一段就不值了，这条线画得出来 —— 知道自己这行的钱花到哪儿开始不划算  
  <sub>适合谁读：S1 S2 · 待写</sub>
- 品牌搜索量能当考虑度吗：拿什么交叉验证 —— 知道品牌搜索量能说明什么、不能说明什么  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 一次 Geo 实验，让五个渠道共用一个对照组 —— 知道怎么用一块停投的地方，同时回答五个渠道的问题  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>

### 2-research · 这类数怎么量才准，以及竞品、行业、品类、品牌、用户各一页

- **[份额的分母，先定清楚再说](docs/2-research/01-share-denominator/cn.md)** —— 报任何一个份额之前，能说清分母是谁、分子装了什么、自己在不在框里  
  <sub>适合谁读：S2 S4</sub>
- 面板数据和全量统计，偏差方向相反 —— 知道这两类数各自偏哪边，什么时候该信哪个  
  <sub>适合谁读：S4 · 待写</sub>
- 同一个数，用两个来源各出一次 —— 会给关键数字配第二个来源，并且知道两个来源不一致时先查什么  
  <sub>适合谁读：S4 · 待写</sub>
- 样本覆盖不到的地方，图上要留白 —— 看出一个数覆盖了谁、没覆盖谁，并且能在图上标出来  
  <sub>适合谁读：S4 · 待写</sub>
- 季调数和非季调数，别混着画 —— 知道两个口径为什么对不上，一张图上该用哪个  
  <sub>适合谁读：S3 S4 · 待写</sub>
- 竞品条目怎么写：来源、口径、时间 —— 能写出一份别人能查、也能更新的竞品条目  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 两家并排比：份额与增速 —— 把两家公司放进一张表里比，而且比的是同一件事  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 用户调研的数，先看样本怎么抽的 —— 拿到一份调研结果，先判断这个样本能不能代表你想问的人  
  <sub>适合谁读：S4 · 待写</sub>
- 问卷、访谈、行为数据，三种偏差方向 —— 知道三种数据各自偏哪边，什么时候能互相补  
  <sub>适合谁读：S4 · 待写</sub>
- 需求强度怎么排：别用平均数 —— 给需求排序时用对的方法，并能说清排序依据  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 行业条目：规模、增速、集中度 —— 能写出一份行业条目：四格数字加口径  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 品类条目：价格带与促销奏 —— 能写出一份品类条目，画出价格带和促销节奏  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 品牌条目：公开信号与它们的口径 —— 能查出一个品牌的位置，用的全是公开可查的数  
  <sub>适合谁读：S2 S4 · 待写</sub>

### 3-experiment · 怎么设计一个真能回答你问题的实验

- 对照组不是「没投的那群人」那么简单 —— 知道对照组该长什么样，以及几种常见的错法  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- 样本量不够，结论连方向都可能错 —— 知道差多少算够，以及为什么小样本会让你把方向搞反  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 多重检验：测的组越多，假阳性越多 —— 知道测了一堆组合以后该怎么读结果  
  <sub>适合谁读：S4 · 待写</sub>
- 置信区间比那个点估计值更重要 —— 不再只报一个数，习惯带上区间  
  <sub>适合谁读：S2 S3 S4 · 待写</sub>

### 4-analytics · 平台给你的那些数，到底说明了什么

- 花费和收入放在一起看，才知道赚没赚 —— 能把花费和收入放进同一张表，算出自己的真实账  
  <sub>适合谁读：S1 S2 · 待写</sub>
- 渠道 ROI 排序，不等于该往哪加钱 —— 知道 ROI 排名和加钱顺序不是一回事  
  <sub>适合谁读：S1 S2 · 待写</sub>
- 平台口径和增量口径，是两套账 —— 手里同时有两套数时，知道怎么并列而不混用  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- 边际 ROI 往下掉，平均 ROI 看不出来 —— 能画出自己渠道的边际曲线，并读出拐点  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- 三周之后再看，那次变化到底是不是它造成的 —— 知道一次投放的效果什么时候才算完，以及怎么判断  
  <sub>适合谁读：S2 S3 S4 · 待写</sub>

### 5-media · 这一笔投放、这次促销本身的数

- 渠道报表里的 CPM，和你能谈下来的 CPM 不是一个口径 —— 能问对渠道报价里那个 CPM 是怎么算出来的  
  <sub>适合谁读：S1 S2 S3 · 待写</sub>
- 促销把需求提前了，这条折线会拐 —— 促销结束后能看出真实影响，而不是把提前的量算成增量  
  <sub>适合谁读：S1 S2 · 待写</sub>
- 素材疲劳：同一素材的 CTR 会自己往下掉 —— 知道素材的疲劳曲线，以及什么时候该换  
  <sub>适合谁读：S1 S3 · 待写</sub>
- 地域投放图：哪里便宜、哪里贵 —— 能读一张地域成本图，知道贵在哪儿  
  <sub>适合谁读：S1 S2 · 待写</sub>
- 预算节奏：一天均匀花和集中在周末花，数不一样 —— 知道花钱的节奏本身会改结果  
  <sub>适合谁读：S1 S3 · 待写</sub>

### 6-optimization · 几个渠道之间，钱怎么分

- 等边际原则：各渠道边际 ROI 拉平即最优 —— 知道在什么条件下各渠道边际拉平就是最优  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- 约束条件先写清楚，再谈最优 —— 动优化之前先把约束列全  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 挪钱之后：两件你会算错的事 —— 挪完预算以后能自己查一遍  
  <sub>适合谁读：S1 S2 · 待写</sub>

### 7-visibility · 在搜索、社媒和 AI 答案里，有多少人看得见你

- 可见度是三把尺子：份额、位次、情绪 —— 知道可见度不是一个数，是三个  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 份额怎么算：SEO 一种，GEO 一种 —— 能算出搜索里的份额，和 AI 答案里的份额  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 同一个问题问两次，答案不一样 —— 知道 GEO 的数要问很多次，以及为什么一次不算数  
  <sub>适合谁读：S4 · 待写</sub>
- 光有声量不够，情绪得一起出 —— 知道声量为什么要带情绪  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 品牌词看健康，品类词看机会 —— 知道品牌词和品类词各自能告诉你什么  
  <sub>适合谁读：S2 S4 · 待写</sub>
- 词表排错，后面全错 —— 会排一张关键词表  
  <sub>适合谁读：S3 S4 · 待写</sub>
- 进来的是一张表，五个字段 —— 知道交上来的表长什么样，缺哪一列就不能用  
  <sub>适合谁读：S3 S4 · 待写</sub>
- 把四条线并排，才知道哪条在动 —— 能把多条可见度线索并排着读  
  <sub>适合谁读：S2 S4 · 待写</sub>

### 8-toolbox · 八个工具各一页——是字典，不是课程

- 工具箱总览：八个工具一张表 —— 知道八个工具各自管什么、什么时候用  
  <sub>适合谁读：S1 S2 S3 S4 · 待写</sub>
- 归因：把功劳分给各个接触点 —— 看懂归因在做什么，它什么时候会骗你  
  <sub>适合谁读：S4 · 待写</sub>
- 增量实验：拿一块地方做对照 —— 看懂增量实验的读法与代价  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- MMM 贡献分解：把长期贡献拆开 —— 看懂 MMM 拆出来的贡献是怎么来的  
  <sub>适合谁读：S4 · 待写</sub>
- Adstock 衰减：广告的效果会拖多久 —— 看懂广告效果随时间衰减的形状  
  <sub>适合谁读：S4 · 待写</sub>
- Hill 饱和曲线：效果怎么撞天花板 —— 看懂饱和曲线两个参数各管什么  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- 边际 ROI 与平均 ROI：两个不同的数 —— 不会再把这两个数搞混  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- 等边际原则：最优分配的判据 —— 知道这个原则说了什么、成立的条件是什么  
  <sub>适合谁读：S1 S2 S4 · 待写</sub>
- 置信区间与拟合度：模型能信几分 —— 知道一个模型的两个可信度指标各管什么  
  <sub>适合谁读：S4 · 待写</sub>

---

**规划与讨论**：<https://github.com/edwinjhlee/ai/issues/52>
