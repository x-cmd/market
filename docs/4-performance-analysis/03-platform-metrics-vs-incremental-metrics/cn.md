# 平台报的数字，和真实效果不是一回事

后台那个 ROAS 4.0，和实验测出的 0.3，讲的是同一笔广告费。

**它们不是两个答案，是两个不同的问题。** 平台那本账记「沾过广告的订单」，增量那本账记「停投后少掉的单」。**两个数不能相加，也不能用一个去纠正另一个。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%90%8C%E4%B8%80%E6%89%B9%E5%B9%BF%E5%91%8A%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%E4%B8%89%E4%B8%AA%E6%8F%90%E5%8D%87%E5%80%BC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%E5%B9%B4%E9%BE%84%E6%80%A7%E5%88%AB%22%2C%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%E6%8F%90%E5%8D%87%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B73%2C222%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%90%8C%E4%B8%80%E6%89%B9%E5%B9%BF%E5%91%8A%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%E4%B8%89%E4%B8%AA%E6%8F%90%E5%8D%87%E5%80%BC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%E5%B9%B4%E9%BE%84%E6%80%A7%E5%88%AB%22%2C%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%E6%8F%90%E5%8D%87%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B73%2C222%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="facebook_lift_three_ways"></a>

**一句话带走：平台数字用来调平台内的投放，增量数字用来决定这笔钱还要不要继续花。**

## 两套数，该怎么并排放

**手里同时有两套数，最容易犯的错不是选错一个，是把它们放在一起算。** 平台报表和你自己做的实验各说各的，可最后常被填进同一列。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%B9%B3%E5%8F%B0%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%20vs%20%E5%A2%9E%E9%87%8F%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%AE%A2%E5%8D%95%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E8%B4%A6%EF%BC%9A%E6%B2%BE%E8%BF%87%E5%B9%BF%E5%91%8A%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%85%B6%E4%B8%AD%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E4%BC%9A%E6%B6%88%E5%A4%B1%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%A2%9E%E9%87%8F%E8%B4%A6%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E5%B0%91%E6%8E%89%E7%9A%84%E8%AE%A2%E5%8D%95%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A60%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1000%2C250%2C250%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%B9%B3%E5%8F%B0%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%20vs%20%E5%A2%9E%E9%87%8F%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%AE%A2%E5%8D%95%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E8%B4%A6%EF%BC%9A%E6%B2%BE%E8%BF%87%E5%B9%BF%E5%91%8A%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%85%B6%E4%B8%AD%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E4%BC%9A%E6%B6%88%E5%A4%B1%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%A2%9E%E9%87%8F%E8%B4%A6%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E5%B0%91%E6%8E%89%E7%9A%84%E8%AE%A2%E5%8D%95%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A60%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1000%2C250%2C250%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="platform_vs_incremental_containment"></a>

### 两本账记的不是同一件事

**平台那本账从曝光记起。** 曝光、点击、加购、成交，凡是这次会话碰过广告的订单，都记在广告名下。

**增量那本账只有一个条目：停投后不再成交的单。**

**两本账的分子不是一类东西。** 一本是订单数，一本是订单数的差额。放进同一个公式，等于拿销售额和利润率相加。

**关系是包含，不是并列。** 上面那张图里，增量那 250 单也在平台那 1000 单里面。叠起来加，得出的 1250 单里有 250 单被数了两遍。

**平台那本账是加法，增量那本账是减法。**

**两本账各自都成立，问题是回答的问题不同。** 平台那本账回答「这趟广告带来了多少笔沾上它的订单」，增量那本账回答「不投这笔钱，这些订单会消失吗」。

**第一个问题不需要对照组，第二个必须有。** 同一个 4.0 的 ROAS，读出来是两回事。

## 两本账，各记什么

### 平台那本账：把整条漏斗记在自己名下

**平台口径有个实在的优点：它把整条链路都记下来了。** 广告主看不到曝光、点击、加购，只能看到成交。

**归因窗口是这套账的时间边界。** 点过广告之后 7 天内、14 天内、30 天内下的单，都算这笔广告的。窗口越长，沾上的订单越多，报表上的 ROAS 也越高。同一份投放把窗口从 7 天改成 30 天，那个数能差出一大截，而你的钱一分没多花。这也是两个广告主的报表没法直接比的原因。

### 增量那本账：只记停投后少掉的那部分

**增量的定义只有一句话：这笔广告停了之后，不再成交的那些单。**

**它跟广告费没关系，跟归因窗口也没关系。** 增量是差额，不是比值，也不是某一笔点击的功劳。

**代价是要有对照组。** 停投的那批地方，得留一批不投的地方做对照，否则你只知道总量掉了多少，不知道掉的是本来就要买的还是广告买来的。


## 差是从哪来的

### 曝光不随机：平台把广告投给了本来就更可能买的人

**Facebook 2019 年那篇论文里，一个广告活动，实验测出的真实提升是 73%，** 观测口径算出 316%，精确匹配之后还有 222%。

**差的来源是投放本身。** 算法挑人挑得准，恰好挑中的就是意向最强的那批。这批人本来就更可能买，广告一来就成交，于是被算成广告的功劳。

**最朴素的对比是：看到了广告的人 vs 没看到广告的人。** 看到的人本来就更可能买，观测口径就这样高估到四倍。

### 归因窗口：多等几天，就多认几笔单

**窗口每多一天，平台那本账就多认一笔单。** 同一笔投放，换个窗口就得出一个不同的数。

### 自然需求被认领：广告抢的是本来就要来的单

**eBay 2015 年那批实验里，非品牌词搜索广告的 ROI，三种算法三个数。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22eBay%20%E9%9D%9E%E5%93%81%E7%89%8C%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%9A%E5%9B%9E%E6%8A%A5%E7%8E%87%E7%9A%84%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%EF%BC%88%E6%97%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%EF%BC%88%E5%8A%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E5%9C%B0%E5%9F%9F%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22eBay%20%E9%9D%9E%E5%93%81%E7%89%8C%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%9A%E5%9B%9E%E6%8A%A5%E7%8E%87%E7%9A%84%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%EF%BC%88%E6%97%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%EF%BC%88%E5%8A%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E5%9C%B0%E5%9F%9F%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="ebay_roi_three_ways"></a>

**回归算出 4100%，加上时间和地域控制变量还有 1400%，随机实验测出来是 −63%，95% 置信区间从 −124% 到 −3%。**

**正负号反了。** 花钱买来的不是订单，是把本来就打算买的人拦下来付了广告费。

## 并排写，别相加

### 一张表，两列，各标各的口径

**表头要写清三件事：这一列是什么口径、数据截至哪天。**

| 口径 | 平台报表（7 天点击归因） | 增量实验（geo 随机对照） |
|---|---|---|
| 归到的订单 | 4,000 单 | 300 单 |
| 广告花费 | 48,000 美元 | 48,000 美元 |
| 带来的销售额 | 192,000 美元 | 14,400 美元 |
| 回报率 | 4.0 | 0.3 |
| 数据截至 | 2026-10-31 | 2026-10-31 |

**两列并排放，各自站得住，谁也不去改谁。** 有人问「到底哪个对」，这问题本身问错了：左列回答平台内的优化，右列回答该不该继续投。

**两个数不要加。** 增量订单已经包含在平台订单里，加起来等于把同一批单卖两遍。

## 什么时候用哪一套

### 谈平台内的优化：平台口径

**出价、定向、创意、人群包，这些事全都在平台的规则里发生，** 平台的数就是这些动作的评分板。素材 A 和素材 B 谁好，平台口径直接给答案。

**但平台口径只能横向比平台自己的东西。** 它能告诉你素材 A 比素材 B 好，不能告诉你这个渠道该不该继续投。

### 谈该不该继续花：增量口径

**决定续不续投、看回报率够不够撑起这条渠道，** 用增量口径。

**一次 geo 实验里，平台报的每次点击成本 2.4 美元，测出的每次增量点击成本是 3.0 美元。**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20vs%20%E6%B5%8B%E5%87%BA%E7%9A%84%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%22%2C%22%E6%B5%8B%E5%87%BA%E7%9A%84%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20CPIC%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20vs%20%E6%B5%8B%E5%87%BA%E7%9A%84%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%22%2C%22%E6%B5%8B%E5%87%BA%E7%9A%84%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20CPIC%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="geo_cpc_vs_cpic"></a>

**付费点击里有 20% 是从自然搜索抢来的，不是多出来的。** 平台报的 CPC 系统性低估，因为分母混进了本来就会发生的点击。

### 什么时候两套都不够用

**手上只有平台数，没有对照，** 两套都写不了。增量那列只能写「未测」，不能拿平台数乘系数估。

**这次该测没测，后面就没有第二本账了。** 平台那本账随时能拉，增量那本账只能在有对照时存在。

## 两本账各自记，不要合并成一笔

**平台数字和增量数字不是「哪个更准」的关系，是「回答哪个问题」的关系。**

**并排放，标口径和日期，不做加总。** 平台内的优化看平台口径，该不该继续花看增量口径。

[→ 没有广告，这些单会成交吗](../../1-report-overview/06-incrementality-chart/cn.md) · [→ 归因模型：平台怎么把这笔单算到广告名下](../../8-analysis-toolbox/01-attribution/cn.md) · [→ 增量测试：怎么测出停投会少掉多少](../../8-analysis-toolbox/02-incrementality-testing/cn.md) · [→ ROI 排名，不是加钱顺序](../02-roi-ranking-vs-budget-allocation/cn.md)

**数据**：Facebook 的 73% / 222% / 316% 来自 Gordon, Zettelmeyer, Bhargava & Chapsky, *Marketing Science* 38(2), 2019（实验组 2550 万人，只有 25% 真看到广告）。eBay 的 4100% / 1400% / −63% 来自 Blake, Nosko & Tadelis, *Econometrica* 83(1), 2015（置信区间 −124% 到 −3%）。geo 实验的 2.4 与 3.0 美元和「付费点击里 20% 来自自然搜索」来自 Vaver & Koehler, *Measuring Ad Effectiveness Using Geo Experiments*, Google Inc., 2011。表里的 4,000 单 / 300 单和图里的 1000 单 / 250 单都是**算例**。

**复现**：论文数据没有公开接口，`curl -sL -A 'Mozilla/5.0' https://www.nber.org/papers/w20171` 取 eBay 那篇摘要页，`curl -sL -A 'Mozilla/5.0' https://pubsonline.informs.org/doi/10.1287/mksc.2018.1135` 取 Facebook 那篇摘要页；口径卡 `paid_search_roi_observed_vs_randomized`、`ad_lift_observed_vs_rct`、`geo_incremental_click_cost` 的原始值见 `spec/metric-cards.yml`。
