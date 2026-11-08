# MMM 贡献分解：把长期贡献拆开

「这个季度电视广告带来了 14% 的销售。」

这句话里的 14%，是从一个回归模型里拆出来的。**拆的方式不止一种，拆出来的数可以差很远。**

MMM（Marketing Mix Modeling）做的事，是把过去几年每周的销售，摆在各种广告花费、季节、价格、促销的旁边，用一个回归去解释它。然后问：模型算出来，每个渠道各贡献了多少。

拆贡献这件事本身不复杂。**难的是拆之前那几步——基线、饱和、时滞。** 这三样决定了拆出来的数是「这个渠道挣了多少」还是「这个渠道占了模型解释力的多少」。

## MMM 贡献分解在做什么

**一句话：把销售的变化，摊回到各个解释它的变量上。**

模型跑完之后，每个渠道的系数乘以它的实际花费，得到这个渠道的贡献。加起来，再加上基线，等于模型预测的销售。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%AD%A3%E5%BA%A6%E9%87%8C%EF%BC%8C%E5%90%84%E6%B8%A0%E9%81%93%E5%AF%B9%E9%94%80%E5%94%AE%E7%9A%84%E8%B4%A1%E7%8C%AE%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%23f59e0b%22%2C%22%2364748b%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E7%94%B5%E8%A7%86%22%2C%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%2C%22%E5%9F%BA%E7%BA%BF%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E9%94%80%E5%94%AE%E7%9A%84%E6%AF%94%E4%BE%8B%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B38%2C21%2C14%2C9%2C18%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%AD%A3%E5%BA%A6%E9%87%8C%EF%BC%8C%E5%90%84%E6%B8%A0%E9%81%93%E5%AF%B9%E9%94%80%E5%94%AE%E7%9A%84%E8%B4%A1%E7%8C%AE%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%23f59e0b%22%2C%22%2364748b%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E7%94%B5%E8%A7%86%22%2C%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%2C%22%E5%9F%BA%E7%BA%BF%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E9%94%80%E5%94%AE%E7%9A%84%E6%AF%94%E4%BE%8B%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B38%2C21%2C14%2C9%2C18%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%AD%A3%E5%BA%A6%E9%87%8C%EF%BC%8C%E5%90%84%E6%B8%A0%E9%81%93%E5%AF%B9%E9%94%80%E5%94%AE%E7%9A%84%E8%B4%A1%E7%8C%AE%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%23f59e0b%22%2C%22%2364748b%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E7%94%B5%E8%A7%86%22%2C%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%2C%22%E5%9F%BA%E7%BA%BF%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E9%94%80%E5%94%AE%E7%9A%84%E6%AF%94%E4%BE%8B%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B38%2C21%2C14%2C9%2C18%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430" width="760" alt="mmm_contribution_split"></a>

这张图里，**基线占了 18%**。那 18% 是没有广告也会有的销售。剩下 82% 才是各渠道分掉的。

**MMM 的贡献是「模型的贡献」，不是「广告的功劳」。** 这两件事不一样，后面会讲差在哪。

**它跟归因最大的不同是时间尺度。** 归因看的是一周里的一串接触点，MMM 看的是几年里几百个周次。MMM 要回答的是「长期看，钱该往哪个渠道走」，不是「上一单是谁带来的」。

## 贡献是怎么拆的

**拆贡献之前有三样东西必须先定下来。三样都定不对，贡献就拆不对。**

### 一、基线

**基线是「什么都不投也会有的销售」。** 季节、趋势、价格变动、促销周期，这些不靠广告发生的东西，都归到基线里。

基线怎么定，直接改贡献。基线定得低，各渠道的贡献加起来就大；定得高，贡献就小。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%9F%BA%E7%BA%BF%E8%AE%BE%E5%BE%97%E4%B8%8D%E5%90%8C%EF%BC%8C%E5%90%84%E6%B8%A0%E9%81%93%E8%B4%A1%E7%8C%AE%E8%B7%9F%E7%9D%80%E5%8F%98%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%23f59e0b%22%2C%22%2364748b%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9F%BA%E7%BA%BF%20A%5Cn%EF%BC%88%E5%8D%A0%E9%94%80%E5%94%AE%2020%25%EF%BC%89%22%2C%22%E5%9F%BA%E7%BA%BF%20B%5Cn%EF%BC%88%E5%8D%A0%E9%94%80%E5%94%AE%2040%25%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E7%94%B5%E8%A7%86%22%2C%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22data%22%3A%5B38%2C29%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22data%22%3A%5B21%2C16%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E7%94%B5%E8%A7%86%22%2C%22data%22%3A%5B14%2C11%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%2C%22data%22%3A%5B9%2C7%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%5D%7D&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%9F%BA%E7%BA%BF%E8%AE%BE%E5%BE%97%E4%B8%8D%E5%90%8C%EF%BC%8C%E5%90%84%E6%B8%A0%E9%81%93%E8%B4%A1%E7%8C%AE%E8%B7%9F%E7%9D%80%E5%8F%98%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%23f59e0b%22%2C%22%2364748b%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9F%BA%E7%BA%BF%20A%5Cn%EF%BC%88%E5%8D%A0%E9%94%80%E5%94%AE%2020%25%EF%BC%89%22%2C%22%E5%9F%BA%E7%BA%BF%20B%5Cn%EF%BC%88%E5%8D%A0%E9%94%80%E5%94%AE%2040%25%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E7%94%B5%E8%A7%86%22%2C%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22data%22%3A%5B38%2C29%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22data%22%3A%5B21%2C16%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E7%94%B5%E8%A7%86%22%2C%22data%22%3A%5B14%2C11%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%2C%22data%22%3A%5B9%2C7%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%5D%7D&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%9F%BA%E7%BA%BF%E8%AE%BE%E5%BE%97%E4%B8%8D%E5%90%8C%EF%BC%8C%E5%90%84%E6%B8%A0%E9%81%93%E8%B4%A1%E7%8C%AE%E8%B7%9F%E7%9D%80%E5%8F%98%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%23f59e0b%22%2C%22%2364748b%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9F%BA%E7%BA%BF%20A%5Cn%EF%BC%88%E5%8D%A0%E9%94%80%E5%94%AE%2020%25%EF%BC%89%22%2C%22%E5%9F%BA%E7%BA%BF%20B%5Cn%EF%BC%88%E5%8D%A0%E9%94%80%E5%94%AE%2040%25%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E7%94%B5%E8%A7%86%22%2C%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22data%22%3A%5B38%2C29%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22data%22%3A%5B21%2C16%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E7%94%B5%E8%A7%86%22%2C%22data%22%3A%5B14%2C11%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%2C%7B%22name%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%2C%22data%22%3A%5B9%2C7%5D%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22total%22%7D%5D%7D&w=760&h=430" width="760" alt="mmm_baseline_sensitivity"></a>

看搜索广告那一列。基线从 20% 提到 40%，它的贡献从 38% 掉到 29%。**同一份数据，同一个模型，只是基线的设定不同，一个渠道的贡献就差了三成。**

所以拿到一份 MMM 报告，先问基线怎么定的。

### 二、饱和

**广告投得越多，效果越好，但好得越来越慢。** 这是所有渠道的共同形状，跟电话线占线一样。

模型必须把这条曲线装进去，否则它会以为「多花钱等于多赚」是线性的，然后在高位给出过高的贡献。曲线长什么样，见 [→ Hill 饱和曲线：效果怎么撞天花板](../05-hill-saturation-curve/cn.md)。

**饱和还有一层意思：同一个渠道在不同价位，效率不一样。** 搜索广告前 10% 的预算可能带回 20% 的销售，最后 10% 只带回 2%。

### 三、时滞

**今天花的广告费，今天不一定见效。**

电视广告的效果可能三周后才出来，搜索广告当天就出来。模型必须把每一期的广告先按衰减曲线摊到后面几期，再进回归。

怎么摊，看 [→ Adstock 衰减：广告的效果会拖多久](../04-adstock-decay/cn.md)。

**这三样没定，贡献分解就只是把模型的设定念了一遍。** 而这三样，每个分析师给的都不一样。

## 它什么时候不靠谱

**MMM 有一个致命的前提：各渠道的花费要能分开。**

如果搜索广告和社交广告的花费总是同涨同落，模型分不清销售的变化该算给谁。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E4%B8%8E%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%8A%B1%E8%B4%B9%EF%BC%9A%E5%90%8C%E6%B6%A8%E5%90%8C%E8%90%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%E6%9C%88%22%2C%222%E6%9C%88%22%2C%223%E6%9C%88%22%2C%224%E6%9C%88%22%2C%225%E6%9C%88%22%2C%226%E6%9C%88%22%2C%227%E6%9C%88%22%2C%228%E6%9C%88%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22data%22%3A%5B100%2C112%2C124%2C118%2C131%2C140%2C133%2C146%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22data%22%3A%5B98%2C108%2C121%2C115%2C128%2C138%2C130%2C142%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E4%B8%8E%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%8A%B1%E8%B4%B9%EF%BC%9A%E5%90%8C%E6%B6%A8%E5%90%8C%E8%90%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%E6%9C%88%22%2C%222%E6%9C%88%22%2C%223%E6%9C%88%22%2C%224%E6%9C%88%22%2C%225%E6%9C%88%22%2C%226%E6%9C%88%22%2C%227%E6%9C%88%22%2C%228%E6%9C%88%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22data%22%3A%5B100%2C112%2C124%2C118%2C131%2C140%2C133%2C146%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22data%22%3A%5B98%2C108%2C121%2C115%2C128%2C138%2C130%2C142%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E4%B8%8E%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%8A%B1%E8%B4%B9%EF%BC%9A%E5%90%8C%E6%B6%A8%E5%90%8C%E8%90%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%E6%9C%88%22%2C%222%E6%9C%88%22%2C%223%E6%9C%88%22%2C%224%E6%9C%88%22%2C%225%E6%9C%88%22%2C%226%E6%9C%88%22%2C%227%E6%9C%88%22%2C%228%E6%9C%88%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22data%22%3A%5B100%2C112%2C124%2C118%2C131%2C140%2C133%2C146%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E8%8A%B1%E8%B4%B9%22%2C%22data%22%3A%5B98%2C108%2C121%2C115%2C128%2C138%2C130%2C142%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=430" width="760" alt="mmm_channel_corr"></a>

两条线几乎叠在一起。这意味着**这两列在回归里给出的系数，模型自己都分不清**。它会强行拆开：一句给你，一句给我，总数对上。**这个分法是数学上唯一解，不是事实。**

**更糟的是，模型不会告诉你它分不清。** 它照样给你一张漂亮的贡献表。

### 怎么知道自己踩了这个坑

**看两列的相关系数。** 在贡献分解跑出来之前，先把各渠道花费之间的相关性算一遍。任何一对超过 0.7 的，贡献就别当真。

**还有一个更省事的办法：把模型的稳定性测出来。** 同一份数据，样本期换一换、基线换一换、饱和曲线换一换，各渠道的贡献排名动不动。动的那个，就是分不开的那个。

### 第二个毛病：贡献排名和加钱顺序不是一回事

**MMM 给你的是贡献占比，不是边际回报。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E6%AF%94%20vs%20%E8%8A%B1%E8%B4%B9%E5%8D%A0%E6%AF%94%EF%BC%9A%E5%9B%9B%E4%B8%AA%E6%B8%A0%E9%81%93%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%8A%B1%E8%B4%B9%E5%8D%A0%E6%AF%94%EF%BC%88%25%EF%BC%89%22%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E6%AF%94%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A16%2C%22data%22%3A%5B%7B%22value%22%3A%5B28%2C38%5D%2C%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%7D%2C%7B%22value%22%3A%5B35%2C21%5D%2C%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%7D%2C%7B%22value%22%3A%5B22%2C14%5D%2C%22name%22%3A%22%E7%94%B5%E8%A7%86%22%7D%2C%7B%22value%22%3A%5B15%2C9%5D%2C%22name%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=440
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E6%AF%94%20vs%20%E8%8A%B1%E8%B4%B9%E5%8D%A0%E6%AF%94%EF%BC%9A%E5%9B%9B%E4%B8%AA%E6%B8%A0%E9%81%93%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%8A%B1%E8%B4%B9%E5%8D%A0%E6%AF%94%EF%BC%88%25%EF%BC%89%22%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E6%AF%94%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A16%2C%22data%22%3A%5B%7B%22value%22%3A%5B28%2C38%5D%2C%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%7D%2C%7B%22value%22%3A%5B35%2C21%5D%2C%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%7D%2C%7B%22value%22%3A%5B22%2C14%5D%2C%22name%22%3A%22%E7%94%B5%E8%A7%86%22%7D%2C%7B%22value%22%3A%5B15%2C9%5D%2C%22name%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=440"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E6%AF%94%20vs%20%E8%8A%B1%E8%B4%B9%E5%8D%A0%E6%AF%94%EF%BC%9A%E5%9B%9B%E4%B8%AA%E6%B8%A0%E9%81%93%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%8A%B1%E8%B4%B9%E5%8D%A0%E6%AF%94%EF%BC%88%25%EF%BC%89%22%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%B4%A1%E7%8C%AE%E5%8D%A0%E6%AF%94%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A16%2C%22data%22%3A%5B%7B%22value%22%3A%5B28%2C38%5D%2C%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%7D%2C%7B%22value%22%3A%5B35%2C21%5D%2C%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%7D%2C%7B%22value%22%3A%5B22%2C14%5D%2C%22name%22%3A%22%E7%94%B5%E8%A7%86%22%7D%2C%7B%22value%22%3A%5B15%2C9%5D%2C%22name%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%22%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=440" width="760" alt="mmm_contribution_vs_spend"></a>

横轴是花费占比，纵轴是贡献占比。**点落在对角线上方的渠道，钱花得值；落在下面的，钱花多了。**

社交广告花了 35% 的钱，只换来 21% 的贡献，它在线下面。搜索广告花了 28%，换来 38%，它在线上面。

**所以 MMM 贡献分解最直接的用处，不是「谁贡献大」，是「谁贡献小」。** 贡献占比和花费占比一比，谁多花了自己的钱，就出来了。

**但从这张图直接得出「社交广告该减钱」，还差一步。** 因为贡献占比是历史平均值，而你要决定的是下个月的分配。这两件事之间隔着边际 ROI 和等边际原则，见 [→ 边际 ROI 和平均 ROI：两个不同的数](../06-marginal-vs-average-roi/cn.md) 和 [→ 等边际原则：最优分配的判据](../07-equal-marginal-returns-principle/cn.md)。

## 拿到贡献数以后

**结论。**

MMM 贡献分解做的事，是把销售的变化摊回到各个解释它的变量上。它拆出来的数，取决于三样设定：**基线、饱和、时滞**。这三样每个分析师给得都不一样，所以同一个数在两份报告里不一样，是正常的。

**它最大的软肋是变量之间分不开的时候。** 而这种情况下模型不会报警，它照样给你一张表。所以拿到 MMM 报告，先看三件事：基线怎么定的，渠道花费的相关性是多少，换一换设定排名动不动。

还有一条：**它是观察到的关联，不是因果。** 想要因果，得留对照。

[→ 再多加一块钱，还赚得回来吗](../../4-performance-analysis/04-marginal-roi-decay/cn.md) · [→ 边际 ROI 和平均 ROI：两个不同的数](../06-marginal-vs-average-roi/cn.md) · [→ 归因：把功劳分给各个接触点](../01-attribution/cn.md)

**数据**：图里的数是一个算例，用来说明贡献分解受基线设定影响、受变量相关性影响，以及贡献占比与花费占比可以不一致；不是某一家的真实 MMM 结果。**复现**：图里的数是算例，没有一条 x-cmd 命令能把它们重跑一遍；换成你自己的数，把链接里 d= 参数的 series 数据数组改掉就行。
