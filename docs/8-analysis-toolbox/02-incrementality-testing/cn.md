# 增量实验：拿一块地方做对照

「这个渠道停了，单会掉多少。」

报表答不了。报表记的是**发生过的事**：谁点了广告，谁下了单。它没记一件看不见的事——**那些本来就会下单的人**。

所以你手上有两条路：继续看报表猜一个数字，或者**留一块地方不投广告**，让它替你回答。第二条路就是增量实验。

## 增量实验在做什么

**增量，说白了就是：停投之后，不再成交的那些单。**

本来就会成交的单不算增量。那些人本来就要买，只是搜的时候顺手看见了你。停掉之后不再成交的，才是广告拽回来的。

这跟 [→ 没有广告，这些单会成交吗](../../1-report-overview/06-incrementality-chart/cn.md) 里那两本账是同一件事：平台那本账记整条漏斗，增量那本账只记停掉之后少掉的那些单。**要算出「少掉多少」，你手里必须有一块没投过的地方。**

### 实验要成立，需要三样东西

**一、随机。** 两边必须随机分，不能挑。挑出来的两块地方，本来就不一样。

**二、一块真的没投的地方。** 不是「投得少一点」，是**完全不投**。投了一半，你不知道少掉的那些单是被广告拽走的，还是被隔壁接走了。

**三、够长的时间。** 下面会讲为什么这条最容易踩坑。少一样，出来的数就只是个看起来很专业的猜测。

**最难的是随机。** 线下比门店，你知道谁在哪座城。只有广告：你手里有订单，没有「谁看到了广告」。三种做法都绕不开同一个问题：**对照组那批人，你得保证他们没被投到。**

## 三种做法

**都是把东西随机分成两半，只是随机的东西不同。**

### 地理切分

**做法：把地区随机分成两组，一组照常投，另一组完全不投。**

这是 Google 在 2011 年那篇《Measuring Ad Effectiveness Using Geo Experiments》里用的做法，也是现在各家平台的 geo-lift。

它有两个前提：**广告能按地理投**，以及**结果指标能按地区统计**。美国常用的地理单位是 210 个 Nielsen DMA，邮编太小，一般不用。时间上分两段：前测期两边完全一样，测试期只改实验组。

**代价是「粒度」。** 地区越小，随机分配的样本越少，区间越宽。地区越大，越多人被卷进对照组，广告主越心疼。邮编这个粒度 Google 明确说不行：广告投不准，人也会跨着边界跑。

**换来的是：不需要跟踪到个人。**

### 幽灵广告

**做法：对照组照样参与竞价，只是他们的广告永远抢不到位置。**

这是平台现在主推的做法，Google 与 Meta 的 Conversion Lift 都属这一类。它比地理切分细：随机分的是人，所以样本可以很大，区间可以很窄。

**代价是钱。** 对照组那部分曝光，平台照收。你付了钱，广告没投出去。这笔钱叫「幽灵广告费」，是增量实验里最实在的一笔开销。

它还留了个尾巴：对照组少了这些广告位，竞价环境变了，CPM 可能被抬高。

**三种做法都要满足同一个前提：你能拿到结果指标。** 只有转化数没有销售的渠道，测得出点击的增量，测不出钱的增量。

### 时间切分

**做法：同一批人，前后两段，前一段投后一段不投，拿自己跟自己比。**

这是三种里最便宜的，也是最弱的。

**它不是随机的。** 前后两段的市场环境不同：季节、竞品活动、促销、节假日，全都可能变。你测出来的差，一半是广告，一半是这两段本来就不一样。**时间切分排最后。**

## 它测出来的数长什么样

**同一个实验，能算出两个完全不同的数。**

Google 那篇论文里有一个广告主的搜索广告实验。平台账单显示 CPC 是 2.40 美元，实验测出的 CPIC（每次增量点击的成本）是 3.00 美元。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9ACPC%202.40%20%E7%BE%8E%E5%85%83%EF%BC%8CCPIC%203.00%20%E7%BE%8E%E5%85%83%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%2C%22%E5%AE%9E%E9%AA%8C%E6%B5%8B%E5%87%BA%E7%9A%84%20CPIC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%24%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9ACPC%202.40%20%E7%BE%8E%E5%85%83%EF%BC%8CCPIC%203.00%20%E7%BE%8E%E5%85%83%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%2C%22%E5%AE%9E%E9%AA%8C%E6%B5%8B%E5%87%BA%E7%9A%84%20CPIC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%24%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9ACPC%202.40%20%E7%BE%8E%E5%85%83%EF%BC%8CCPIC%203.00%20%E7%BE%8E%E5%85%83%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%2C%22%E5%AE%9E%E9%AA%8C%E6%B5%8B%E5%87%BA%E7%9A%84%20CPIC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%24%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="geo_cpc_vs_cpic"></a>

**平台报的 CPC 把真实的增量成本低估了 20%。** 付费点击里有 20% 是从自然搜索抢来的，抢过来之后并没有多出点击。

**这 20% 是一整类错误的量级。** 平台报表里每个数都默认假设「这次点击多亏了这笔广告」。

**Facebook 那 15 个实地实验里也有一个结账（购买）实验。** 同一个活动，同一批人：广告主常用的口径（曝光的 vs 未曝光的）算出 **316%**，随机实验测出来是 **73%**。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="fb_checkout_316_vs_73"></a>

**五倍多。** 论文的结论是：观测口径常常根本恢复不出随机实验测出来的效果。匹配、回归、倾向得分这些校正办法都试过，没有一个稳定赢。

## 它什么时候不靠谱

**四个坑，按踩到的频率排。**

### 一、两块地方本来就不一样

地理切分最容易出这个问题：实验组是大学城，对照组是工业区，两边的客流结构从根上就不同。

**随机分配能解决大部分，但不是万能的。** 它保证的是「已知的差异被均匀分开了」，不是「未知的差异不存在」。

Google 那篇论文里有一个专门的做法：先按规模把所有 DMA 排好序，再切成大小相同的组，每组随机挑一个进实验组，**区间能收窄 10% 左右。**

### 二、样本太小

**区间太宽，等于没测。**

地理切分天生样本少。DMA 粒度在美国是 210 个，分成两组每组 105 个，这就是你能有的全部随机样本。

论文里写了一个能直接用的办法：拿前测期的历史数据**造出「假的前测期」和「假的测试期」**，代入方差公式算出区间的宽度。**这一步不花钱，开跑之前就知道这套设计测不测得出东西。**

### 三、时间不够长

**这一条最容易被忽略，代价也最大。**

搜索广告的点击是即时的：花费一停，增量点击立刻停住。但**线下销售不会**。Google 论文的图显示，实验组的花费回到前测水平之后，增量销售还在继续往上走，然后才慢慢消下去。因为买线下商品的人需要时间：做功课、去店里、付钱。

**所以测试期必须长出整个响应滞后期。** 测一半就收工，测出来的是被截断的数，而且是**偏小的**那个数——而一个偏小的数，你看报表可能还挺高兴。

### 四、投放本身漏了

**对照组真的没被投到吗？**

三种做法都有这个漏洞。地理切分是广告投不准，加上人会跨着地区边界跑。幽灵广告是平台可能还是给对照组投了别的广告。时间切分是前后两段的竞品活动不同。**这是所有增量实验里最难查的一个洞**，因为查不出来。

### 还有一件更要紧的事：这个数只对这一次成立

**增量实验测的是「在这段时间、这个投放水平、这一批人」上的增量。**

它不是这个渠道的永久属性。预算变了、素材变了、季节变了、人群变了，增量就变。所以一个 73% 的增量**不能直接乘到你下个月的预算上**，外推的可靠性远低于实验本身。

## 什么时候值得做

**增量实验贵。它只在两种情况下值得：拿这个数去决定钱往哪放，或者拿它去校准你天天在用的那套观测口径。**

一个月投几万、答案你本来就知道、或者你只想知道「这个渠道好不好」而不是「值不值得加钱」，不值得做。

**还有一条不算在成本里的账：对照组那块地方那段时间真的没有广告。** 这不是成本，是你为答案付的价。

## 拿到的数怎么用

**结论。**

增量实验只做一件事：**停掉之后不再成交的那些单，就是增量。** 它测出来的数，比观测口径小得多，也比观测口径真得多——Facebook 那个实验里，一个 316% 一个 73%，差四倍多。**平台报表里的数不是假的，它回答的是另一个问题。**

[→ 没有广告，这些单会成交吗](../../1-report-overview/06-incrementality-chart/cn.md) · [→ 对照组不是「没投的那群人」那么简单](../../3-experiment-design/01-what-a-control-group-is/cn.md)

**数据**：Vaver & Koehler, *Measuring Ad Effectiveness Using Geo Experiments*, Google Inc., 2011（geo 实验的设计与功效分析；210 个 Nielsen DMA；分层分配使区间收窄约 10%；CPC 2.40 美元对 CPIC 3.00 美元）；Gordon, Zettelmeyer, Bhargava & Chapsky, *Marketing Science* 38(2), 2019（Facebook 15 个实地实验；结账实验观测口径 316% 对随机实验 73%）。**复现**：图里的数是这两篇论文报告的结果，没有一条 x-cmd 命令能把它们重跑一遍；换成你自己的数，把链接里 d= 参数的 series 数据数组改掉就行。
