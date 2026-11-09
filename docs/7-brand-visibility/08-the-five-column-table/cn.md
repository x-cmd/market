# 交过来的表，要看哪几列

一张表递过来，五个列名：**词、渠道、日期、次数、情绪**。少一列，结论就变；某一列写得含糊，结论会反着来。

这一页用的是真表：美国区 App Store 上七个鞋服 App 的最近 500 条评论。**同一个词 On，在 Nike 渠道上被读出两个完全相反的结论**——朴素匹配说「On 被提了 125 次，其中 72% 是差评」；逐条核对后说「那 125 次里没有一次在说 On 这个品牌，全是英文介词 on」。

## 拿到表，先看有没有缺列

表到了，先看列。

| 列 | 缺了会怎样 |
|---|---|
| 词 | 把介词当品牌 |
| 渠道 | 自家 App 和零售 App 混着比 |
| 日期 | 「最近 500 条」横跨 4 年 |
| 次数 | 出现次数和提及次数混着叫 |
| 情绪 | 差评率算在错的词上 |

七个 App 里四个是品牌自有 App，三个是多品牌零售 App。**最能说明问题的一格，是「On」这个词在 Nike 渠道上的数。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%8C%89%E5%8D%95%E8%AF%8D%E8%BE%B9%E7%95%8C%E5%8C%B9%E9%85%8D%20on%20%E6%8A%93%E5%88%B0%E7%9A%84%E6%AC%A1%E6%95%B0%20vs%20%E7%9C%9F%E6%AD%A3%E6%8C%87%20On%20%E5%93%81%E7%89%8C%E7%9A%84%E6%AC%A1%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%AC%A1%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%9C%B4%E7%B4%A0%E5%8C%B9%E9%85%8D%20on%22%2C%22%E4%B8%A5%E6%A0%BC%E5%88%A4%E5%AE%9A%20On%20%E5%93%81%E7%89%8C%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%9C%B4%E7%B4%A0%E5%8C%B9%E9%85%8D%20on%22%2C%22data%22%3A%5B105%2C168%2C246%2C81%2C113%2C78%2C43%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E4%B8%A5%E6%A0%BC%E5%88%A4%E5%AE%9A%20On%20%E5%93%81%E7%89%8C%22%2C%22data%22%3A%5B0%2C0%2C47%2C0%2C0%2C0%2C0%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%8C%89%E5%8D%95%E8%AF%8D%E8%BE%B9%E7%95%8C%E5%8C%B9%E9%85%8D%20on%20%E6%8A%93%E5%88%B0%E7%9A%84%E6%AC%A1%E6%95%B0%20vs%20%E7%9C%9F%E6%AD%A3%E6%8C%87%20On%20%E5%93%81%E7%89%8C%E7%9A%84%E6%AC%A1%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%AC%A1%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%9C%B4%E7%B4%A0%E5%8C%B9%E9%85%8D%20on%22%2C%22%E4%B8%A5%E6%A0%BC%E5%88%A4%E5%AE%9A%20On%20%E5%93%81%E7%89%8C%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%9C%B4%E7%B4%A0%E5%8C%B9%E9%85%8D%20on%22%2C%22data%22%3A%5B105%2C168%2C246%2C81%2C113%2C78%2C43%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E4%B8%A5%E6%A0%BC%E5%88%A4%E5%AE%9A%20On%20%E5%93%81%E7%89%8C%22%2C%22data%22%3A%5B0%2C0%2C47%2C0%2C0%2C0%2C0%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%8C%89%E5%8D%95%E8%AF%8D%E8%BE%B9%E7%95%8C%E5%8C%B9%E9%85%8D%20on%20%E6%8A%93%E5%88%B0%E7%9A%84%E6%AC%A1%E6%95%B0%20vs%20%E7%9C%9F%E6%AD%A3%E6%8C%87%20On%20%E5%93%81%E7%89%8C%E7%9A%84%E6%AC%A1%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%AC%A1%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%9C%B4%E7%B4%A0%E5%8C%B9%E9%85%8D%20on%22%2C%22%E4%B8%A5%E6%A0%BC%E5%88%A4%E5%AE%9A%20On%20%E5%93%81%E7%89%8C%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%9C%B4%E7%B4%A0%E5%8C%B9%E9%85%8D%20on%22%2C%22data%22%3A%5B105%2C168%2C246%2C81%2C113%2C78%2C43%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E4%B8%A5%E6%A0%BC%E5%88%A4%E5%AE%9A%20On%20%E5%93%81%E7%89%8C%22%2C%22data%22%3A%5B0%2C0%2C47%2C0%2C0%2C0%2C0%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420" width="760" alt="naive_vs_brand_on_match"></a>

左边是「按单词边界匹配 on 抓到的次数」，右边是「逐条核对后确认真的在说 On 品牌的次数」。Nike 那一栏：左边 168，右边 0。

## 五列，各是什么

### 词：字符串不等于指称

英文里 on 是介词，On 是瑞士那个跑鞋品牌，两个在字符层面只差一个大小写。朴素的匹配方式是按单词边界找 on，不管大小写。在 Nike 渠道的 500 条评论里抓到 168 次，逐条打开看全是介词：

> "Love the app **on** my phone, but can't sign in on my iPad"
> "I order a pair of shoes to train for a marathon **on** Nov 1 and they tell me they are out of stock **on** Nov 5"

改成要求品牌专有搭配——`On` 或 `ON` 后面紧跟 Cloud、Running、Shoes、Sneakers、Trainers、Holding 这些品牌自有词，或出现 `on.com`——**这个渠道的数变成 0**。同一套规则在 On 自家 App 里抓到 47 次，分布在 38 条评论里。

168 对 0。**同一份原始数据，同一个词，一个数法说「On 在 Nike 那里被提了 168 次」，另一个说「一次都没有」。** 所以词这一列要写的不是「On」，而是「On（品牌，匹配 On/ON + Cloud|Running|Shoes|Sneakers|Trainers|Holding 或 on.com）」。**写不出这个括号的词，就是不能用的词。**

### 渠道：换个地方就换了个数

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22On%20%E8%BF%99%E4%B8%AA%E8%AF%8D%E5%9C%A8%E5%90%84%E6%B8%A0%E9%81%93%E7%9A%84%E6%8F%90%E5%8F%8A%E6%AC%A1%E6%95%B0%EF%BC%8C%E4%BB%A5%E5%8F%8A%E8%BF%99%E4%BA%9B%E6%8F%90%E5%8F%8A%E6%89%80%E5%9C%A8%E8%AF%84%E8%AE%BA%E7%9A%84%E5%B7%AE%E8%AF%84%E7%8E%87%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22On%20%E8%87%AA%E5%AE%B6%20App%22%2C%22Nike%20App%22%2C%22Zappos%22%2C%22adidas%20App%22%2C%22DICK%27S%22%2C%22Finish%20Line%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9D%A1%E6%95%B0%20%2F%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%8F%90%E5%88%B0%20on%20%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22%E5%85%B6%E4%B8%AD%201-2%20%E6%98%9F%E5%8D%A0%E6%AF%94%28%25%29%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%8F%90%E5%88%B0%20on%20%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22data%22%3A%5B158%2C125%2C84%2C59%2C64%2C89%2C40%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%85%B6%E4%B8%AD%201-2%20%E6%98%9F%E5%8D%A0%E6%AF%94%28%25%29%22%2C%22data%22%3A%5B17.1%2C72.0%2C28.6%2C35.6%2C42.2%2C58.4%2C42.5%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22On%20%E8%BF%99%E4%B8%AA%E8%AF%8D%E5%9C%A8%E5%90%84%E6%B8%A0%E9%81%93%E7%9A%84%E6%8F%90%E5%8F%8A%E6%AC%A1%E6%95%B0%EF%BC%8C%E4%BB%A5%E5%8F%8A%E8%BF%99%E4%BA%9B%E6%8F%90%E5%8F%8A%E6%89%80%E5%9C%A8%E8%AF%84%E8%AE%BA%E7%9A%84%E5%B7%AE%E8%AF%84%E7%8E%87%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22On%20%E8%87%AA%E5%AE%B6%20App%22%2C%22Nike%20App%22%2C%22Zappos%22%2C%22adidas%20App%22%2C%22DICK%27S%22%2C%22Finish%20Line%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9D%A1%E6%95%B0%20%2F%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%8F%90%E5%88%B0%20on%20%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22%E5%85%B6%E4%B8%AD%201-2%20%E6%98%9F%E5%8D%A0%E6%AF%94%28%25%29%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%8F%90%E5%88%B0%20on%20%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22data%22%3A%5B158%2C125%2C84%2C59%2C64%2C89%2C40%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%85%B6%E4%B8%AD%201-2%20%E6%98%9F%E5%8D%A0%E6%AF%94%28%25%29%22%2C%22data%22%3A%5B17.1%2C72.0%2C28.6%2C35.6%2C42.2%2C58.4%2C42.5%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22On%20%E8%BF%99%E4%B8%AA%E8%AF%8D%E5%9C%A8%E5%90%84%E6%B8%A0%E9%81%93%E7%9A%84%E6%8F%90%E5%8F%8A%E6%AC%A1%E6%95%B0%EF%BC%8C%E4%BB%A5%E5%8F%8A%E8%BF%99%E4%BA%9B%E6%8F%90%E5%8F%8A%E6%89%80%E5%9C%A8%E8%AF%84%E8%AE%BA%E7%9A%84%E5%B7%AE%E8%AF%84%E7%8E%87%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22On%20%E8%87%AA%E5%AE%B6%20App%22%2C%22Nike%20App%22%2C%22Zappos%22%2C%22adidas%20App%22%2C%22DICK%27S%22%2C%22Finish%20Line%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9D%A1%E6%95%B0%20%2F%20%25%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E6%8F%90%E5%88%B0%20on%20%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22%E5%85%B6%E4%B8%AD%201-2%20%E6%98%9F%E5%8D%A0%E6%AF%94%28%25%29%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E6%8F%90%E5%88%B0%20on%20%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22data%22%3A%5B158%2C125%2C84%2C59%2C64%2C89%2C40%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%85%B6%E4%B8%AD%201-2%20%E6%98%9F%E5%8D%A0%E6%AF%94%28%25%29%22%2C%22data%22%3A%5B17.1%2C72.0%2C28.6%2C35.6%2C42.2%2C58.4%2C42.5%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420" width="760" alt="on_mentions_by_channel"></a>

自有 App 一侧：On 158 条、Nike 125 条、adidas 59 条、Under Armour 40 条提到 on。零售 App 一侧：Zappos 84 条、Finish Line 89 条、DICK'S 64 条。

**这些数没有一个是「On 被提了多少次」。** Nike 的 125 条里只有 0 条在说 On 这个品牌；Finish Line 的 89 条也全是介词。它们量的是「on 这个英文词出现了多少次」。

渠道这一列管的是**这条数据在多大程度上能代表你要说的那个对象**。自有 App 的评论里品牌名出现得最多，但褒贬的对象是 App 的登录、发货、退换货，不是鞋。**自家 App 的数偏乐观，零售 App 的数才带外部视角。**

### 次数：出现次数、提及次数、评论条数

原始数据 3,484 条评论。在 On 渠道里，品牌词 On 出现 47 次，分布在 38 条评论里，**7 条评论提到了不止一次**，比如这条："This is my 6th **On** Cloud shoes that I owned. The **On** Cloud family is the BEST."

两种算法都对，回答的是不同问题。**「出现次数」量的是这个词在语料里的密度，「提及次数」量的是有多少个人说了它。** 一次说五遍的人，在提及次数里算 5，在出现次数里算 5；五个各说一遍的人，前者算 5，后者算 1。分母也跟着变：47 除以 484 是 9.7%，38 除以 484 是 7.9%，**两个都叫「提及率」，差 1.9 个百分点**。

### 情绪：谁打的标

这一页用 App Store 的星级——**每位写评论的用户自己点的 1 到 5 星**，标的人和说话的人是同一个人，三种打标方式里最可信的一种。另一两种打标方式的差别见 [提到你的次数，和说的是好话坏话](../../7-brand-visibility/05-volume-without-sentiment-is-blind/cn.md)。要紧的是**它挂在哪个词上**。

用朴素匹配，Nike 渠道里提到 on 的 125 条评论，1-2 星占 72.0%，均分 2.02。**这是一条看起来很有新闻价值的数：「On 在 Nike 官方 App 上被大量提及，72% 是差评。」** 严格核对后这个数不存在：那 125 条是 Nike 用户在骂 App 登录、骂缺货、骂筛选功能。

On 自家 App 里 38 条真·On 提及的评论，1-2 星占 10.5%，均分 4.61。

**同一个词，两套匹配，情绪从 72% 差评变成 10.5% 差评，方向完全相反。**

### 日期：是观测日还是统计窗

日期在这张表里同时扮演两个角色：**观测日**（哪天取的数）和**统计窗**（这段时间的数据）。**观测日不重要，统计窗才要命。** 七个 App 都是「最近 500 条」，听起来同一个口径，但摊开差 12 倍。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%E6%98%AF%E3%80%8C%E6%9C%80%E8%BF%91%20500%20%E6%9D%A1%E8%AF%84%E8%AE%BA%E3%80%8D%EF%BC%8C%E6%91%8A%E5%BC%80%E7%9A%84%E5%A4%A9%E6%95%B0%E5%B7%AE%2012%20%E5%80%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%A6%86%E7%9B%96%E5%A4%A9%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A60%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1415%2C597%2C932%2C114%2C1222%2C119%2C493%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%E6%98%AF%E3%80%8C%E6%9C%80%E8%BF%91%20500%20%E6%9D%A1%E8%AF%84%E8%AE%BA%E3%80%8D%EF%BC%8C%E6%91%8A%E5%BC%80%E7%9A%84%E5%A4%A9%E6%95%B0%E5%B7%AE%2012%20%E5%80%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%A6%86%E7%9B%96%E5%A4%A9%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A60%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1415%2C597%2C932%2C114%2C1222%2C119%2C493%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E6%A0%B7%E6%98%AF%E3%80%8C%E6%9C%80%E8%BF%91%20500%20%E6%9D%A1%E8%AF%84%E8%AE%BA%E3%80%8D%EF%BC%8C%E6%91%8A%E5%BC%80%E7%9A%84%E5%A4%A9%E6%95%B0%E5%B7%AE%2012%20%E5%80%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%A6%86%E7%9B%96%E5%A4%A9%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A60%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1415%2C597%2C932%2C114%2C1222%2C119%2C493%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="coverage_span_days"></a>

Zappos 的最近 500 条横跨 **1,415 天**（2022-12-15 到 2026-10-30），日均 0.35 条。adidas 和 DICK'S 只跨 **114 天**和 **119 天**，日均 4.4 条和 4.2 条。

**同样是「500 条」，一个是近四年的历史快照，一个是最近三个月的密集日志。** 表上只写「最近 500 条评论」，读者不知道这个数覆盖了多久。取固定窗口——2026-08-10 到 2026-11-08 这 90 天——再数一遍。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%BF%91%2090%20%E5%A4%A9%E7%AA%97%E5%8F%A3%E5%86%85%EF%BC%9A%E5%90%84%E6%B8%A0%E9%81%93%E8%90%BD%E8%BF%9B%E7%AA%97%E5%8F%A3%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%20vs%20%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E7%9A%84%E6%9D%A1%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9D%A1%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E7%AA%97%E5%8F%A3%E5%86%85%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E5%93%81%E7%89%8C%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E7%AA%97%E5%8F%A3%E5%86%85%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22data%22%3A%5B10%2C55%2C66%2C401%2C26%2C334%2C36%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E5%93%81%E7%89%8C%22%2C%22data%22%3A%5B0%2C0%2C1%2C0%2C0%2C0%2C0%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%BF%91%2090%20%E5%A4%A9%E7%AA%97%E5%8F%A3%E5%86%85%EF%BC%9A%E5%90%84%E6%B8%A0%E9%81%93%E8%90%BD%E8%BF%9B%E7%AA%97%E5%8F%A3%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%20vs%20%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E7%9A%84%E6%9D%A1%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9D%A1%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E7%AA%97%E5%8F%A3%E5%86%85%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E5%93%81%E7%89%8C%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E7%AA%97%E5%8F%A3%E5%86%85%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22data%22%3A%5B10%2C55%2C66%2C401%2C26%2C334%2C36%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E5%93%81%E7%89%8C%22%2C%22data%22%3A%5B0%2C0%2C1%2C0%2C0%2C0%2C0%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E8%BF%91%2090%20%E5%A4%A9%E7%AA%97%E5%8F%A3%E5%86%85%EF%BC%9A%E5%90%84%E6%B8%A0%E9%81%93%E8%90%BD%E8%BF%9B%E7%AA%97%E5%8F%A3%E7%9A%84%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%20vs%20%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E7%9A%84%E6%9D%A1%E6%95%B0%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22Zappos%22%2C%22Nike%22%2C%22On%22%2C%22adidas%22%2C%22Finish%20Line%22%2C%22DICK%27S%22%2C%22Under%20Armour%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%9D%A1%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E7%AA%97%E5%8F%A3%E5%86%85%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E5%93%81%E7%89%8C%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E7%AA%97%E5%8F%A3%E5%86%85%E8%AF%84%E8%AE%BA%E6%9D%A1%E6%95%B0%22%2C%22data%22%3A%5B10%2C55%2C66%2C401%2C26%2C334%2C36%5D%2C%22type%22%3A%22bar%22%7D%2C%7B%22name%22%3A%22%E5%85%B6%E4%B8%AD%E6%8F%90%E5%88%B0%20On%20%E5%93%81%E7%89%8C%22%2C%22data%22%3A%5B0%2C0%2C1%2C0%2C0%2C0%2C0%5D%2C%22type%22%3A%22bar%22%7D%5D%7D&w=760&h=420" width="760" alt="ninety_day_coverage"></a>

Zappos 的 500 条里有 **10 条**落进这 90 天，Nike 55 条，adidas 401 条，DICK'S 334 条。**Zappos 在这个窗口里几乎没有数据。**

于是「Zappos 渠道近 90 天提到 On 的次数 = 0」这个格子出现了。它是真的，但意思不是「On 在 Zappos 上没声量」，而是「**Zappos 这 90 天只有 10 条评论，其中 0 条提到 On**」。

## 没查到，不等于零

表上出现 0，至少有三种可能，表格本身经常分不出来。

**第一种：这个渠道在这个窗口里几乎没数据。** 上面那个 Zappos 的 0 就是这种。**这是覆盖度问题，不是市场问题。**

**第二种：数据源不支持这个粒度。** 上一节那个 500 条的上限就是例子——**接口的形状替你决定了统计窗的长度，而且表上不会自动写出来。**

**第三种：真的没有。** 这一页里最接近的是 HOKA 在 adidas App 上的 1 次提及——但 1 次也是 1 次，写成「0 次」才是错的。

**所以空格子要分三档写。** 「0（该渠道窗口内 10 条评论，均已核对，无匹配）」和「0（该渠道窗口内 0 条评论，无覆盖）」和「NA（接口不支持该粒度）」，是三件不同的事。Apple 自己的文档也点了同一件事：**商店累计评分是按地区分开算的**，同一款应用在美国区和日本区是两个数——**渠道这一列不写地区，等于没写。**

## 缺一列这张表就不能用

五列里，词、渠道、日期、次数各挡掉一种错误读法，最贵的是情绪那一列。把 72% 差评率安在一个根本没被提到的品牌上，不是数字错，是**结论反了**，而且反过来的方向看起来更像一条真新闻。

**还有一件表上不会自动告诉你的事：这张表的每个格子都有不确定度。** 词匹配规则的松紧、情绪判断靠不靠得住，都得跟着数一起交出去。On 的次数是 47 次还是 0 次，差别就在「必须大写」这一条规则上——**这个差别是逐条读完 3,484 条评论定下来的。**

**最后一句要带走的话：拿到表先数列。** 五列齐了才动手，补不齐的格子写清楚为什么空。**一张表里最危险的不是缺列，是缺了列还带着一个漂亮的数字。**

**数据**：评论取自 Apple iTunes Customer Reviews RSS（美国区，`sortby=mostrecent`，每个 App 翻满 10 页共 500 条）。7 个 App 合计 3,484 条（On 484 条），覆盖 2022-12-15 至 2026-11-07，取数 2026-11-09。App 分别是 On（6449706677）、Nike（1095459556）、adidas（1266591536）、Under Armour（1092704571）、Zappos（392988420）、Finish Line（905940653）、DICK'S（556653197）。情绪取用户自己点的星级（1-2 星记为负）。On 的严格匹配规则为 `On`/`ON` 后紧跟 Cloud|Running|Shoes|Sneakers|Trainers|Holding 或 `on.com`，其余品牌词按词边界匹配。「按地区分开算」一句出自 Apple Developer 文档 *Ratings, reviews, and responses*。词匹配的松紧是最大的不确定度，严格判定由逐条阅读 3,484 条评论得出。

**复现**：`curl -sL --compressed -A 'Mozilla/5.0' 'https://itunes.apple.com/us/rss/customerreviews/page=1/id=1095459556/sortby=mostrecent/json'`
