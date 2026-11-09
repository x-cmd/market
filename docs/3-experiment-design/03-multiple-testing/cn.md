# 测的组合太多，会看到假效果

**一次跑了二十个组合，报告里有三个「显著」——其中至少一个大概率是假的。**

如果每个组合的检验都是单独的，那么二十次里有几个「显著」完全可能只是运气。第五个组合看起来涨了 8%，第十一个涨了 4%，第十八个涨了 11%。三张截图往群里一贴，红的绿的都有。

问题不在数字算错。**每个数字单独看都没毛病，错在你把它们当成二十次独立抽奖，实际是二十次从同一个袋子里摸签。**

## 三个「显著」是怎么来的

某 SaaS 公司做落地页改版。他们没做一次 A/B 测试，而是拆成五处改动各测一个变体：主标题、首屏图片、按钮文案、页面长度、信任标识。五处里有三处都指向同一个方向——标题换短、图片换真人、按钮从「免费试用」改成「开始免费试用」。

```
组合            转化率    相对对照
对照（原页面）      3.05%          —
A 标题短版        3.42%       +12.1%
B 图片真人版      3.51%       +15.1%
C 按钮文案        2.88%        -5.6%
D 页面变短        3.11%        +2.0%
E 信任标识        3.47%       +13.8%
```

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%94%B9%E7%89%88%E6%96%B9%E6%A1%88%EF%BC%9A%E5%8D%95%E7%9C%8B%E4%B8%89%E4%B8%AA%E6%98%BE%E8%91%97%20vs%20%E5%90%88%E5%B9%B6%E6%88%90%E4%B8%80%E4%B8%AA%E5%81%87%E8%AE%BE%E5%86%8D%E6%B5%8B%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%232563eb%22%2C%22%232563eb%22%2C%22%2364748b%22%2C%22%2364748b%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%AF%B9%E7%85%A7%22%2C%22A%20%E6%A0%87%E9%A2%98%E7%9F%AD%22%2C%22B%20%E5%9B%BE%E7%89%87%E7%9C%9F%E4%BA%BA%22%2C%22C%20%E6%8C%89%E9%92%AE%E6%96%87%E6%A1%88%22%2C%22D%20%E9%A1%B5%E9%9D%A2%E5%8F%98%E7%9F%AD%22%2C%22E%20%E4%BF%A1%E4%BB%BB%E6%A0%87%E8%AF%86%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B3.05%2C3.42%2C3.51%2C2.88%2C3.11%2C3.47%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%94%B9%E7%89%88%E6%96%B9%E6%A1%88%EF%BC%9A%E5%8D%95%E7%9C%8B%E4%B8%89%E4%B8%AA%E6%98%BE%E8%91%97%20vs%20%E5%90%88%E5%B9%B6%E6%88%90%E4%B8%80%E4%B8%AA%E5%81%87%E8%AE%BE%E5%86%8D%E6%B5%8B%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%232563eb%22%2C%22%232563eb%22%2C%22%2364748b%22%2C%22%2364748b%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%AF%B9%E7%85%A7%22%2C%22A%20%E6%A0%87%E9%A2%98%E7%9F%AD%22%2C%22B%20%E5%9B%BE%E7%89%87%E7%9C%9F%E4%BA%BA%22%2C%22C%20%E6%8C%89%E9%92%AE%E6%96%87%E6%A1%88%22%2C%22D%20%E9%A1%B5%E9%9D%A2%E5%8F%98%E7%9F%AD%22%2C%22E%20%E4%BF%A1%E4%BB%BB%E6%A0%87%E8%AF%86%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B3.05%2C3.42%2C3.51%2C2.88%2C3.11%2C3.47%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%94%B9%E7%89%88%E6%96%B9%E6%A1%88%EF%BC%9A%E5%8D%95%E7%9C%8B%E4%B8%89%E4%B8%AA%E6%98%BE%E8%91%97%20vs%20%E5%90%88%E5%B9%B6%E6%88%90%E4%B8%80%E4%B8%AA%E5%81%87%E8%AE%BE%E5%86%8D%E6%B5%8B%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%232563eb%22%2C%22%232563eb%22%2C%22%2364748b%22%2C%22%2364748b%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%AF%B9%E7%85%A7%22%2C%22A%20%E6%A0%87%E9%A2%98%E7%9F%AD%22%2C%22B%20%E5%9B%BE%E7%89%87%E7%9C%9F%E4%BA%BA%22%2C%22C%20%E6%8C%89%E9%92%AE%E6%96%87%E6%A1%88%22%2C%22D%20%E9%A1%B5%E9%9D%A2%E5%8F%98%E7%9F%AD%22%2C%22E%20%E4%BF%A1%E4%BB%BB%E6%A0%87%E8%AF%86%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B3.05%2C3.42%2C3.51%2C2.88%2C3.11%2C3.47%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="five_variant_lift"></a>

跑出来的报告写着：「三个变体显著优于对照，可以合并上线。」

**单看每一个 p 值都很漂亮。** 但这份报告漏掉了一件最要紧的事：**这五组同时分走同一批访客，A 组和 B 组其实在抢同一批人。** A 组比对照多出的 0.37 个百分点，和 B 组多出的 0.46 个百分点，可能出自同一批「今天心情好点了就点了」的访客。同一个人，今天先看到 A 版、明天再看到 B 版，两次都记成了他「更愿意转化」。

更要命的是「合并上线」这四个字。三个各自显著的变体一旦叠在一起，它们会互相放大还是互相抵消，在单独测的时候完全看不见。**三个「显著」叠起来的东西，可能一个都不显著。**

## 假阳性从哪来

**假阳性**（false positive）：检验说「有效果」，实际上没有效果。每个检验都有一个显著性水平，习惯取 0.05，意思是「就算真没效果，也有 5% 的概率被判成有效果」。

这个 5% 单看很小。**问题在于它要被乘上次数。**

假设二十个组合，每个都是零效果——没有一处改动真的带来提升。单独看每一个，5% 的概率误报。二十个一起看，至少错报一个的概率是：

**1 − 0.95²⁰ ≈ 64%**

也就是说，**六成以上的概率，二十个零效果的组合里会冒出一个「显著」。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%B7%91%20m%20%E7%BB%84%E9%9B%B6%E6%95%88%E6%9E%9C%E6%A3%80%E9%AA%8C%EF%BC%8C%E8%87%B3%E5%B0%91%E9%94%99%E6%8A%A5%E4%B8%80%E4%B8%AA%E7%9A%84%E6%A6%82%E7%8E%87%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%20%E7%BB%84%22%2C%225%20%E7%BB%84%22%2C%2210%20%E7%BB%84%22%2C%2220%20%E7%BB%84%22%2C%2250%20%E7%BB%84%22%2C%22100%20%E7%BB%84%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%A6%82%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B5%2C23%2C40%2C64%2C92%2C99%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%B7%91%20m%20%E7%BB%84%E9%9B%B6%E6%95%88%E6%9E%9C%E6%A3%80%E9%AA%8C%EF%BC%8C%E8%87%B3%E5%B0%91%E9%94%99%E6%8A%A5%E4%B8%80%E4%B8%AA%E7%9A%84%E6%A6%82%E7%8E%87%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%20%E7%BB%84%22%2C%225%20%E7%BB%84%22%2C%2210%20%E7%BB%84%22%2C%2220%20%E7%BB%84%22%2C%2250%20%E7%BB%84%22%2C%22100%20%E7%BB%84%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%A6%82%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B5%2C23%2C40%2C64%2C92%2C99%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%B7%91%20m%20%E7%BB%84%E9%9B%B6%E6%95%88%E6%9E%9C%E6%A3%80%E9%AA%8C%EF%BC%8C%E8%87%B3%E5%B0%91%E9%94%99%E6%8A%A5%E4%B8%80%E4%B8%AA%E7%9A%84%E6%A6%82%E7%8E%87%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%20%E7%BB%84%22%2C%225%20%E7%BB%84%22%2C%2210%20%E7%BB%84%22%2C%2220%20%E7%BB%84%22%2C%2250%20%E7%BB%84%22%2C%22100%20%E7%BB%84%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%A6%82%E7%8E%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B5%2C23%2C40%2C64%2C92%2C99%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="false_positive_rate_by_m"></a>

这不是小概率事件，是**大概率事件**。二十次抽奖，每次 5% 的中奖率，你几乎必然收到至少一封中奖短信。收到的那一封，跟「这个组合真的有效果」之间没有任何关系。

再换个方向看：**在二十个组合里，那个最大的显著效果，它本身就被挑过了。** 你不是在看二十个独立的 p 值，是在看二十个里最小的那个，而最小的那个天然偏向小。**是「挑」这个动作制造了那个效果，不一定是改动本身。**

## 组数翻倍，假阳性跟着涨

同样的算术，换成「跑了几组」这个角度看更清楚：

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BB%84%E6%95%B0%E7%BF%BB%E5%80%8D%EF%BC%8C%E6%9C%9F%E6%9C%9B%E5%81%87%E9%98%B3%E6%80%A7%E4%B8%AA%E6%95%B0%E8%B7%9F%E7%9D%80%E6%B6%A8%EF%BC%880.05%20%C3%97%20%E7%BB%84%E6%95%B0%EF%BC%89%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%22%2C%225%22%2C%2210%22%2C%2220%22%2C%2250%22%2C%22100%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9C%9F%E6%9C%9B%E5%81%87%E9%98%B3%E6%80%A7%E4%B8%AA%E6%95%B0%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22line%22%2C%22data%22%3A%5B0.05%2C0.25%2C0.5%2C1%2C2.5%2C5%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BB%84%E6%95%B0%E7%BF%BB%E5%80%8D%EF%BC%8C%E6%9C%9F%E6%9C%9B%E5%81%87%E9%98%B3%E6%80%A7%E4%B8%AA%E6%95%B0%E8%B7%9F%E7%9D%80%E6%B6%A8%EF%BC%880.05%20%C3%97%20%E7%BB%84%E6%95%B0%EF%BC%89%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%22%2C%225%22%2C%2210%22%2C%2220%22%2C%2250%22%2C%22100%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9C%9F%E6%9C%9B%E5%81%87%E9%98%B3%E6%80%A7%E4%B8%AA%E6%95%B0%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22line%22%2C%22data%22%3A%5B0.05%2C0.25%2C0.5%2C1%2C2.5%2C5%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BB%84%E6%95%B0%E7%BF%BB%E5%80%8D%EF%BC%8C%E6%9C%9F%E6%9C%9B%E5%81%87%E9%98%B3%E6%80%A7%E4%B8%AA%E6%95%B0%E8%B7%9F%E7%9D%80%E6%B6%A8%EF%BC%880.05%20%C3%97%20%E7%BB%84%E6%95%B0%EF%BC%89%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%22%2C%225%22%2C%2210%22%2C%2220%22%2C%2250%22%2C%22100%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9C%9F%E6%9C%9B%E5%81%87%E9%98%B3%E6%80%A7%E4%B8%AA%E6%95%B0%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22line%22%2C%22data%22%3A%5B0.05%2C0.25%2C0.5%2C1%2C2.5%2C5%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="expected_false_positives"></a>

**期望假阳性个数就是组数乘以 0.05。** 跑 100 组，期望是 5 个假阳性。这 5 个不是「运气不好」，是规则算出来的必然结果。

还有一层损失：**真的效果会被稀释。** 二十个组合里有一个真涨了 10%，另外十九个都是零，那个真的效果排第 1，很显眼。但如果真效果排在第 5，而前面 4 个是假的，你的注意力会先被前面抓住——**四个假的排在一个真的前面，而你拿最显著的那个去汇报。**

**组数翻倍，假阳性的个数跟着涨。你找到真东西的概率却未必跟着涨——前面那串假的，会把真的挤到看不见的位置。**

## 三种收拾办法

### 事前定好要看哪几个

最省事的一种：**实验开始前就把要检验的假设写下来，写几个算几个。**

跑完数据只看你事先写好的那几个，其他的一律不看。这叫「预先指定」。它有效，是因为**它把「看数据挑结果」这个动作从流程里删掉了**。

写下来的东西通常很短：「标题短版会不会提升转化」「按钮文案会不会提升转化」。三个假设就是三个检验，至少错一个的概率是 14%，不是 64%。

代价也真实：**你可能看完数据才发现有个想不到的地方效果特别好，然后错过了它。** 这就是预先指定的价钱。

### 校正：让阈值跟着组数变

第二种的思路是：**既然多测会多加假阳性，那就把判定的门槛收紧到刚好抵掉。**

最常见的是 **Bonferroni 校正**（Bonferroni correction）：要检验 m 个假设，就把显著性水平从 0.05 降到 0.05/m。测 20 组，阈值变成 0.0025——每一组都要有非常强的证据才算数。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%205%25%20%E6%98%BE%E8%91%97%E9%97%A8%E6%A7%9B%EF%BC%8C%E7%BB%84%E6%95%B0%E4%B8%8D%E5%90%8C%E8%A6%81%E6%B1%82%E7%9A%84%E8%AF%81%E6%8D%AE%E5%BC%BA%E5%BA%A6%E4%B8%8D%E5%90%8C%EF%BC%88Bonferroni%20%E9%98%88%E5%80%BC%EF%BC%89%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%20%E7%BB%84%22%2C%225%20%E7%BB%84%22%2C%2210%20%E7%BB%84%22%2C%2220%20%E7%BB%84%22%2C%2250%20%E7%BB%84%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%98%BE%E8%91%97%E6%80%A7%E9%98%88%E5%80%BC%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B0.05%2C0.01%2C0.005%2C0.0025%2C0.001%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%205%25%20%E6%98%BE%E8%91%97%E9%97%A8%E6%A7%9B%EF%BC%8C%E7%BB%84%E6%95%B0%E4%B8%8D%E5%90%8C%E8%A6%81%E6%B1%82%E7%9A%84%E8%AF%81%E6%8D%AE%E5%BC%BA%E5%BA%A6%E4%B8%8D%E5%90%8C%EF%BC%88Bonferroni%20%E9%98%88%E5%80%BC%EF%BC%89%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%20%E7%BB%84%22%2C%225%20%E7%BB%84%22%2C%2210%20%E7%BB%84%22%2C%2220%20%E7%BB%84%22%2C%2250%20%E7%BB%84%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%98%BE%E8%91%97%E6%80%A7%E9%98%88%E5%80%BC%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B0.05%2C0.01%2C0.005%2C0.0025%2C0.001%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%205%25%20%E6%98%BE%E8%91%97%E9%97%A8%E6%A7%9B%EF%BC%8C%E7%BB%84%E6%95%B0%E4%B8%8D%E5%90%8C%E8%A6%81%E6%B1%82%E7%9A%84%E8%AF%81%E6%8D%AE%E5%BC%BA%E5%BA%A6%E4%B8%8D%E5%90%8C%EF%BC%88Bonferroni%20%E9%98%88%E5%80%BC%EF%BC%89%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%221%20%E7%BB%84%22%2C%225%20%E7%BB%84%22%2C%2210%20%E7%BB%84%22%2C%2220%20%E7%BB%84%22%2C%2250%20%E7%BB%84%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%98%BE%E8%91%97%E6%80%A7%E9%98%88%E5%80%BC%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B0.05%2C0.01%2C0.005%2C0.0025%2C0.001%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="bonferroni_threshold"></a>

Bonferroni 很保守，容易漏掉真东西。它的松一点的表亲是 **Holm 校正**（Holm correction）：把 20 个 p 值从小到大排好，第一个要小于 0.05/20，第二个要小于 0.05/19……门槛逐级放松，但总数不变。它的思路是：排第一的那组给最严的门槛，排第二的稍微松一点，排到最后一组门槛接近 0.05。

还有 **Benjamini–Hochberg 过程**（Benjamini-Hochberg procedure），控制的是「假阳性占所有被判为阳性的比例」，不是「至少错一个的概率」。测 100 组时它比 Bonferroni 宽松得多，能捞回不少真效果。代价也实在：**它不再保证整族里「至少错报一个」的概率被压在 5%，只保证错报的比例被控制住。**

### 用统一分组的检验

第三种最彻底：**不要一个一个组合地测，改成一次测所有组合。**

传统 A/B 测试问的是「B 比 A 好吗」。统一分组的检验（omnibus test，常用的两个是方差分析 ANOVA 和它不要求正态分布的版本 Kruskal-Wallis）问的是另一个问题：**「这几组之间，有没有至少一组不一样？」**

如果整体检验不显著，结论就是「这几组里没有可辨认的差别」，一次把所有组合都保护住。整体显著，才往下做成对比较，看是哪几组之间差。

这套做法的关键是**它把选择动作留在了流程内部**：整体检验、后续比较、多重比较校正，都是事先定好的规则，不是人看着数据挑。

三种办法的共同点只有一个：**「挑哪个」这个决定，在看到数据之前就已经做完了。** 算错了还能改，但在二十个结果里挑一个出来当发现，这一步没法事后补做。

## 先定要问的问题，再决定测多少组

回到开头那个 SaaS 的例子。真正的问题不是「五个变体里哪三个赢了」，而是：

**「我要回答的是一个什么问题？」**

如果问题是「改版有没有用」，那正确设计是一个实验、两个组、一个预注册的假设。五处改动里如果非要挑一个先测，就挑历史上证据最强的那处做 A/B，确认有效果了再往下拆。

如果问题是「这五处改动分别有没有用」，那这是一个五重检验。你得接受 23% 的假阳性概率，或者把阈值调到 0.01 并事先说明只有超过这个门槛才算数。

**测几组不是由「能测几组」决定的，是由「要回答几个问题」决定的。** 顺序反了，就会出现开头那个局面：先跑起来、跑出一堆数、再拿着这堆数去找问题。而你挑中的，一定是那堆数里最亮的几个——**它们亮，多半是因为你先挑了它们。**

同样的道理延伸到日常读数：一次看二十个渠道、二十个广告位、二十个落地页，然后挑显著的去加预算——**这是同一件事，只是换了个马甲。**

[→ 对照组该怎么定](../01-what-a-control-group-is/cn.md) · [→ 样本太少结论会反](../02-sample-size-and-power/cn.md) · [→ 一个数要配一个区间](../04-confidence-intervals/cn.md)

**数据**：概率与期望假阳性个数按二项分布公式算得（1 − 0.95^m 与 0.05m），示例转化率与五组变体数据是算例，截至 2026 年。Bonferroni、Holm、Benjamini–Hochberg 校正与 ANOVA / Kruskal-Wallis 统一分组检验的定义见 Benjamini & Hochberg, *JRSS-B* 57(1), 1995。Holm, *Scandinavian Journal of Statistics* 6(4), 1979。

**复现**：算一遍「跑 m 组至少错报一个的概率」和期望假阳性个数：`python3 -c "m=[1,5,10,20,50,100]; [print(k, round(1-0.95**k,3), round(0.05*k,2)) for k in m]"`
