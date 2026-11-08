# 等边际原则：最优分配的判据

「100 万预算，四个渠道，怎么分？」

这个问题没有标准答案，但有一个**判据**：分完之后，各渠道的**边际回报要一样高**。

不是每个渠道 ROI 一样高，是**每多花一块钱换回来的**一样多。

## 等边际原则说了什么

**前提：预算总量固定。** 就是 100 万，多了没有，少了也不行，你得把这 100 万分完。

**判据：分到各渠道的边际回报相等时，总回报最大。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%A4%E4%B8%AA%E6%B8%A0%E9%81%93%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%EF%BC%9A%E4%BA%A4%E7%82%B9%E5%B0%B1%E6%98%AF%E9%92%B1%E8%AF%A5%E5%88%86%E7%9A%84%E5%9C%B0%E6%96%B9%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220-10%E4%B8%87%22%2C%2210-20%E4%B8%87%22%2C%2220-30%E4%B8%87%22%2C%2230-40%E4%B8%87%22%2C%2240-50%E4%B8%87%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22data%22%3A%5B4.8%2C3.1%2C2.0%2C1.1%2C0.4%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22data%22%3A%5B1.2%2C1.8%2C2.4%2C2.9%2C3.3%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%A4%E4%B8%AA%E6%B8%A0%E9%81%93%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%EF%BC%9A%E4%BA%A4%E7%82%B9%E5%B0%B1%E6%98%AF%E9%92%B1%E8%AF%A5%E5%88%86%E7%9A%84%E5%9C%B0%E6%96%B9%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220-10%E4%B8%87%22%2C%2210-20%E4%B8%87%22%2C%2220-30%E4%B8%87%22%2C%2230-40%E4%B8%87%22%2C%2240-50%E4%B8%87%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22data%22%3A%5B4.8%2C3.1%2C2.0%2C1.1%2C0.4%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22data%22%3A%5B1.2%2C1.8%2C2.4%2C2.9%2C3.3%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%A4%E4%B8%AA%E6%B8%A0%E9%81%93%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%EF%BC%9A%E4%BA%A4%E7%82%B9%E5%B0%B1%E6%98%AF%E9%92%B1%E8%AF%A5%E5%88%86%E7%9A%84%E5%9C%B0%E6%96%B9%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220-10%E4%B8%87%22%2C%2210-20%E4%B8%87%22%2C%2220-30%E4%B8%87%22%2C%2230-40%E4%B8%87%22%2C%2240-50%E4%B8%87%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22data%22%3A%5B4.8%2C3.1%2C2.0%2C1.1%2C0.4%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22data%22%3A%5B1.2%2C1.8%2C2.4%2C2.9%2C3.3%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=430" width="760" alt="equal_marginal_two_channels"></a>

搜索广告的边际回报往下走，社交广告的边际回报往上走。**两条线交在 20–30 万那一档上，数值约 2.0 到 2.4。**

交点就是答案：**两边各花到边际回报都是 2 左右的那一档，总回报最大。**

### 分完之后长什么样

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%20100%20%E4%B8%87%EF%BC%8C%E5%88%86%E9%85%8D%E4%B8%8D%E5%90%8C%EF%BC%8C%E6%80%BB%E5%9B%9E%E6%8A%A5%E4%B8%8D%E5%90%8C%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%85%A8%E9%83%A8%E7%BB%99%E6%90%9C%E7%B4%A2%5Cn%EF%BC%88%E6%8C%89%E5%B9%B3%E5%9D%87%20ROI%EF%BC%89%22%2C%22%E4%B8%A4%E8%BE%B9%E6%8C%89%E8%BE%B9%E9%99%85%E6%8B%89%E5%B9%B3%5Cn%EF%BC%88%E6%8C%89%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%89%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%20%C3%B7%20%E6%80%BB%E8%8A%B1%E8%B4%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1.14%2C2.3%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%20100%20%E4%B8%87%EF%BC%8C%E5%88%86%E9%85%8D%E4%B8%8D%E5%90%8C%EF%BC%8C%E6%80%BB%E5%9B%9E%E6%8A%A5%E4%B8%8D%E5%90%8C%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%85%A8%E9%83%A8%E7%BB%99%E6%90%9C%E7%B4%A2%5Cn%EF%BC%88%E6%8C%89%E5%B9%B3%E5%9D%87%20ROI%EF%BC%89%22%2C%22%E4%B8%A4%E8%BE%B9%E6%8C%89%E8%BE%B9%E9%99%85%E6%8B%89%E5%B9%B3%5Cn%EF%BC%88%E6%8C%89%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%89%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%20%C3%B7%20%E6%80%BB%E8%8A%B1%E8%B4%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1.14%2C2.3%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%20100%20%E4%B8%87%EF%BC%8C%E5%88%86%E9%85%8D%E4%B8%8D%E5%90%8C%EF%BC%8C%E6%80%BB%E5%9B%9E%E6%8A%A5%E4%B8%8D%E5%90%8C%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%85%A8%E9%83%A8%E7%BB%99%E6%90%9C%E7%B4%A2%5Cn%EF%BC%88%E6%8C%89%E5%B9%B3%E5%9D%87%20ROI%EF%BC%89%22%2C%22%E4%B8%A4%E8%BE%B9%E6%8C%89%E8%BE%B9%E9%99%85%E6%8B%89%E5%B9%B3%5Cn%EF%BC%88%E6%8C%89%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%89%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%20%C3%B7%20%E6%80%BB%E8%8A%B1%E8%B4%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1.14%2C2.3%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430&w=760&h=430" width="760" alt="equal_marginal_total_return"></a>

**同样是 100 万，全给搜索广告，总回报是 1.14；按边际拉平，总回报是 2.30。**

**差了一倍多。** 这就是「ROI 最高的渠道不该加最多钱」的代价——按平均 ROI 排，会把已经饱和的搜索广告喂饱，而刚起步的社交广告一分钱没分到。

## 它怎么推出来的

**不用公式也能说清。**

假设你现在的分配不是最优的：搜索广告的边际回报是 2.0，社交广告是 1.2。

**那么从社交广告那边挪 1 块到搜索广告：**

- 搜索广告多 1 块，多赚 2.0。
- 社交广告少 1 块，少赚 1.2。
- **净多赚 0.8。**

**总预算没变，总回报却涨了。** 所以原来的分配不是最优的。

**继续挪，挪到两边边际回报相等为止。** 这时再挪一块过去，一边多赚一边少赚，净效果是 0。

**再挪一块呢？** 少的那个渠道边际回报更高了，多的那个渠道边际回报更低了，于是净效果变成负的。

**所以「两边相等」这个点，是「再挪就没好处」和「再挪就吃亏」的分界。**

### 一个不等式

写成数学就是：设总预算固定为 B，各渠道投入 xᵢ，总回报 F = Σ fᵢ(xᵢ)，要最大化 F。

最优解满足的条件是 **f₁′(x₁) = f₂′(x₂) = … = λ**，也就是**所有渠道的边际回报都等于同一个数 λ**。

**λ 有个名字，叫影子价格**：预算每多给 1 块，总回报能多涨多少。**它同时也是你愿意为多一块钱付的上限。**

### 但只有一条渠道时，这条原则说什么都没说

**一个渠道只有一个边际回报，它跟谁相等？** 跟它自己相等。这条原则在单渠道情况下是空的。

**所以它只在多渠道、有取舍的场景下有意义。** 有一个渠道时，你要问的是别的：这块钱值不值得花，见 [→ 边际 ROI 和平均 ROI](../06-marginal-vs-average-roi/cn.md)。

## 它什么时候不靠谱

**这个原则有四条成立条件。破一条，结论就不成立。**

### 一、边际不可估

**整条原则建立在「你知道每个渠道的边际回报」这件事上。**

如果边际 ROI 根本估不出来——花费没分档、每档样本太少、或者根本就是拍脑袋估的——**那你连交点在哪都不知道，无从拉平。**

**这种情况下的正确做法是：先别优化分配，先去把边际估出来。** 拿一个不存在的交点去分钱，比不做优化更糟。

### 二、有硬约束

**真实世界有约束：社交广告不能超过 40%、电视要占品牌预算的 15%、新渠道必须留 10%。**

**有约束的时候，等边际拉平可能做不到。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%8A%A0%E4%BA%86%E7%BA%A6%E6%9D%9F%EF%BC%9A%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E4%B8%8D%E8%83%BD%E8%B6%85%E8%BF%87%2040%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%88%E6%97%A0%E7%BA%A6%E6%9D%9F%EF%BC%89%22%2C%22%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%88%E7%A4%BE%E4%BA%A4%20%E2%89%A4%2040%25%EF%BC%89%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%20%C3%B7%20%E6%80%BB%E8%8A%B1%E8%B4%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22t%22%2C%22data%22%3A%5B50%2C60%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22inside%22%7D%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22t%22%2C%22data%22%3A%5B50%2C40%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22inside%22%7D%7D%5D%7D&w=760&h=430&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%8A%A0%E4%BA%86%E7%BA%A6%E6%9D%9F%EF%BC%9A%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E4%B8%8D%E8%83%BD%E8%B6%85%E8%BF%87%2040%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%88%E6%97%A0%E7%BA%A6%E6%9D%9F%EF%BC%89%22%2C%22%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%88%E7%A4%BE%E4%BA%A4%20%E2%89%A4%2040%25%EF%BC%89%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%20%C3%B7%20%E6%80%BB%E8%8A%B1%E8%B4%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22t%22%2C%22data%22%3A%5B50%2C60%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22inside%22%7D%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22t%22%2C%22data%22%3A%5B50%2C40%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22inside%22%7D%7D%5D%7D&w=760&h=430&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%8A%A0%E4%BA%86%E7%BA%A6%E6%9D%9F%EF%BC%9A%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%E4%B8%8D%E8%83%BD%E8%B6%85%E8%BF%87%2040%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%230891b2%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%88%E6%97%A0%E7%BA%A6%E6%9D%9F%EF%BC%89%22%2C%22%E7%AD%89%E8%BE%B9%E9%99%85%EF%BC%88%E7%A4%BE%E4%BA%A4%20%E2%89%A4%2040%25%EF%BC%89%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%20%C3%B7%20%E6%80%BB%E8%8A%B1%E8%B4%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22t%22%2C%22data%22%3A%5B50%2C60%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22inside%22%7D%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22bar%22%2C%22stack%22%3A%22t%22%2C%22data%22%3A%5B50%2C40%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22inside%22%7D%7D%5D%7D&w=760&h=430&w=760&h=430" width="760" alt="equal_marginal_with_constraint"></a>

**加了「社交广告不超过 40%」这条约束，社交广告被按在 40%，搜索广告被迫多拿 10 万，总回报从 2.30 掉到 1.97。**

**这时候两边边际回报不再相等。** 社交那边被约束住了，它的边际回报会高于搜索那边——按理说可以再多给社交一点，但约束不让。

**约束会吃掉一部分收益，这是明摆着的代价。** 但约束本身常常是别的东西换来的（品牌要求、渠道合约、给新渠道留位置），**别让优化算法把它当成错误给优化掉。**

### 三、总量不固定

**这条原则的前提是「100 万必须花完」。**

如果预算其实可以调——花 80 万赚 1.6，花 100 万赚 2.30，花 120 万赚 3.2——那多花的钱有没有回报，是另一个问题。

**这时候判据变了：只要还有一块钱的边际回报大于 0，就值得加。** 这不是等边际，是「边际大于零就加」。

**等边际管的是「怎么分」，不管「该分多少」。** 这两件事经常被混在一起。

### 四、渠道之间有相互影响

**等边际假设每个渠道各管各的，加这个不影响那个。**

现实里常常不是这样。搜索广告加钱，可能抢了自然搜索的点击（eBay 那个 99.5% 就是这件事）。电视广告加钱，可能提升品牌搜索量，那部分收益算在搜索广告上。两个渠道一起投，可能有互补效应。

**有交叉影响的时候，「各渠道的边际」不是独立的，等边际拉平的那个点未必是最优点。**

**这一条很难量化，但它不是空话。** 平台的归因本身就是在分摊这种交叉影响，分摊规则换一套，分钱的结论就跟着变，见 [→ 归因：把功劳分给各个接触点](../01-attribution/cn.md)。

## 拿到分配结论以后

**结论。**

等边际原则说的是：**固定总量下，各渠道的边际回报相等时，总回报最大。**

它不复杂，一句话的直觉：钱从边际低的地方挪到边际高的地方，总回报涨；挪到两边一样高的时候，停。

**但它是「怎么分」的判据，不是「该分多少」的判据，也不是「每个渠道单独值不值」的判据。** 而且它要成立，边际得估得出来、约束得先列清、总量得是固定的。

**最常见的失败方式，是拿一个拍出来的边际 ROI 去拉平，然后拿着一份看起来很精确的分配表。** 边际不可估的时候，正确做法是先别优化。

[→ 边际 ROI 和平均 ROI：两个不同的数](../06-marginal-vs-average-roi/cn.md) · [→ 钱怎么分，才不会白花](../../6-budget-optimization/01-equal-marginal-returns/cn.md) · [→ 挪完预算，要复查两件事](../../6-budget-optimization/03-after-the-shift-what-goes-wrong/cn.md)

**数据**：图里的数是一个算例，用来说明等边际的交点在哪里、按平均 ROI 分和按边际分差多少、以及加上硬约束后分配会怎么变。不是某一家的真实投放数据。**复现**：图里的数是算例，没有一条 x-cmd 命令能把它们重跑一遍；换成你自己的数，把链接里 d= 参数的 series 数据数组改掉就行。
