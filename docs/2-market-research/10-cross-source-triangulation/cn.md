# 一个数敢不敢用，先找第二个来源对一遍

一份财报说这个季度卖了 2019 亿美元，同一份材料的三个分部加起来却是 2020 亿。另一份财报说这一年的营收「持平」，同一句话的后半截写着「按固定汇率算跌了 2%」。

这些差异不是有人算错，是每个数字背后都站着一套没写出来的口径。**两个来源对一遍，不是为了找出一个「真的那个」，是为了知道差在哪一格。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22NIKE%20FY2026%20%E5%88%86%E9%83%A8%E8%90%A5%E6%94%B6%E5%A2%9E%E9%80%9F%EF%BC%9A%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%20vs%20%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%A4%A7%E4%B8%AD%E5%8D%8E%E5%8C%BA%E9%9E%8B%E7%B1%BB%22%2C%22%E5%A4%A7%E4%B8%AD%E5%8D%8E%E5%8C%BA%E5%90%88%E8%AE%A1%22%2C%22EMEA%E9%9E%8B%E7%B1%BB%22%2C%22APLA%E5%90%88%E8%AE%A1%22%2C%22Converse%E5%85%A8%E5%B9%B4%22%2C%22NIKE%E5%93%81%E7%89%8C%E5%90%88%E8%AE%A1%22%2C%22NIKE%E5%85%AC%E5%8F%B8%E5%90%88%E8%AE%A1%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%90%8C%E6%AF%94%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%22%2C%22%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%22%2C%22data%22%3A%5B-13%2C-11%2C1%2C0%2C-31%2C1%2C0%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%2C%22data%22%3A%5B-15%2C-13%2C-5%2C-1%2C-32%2C-1%2C-2%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=440
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22NIKE%20FY2026%20%E5%88%86%E9%83%A8%E8%90%A5%E6%94%B6%E5%A2%9E%E9%80%9F%EF%BC%9A%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%20vs%20%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%A4%A7%E4%B8%AD%E5%8D%8E%E5%8C%BA%E9%9E%8B%E7%B1%BB%22%2C%22%E5%A4%A7%E4%B8%AD%E5%8D%8E%E5%8C%BA%E5%90%88%E8%AE%A1%22%2C%22EMEA%E9%9E%8B%E7%B1%BB%22%2C%22APLA%E5%90%88%E8%AE%A1%22%2C%22Converse%E5%85%A8%E5%B9%B4%22%2C%22NIKE%E5%93%81%E7%89%8C%E5%90%88%E8%AE%A1%22%2C%22NIKE%E5%85%AC%E5%8F%B8%E5%90%88%E8%AE%A1%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%90%8C%E6%AF%94%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%22%2C%22%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%22%2C%22data%22%3A%5B-13%2C-11%2C1%2C0%2C-31%2C1%2C0%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%2C%22data%22%3A%5B-15%2C-13%2C-5%2C-1%2C-32%2C-1%2C-2%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=440"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22NIKE%20FY2026%20%E5%88%86%E9%83%A8%E8%90%A5%E6%94%B6%E5%A2%9E%E9%80%9F%EF%BC%9A%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%20vs%20%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%A4%A7%E4%B8%AD%E5%8D%8E%E5%8C%BA%E9%9E%8B%E7%B1%BB%22%2C%22%E5%A4%A7%E4%B8%AD%E5%8D%8E%E5%8C%BA%E5%90%88%E8%AE%A1%22%2C%22EMEA%E9%9E%8B%E7%B1%BB%22%2C%22APLA%E5%90%88%E8%AE%A1%22%2C%22Converse%E5%85%A8%E5%B9%B4%22%2C%22NIKE%E5%93%81%E7%89%8C%E5%90%88%E8%AE%A1%22%2C%22NIKE%E5%85%AC%E5%8F%B8%E5%90%88%E8%AE%A1%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%90%8C%E6%AF%94%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%22%2C%22%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%8A%A5%E5%91%8A%E5%8F%A3%E5%BE%84%22%2C%22data%22%3A%5B-13%2C-11%2C1%2C0%2C-31%2C1%2C0%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%9B%BA%E5%AE%9A%E6%B1%87%E7%8E%87%E5%8F%A3%E5%BE%84%22%2C%22data%22%3A%5B-15%2C-13%2C-5%2C-1%2C-32%2C-1%2C-2%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=440" width="760" alt="nike_fy26_reported_vs_constant_currency"></a>

**这一节讲完你会知道：两个数对不上的时候，先查哪三样东西。**

## 两个数差三成，先查什么

**先别问谁对，先问它们各自量的什么。**

2026 财年，NIKE 交了两份材料：业绩公告（8-K 附件 99.1）和 10-K 里逐项打标的财务数据（XBRL）。两份材料说同一件事——全年营收 463.98 亿美元。公告的原话是「营收持平，按固定汇率口径跌 2%」。

这里有两个数：持平，和跌 2%。差 2 个百分点，听起来不多。但把同样两套口径铺到分部上，差距会拉得更开。看 EMEA 那一列：报告口径 +1%，固定汇率口径 −5%。同一个分部、同一财年，一个说涨了一个说跌了。

原因不在生意，在汇率。NIKE 的欧洲收入大多用欧元和英镑记账，2026 财年这些货币相对美元是贬的。**报告口径**回答「公司账上今年收到了多少美元」，**固定汇率口径**回答「如果汇率没变，货还是卖那么多吗」。混着用，就会得出「大中华区跌了 13%，欧洲涨了 1%」这种自相矛盾的话。

### 差三成以上的，是分母换了

上面差的是几个百分点。真正差三成以上的，是换一个分母。

美国零售业有多大？三个官方数字都能查到：美国普查局（Census）2025 年全美零售额 **83,510 亿美元**，美国经济分析局（BEA）零售业总产出 **29,452 亿美元**，BEA 零售业增加值 **18,104 亿美元**。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BE%8E%E5%9B%BD%E9%9B%B6%E5%94%AE%E4%B8%9A%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9A%E4%B8%89%E4%B8%AA%E5%AE%98%E6%96%B9%E6%95%B0%EF%BC%8C%E5%B7%AE%E7%9A%84%E4%B8%8D%E6%98%AF%E4%B8%80%E7%82%B9%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Census%20%E9%9B%B6%E5%94%AE%E9%A2%9D%EF%BC%88%E9%9B%B6%E5%94%AE%E5%95%86%E6%80%BB%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%89%22%2C%22BEA%20%E6%80%BB%E4%BA%A7%E5%87%BA%EF%BC%88%E5%90%AB%E4%B8%AD%E9%97%B4%E6%8A%95%E5%85%A5%EF%BC%89%22%2C%22BEA%20%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88%E5%87%80%E5%88%9B%E9%80%A0%E7%9A%84%E4%BB%B7%E5%80%BC%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%2C%22width%22%3A110%2C%22overflow%22%3A%22break%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%8D%81%E4%BA%BF%E7%BE%8E%E5%85%83%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%222025%20%E5%B9%B4%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B8351%2C2945.2%2C1810.4%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BE%8E%E5%9B%BD%E9%9B%B6%E5%94%AE%E4%B8%9A%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9A%E4%B8%89%E4%B8%AA%E5%AE%98%E6%96%B9%E6%95%B0%EF%BC%8C%E5%B7%AE%E7%9A%84%E4%B8%8D%E6%98%AF%E4%B8%80%E7%82%B9%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Census%20%E9%9B%B6%E5%94%AE%E9%A2%9D%EF%BC%88%E9%9B%B6%E5%94%AE%E5%95%86%E6%80%BB%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%89%22%2C%22BEA%20%E6%80%BB%E4%BA%A7%E5%87%BA%EF%BC%88%E5%90%AB%E4%B8%AD%E9%97%B4%E6%8A%95%E5%85%A5%EF%BC%89%22%2C%22BEA%20%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88%E5%87%80%E5%88%9B%E9%80%A0%E7%9A%84%E4%BB%B7%E5%80%BC%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%2C%22width%22%3A110%2C%22overflow%22%3A%22break%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%8D%81%E4%BA%BF%E7%BE%8E%E5%85%83%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%222025%20%E5%B9%B4%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B8351%2C2945.2%2C1810.4%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BE%8E%E5%9B%BD%E9%9B%B6%E5%94%AE%E4%B8%9A%E6%9C%89%E5%A4%9A%E5%A4%A7%EF%BC%9A%E4%B8%89%E4%B8%AA%E5%AE%98%E6%96%B9%E6%95%B0%EF%BC%8C%E5%B7%AE%E7%9A%84%E4%B8%8D%E6%98%AF%E4%B8%80%E7%82%B9%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Census%20%E9%9B%B6%E5%94%AE%E9%A2%9D%EF%BC%88%E9%9B%B6%E5%94%AE%E5%95%86%E6%80%BB%E9%94%80%E5%94%AE%E9%A2%9D%EF%BC%89%22%2C%22BEA%20%E6%80%BB%E4%BA%A7%E5%87%BA%EF%BC%88%E5%90%AB%E4%B8%AD%E9%97%B4%E6%8A%95%E5%85%A5%EF%BC%89%22%2C%22BEA%20%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88%E5%87%80%E5%88%9B%E9%80%A0%E7%9A%84%E4%BB%B7%E5%80%BC%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%2C%22width%22%3A110%2C%22overflow%22%3A%22break%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%8D%81%E4%BA%BF%E7%BE%8E%E5%85%83%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%222025%20%E5%B9%B4%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B8351%2C2945.2%2C1810.4%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="us_retail_three_official_numbers"></a>

同一行零售业，三个数，最大的和最小的差 **4.6 倍**。

Census 的零售额是零售商卖东西收到的钱，一件 500 美元的外套在服装店被数一次，在品牌总部算销售额时又被数一次，在批发商那里还数一次。BEA 的总产出扣掉这些中间环节，剩下的是零售环节新创造的价值。

**差三成、四倍、六倍，都不是谁在骗你，是这三个数量根本不是同一件事。**

## 两个数一样，也可能错

**两个来源给出几乎相同的数，通常让人放心。有时候恰恰该警惕。**

欧盟 2024 年的电商占比，Eurostat 给了两个：网络销售占企业总营业额 **19.82%**，其中卖给消费者的部分占企业总营业额 **8.49%**。这不是重复测量，是同一份调查里的两个分子：第一个含 B2B，第二个只留 B2C。

**换成「第二个来源」的角度看：** 假如第一个来源是公司后台的 19.82%，第二个来源是行业协会报的 18%，你会松一口气。但它们很可能来自同一个企业样本、同一套问卷口径——**它们一致，只说明上游一致。**真正的第二个来源，口径要独立：不是同一批数据换个算法，是两批不同的数据。

### 一个更隐蔽的陷阱：加总对不上

亚马逊 2026 财年第三季度业绩公告里有三条项目符号：北美分部 1129 亿美元，国际分部 431 亿美元，AWS 分部 460 亿美元。同一份材料的标题写着：净销售额 2019 亿美元。

**三个分部加起来是 2020 亿，比总数多 1 亿。**

差的不是舍入误差。AWS 卖给亚马逊自家北美和国际分部的云服务收入，在分部表里两边都算了一遍，到合并层要消掉，这 1 亿就是消抵数。两边都对：标题那个数是合并后的，分部那个数是消抵前的。**同一个数出现两次，先看它是不是同一个数。**

## 第二个来源怎么选

**不是找一个更权威的，是找一个跟你手上这个错得不一样的。**

如果第二个来源跟第一个用同一套方法算，它俩要么一起错，要么一起对——这种「对一遍」是白做的。

eBay 品牌词广告的回报率，2015 年一篇发在《Econometrica》上的论文（Blake、Nosko、Tadelis）算出三个数：常规回归 **4100%**，加时间和地区控制变量 **1400%**，随机实验 **−63%**（95% 置信区间 −124% 到 −3%）。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%EF%BC%8C%E5%87%A0%E4%B8%AA%E7%AE%97%E6%B3%95%E5%87%A0%E4%B8%AA%E6%95%B0%EF%BC%9A%E7%AC%AC%E4%BA%8C%E4%B8%AA%E6%9D%A5%E6%BA%90%E8%A6%81%E7%8B%AC%E7%AB%8B%E5%9C%A8%E6%96%B9%E6%B3%95%E4%B8%8A%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%EF%BC%88%E5%9B%9E%E5%BD%92%2F%E5%8C%B9%E9%85%8D%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%9B%9E%E6%8A%A5%E7%8E%87%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E5%B8%B8%E8%A7%84%E5%9B%9E%E5%BD%92%22%2C%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E5%8A%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%22%2C%22Facebook%EF%BC%9A%E5%8F%AA%E7%9C%8B%E6%9B%9D%E5%85%89%22%2C%22Facebook%EF%BC%9A%E5%B9%B4%E9%BE%84%E6%80%A7%E5%88%AB%E5%8C%B9%E9%85%8D%22%2C%22Facebook%EF%BC%9A%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%2C%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22grid%22%3A%7B%22left%22%3A170%2C%22right%22%3A70%2C%22top%22%3A80%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%EF%BC%88%E5%9B%9E%E5%BD%92%2F%E5%8C%B9%E9%85%8D%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C316%2C222%2Cnull%2Cnull%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%2C%7B%22name%22%3A%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%2Cnull%2C73%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%EF%BC%8C%E5%87%A0%E4%B8%AA%E7%AE%97%E6%B3%95%E5%87%A0%E4%B8%AA%E6%95%B0%EF%BC%9A%E7%AC%AC%E4%BA%8C%E4%B8%AA%E6%9D%A5%E6%BA%90%E8%A6%81%E7%8B%AC%E7%AB%8B%E5%9C%A8%E6%96%B9%E6%B3%95%E4%B8%8A%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%EF%BC%88%E5%9B%9E%E5%BD%92%2F%E5%8C%B9%E9%85%8D%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%9B%9E%E6%8A%A5%E7%8E%87%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E5%B8%B8%E8%A7%84%E5%9B%9E%E5%BD%92%22%2C%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E5%8A%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%22%2C%22Facebook%EF%BC%9A%E5%8F%AA%E7%9C%8B%E6%9B%9D%E5%85%89%22%2C%22Facebook%EF%BC%9A%E5%B9%B4%E9%BE%84%E6%80%A7%E5%88%AB%E5%8C%B9%E9%85%8D%22%2C%22Facebook%EF%BC%9A%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%2C%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22grid%22%3A%7B%22left%22%3A170%2C%22right%22%3A70%2C%22top%22%3A80%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%EF%BC%88%E5%9B%9E%E5%BD%92%2F%E5%8C%B9%E9%85%8D%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C316%2C222%2Cnull%2Cnull%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%2C%7B%22name%22%3A%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%2Cnull%2C73%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%EF%BC%8C%E5%87%A0%E4%B8%AA%E7%AE%97%E6%B3%95%E5%87%A0%E4%B8%AA%E6%95%B0%EF%BC%9A%E7%AC%AC%E4%BA%8C%E4%B8%AA%E6%9D%A5%E6%BA%90%E8%A6%81%E7%8B%AC%E7%AB%8B%E5%9C%A8%E6%96%B9%E6%B3%95%E4%B8%8A%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%EF%BC%88%E5%9B%9E%E5%BD%92%2F%E5%8C%B9%E9%85%8D%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%9B%9E%E6%8A%A5%E7%8E%87%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E5%B8%B8%E8%A7%84%E5%9B%9E%E5%BD%92%22%2C%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E5%8A%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%22%2C%22Facebook%EF%BC%9A%E5%8F%AA%E7%9C%8B%E6%9B%9D%E5%85%89%22%2C%22Facebook%EF%BC%9A%E5%B9%B4%E9%BE%84%E6%80%A7%E5%88%AB%E5%8C%B9%E9%85%8D%22%2C%22Facebook%EF%BC%9A%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%2C%22eBay%20%E5%93%81%E7%89%8C%E8%AF%8D%EF%BC%9A%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22grid%22%3A%7B%22left%22%3A170%2C%22right%22%3A70%2C%22top%22%3A80%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%EF%BC%88%E5%9B%9E%E5%BD%92%2F%E5%8C%B9%E9%85%8D%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C316%2C222%2Cnull%2Cnull%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%2C%7B%22name%22%3A%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5Bnull%2Cnull%2Cnull%2Cnull%2C73%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="ad_roi_three_methods"></a>

**这三个数的差距比上面所有例子都大，而它们量的是同一笔广告花费。**

前两个都还在用「看过广告的人 vs 没看过的人」做对照，但平台会把广告投给本来就更可能买的人，这是选择偏差。第三个是随机实验：人被随机分到「能看到广告」和「看不到广告」两组，两组除了广告以外完全一样。−63% 的意思是，在 eBay 那个场景里，停掉品牌词广告省下的钱比多赚到的还多。Facebook 那次实验（Gordon 等人，2019）是同一个故事：观测口径 316%，随机实验 73%。

> 第二个来源如果只是「同一批数据换个模型跑一遍」，它发现不了模型的偏差。第二个来源必须在**方法**上跟第一个独立。

具体到选源，三条：

- **口径独立**：分母、覆盖范围、统计对象不能是同一个，否则它复述的是第一个来源的假设。
- **时间窗能对齐**：一个季度、一个财年、一个自然年、滚动十二个月——不对齐就比不了。
- **已知它偏哪边**：调研数据通常高估「重度用户」，普查通常漏掉最小的那些。知道偏向，才能拿它当尺子。

## 对不上，先查哪一样

**顺序不能乱。先查口径，再查时点，最后才查谁算错。**反过来做，你会花一整天去查一个根本没错的人。

### 查口径

**分母、覆盖范围、统计对象——三样。**

刚才美国零售那个 4.6 倍，全在分母和统计对象上。

欧盟零售业 2022 年的增速，Eurostat 自己有两个源给出两个数：国民账户（nama_10_a64）零售业增加值 **+5.24%**，短期商业统计（sts_trtu_m）营业额指数 **+7.97%**。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%AC%A7%E7%9B%9F%E9%9B%B6%E5%94%AE%E4%B8%9A%202022%20%E5%B9%B4%E5%A2%9E%E9%80%9F%EF%BC%9A%E4%B8%A4%E4%B8%AA%20Eurostat%20%E6%BA%90%E7%BB%99%E5%87%BA%E4%B8%A4%E4%B8%AA%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E5%9B%BD%E6%B0%91%E8%B4%A6%E6%88%B7%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88nama_10_a64%EF%BC%89%22%2C%22%E7%9F%AD%E6%9C%9F%E5%95%86%E4%B8%9A%E7%BB%9F%E8%AE%A1%EF%BC%88sts_trtu_m%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%222022%20%E5%B9%B4%E5%90%8C%E6%AF%94%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%90%8C%E6%AF%94%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%9B%BD%E6%B0%91%E8%B4%A6%E6%88%B7%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88nama_10_a64%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B5.24%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%2C%7B%22name%22%3A%22%E7%9F%AD%E6%9C%9F%E5%95%86%E4%B8%9A%E7%BB%9F%E8%AE%A1%EF%BC%88sts_trtu_m%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B7.97%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=380
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%AC%A7%E7%9B%9F%E9%9B%B6%E5%94%AE%E4%B8%9A%202022%20%E5%B9%B4%E5%A2%9E%E9%80%9F%EF%BC%9A%E4%B8%A4%E4%B8%AA%20Eurostat%20%E6%BA%90%E7%BB%99%E5%87%BA%E4%B8%A4%E4%B8%AA%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E5%9B%BD%E6%B0%91%E8%B4%A6%E6%88%B7%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88nama_10_a64%EF%BC%89%22%2C%22%E7%9F%AD%E6%9C%9F%E5%95%86%E4%B8%9A%E7%BB%9F%E8%AE%A1%EF%BC%88sts_trtu_m%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%222022%20%E5%B9%B4%E5%90%8C%E6%AF%94%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%90%8C%E6%AF%94%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%9B%BD%E6%B0%91%E8%B4%A6%E6%88%B7%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88nama_10_a64%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B5.24%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%2C%7B%22name%22%3A%22%E7%9F%AD%E6%9C%9F%E5%95%86%E4%B8%9A%E7%BB%9F%E8%AE%A1%EF%BC%88sts_trtu_m%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B7.97%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=380"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%AC%A7%E7%9B%9F%E9%9B%B6%E5%94%AE%E4%B8%9A%202022%20%E5%B9%B4%E5%A2%9E%E9%80%9F%EF%BC%9A%E4%B8%A4%E4%B8%AA%20Eurostat%20%E6%BA%90%E7%BB%99%E5%87%BA%E4%B8%A4%E4%B8%AA%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E5%9B%BD%E6%B0%91%E8%B4%A6%E6%88%B7%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88nama_10_a64%EF%BC%89%22%2C%22%E7%9F%AD%E6%9C%9F%E5%95%86%E4%B8%9A%E7%BB%9F%E8%AE%A1%EF%BC%88sts_trtu_m%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%222022%20%E5%B9%B4%E5%90%8C%E6%AF%94%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%90%8C%E6%AF%94%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%9B%BD%E6%B0%91%E8%B4%A6%E6%88%B7%E5%A2%9E%E5%8A%A0%E5%80%BC%EF%BC%88nama_10_a64%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B5.24%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%2C%7B%22name%22%3A%22%E7%9F%AD%E6%9C%9F%E5%95%86%E4%B8%9A%E7%BB%9F%E8%AE%A1%EF%BC%88sts_trtu_m%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B7.97%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=380" width="760" alt="eu_retail_growth_two_sources"></a>

差 2.7 个百分点。两个都是 Eurostat 的官方统计，都是「欧盟零售业 2022 年」。

差别在口径和口径之外的东西：国民账户从企业年报和行政数据往回推，覆盖到短期调查够不着的部分。短期商业统计直接问企业这个月卖了多少，快，但填表天数少、门槛低，小企业更容易被漏掉。**这一步要问的是：这两个数量的对象一样吗？覆盖一样吗？**

### 查时点

**季末快照还是月均？累计还是当期？**

同一个 BEA 零售业总产出，2025 年的两个算法给出两个增速：年度序列（44RT-A）从 28341 亿到 29452 亿，**+3.92%**；季度序列（44RT-Q）拿第四季对第四季，从 28976 亿到 29808 亿，**+2.87%**。年度序列是四个季度平均之后比，季度序列是拿年末对年末。

**问三句：**对方报的是期末那一瞬间，还是这一段期间的平均？是累计值还是当期值？增长是跟去年同期比，还是跟上一期比？

亚马逊那条第三季度公告里就有一个现成的例子。净销售额同比「涨 12%」，但公告紧接着说：2026 年的 Prime Day 挪到了第二季度，2025 年的整个在第三季度，**排除这个挪动，同比涨幅会高大约 400 个基点**。同一个季度，12% 和大约 16%。两个都对，一个按日历，一个按活动对齐。**时点对不上的表现，通常是「方向对、幅度不对」，或者「一个季度一个方向」。**

## 第二个来源是纠错工具，不是装饰

**给关键数字配第二个来源，是为了在它错的时候能发现。**

如果第二个来源永远跟第一个一致，你会以为自己很安全，其实只是有了一个漂亮的确认。真正有用的做法是：**先写下你预计两个来源会差多少、往哪个方向差，再去看实际差多少。** 你知道 Eurostat 的电商调查漏了雇员 10 人以下的小店，所以你会预计零售业占比被低估；你知道美国零售的普查局数和 BEA 数差着好几倍，所以任何一句「零售占 GDP 百分之多少」，你都会去找另一个分母。

**预计跟实际的差，才是信息。差得比你预计的小，说明第二个来源不够独立。差得比你预计的大，说明有东西你还没看见。**

**第二个来源不是装饰。它把「我以为这是对的」变成「我知道这个数在哪一格会错」。**

[→ 同一个占比能指四件事](../../2-market-research/08-share-denominator/cn.md) · [→ 调研数据和官方数据哪个更可信](../../2-market-research/09-panel-vs-census-bias/cn.md) · [→ 这个数漏了谁](../../2-market-research/11-coverage-gaps/cn.md)

**数据**：NIKE 2026 财年业绩公告（SEC 8-K 附件 99.1）与 10-K XBRL；Amazon 2026 财年第三季度业绩公告（SEC 8-K 附件 99.1）与 10-Q XBRL；美国普查局 2025 年零售额 83,510 亿美元（口径卡 `us_retail_peer_shares`）；BEA GDPbyIndustry-15 与 GDPbyIndustry-1（2025 年）；Eurostat nama_10_a64 与 sts_trtu_m（2022 年）；Blake、Nosko、Tadelis，*Econometrica* 2015；Gordon 等，*Marketing Science* 2019。截至 2026 年 11 月 8 日。**复现**：`x dbnomics data BEA/GDPbyIndustry-15/44RT-A`
