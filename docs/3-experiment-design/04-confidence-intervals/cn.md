# 一个数，要配一个区间

**「这个渠道的 ROI 是 4.0。」这句话本身没错，但它只说了一半，漏掉的那一半往往更值钱。**

4.0 是**点估计**——用这一批数据算出来的数。实验重跑一百遍，你会得到一百个不一样的数，4.0 只是其中一个。**置信区间**（confidence interval）把这些数圈出一块地：真值落在里面的概率是 95%。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BE%8E%E5%9B%BD%E5%AE%B6%E5%85%B7%E4%B8%8E%E5%AE%B6%E5%B1%85%E7%94%A8%E5%93%81%E4%B8%93%E5%8D%96%E5%BA%97%EF%BC%9A%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%E4%B8%8E%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%222019%20%E5%B9%B4%22%2C%222020%20%E5%B9%B4%22%2C%222021%20%E5%B9%B4%22%2C%222022%20%E5%B9%B4%22%2C%222023%20%E5%B9%B4%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E7%82%B9%E4%BC%B0%E8%AE%A1%EF%BC%88%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%8C%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E7%82%B9%E4%BC%B0%E8%AE%A1%EF%BC%88%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%8C%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B10713%2C10024%2C12490%2C12647%2C12020%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%2C%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B97%2C1249%2C142%2C113%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=440
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BE%8E%E5%9B%BD%E5%AE%B6%E5%85%B7%E4%B8%8E%E5%AE%B6%E5%B1%85%E7%94%A8%E5%93%81%E4%B8%93%E5%8D%96%E5%BA%97%EF%BC%9A%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%E4%B8%8E%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%222019%20%E5%B9%B4%22%2C%222020%20%E5%B9%B4%22%2C%222021%20%E5%B9%B4%22%2C%222022%20%E5%B9%B4%22%2C%222023%20%E5%B9%B4%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E7%82%B9%E4%BC%B0%E8%AE%A1%EF%BC%88%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%8C%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E7%82%B9%E4%BC%B0%E8%AE%A1%EF%BC%88%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%8C%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B10713%2C10024%2C12490%2C12647%2C12020%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%2C%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B97%2C1249%2C142%2C113%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=440"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BE%8E%E5%9B%BD%E5%AE%B6%E5%85%B7%E4%B8%8E%E5%AE%B6%E5%B1%85%E7%94%A8%E5%93%81%E4%B8%93%E5%8D%96%E5%BA%97%EF%BC%9A%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%E4%B8%8E%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%222019%20%E5%B9%B4%22%2C%222020%20%E5%B9%B4%22%2C%222021%20%E5%B9%B4%22%2C%222022%20%E5%B9%B4%22%2C%222023%20%E5%B9%B4%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E7%82%B9%E4%BC%B0%E8%AE%A1%EF%BC%88%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%8C%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E7%82%B9%E4%BC%B0%E8%AE%A1%EF%BC%88%E6%9C%88%E5%9D%87%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%8C%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B10713%2C10024%2C12490%2C12647%2C12020%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%2C%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E4%B8%87%E7%BE%8E%E5%85%83%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B97%2C1249%2C142%2C113%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=440" width="760" alt="bea_ci_halfwidth_by_year"></a>

美国家具与家居用品专卖店月度销售额（BEA 官方数据）。蓝柱是月均点估计，橙柱是 95% 区间半宽。**同样 12 个月的数据，2019 年的区间半宽是 97 百万美元，2020 年是 1249 百万美元，差了 13 倍。** 2020 年就是疫情那一年，3 月到 6 月的销售额像坐过山车。**样本量一样，波动越大区间越宽。**

## 为什么 4.0 后面要跟一个区间

**因为 4.0 是所有可能结果里最「像真的」那一个，不是最可靠的那一个。** eBay 的一次真实投放把这件事摊开了：Blake、Nosko 和 Tadelis 在 *Econometrica* 2015 年那篇论文里，把同一批品牌词广告用三种办法算 ROI。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%E6%8A%95%E6%94%BE%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%E7%BB%99%E5%87%BA%E7%9A%84%20ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%230891b2%22%2C%22%23dc2626%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%EF%BC%88%E4%B8%8D%E5%8A%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%EF%BC%88%E5%8A%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E5%9C%B0%E5%8C%BA%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22ROI%EF%BC%88%25%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%E6%8A%95%E6%94%BE%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%E7%BB%99%E5%87%BA%E7%9A%84%20ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%230891b2%22%2C%22%23dc2626%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%EF%BC%88%E4%B8%8D%E5%8A%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%EF%BC%88%E5%8A%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E5%9C%B0%E5%8C%BA%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22ROI%EF%BC%88%25%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%E6%8A%95%E6%94%BE%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%E7%BB%99%E5%87%BA%E7%9A%84%20ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%230891b2%22%2C%22%23dc2626%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%EF%BC%88%E4%B8%8D%E5%8A%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%EF%BC%88%E5%8A%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E5%9C%B0%E5%8C%BA%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22ROI%EF%BC%88%25%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="ebay_roi_three_ways"></a>

回归不加控制变量：**4100%**。加上时间项和地区控制变量：**1400%**。随机实验：**−63%**，95% 置信区间 **[−124%, −3%]**。

前两个数是被观测口径污染的：广告投给本来就要买的人，买的人多是因为被投了。真正扎眼的是第三个：**−63% 的区间整个在零以下**，随机实验说这些广告不但没赚回来，还倒赔。

**一、把「负多少」说清楚了。** −63% 看着温和，好像「稍微亏一点」。但下限是 −124%：**投一块钱进去，亏一块二**。这个数字直接否掉了「再投一笔试试」。

**二、把「有多确定」说清楚了。** 上限 −3% 离零只有 3 个百分点，**实验再大一点，区间上端可能就跨过零了**，答案会从「确定是亏」变成「可能也可能是亏」。前者是关掉，后者是继续观察。**不带区间的 −63% 分不出这两者。**

## 点估计 4.0 是最好猜的那个数，不是最靠得住的

很多争论停在「到底是 4.0 还是 3.4」上，各拿一个点估计谁也说服不了谁——**因为点估计的差别，通常小于两个区间各自的宽度。** **区间把争论从「谁的数对」换成「差多少才够大」。**

但区间本身也不能当结论。**区间的宽度是你自己的实验设计决定的，不是数据本身告诉你的。** 还有一层更隐蔽的：**区间只覆盖「模型形式是对的」这个前提，不覆盖模型形式本身对不对。** 口径偏了，区间再窄也偏。**看了一堆模型只报最好的那个，区间是假的。**

## 区间在说什么

**95% 置信区间，正确的意思是：真值有 95% 的概率落在这个范围里。** 这句话约束的是**真值**，不是「你算出来的数」。设真实效果是 +2 个百分点，每组测 200 人，区间半宽约 29 个百分点（[样本量与检验力](../02-sample-size-and-power/cn.md) 的算例），算出来的数落在 +31% 到 −27% 之间都正常。

**每重跑 20 次，大约有 1 次，那个 95% 的区间盖不住真值。** 这 5% 写「95% 置信区间」时已扣掉。**它不是「这次有 95% 的把握」，是「这个方法有 95% 的覆盖率」。**


## 区间有多宽，由什么决定

**三样东西：样本量、变异程度、效应大小。** 样本量这一项，标准误跟它的平方根成反比。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%95%88%E5%BA%94%EF%BC%8C%E6%A0%B7%E6%9C%AC%E9%87%8F%E4%B8%8D%E5%90%8C%E7%BB%99%E5%87%BA%E7%9A%84%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%AF%8F%E7%BB%84%2050%20%E4%BA%BA%22%2C%22%E6%AF%8F%E7%BB%84%20200%20%E4%BA%BA%22%2C%22%E6%AF%8F%E7%BB%84%202000%20%E4%BA%BA%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%99%BE%E5%88%86%E7%82%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E5%88%86%E7%82%B9%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B56%2C29%2C9%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%95%88%E5%BA%94%EF%BC%8C%E6%A0%B7%E6%9C%AC%E9%87%8F%E4%B8%8D%E5%90%8C%E7%BB%99%E5%87%BA%E7%9A%84%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%AF%8F%E7%BB%84%2050%20%E4%BA%BA%22%2C%22%E6%AF%8F%E7%BB%84%20200%20%E4%BA%BA%22%2C%22%E6%AF%8F%E7%BB%84%202000%20%E4%BA%BA%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%99%BE%E5%88%86%E7%82%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E5%88%86%E7%82%B9%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B56%2C29%2C9%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%95%88%E5%BA%94%EF%BC%8C%E6%A0%B7%E6%9C%AC%E9%87%8F%E4%B8%8D%E5%90%8C%E7%BB%99%E5%87%BA%E7%9A%84%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%AF%8F%E7%BB%84%2050%20%E4%BA%BA%22%2C%22%E6%AF%8F%E7%BB%84%20200%20%E4%BA%BA%22%2C%22%E6%AF%8F%E7%BB%84%202000%20%E4%BA%BA%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%99%BE%E5%88%86%E7%82%B9%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E7%99%BE%E5%88%86%E7%82%B9%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B56%2C29%2C9%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="ci_width_vs_sample_size"></a>

同一个效应量，每组 50 人时区间半宽 **56 个百分点**，每组 200 人时 **29 个百分点**，每组 2000 人时 **9 个百分点**。**样本量翻 40 倍，区间宽度只收到六分之一。**

**变异程度。** 开头那张图已经说了：2019 年半宽 97 百万美元，2020 年 1249 百万美元。**加样本能改善一点，改不了根本——变异大是生意本身的事。**

**效应大小。** 这一项最反直觉：**你想测的效果越小，需要的样本越多，而且是平方关系**——效果减半，样本翻两番。

## 区间重叠了，能不能比

**能比，但要比的是差值，不是两个点估计各自的值。** 区间重叠说的是「各自绝对水平」，你想问的却是「A 比 B 好多少」。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%A4%E4%B8%AA%E6%B8%A0%E9%81%93%E7%9A%84%20ROI%EF%BC%9A%E7%82%B9%E4%BC%B0%E8%AE%A1%E4%B8%8E%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%B8%A0%E9%81%93%20A%EF%BC%88%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%89%22%2C%22%E6%B8%A0%E9%81%93%20B%EF%BC%88%E4%BF%A1%E6%81%AF%E6%B5%81%E5%B9%BF%E5%91%8A%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%E6%AF%8F%201%20%E5%85%83%E6%8A%95%E5%85%A5%E6%8D%A2%E5%9B%9E%E5%A4%9A%E5%B0%91%E5%85%83%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%2C%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E4%B8%8A%E4%B8%8B%E5%90%84%E5%B7%AE%E8%BF%99%E4%B9%88%E5%A4%9A%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4.0%2C3.4%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%2C%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E4%B8%8A%E4%B8%8B%E5%90%84%E5%B7%AE%E8%BF%99%E4%B9%88%E5%A4%9A%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.8%2C1.3%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=440
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%A4%E4%B8%AA%E6%B8%A0%E9%81%93%E7%9A%84%20ROI%EF%BC%9A%E7%82%B9%E4%BC%B0%E8%AE%A1%E4%B8%8E%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%B8%A0%E9%81%93%20A%EF%BC%88%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%89%22%2C%22%E6%B8%A0%E9%81%93%20B%EF%BC%88%E4%BF%A1%E6%81%AF%E6%B5%81%E5%B9%BF%E5%91%8A%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%E6%AF%8F%201%20%E5%85%83%E6%8A%95%E5%85%A5%E6%8D%A2%E5%9B%9E%E5%A4%9A%E5%B0%91%E5%85%83%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%2C%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E4%B8%8A%E4%B8%8B%E5%90%84%E5%B7%AE%E8%BF%99%E4%B9%88%E5%A4%9A%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4.0%2C3.4%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%2C%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E4%B8%8A%E4%B8%8B%E5%90%84%E5%B7%AE%E8%BF%99%E4%B9%88%E5%A4%9A%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.8%2C1.3%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=440"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%A4%E4%B8%AA%E6%B8%A0%E9%81%93%E7%9A%84%20ROI%EF%BC%9A%E7%82%B9%E4%BC%B0%E8%AE%A1%E4%B8%8E%2095%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%B8%A0%E9%81%93%20A%EF%BC%88%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%89%22%2C%22%E6%B8%A0%E9%81%93%20B%EF%BC%88%E4%BF%A1%E6%81%AF%E6%B5%81%E5%B9%BF%E5%91%8A%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%E6%AF%8F%201%20%E5%85%83%E6%8A%95%E5%85%A5%E6%8D%A2%E5%9B%9E%E5%A4%9A%E5%B0%91%E5%85%83%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%2C%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E4%B8%8A%E4%B8%8B%E5%90%84%E5%B7%AE%E8%BF%99%E4%B9%88%E5%A4%9A%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22ROI%20%E7%82%B9%E4%BC%B0%E8%AE%A1%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4.0%2C3.4%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%2C%7B%22name%22%3A%22%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%E4%B8%8A%E4%B8%8B%E5%90%84%E5%B7%AE%E8%BF%99%E4%B9%88%E5%A4%9A%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.8%2C1.3%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=440" width="760" alt="two_channel_roi_ci"></a>

渠道 A（搜索广告）ROI 点估计 **4.0**，95% 区间 **[1.2, 6.8]**，半宽 2.8。渠道 B（信息流广告）点估计 **3.4**，95% 区间 **[2.1, 4.7]**，半宽 1.3。**A 的区间更宽，不代表 A 更差，只代表 A 那场实验设计得更糙。**

差值是 4.0 − 3.4 = **0.6**。两个标准误平方和再开根是差值的标准误，1.96 倍是 ±3.09，**差值的 95% 区间是 [−2.5, 3.7]**。**跨过零，以现有数据你分不出 A 和 B 谁好。**

**那这 0.6 能不能拿去加预算？** 看业务量级。渠道 A 一个月花 100 万、B 花 50 万，0.6 的 ROI 差距在 A 上是每月 60 万增量收入，**远大于两个渠道的区间半宽**，那就值得比。**如果两个渠道一个月各花 5 万，这 0.6 只有 3 万块，不值得再买一轮流量。**

**差值区间跨过零的时候别硬比。** 硬比的做法是「A 4.0 > B 3.4，所以 A 好」。这个结论的强度取决于两个渠道是各自独立测的，还是同一个实验里的两个组。**同一场实验的两个组，差值可直接算。**

## ROI 4.0，区间从 1.2 到 6.8

某消费品牌 2024 年在自家 App 里做搜索广告增量测试。投放期内搜索广告花了 **100 万元**，随机分流的对照测出增量收入 **400 万元**，**ROI 点估计是 4.0**。

跑出来的 95% 置信区间是 **[1.2, 6.8]**。**翻译成钱：** 增量收入 400 万、ROI 4.0。下限 120 万、ROI 1.2，上限 680 万、ROI 6.8。

**只有 ROI 4.0：** 每投一块钱换回四块，按这个数推预算，下个月加投 50 万，预期带回 200 万增量收入。**这是把点估计当承诺。** 带上区间 [1.2, 6.8]：最坏的情况只带回 120 万，**还是正的，但只剩 20 万净增**；最好的情况带回 680 万，净增 580 万。**下限那端勉强回本，上限那端是小生意变成好生意。**

**这个区间的实际用途，是它直接否掉了一个具体动作。** 那个团队原本打算在 ROI 4.0 之后加投 200 万。看完区间他们没加——**因为如果真值在 1.2 那一端，加投的 200 万带回来的增量收入扣掉投放本身，可能只是持平。**「看起来稳赚」变成「先小步试」。

**代价也写清楚：** 实验跑了六周，实验组占 10% 流量，曝光损失大约是这段时间自然流量的一个百分点。**严谨是有账单的。**

## 报数带上区间

**以后每个数，都带上它的区间。** 报数时把三件事一起说：**点估计是多少、区间多宽、这个区间是在什么样本量和什么口径下得到的。** 第三件最容易被省，但**同一个数不带这行字，半年后没人知道它出自多大的实验。**

可以抄的格式：

```text
增量 ROI 4.0，95% 置信区间 [1.2, 6.8]；n = 每组 12,480，实验期 6 周，
随机分流，指标为 14 天内增量订单金额。
```

两个坑在 FAQ 里写透了：只报显著的那个区间是假的，见 [多重比较](../03-multiple-testing/cn.md)；区间宽也不能当「所以你还是用点估计吧」。

[→ 对照组该怎么定](../01-what-a-control-group-is/cn.md) · [→ 样本太少，结论会反着](../02-sample-size-and-power/cn.md) · [→ 测的组合太多](../03-multiple-testing/cn.md) · [→ 置信区间和拟合度](../../8-analysis-toolbox/08-confidence-intervals-and-fit/cn.md)

**数据**：美国家具与家居用品专卖店的月度销售额取自 BEA 零售销售统计（`x dbnomics data BEA/NIUnderlyingDetail-U00500/T05008-M`，截至 2023 年末），区间按各年 12 个月的均值、标准误和 1.96 倍标准误算出（口径卡 `us_furniture_store_sales_price_volume`）。eBay 的三种 ROI 算法（4100%、1400%、−63%，95% 区间 [−124%, −3%]）出自 Blake, Nosko & Tadelis, *Econometrica* 83(1), 2015（口径卡 `paid_search_roi_observed_vs_randomized`）。区间半宽三档（56 / 29 / 9 个百分点）取自口径卡 `ci_width_vs_sample_size`。「ROI 4.0、区间 [1.2, 6.8]」的场景与流量成本是算例，不对应具体公司。

**复现**：BEA 数据的区间这样算，命令是 `x dbnomics data BEA/NIUnderlyingDetail-U00500/T05008-M`：

```
x dbnomics data BEA/NIUnderlyingDetail-U00500/T05008-M | python3 -c "
import sys, math, statistics as st
d = {}
for l in sys.stdin:
    l = l.strip()
    if not l or l.startswith('period'): continue
    k, v = l.split('\t'); d[k] = float(v)
for y in ('2019','2020','2021','2022','2023'):
    v = [x for k, x in sorted(d.items()) if k.startswith(y)]
    m, sd = st.mean(v), st.stdev(v)
    hw = 1.96 * sd / math.sqrt(len(v))
    print(y, 'n=%d mean=%.1f halfwidth=%.1f CI=[%.1f, %.1f]' % (len(v), m, hw, m-hw, m+hw))
"
```
