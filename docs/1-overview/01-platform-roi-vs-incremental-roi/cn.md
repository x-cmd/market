# 回归算出来赚 41 倍，实验测出来倒亏六成

周一早上十点，你把上周的广告后台截图发到群里。

投了 3 万，带来的成交额 12 万，ROAS 4.0。老板回了三个字：继续加。

这个数你信。它是平台算的，口径你也认：沾过广告的订单，都算广告的功劳。

但这里还藏着第二个问题，一个平台不会替你问：**如果这 3 万停掉，那 12 万还会剩多少？**

这两个问题不是一回事。第一个问题，后台给你答案。第二个问题的答案，才是你买广告时真正想买的东西。

**增量，说白了就是：停掉广告之后，不再成交的那些单。**

本来就会成交的单不算增量——那些人本来就打算买，只是搜的时候顺手看见了你。停掉之后不再成交的，才是广告拽回来的。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22eBay%20%E9%9D%9E%E5%93%81%E7%89%8C%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%9A%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%EF%BC%8C%E4%B8%89%E4%B8%AA%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A40%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%5Cn%EF%BC%88%E6%97%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%5Cn%EF%BC%88%E6%97%B6%E9%97%B4%2B%E5%9C%B0%E5%9F%9F%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E6%9C%89%E5%AF%B9%E7%85%A7%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%E6%AF%8F%201%20%E7%BE%8E%E5%85%83%E5%B9%BF%E5%91%8A%E8%B4%B9%E5%B8%A6%E6%9D%A5%E7%9A%84%E5%A2%9E%E9%87%8F%E9%94%80%E5%94%AE%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%2C%22max%22%3A4500%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22eBay%20%E9%9D%9E%E5%93%81%E7%89%8C%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%9A%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%EF%BC%8C%E4%B8%89%E4%B8%AA%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A40%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%5Cn%EF%BC%88%E6%97%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%5Cn%EF%BC%88%E6%97%B6%E9%97%B4%2B%E5%9C%B0%E5%9F%9F%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E6%9C%89%E5%AF%B9%E7%85%A7%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%E6%AF%8F%201%20%E7%BE%8E%E5%85%83%E5%B9%BF%E5%91%8A%E8%B4%B9%E5%B8%A6%E6%9D%A5%E7%9A%84%E5%A2%9E%E9%87%8F%E9%94%80%E5%94%AE%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%2C%22max%22%3A4500%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22eBay%20%E9%9D%9E%E5%93%81%E7%89%8C%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%9A%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%EF%BC%8C%E4%B8%89%E4%B8%AA%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A40%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%5Cn%EF%BC%88%E6%97%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%5Cn%EF%BC%88%E6%97%B6%E9%97%B4%2B%E5%9C%B0%E5%9F%9F%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E6%9C%89%E5%AF%B9%E7%85%A7%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%EF%BC%88%E6%AF%8F%201%20%E7%BE%8E%E5%85%83%E5%B9%BF%E5%91%8A%E8%B4%B9%E5%B8%A6%E6%9D%A5%E7%9A%84%E5%A2%9E%E9%87%8F%E9%94%80%E5%94%AE%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%2C%22max%22%3A4500%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="ebay_roi_three_ways"></a>

**2015 年，eBay 联合三个经济学家做过一次大规模随机实验。** 做法是把用户随机劈成两半：一半能看到搜索广告，一半看不到。

同一批广告，三种算法，三个数。

最常见的做法是回归，控制变量越少越好，它算出非品牌词搜索广告的回报率超过 4100%。每花 1 美元，带回 41 美元。

加上时间和地域的控制变量，还是超过 1400%。

同一批广告，随机实验测出来：**ROI 是 −63%**，95% 置信区间从 −124% 到 −3%。

不是小了六十倍。是**正负号反了**。

**Facebook 也给自己做过同样的体检。**

2019 年，Facebook 的研究者和西北大学商学院的人，把 15 个广告活动的随机实验结果，拿去跟广告主平时用的观测方法比了一遍。

其中一个活动值得跟着看。2015 年上半年，一家全渠道零售商跑了两周广告，2550 万用户按七三分成实验组和对照组，指标是结账页的转化。

实验组转化率 0.045%，对照组 0.033%。但只有 37% 的实验组真的看到了广告。按真实曝光折算，广告把转化率抬高了 **73%**，95% 置信区间 49% 到 103%。

现在把对照组扔掉。这就是广告主没有实验时的处境：目标人群里有人看到、有人没看到，你只能自己比。

看到广告的人转化率 0.061%，没看到的 0.019%。一除，316%。

比真实效果高了四倍还多。

退一步，只按年龄和性别做精确匹配，降到 222%。还是三倍。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%EF%BC%9A73%25%20%C2%B7%20222%25%20%C2%B7%20316%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%5Cn%EF%BC%88%E5%B9%B4%E9%BE%84%2B%E6%80%A7%E5%88%AB%EF%BC%89%22%2C%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%B3%E5%8F%B0%E5%B8%B8%E7%94%A8%E5%8F%A3%E5%BE%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%E6%8F%90%E5%8D%87%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%2C%22max%22%3A350%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B73%2C222%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%EF%BC%9A73%25%20%C2%B7%20222%25%20%C2%B7%20316%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%5Cn%EF%BC%88%E5%B9%B4%E9%BE%84%2B%E6%80%A7%E5%88%AB%EF%BC%89%22%2C%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%B3%E5%8F%B0%E5%B8%B8%E7%94%A8%E5%8F%A3%E5%BE%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%E6%8F%90%E5%8D%87%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%2C%22max%22%3A350%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B73%2C222%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E5%B9%BF%E5%91%8A%E6%B4%BB%E5%8A%A8%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%EF%BC%9A73%25%20%C2%B7%20222%25%20%C2%B7%20316%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%5Cn%EF%BC%88%E5%B9%B4%E9%BE%84%2B%E6%80%A7%E5%88%AB%EF%BC%89%22%2C%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%B3%E5%8F%B0%E5%B8%B8%E7%94%A8%E5%8F%A3%E5%BE%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%E6%8F%90%E5%8D%87%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%2C%22max%22%3A350%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B73%2C222%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="facebook_study4_lift"></a>

**问题出在曝光上。曝光不是随机的。**

看到广告的人，本来就更可能买。他们更可能用手机，更可能已婚，更可能是女性。在广告主的后台里，这些差异你看不见——你不知道谁看到了广告。

回归能纠正一部分。纠正不了的那部分，留在数里了。

**那这笔账差在哪？**

eBay 那个 −63%，不是说搜索广告没用。

那篇论文的结论拆开是两句话。第一句：品牌词广告——用户搜的词里已经带着你的名字——**几乎没有可测量的短期收益**。你买到的，是那些本来就要搜你名字的人。第二句：非品牌词确实有正面影响，但主要来自新用户和低频用户；**高频用户占了广告开支的大头，而他们的购买没被广告改变**。

所以真正要问的不是「广告有没有用」。是**哪些广告在造需求，哪些在收割已经存在的需求**。

这两件事的比例，决定了你下个月该不该加预算。

拿你自己算一遍。假设你每个月在搜索广告上花 30 万。要是其中三成买到的都是本来就会下单的人，那这 9 万，对应的销售额你原来就拿得到。

不是少赚。是把已经到手的数记成了增量，然后准备往里加钱。

不测，你只能靠猜。猜错代价不是少赚一点——是**把下一笔钱投到本来就会成交的订单上，还以为自己在拉新**。

**这不只是广告的事。**

任何时候你拿两拨人比，都会撞上同一件事：这两拨人本来就不一样。

你把 A 城和 B 城的门店放一起比，A 城开在大学城，B 城开在写字楼，客流结构都不一样。这时候算出来的「A 店转化更高」，有多少是广告的功劳？

你做了一次改版，A 组看新版、B 组看旧版。分组随机，这叫实验。分组按注册时间切，那两拨人本来就不一样。

广告这件事特殊在——**你看不见曝光**。

线下比门店，你知道谁在哪座城。价格 A/B 测试，你知道谁分到了哪组。只有广告：你手里有订单，没有「谁看到了」。

**平台为什么把这么要紧的事放在另一个菜单里？**

Google 有 geo-lift，Meta 有 Conversion Lift，都不假。但它们都不在你每天看的那张表里。要另外设计、另外设对照、另外等一段时间、另外接受一个可能很难看的结论。

这不是平台藏你。数据在平台手里，恰恰是因为平台知道谁看到了广告——而这正是你做不了实验的原因。

**先说清楚：平台没骗你。**

它报的那个数回答的是「哪些订单沾过广告」。这个问题它答得又准又快，因为数据就在它手里。

而「广告创造了多少」是另一个问题，要另一套办法。

**三件不费钱的事。**

第一，**留一个小对照组**。不用全城停投，挑几个城市、一块区域、一段时段停一小块就够。有对照和没对照是两个世界，怎么做见 [→ 对照组不是「没投的那群人」那么简单](../../3-experiment/01-what-a-control-group-is/cn.md)。

第二，**别把两套账混着看**。平台报表里的那个 ROI，和你自己测出来的那个 ROI，不是一个数。详见 [→ 平台口径和增量口径，是两套账](../../4-analytics/03-platform-metrics-vs-incremental-metrics/cn.md)。

第三，**记住每种口径的偏向方向**。观测法——平台报表、最后点击归因——是**高估**。不是「稍微夸大」，是系统性地往大了算。品牌词那一块，它能把负的算成正的。

**结论。**

平台报的那个数不是假的。增量测出来的那个数也不是假的。错的是你把两个数当成了同一个数。

广告到底创造了多少，不测就不知道。不测也还有一条底线：别把收割当成创造。

[→ 平台口径和增量口径，是两套账](../../4-analytics/03-platform-metrics-vs-incremental-metrics/cn.md)

**数据**：Blake, Nosko & Tadelis, *Econometrica* 83(1), 2015（eBay 随机实验）；Gordon, Zettelmeyer, Bhargava & Chapsky, *Marketing Science* 38(2), 2019（Facebook 15 个实地实验）。**复现**：图里的数是这两篇论文报告的实验结果，没有一条 x-cmd 命令能把它们重跑一遍；换成你自己的数，把链接里 `d=` 的 `series[].data` 数组改掉就行。
