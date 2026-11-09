# 算最优之前，先把限制列出来

解算器不会替你检查现实。它只把你给的约束算完。你不给，它就当没有约束。

**上一篇那个算例里已经埋了一堵墙。** 三个渠道、100 万总量，边际拉平的解是搜索 30 万、社交 40 万、内容 30 万，总回报 2.52。但社交渠道有合同锁死的量，不超过 30 万。解算器不知道这堵墙，算出来的是 40 万——差 10 万，总回报从 2.52 掉到 2.45。

## 为什么算出来的最优做不到

**这还只是一个约束。**

## 先把这五类限制列出来

**一、合同锁死的量。** 某渠道承诺一年花多少钱，或者某类广告位买断了一段时间。这些数在合同里，不在报表里——但解算必须知道。

**二、必须花到的下限。** 品牌要维持曝光，新品要铺渠道，某些平台的算法要求你每天有一定消耗。下限不会出现在「上个月花了多少」里，它在运营的承诺里。

**三、卖得出的量。** 库存只够投这么多周，产能只够这么多单。**这一条最容易被忘，因为它是仓库的事，不是市场部的事**——但它决定你能把预算花到多大。

**四、人手。** 投放团队一天能调几次出价、能盯住几个账户、素材多久能上一批。这些不写进约束，优化解就会长出一个没人执行得下去的样子。

**五、法规与平台规则。** 某些品类的广告有限制，Cookie 同意的规定会改变你能测到什么，某些渠道对某些行业直接不接。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%90%A5%E9%94%80%E5%B9%BF%E5%91%8A%E8%B4%B9%E5%8D%A0%E8%90%A5%E6%94%B6%E7%9A%84%E6%AF%94%E9%87%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22NIKE%22%2C%22Deckers%22%5D%2C%22top%22%3A28%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22FY2023%22%2C%22FY2024%22%2C%22FY2025%22%2C%22FY2026%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%8D%A0%E8%90%A5%E6%94%B6%EF%BC%88%25%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22NIKE%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B7.93%2C8.34%2C10.13%2C10.25%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%232563eb%22%7D%7D%2C%7B%22name%22%3A%22Deckers%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B7.48%2C8.14%2C8.67%2C9.06%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%90%A5%E9%94%80%E5%B9%BF%E5%91%8A%E8%B4%B9%E5%8D%A0%E8%90%A5%E6%94%B6%E7%9A%84%E6%AF%94%E9%87%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22NIKE%22%2C%22Deckers%22%5D%2C%22top%22%3A28%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22FY2023%22%2C%22FY2024%22%2C%22FY2025%22%2C%22FY2026%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%8D%A0%E8%90%A5%E6%94%B6%EF%BC%88%25%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22NIKE%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B7.93%2C8.34%2C10.13%2C10.25%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%232563eb%22%7D%7D%2C%7B%22name%22%3A%22Deckers%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B7.48%2C8.14%2C8.67%2C9.06%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%90%A5%E9%94%80%E5%B9%BF%E5%91%8A%E8%B4%B9%E5%8D%A0%E8%90%A5%E6%94%B6%E7%9A%84%E6%AF%94%E9%87%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22NIKE%22%2C%22Deckers%22%5D%2C%22top%22%3A28%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22FY2023%22%2C%22FY2024%22%2C%22FY2025%22%2C%22FY2026%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%8D%A0%E8%90%A5%E6%94%B6%EF%BC%88%25%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22NIKE%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B7.93%2C8.34%2C10.13%2C10.25%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%232563eb%22%7D%7D%2C%7B%22name%22%3A%22Deckers%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B7.48%2C8.14%2C8.67%2C9.06%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="mkt_share_of_revenue"></a>

**真实的约束，长这样。** 上面这条是 NIKE 和 Deckers 的营销广告费占营收比重（SEC XBRL，2026-11 取数）。

NIKE 三年里营收从 512 亿降到 464 亿，跌了 9.4%；营销广告费却从 40.6 亿涨到 47.5 亿，涨了 17%。**投放强度被动从 7.93% 抬到 10.25%**——营收掉了，预算没跟着掉，比例就上去了。

Deckers 是另一种：营收三年涨了 50.7%，营销费率也从 7.48% 走到 9.06%。**这是主动加投，不是被动抬升。**

同样一条「营销费率」的线，一个是约束在起作用，一个是选择在做主。分不清这两种，你会把「被动抬升」当成「增长乏力」，然后把预算加到最不该加的地方。

## 约束没列全，会算出什么

**第一种：解算器给你一个你做不到的解。** 它不知道你只有两个人做投放，于是把 40% 的预算排给需要每天盯的渠道。

**第二种：更贵的一种——你手工改回现实，但改法不是最优的。** 你看到社交超了 10 万，把内容挪过去 10 万。**你只改了违反最明显的那一条约束**，剩下的约束还在，你得到一个「能执行但不是最优」的解。

**第三种：最危险。** 解算器给了你一个看起来很合理的解，而你不知道它违反了某条你不知道存在的约束。你照着执行，三个月后才发现那个渠道根本没有承接能力。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%89%E6%9D%A1%E8%BE%B9%E9%99%85%E6%9B%B2%E7%BA%BF%EF%BC%8C%E5%92%8C%E4%B8%89%E5%A0%B5%E5%A2%99%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E5%86%85%E5%AE%B9%E6%8A%95%E6%94%BE%22%5D%2C%22top%22%3A28%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220-10%E4%B8%87%22%2C%2210-20%E4%B8%87%22%2C%2220-30%E4%B8%87%22%2C%2230-40%E4%B8%87%22%2C%2240-50%E4%B8%87%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%AF%8F%2010%20%E4%B8%87%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B4.8%2C3.4%2C2.0%2C1.1%2C0.4%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%232563eb%22%7D%2C%22markLine%22%3A%7B%22silent%22%3Atrue%2C%22symbol%22%3A%22none%22%2C%22lineStyle%22%3A%7B%22type%22%3A%22dashed%22%2C%22color%22%3A%22%23dc2626%22%2C%22width%22%3A2%7D%2C%22label%22%3A%7B%22formatter%22%3A%22%E7%A4%BE%E4%BA%A4%20%E2%89%A4%2030%20%E4%B8%87%22%2C%22position%22%3A%22insideEndTop%22%2C%22fontSize%22%3A10%2C%22color%22%3A%22%23dc2626%22%7D%2C%22data%22%3A%5B%7B%22xAxis%22%3A1.5%7D%5D%7D%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B1.0%2C1.5%2C1.8%2C2.0%2C2.3%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%2C%7B%22name%22%3A%22%E5%86%85%E5%AE%B9%E6%8A%95%E6%94%BE%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B3.9%2C2.8%2C2.0%2C1.3%2C0.7%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2364748b%22%7D%2C%22markLine%22%3A%7B%22silent%22%3Atrue%2C%22symbol%22%3A%22none%22%2C%22lineStyle%22%3A%7B%22type%22%3A%22dashed%22%2C%22color%22%3A%22%230891b2%22%2C%22width%22%3A2%7D%2C%22label%22%3A%7B%22formatter%22%3A%22%E5%86%85%E5%AE%B9%20%E2%89%A4%2035%20%E4%B8%87%22%2C%22position%22%3A%22insideEndTop%22%2C%22fontSize%22%3A10%2C%22color%22%3A%22%230891b2%22%7D%2C%22data%22%3A%5B%7B%22xAxis%22%3A2.5%7D%5D%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%89%E6%9D%A1%E8%BE%B9%E9%99%85%E6%9B%B2%E7%BA%BF%EF%BC%8C%E5%92%8C%E4%B8%89%E5%A0%B5%E5%A2%99%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E5%86%85%E5%AE%B9%E6%8A%95%E6%94%BE%22%5D%2C%22top%22%3A28%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220-10%E4%B8%87%22%2C%2210-20%E4%B8%87%22%2C%2220-30%E4%B8%87%22%2C%2230-40%E4%B8%87%22%2C%2240-50%E4%B8%87%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%AF%8F%2010%20%E4%B8%87%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B4.8%2C3.4%2C2.0%2C1.1%2C0.4%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%232563eb%22%7D%2C%22markLine%22%3A%7B%22silent%22%3Atrue%2C%22symbol%22%3A%22none%22%2C%22lineStyle%22%3A%7B%22type%22%3A%22dashed%22%2C%22color%22%3A%22%23dc2626%22%2C%22width%22%3A2%7D%2C%22label%22%3A%7B%22formatter%22%3A%22%E7%A4%BE%E4%BA%A4%20%E2%89%A4%2030%20%E4%B8%87%22%2C%22position%22%3A%22insideEndTop%22%2C%22fontSize%22%3A10%2C%22color%22%3A%22%23dc2626%22%7D%2C%22data%22%3A%5B%7B%22xAxis%22%3A1.5%7D%5D%7D%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B1.0%2C1.5%2C1.8%2C2.0%2C2.3%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%2C%7B%22name%22%3A%22%E5%86%85%E5%AE%B9%E6%8A%95%E6%94%BE%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B3.9%2C2.8%2C2.0%2C1.3%2C0.7%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2364748b%22%7D%2C%22markLine%22%3A%7B%22silent%22%3Atrue%2C%22symbol%22%3A%22none%22%2C%22lineStyle%22%3A%7B%22type%22%3A%22dashed%22%2C%22color%22%3A%22%230891b2%22%2C%22width%22%3A2%7D%2C%22label%22%3A%7B%22formatter%22%3A%22%E5%86%85%E5%AE%B9%20%E2%89%A4%2035%20%E4%B8%87%22%2C%22position%22%3A%22insideEndTop%22%2C%22fontSize%22%3A10%2C%22color%22%3A%22%230891b2%22%7D%2C%22data%22%3A%5B%7B%22xAxis%22%3A2.5%7D%5D%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%89%E6%9D%A1%E8%BE%B9%E9%99%85%E6%9B%B2%E7%BA%BF%EF%BC%8C%E5%92%8C%E4%B8%89%E5%A0%B5%E5%A2%99%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22%E5%86%85%E5%AE%B9%E6%8A%95%E6%94%BE%22%5D%2C%22top%22%3A28%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220-10%E4%B8%87%22%2C%2210-20%E4%B8%87%22%2C%2220-30%E4%B8%87%22%2C%2230-40%E4%B8%87%22%2C%2240-50%E4%B8%87%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%AF%8F%2010%20%E4%B8%87%E7%9A%84%E8%BE%B9%E9%99%85%E5%9B%9E%E6%8A%A5%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B4.8%2C3.4%2C2.0%2C1.1%2C0.4%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%232563eb%22%7D%2C%22markLine%22%3A%7B%22silent%22%3Atrue%2C%22symbol%22%3A%22none%22%2C%22lineStyle%22%3A%7B%22type%22%3A%22dashed%22%2C%22color%22%3A%22%23dc2626%22%2C%22width%22%3A2%7D%2C%22label%22%3A%7B%22formatter%22%3A%22%E7%A4%BE%E4%BA%A4%20%E2%89%A4%2030%20%E4%B8%87%22%2C%22position%22%3A%22insideEndTop%22%2C%22fontSize%22%3A10%2C%22color%22%3A%22%23dc2626%22%7D%2C%22data%22%3A%5B%7B%22xAxis%22%3A1.5%7D%5D%7D%7D%2C%7B%22name%22%3A%22%E7%A4%BE%E4%BA%A4%E5%B9%BF%E5%91%8A%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B1.0%2C1.5%2C1.8%2C2.0%2C2.3%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%2C%7B%22name%22%3A%22%E5%86%85%E5%AE%B9%E6%8A%95%E6%94%BE%22%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22data%22%3A%5B3.9%2C2.8%2C2.0%2C1.3%2C0.7%5D%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2364748b%22%7D%2C%22markLine%22%3A%7B%22silent%22%3Atrue%2C%22symbol%22%3A%22none%22%2C%22lineStyle%22%3A%7B%22type%22%3A%22dashed%22%2C%22color%22%3A%22%230891b2%22%2C%22width%22%3A2%7D%2C%22label%22%3A%7B%22formatter%22%3A%22%E5%86%85%E5%AE%B9%20%E2%89%A4%2035%20%E4%B8%87%22%2C%22position%22%3A%22insideEndTop%22%2C%22fontSize%22%3A10%2C%22color%22%3A%22%230891b2%22%7D%2C%22data%22%3A%5B%7B%22xAxis%22%3A2.5%7D%5D%7D%7D%5D%7D&w=760&h=420" width="760" alt="marginal_with_constraints"></a>

**约束是怎么改解的。** 上面这张图接着上一篇那三条边际曲线，把约束画成竖线：社交渠道 30 万封顶（合同），内容渠道 35 万封顶（库存）。

**没有墙的时候**，三条线在 20–30 万和 30–40 万之间交汇，共同的边际大约 2.0。**有墙的时候**，交点被墙切掉了，最优解往墙角挪。

**墙不是把方案缩小，是把方案挪位。** 社交封顶 30 万，搜索那 30 万没动，多的 10 万去了内容——内容从 30 万涨到 40 万，它的边际从 2.0 掉到 1.3。**这就是那 0.07 的总回报差从哪来的。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%20100%20%E4%B8%87%EF%BC%8C%E7%BA%A6%E6%9D%9F%E8%B6%8A%E5%8A%A0%E8%B6%8A%E5%A4%9A%EF%BC%8C%E8%83%BD%E6%8B%BF%E5%88%B0%E7%9A%84%E5%9B%9E%E6%8A%A5%E8%B6%8A%E5%B0%91%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A90%2C%22top%22%3A60%2C%22bottom%22%3A70%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%B2%A1%E6%9C%89%E7%BA%A6%E6%9D%9F%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B0%81%E9%A1%B6%2030%20%E4%B8%87%22%2C%22%E5%86%8D%E5%B0%81%E5%86%85%E5%AE%B9%E4%B8%8E%E6%90%9C%E7%B4%A2%22%2C%22%E5%86%8D%E5%8A%A0%E4%B8%8A%E5%88%AB%E7%9A%84%E7%BA%A6%E6%9D%9F%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%2C%22rotate%22%3A18%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%EF%BC%88%E6%AF%8F%201%20%E5%9D%97%E9%92%B1%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.52%2C2.45%2C2.32%2C2.18%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%20100%20%E4%B8%87%EF%BC%8C%E7%BA%A6%E6%9D%9F%E8%B6%8A%E5%8A%A0%E8%B6%8A%E5%A4%9A%EF%BC%8C%E8%83%BD%E6%8B%BF%E5%88%B0%E7%9A%84%E5%9B%9E%E6%8A%A5%E8%B6%8A%E5%B0%91%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A90%2C%22top%22%3A60%2C%22bottom%22%3A70%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%B2%A1%E6%9C%89%E7%BA%A6%E6%9D%9F%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B0%81%E9%A1%B6%2030%20%E4%B8%87%22%2C%22%E5%86%8D%E5%B0%81%E5%86%85%E5%AE%B9%E4%B8%8E%E6%90%9C%E7%B4%A2%22%2C%22%E5%86%8D%E5%8A%A0%E4%B8%8A%E5%88%AB%E7%9A%84%E7%BA%A6%E6%9D%9F%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%2C%22rotate%22%3A18%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%EF%BC%88%E6%AF%8F%201%20%E5%9D%97%E9%92%B1%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.52%2C2.45%2C2.32%2C2.18%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%20100%20%E4%B8%87%EF%BC%8C%E7%BA%A6%E6%9D%9F%E8%B6%8A%E5%8A%A0%E8%B6%8A%E5%A4%9A%EF%BC%8C%E8%83%BD%E6%8B%BF%E5%88%B0%E7%9A%84%E5%9B%9E%E6%8A%A5%E8%B6%8A%E5%B0%91%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A70%2C%22right%22%3A90%2C%22top%22%3A60%2C%22bottom%22%3A70%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%B2%A1%E6%9C%89%E7%BA%A6%E6%9D%9F%22%2C%22%E7%A4%BE%E4%BA%A4%E5%B0%81%E9%A1%B6%2030%20%E4%B8%87%22%2C%22%E5%86%8D%E5%B0%81%E5%86%85%E5%AE%B9%E4%B8%8E%E6%90%9C%E7%B4%A2%22%2C%22%E5%86%8D%E5%8A%A0%E4%B8%8A%E5%88%AB%E7%9A%84%E7%BA%A6%E6%9D%9F%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%2C%22rotate%22%3A18%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%80%BB%E5%9B%9E%E6%8A%A5%EF%BC%88%E6%AF%8F%201%20%E5%9D%97%E9%92%B1%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.52%2C2.45%2C2.32%2C2.18%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="return_vs_constraints"></a>

**同一条曲线，约束每加一层，能拿到的回报就少一截。** 2.52 → 2.45 → 2.32。

**回报会少，但这是好事。** 那个 2.52 本身是假的——它建立在你做不到的假设上。**真实的 2.32 比假的 2.52 有用得多**，因为它你能执行。

## 一个算出来、做不到的最优解

把上一篇的算例收尾。三个渠道、100 万，约束一次加齐：

- 社交渠道合同封顶 30 万
- 内容渠道库存只够 35 万
- 搜索渠道的平台日预算上限，折算下来 35 万

**没有约束的解**：搜索 30 万、社交 40 万、内容 30 万，总回报 2.52。

**把三堵墙都砌上**：社交 30 万（4.3）、内容 35 万（8.7）、搜索 35 万（10.2），总回报 **2.32**。

**这个解和拉平解长得完全不一样。** 拉平解是三个渠道各占三分之一的样子（30/40/30）；带约束的解是 35/30/35——**搜索和内容各拿 35 万，社交被压到 30 万。** 搜索那条最陡的线反而拿到了最多的钱，因为它最早见顶，得在前面把量占住。

**这就是为什么约束要先列。** 约束不是算完之后再检查一遍的东西——**它会改解的形状**。你在解算完之后才发现「社交不能超过 30 万」，然后手工改，等于放弃了这一轮优化；你在解算之前就知道，最优解根本不是那个样子。

## 先列约束，再解

顺序是死的：**列约束 → 解 → 验可行**。

**列约束这一步最容易糊弄。** 最常见的情况是：你脑子里列的其实是「我希望它算出来的样子」，不是现实。每一条约束都要能回答三个问题：**谁定的？写在哪儿？什么时候失效？**

- 合同锁死的量——写在合同里，续约时失效
- 库存——仓库系统里，每天变
- 人手——排期表上，人走了就变
- 法规——法务或平台政策里，改一次变一次

**答不上「写在哪儿」的约束，多半是想当然的。** 想当然的约束会让解算器给出一个看起来严谨、其实没人能执行的结果。

**顺带说一句：约束是会变的。** 库存这个月紧、下个月松；合同这个季度到期、下个季度重签；人手换了一批，盯账户的效率变了。**所以约束表要有日期，也要定期重算。** 拿三个月的旧约束去解今天的预算，等于解了一个不存在的问题。

**最后一步别省。** 解算器给你的解，要拿回现实的清单上逐条对一遍：对得上，执行；对不上，重解。**这一遍是机械活，但它是整条链上唯一能挡住「一个漂亮的错数」的地方。**

[→ 挪完预算，要复查两件事](../../6-budget-optimization/03-after-the-shift-what-goes-wrong/cn.md)

**数据**：营销费用率取自 SEC EDGAR XBRL（NIKE CIK 320187、Deckers CIK 910521 的 `us-gaap/MarketingAndAdvertisingExpense` 与 `RevenueFromContractWithCustomerExcludingAssessedTax`），2026-11-08 抓取；Skechers 与 Wolverine 的 XBRL 里没有单独列营销费用，因此未进图。边际曲线与约束算例是示意数据，承接 [→ 钱怎么分，才不会白花](../01-equal-marginal-returns/cn.md) 的同一套模型。**复现**：`curl -s -H 'User-Agent: <你> <邮箱>' https://data.sec.gov/api/xbrl/companyconcept/CIK0000320187/us-gaap/MarketingAndAdvertisingExpense.json`
