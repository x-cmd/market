# 八个工具，一张表

「这个渠道到底带来了多少？」

这句话有八种问法，也对应八种工具。**搞混工具，比算错数更麻烦**——因为算错了数会有人来问，用错了工具，数字看着漂亮，直接就进预算表了。

这张表把这八样工具摆在一起：各自干什么、要喂什么进去、吐出什么来、在站里哪一篇讲过。

**一句话：八个工具没有谁取代谁，它们管的是链条上不同的环节。**

## 八个工具各管什么

**先看这张表。** 左边是工具，中间三列是它的输入和输出，最右边是站内讲过它的那一篇。

| 工具 | 干什么 | 输入 | 输出 | 在哪篇用过 |
|---|---|---|---|---|
| 归因 | 把一单的功劳分给各个接触点 | 一单转化路径上的接触点序列 | 每单每个接触点的分摊份额 | [→ 归因：把功劳分给各个接触点](../../8-analysis-toolbox/01-attribution/cn.md) |
| 增量实验 | 测停投之后会少掉多少单 | 一块不投广告的地方加前后两期销售 | 增量销售额、增量点击、增量成本 | [→ 增量实验：拿一块地方做对照](../../8-analysis-toolbox/02-incrementality-testing/cn.md) |
| MMM 贡献分解 | 把长期销售变化摊回各渠道 | 几年周次销售、渠道花费、价格促销 | 各渠道贡献占比 | [→ MMM 贡献分解：把长期贡献拆开](../../8-analysis-toolbox/03-mmm-contribution/cn.md) |
| Adstock 衰减 | 把过去的投放按衰减曲线累积到今天 | 逐日花费序列、一条衰减率 | 累积后的效果序列 | [→ Adstock 衰减：广告的效果会拖多久](../../8-analysis-toolbox/04-adstock-decay/cn.md) |
| Hill 饱和曲线 | 描述投入增加时效果怎么递减 | 逐档花费、逐档回报 | 饱和点 k、弹性 α | [→ Hill 饱和曲线：效果怎么撞天花板](../../8-analysis-toolbox/05-hill-saturation-curve/cn.md) |
| 边际 ROI 与平均 ROI | 分清回头看的总数和最后一块钱的回报 | 分档花费、分档回报 | 平均 ROI、边际 ROI | [→ 边际 ROI 和平均 ROI：两个不同的数](../../8-analysis-toolbox/06-marginal-vs-average-roi/cn.md) |
| 等边际原则 | 判断预算怎么分才不白花 | 各渠道分档边际回报曲线 | 最优分配比例 | [→ 等边际原则：最优分配的判据](../../8-analysis-toolbox/07-equal-marginal-returns-principle/cn.md) |
| 置信区间与拟合度 | 给一个模型定可信度 | 模型输出、样本量 | 区间半宽、R² | [→ 置信区间和拟合度：模型能信几分](../../8-analysis-toolbox/08-confidence-intervals-and-fit/cn.md) |

**这张表里最要紧的一列是「输出」。** 前两个工具输出的是钱和单，第三个输出的是百分比，后两个输出的是曲线，第六第七输出的是倍数。

**它们的口径不一样，所以不能互相替代，也不能加在一起。** 一个渠道的贡献占 21%、它的边际 ROI 是 1.8 倍、它的增量回报是 73%——这三个数是三把尺子量的三样东西。

## 每个工具管哪一步

**把链条摆开，八个工具各占一格。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%9B%9B%E4%B8%AA%E9%97%AE%E9%A2%98%EF%BC%8C%E5%85%AB%E4%B8%AA%E5%B7%A5%E5%85%B7%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E8%BF%99%E5%8D%95%E6%98%AF%E8%B0%81%E5%B8%A6%E6%9D%A5%E7%9A%84%5Cn%EF%BC%88%E4%BA%8B%E5%90%8E%E6%8B%86%E8%B4%A6%EF%BC%89%22%2C%22%E5%B9%BF%E5%91%8A%E5%B8%A6%E6%9D%A5%E5%A4%9A%E5%B0%91%E6%96%B0%E5%A2%9E%5Cn%EF%BC%88%E5%AF%B9%E7%85%A7%EF%BC%89%22%2C%22%E9%95%BF%E6%9C%9F%E5%90%84%E6%B8%A0%E9%81%93%E8%B4%A1%E7%8C%AE%5Cn%EF%BC%88%E5%8E%86%E5%8F%B2%E5%9B%9E%E5%BD%92%EF%BC%89%22%2C%22%E4%B8%8B%E4%B8%80%E7%AC%94%E9%92%B1%E6%94%BE%E5%93%AA%5Cn%EF%BC%88%E8%BE%B9%E9%99%85%E5%88%86%E9%85%8D%EF%BC%89%22%2C%22%E8%BF%99%E4%B8%AA%E6%95%B0%E8%83%BD%E4%BF%A1%E5%87%A0%E5%88%86%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%83%BD%E7%AD%94%E7%9A%84%E5%B7%A5%E5%85%B7%E4%B8%AA%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22%E5%AE%9E%E9%AA%8C%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22%E6%95%B0%E5%AD%A6%E7%B1%BB%E5%B7%A5%E5%85%B7%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E8%A7%82%E6%B5%8B%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B3%2C1%2C3%2C2%2C2%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%AE%9E%E9%AA%8C%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B0%2C1%2C0%2C0%2C1%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E6%95%B0%E5%AD%A6%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B0%2C0%2C2%2C2%2C2%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%9B%9B%E4%B8%AA%E9%97%AE%E9%A2%98%EF%BC%8C%E5%85%AB%E4%B8%AA%E5%B7%A5%E5%85%B7%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E8%BF%99%E5%8D%95%E6%98%AF%E8%B0%81%E5%B8%A6%E6%9D%A5%E7%9A%84%5Cn%EF%BC%88%E4%BA%8B%E5%90%8E%E6%8B%86%E8%B4%A6%EF%BC%89%22%2C%22%E5%B9%BF%E5%91%8A%E5%B8%A6%E6%9D%A5%E5%A4%9A%E5%B0%91%E6%96%B0%E5%A2%9E%5Cn%EF%BC%88%E5%AF%B9%E7%85%A7%EF%BC%89%22%2C%22%E9%95%BF%E6%9C%9F%E5%90%84%E6%B8%A0%E9%81%93%E8%B4%A1%E7%8C%AE%5Cn%EF%BC%88%E5%8E%86%E5%8F%B2%E5%9B%9E%E5%BD%92%EF%BC%89%22%2C%22%E4%B8%8B%E4%B8%80%E7%AC%94%E9%92%B1%E6%94%BE%E5%93%AA%5Cn%EF%BC%88%E8%BE%B9%E9%99%85%E5%88%86%E9%85%8D%EF%BC%89%22%2C%22%E8%BF%99%E4%B8%AA%E6%95%B0%E8%83%BD%E4%BF%A1%E5%87%A0%E5%88%86%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%83%BD%E7%AD%94%E7%9A%84%E5%B7%A5%E5%85%B7%E4%B8%AA%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22%E5%AE%9E%E9%AA%8C%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22%E6%95%B0%E5%AD%A6%E7%B1%BB%E5%B7%A5%E5%85%B7%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E8%A7%82%E6%B5%8B%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B3%2C1%2C3%2C2%2C2%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%AE%9E%E9%AA%8C%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B0%2C1%2C0%2C0%2C1%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E6%95%B0%E5%AD%A6%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B0%2C0%2C2%2C2%2C2%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%9B%9B%E4%B8%AA%E9%97%AE%E9%A2%98%EF%BC%8C%E5%85%AB%E4%B8%AA%E5%B7%A5%E5%85%B7%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E8%BF%99%E5%8D%95%E6%98%AF%E8%B0%81%E5%B8%A6%E6%9D%A5%E7%9A%84%5Cn%EF%BC%88%E4%BA%8B%E5%90%8E%E6%8B%86%E8%B4%A6%EF%BC%89%22%2C%22%E5%B9%BF%E5%91%8A%E5%B8%A6%E6%9D%A5%E5%A4%9A%E5%B0%91%E6%96%B0%E5%A2%9E%5Cn%EF%BC%88%E5%AF%B9%E7%85%A7%EF%BC%89%22%2C%22%E9%95%BF%E6%9C%9F%E5%90%84%E6%B8%A0%E9%81%93%E8%B4%A1%E7%8C%AE%5Cn%EF%BC%88%E5%8E%86%E5%8F%B2%E5%9B%9E%E5%BD%92%EF%BC%89%22%2C%22%E4%B8%8B%E4%B8%80%E7%AC%94%E9%92%B1%E6%94%BE%E5%93%AA%5Cn%EF%BC%88%E8%BE%B9%E9%99%85%E5%88%86%E9%85%8D%EF%BC%89%22%2C%22%E8%BF%99%E4%B8%AA%E6%95%B0%E8%83%BD%E4%BF%A1%E5%87%A0%E5%88%86%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%83%BD%E7%AD%94%E7%9A%84%E5%B7%A5%E5%85%B7%E4%B8%AA%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22%E5%AE%9E%E9%AA%8C%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22%E6%95%B0%E5%AD%A6%E7%B1%BB%E5%B7%A5%E5%85%B7%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E8%A7%82%E6%B5%8B%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B3%2C1%2C3%2C2%2C2%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%AE%9E%E9%AA%8C%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B0%2C1%2C0%2C0%2C1%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E6%95%B0%E5%AD%A6%E7%B1%BB%E5%B7%A5%E5%85%B7%22%2C%22data%22%3A%5B0%2C0%2C2%2C2%2C2%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=430" width="760" alt="tool_coverage_matrix"></a>

**三类工具，三种可信度来源。**

**观测类**（归因、MMM、边际 ROI）——从已经发生的数据里读关系。**它们最快，最便宜，代价是读出来的关系不等于因果。**

**实验类**（增量实验）——留一块地方不投，让事实自己冒出来。**它最可信，代价是花钱、花时间，而且一次只能答一个问题。**

**数学类**（Adstock、Hill、等边际、置信区间）——它们不给数，它们规定**别的工具该怎么算**。没有 Adstock，MMM 的贡献就是错的；没有 Hill，模型的贡献在高位会虚胖。

**所以「什么时候查哪个」这个问题，答案取决于你要的是钱、还是因果、还是可信度。** 下面这三步就是按这个顺序排的。

### 回头看：这单是谁碰到的

**这一步查归因。**

输入是一单的接触点序列，输出是每个接触点分到多少。**归因数的是「谁碰过这一单」，不是「谁创造了这一单」。** 换一条分摊规则，同一批单分出来的数就不同，这是规则的选择，不是事实的差别。

**在这一步能问的问题**：这批订单里搜索占几成、哪条路径最长。**不能问的**：这个渠道值不值得加钱。

### 停下来看：停投会少掉多少

**这一步查增量实验。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E9%97%AE%E9%A2%98%EF%BC%8C%E4%B8%8D%E5%90%8C%E5%B7%A5%E5%85%B7%E7%BB%99%E7%9A%84%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%2C%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%5CneBay%20%E5%93%81%E7%89%8C%E8%AF%8D%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5CneBay%20%E5%93%81%E7%89%8C%E8%AF%8D%22%2C%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%5CnFacebook%20%E7%BB%93%E8%B4%A6%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5CnFacebook%20%E7%BB%93%E8%B4%A6%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%9B%9E%E6%8A%A5%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1400%2C-63%2C316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E9%97%AE%E9%A2%98%EF%BC%8C%E4%B8%8D%E5%90%8C%E5%B7%A5%E5%85%B7%E7%BB%99%E7%9A%84%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%2C%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%5CneBay%20%E5%93%81%E7%89%8C%E8%AF%8D%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5CneBay%20%E5%93%81%E7%89%8C%E8%AF%8D%22%2C%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%5CnFacebook%20%E7%BB%93%E8%B4%A6%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5CnFacebook%20%E7%BB%93%E8%B4%A6%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%9B%9E%E6%8A%A5%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1400%2C-63%2C316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E9%97%AE%E9%A2%98%EF%BC%8C%E4%B8%8D%E5%90%8C%E5%B7%A5%E5%85%B7%E7%BB%99%E7%9A%84%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%2C%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%5CneBay%20%E5%93%81%E7%89%8C%E8%AF%8D%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5CneBay%20%E5%93%81%E7%89%8C%E8%AF%8D%22%2C%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%5CnFacebook%20%E7%BB%93%E8%B4%A6%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5CnFacebook%20%E7%BB%93%E8%B4%A6%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%9B%9E%E6%8A%A5%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1400%2C-63%2C316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430" width="760" alt="observed_vs_randomized_roi"></a>

**这张图是整张工具表最要紧的一条注脚：换工具，答案会反过来。**

eBay 2015 年那场地实验，在随机选中的市场关掉品牌词广告：少掉的点击有 **99.5%** 被自然搜索立即接了回去，测出的品牌词回报是 **−63%**（95% 置信区间 −124% 到 −3%）。同一份数据用观测口径读，回报是 **1400% 以上**。

Facebook 那次结账实验，观测口径算出 **316%**，实验真值 **73%**。观测口径高估了四倍多。

**两个案例的结论是一致的：观测口径恢复不出实验效果。** 匹配、回归校正、倾向得分，论文里都试过。

**所以要看「广告带来了多少新增」，只有增量实验这一格能给数。** 其他工具给的都不是同一个东西。

### 往前看：下一笔钱放哪

**这一步要三个工具接力：边际 ROI、等边际、置信区间。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22100%20%E4%B8%87%E6%80%8E%E4%B9%88%E5%88%86%E7%BB%99%E4%B8%A4%E6%9D%A1%E6%B8%A0%E9%81%93%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%85%A8%E7%BB%99%E6%90%9C%E7%B4%A2%22%2C%22%E6%8C%89%E8%BE%B9%E9%99%85%E6%8B%89%E5%B9%B3%22%2C%22%E7%A4%BE%E4%BA%A4%E4%B8%8D%E8%B6%85%2040%25%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%EF%BC%88%E6%AF%8F%201%20%E5%9D%97%E6%8D%A2%E5%9B%9E%E5%87%A0%E5%87%A0%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1.14%2C2.3%2C1.97%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22100%20%E4%B8%87%E6%80%8E%E4%B9%88%E5%88%86%E7%BB%99%E4%B8%A4%E6%9D%A1%E6%B8%A0%E9%81%93%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%85%A8%E7%BB%99%E6%90%9C%E7%B4%A2%22%2C%22%E6%8C%89%E8%BE%B9%E9%99%85%E6%8B%89%E5%B9%B3%22%2C%22%E7%A4%BE%E4%BA%A4%E4%B8%8D%E8%B6%85%2040%25%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%EF%BC%88%E6%AF%8F%201%20%E5%9D%97%E6%8D%A2%E5%9B%9E%E5%87%A0%E5%87%A0%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1.14%2C2.3%2C1.97%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22100%20%E4%B8%87%E6%80%8E%E4%B9%88%E5%88%86%E7%BB%99%E4%B8%A4%E6%9D%A1%E6%B8%A0%E9%81%93%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%85%A8%E7%BB%99%E6%90%9C%E7%B4%A2%22%2C%22%E6%8C%89%E8%BE%B9%E9%99%85%E6%8B%89%E5%B9%B3%22%2C%22%E7%A4%BE%E4%BA%A4%E4%B8%8D%E8%B6%85%2040%25%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%EF%BC%88%E6%AF%8F%201%20%E5%9D%97%E6%8D%A2%E5%9B%9E%E5%87%A0%E5%87%A0%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1.14%2C2.3%2C1.97%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="equal_marginal_split"></a>

**第一步是边际 ROI。** 平均 ROI 2.28 倍的那条渠道，最后一档的边际 ROI 只有 0.4。**加不加钱看的是最后一块钱，不是整笔账。**

**第二步是等边际。** 分完之后各渠道的边际回报拉平，总回报最大。这个算例里，全给搜索总回报 1.14，按边际拉平是 2.30，**差一倍多**。

**第三步是置信区间。** 拉平之后还要看这个差别稳不稳。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%A0%B7%E6%9C%AC%E9%87%8F%E5%B7%AE%2040%20%E5%80%8D%EF%BC%8C%E5%8C%BA%E9%97%B4%E5%AE%BD%E5%BA%A6%E5%B7%AE%206%20%E5%80%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%A0%B7%E6%9C%AC%202000%22%2C%22%E6%A0%B7%E6%9C%AC%20200%22%2C%22%E6%A0%B7%E6%9C%AC%2050%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%2295%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B9%2C29%2C56%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%A0%B7%E6%9C%AC%E9%87%8F%E5%B7%AE%2040%20%E5%80%8D%EF%BC%8C%E5%8C%BA%E9%97%B4%E5%AE%BD%E5%BA%A6%E5%B7%AE%206%20%E5%80%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%A0%B7%E6%9C%AC%202000%22%2C%22%E6%A0%B7%E6%9C%AC%20200%22%2C%22%E6%A0%B7%E6%9C%AC%2050%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%2295%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B9%2C29%2C56%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%A0%B7%E6%9C%AC%E9%87%8F%E5%B7%AE%2040%20%E5%80%8D%EF%BC%8C%E5%8C%BA%E9%97%B4%E5%AE%BD%E5%BA%A6%E5%B7%AE%206%20%E5%80%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%A0%B7%E6%9C%AC%202000%22%2C%22%E6%A0%B7%E6%9C%AC%20200%22%2C%22%E6%A0%B7%E6%9C%AC%2050%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%2295%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B9%2C29%2C56%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="ci_width_vs_sample"></a>

**同一个效应，样本量差 40 倍，区间宽度差 6 倍。** 区间宽度跟样本量的平方根成反比，所以样本翻一倍，区间只收窄约三成。

**这一格决定前面那一步该不该动手。** 边际回报算出来差 0.2，但区间半宽是 30 个点——那这个差别跟零没有区别，挪钱挪了等于白挪。

## 哪几篇讲过

**工具箱那八篇，每一篇讲一个工具。** 除了原理，它们各自还写清了什么时候用、什么时候会不灵，以及跟别的工具怎么搭。

**工具箱之外的引用，站内按下面这张对表登记。** 每一篇的另一端，指向它自己也用到的工具。

| 工具 | 站内还讲过它的页 |
|---|---|
| 归因 | [→ 一份市场报告怎么跑出来](../01-report-runbook/cn.md)、[→ 没有广告，这些单会成交吗](../06-incrementality-chart/cn.md) |
| 增量实验 | [→ 没有广告，这些单会成交吗](../06-incrementality-chart/cn.md)、[→ 对照组该怎么定](../../3-experiment-design/01-what-a-control-group-is/cn.md) |
| MMM 贡献分解 | [→ 再多加一块钱，还赚得回来吗](../../4-performance-analysis/04-marginal-roi-decay/cn.md)、[→ 边际 ROI 和平均 ROI：两个不同的数](../../8-analysis-toolbox/06-marginal-vs-average-roi/cn.md) |
| Adstock 衰减 | [→ MMM 贡献分解：把长期贡献拆开](../../8-analysis-toolbox/03-mmm-contribution/cn.md)、[→ Hill 饱和曲线：效果怎么撞天花板](../../8-analysis-toolbox/05-hill-saturation-curve/cn.md) |
| Hill 饱和曲线 | [→ MMM 贡献分解：把长期贡献拆开](../../8-analysis-toolbox/03-mmm-contribution/cn.md)、[→ 边际 ROI 和平均 ROI：两个不同的数](../../8-analysis-toolbox/06-marginal-vs-average-roi/cn.md) |
| 边际 ROI 与平均 ROI | [→ 没有广告，这些单会成交吗](../06-incrementality-chart/cn.md)、[→ 再多加一块钱，还赚得回来吗](../../4-performance-analysis/04-marginal-roi-decay/cn.md) |
| 等边际原则 | [→ 钱怎么分，才不会白花](../../6-budget-optimization/01-equal-marginal-returns/cn.md)、[→ 挪完预算，要复查两件事](../../6-budget-optimization/03-after-the-shift-what-goes-wrong/cn.md) |
| 置信区间与拟合度 | [→ 样本太少，结论会反着](../../3-experiment-design/02-sample-size-and-power/cn.md)、[→ 一个数，要配一个区间](../../3-experiment-design/04-confidence-intervals/cn.md) |

**这张对表读出一个规律：工具箱里的工具不是孤立的。**

Adstock 和 Hill 都被 MMM 那一篇调用，因为 MMM 的贡献拆解必须先过这两步。边际 ROI 和等边际总是成对出现，因为等边际要的是边际回报曲线，等边际原则要用，置信区间收尾。

**而每一次跨篇引用，都是从一个问题跳到另一个问题。** 归因在概览那一篇被用来解释「平台记的账和真实的账差在哪」；边际 ROI 在性能那一篇被用来解释「为什么平均数好看不代表还能加量」。

**拿不准某个数该用哪个工具算，回第一张表看「输出」那一列：口径不一样，就不能混着报。**

**复现**：本页所有数都来自站内已有页的算例与已发表研究，没有独立数据源；`ls ~/.x-repo/github.com/x-cmd/market/docs/8-analysis-toolbox/` 可以列出工具箱那八篇，逐篇核对本页表格里的每一行。

**数据**：eBay 品牌词与回报（1400% 以上 / −63%，99.5% 点击被自然搜索接回）来自 Blake, Nosko & Tadelis, *Econometrica* 83(1), 2015。Facebook 结账实验（观测 316% / 实验 73%）来自 Gordon, Zettelmeyer, Bhargava & Chapsky, *Marketing Science* 38(2), 2019。边际与等边际算例（平均 ROI 2.28、边际 0.4、总回报 1.14 / 2.30 / 1.97）与置信区间算例（样本 2000 / 200 / 50 对应区间半宽 9 / 29 / 56 个点）取自站内对应页的算例，截至 2026-11。
