# A channel is worth what it adds, and only a holdout can tell you

"If we stop this channel, how much revenue goes away?"

Reports record what already happened: who clicked, who ordered. They record nothing about the invisible part — **the buyers who were going to buy anyway.**

So there are two ways forward. Guess a number off the reports, or **hold back a slice of the audience and let it answer for you.**

## Incrementality is the orders that stop happening

**In plain terms: incrementality is the set of orders that no longer happen once the ads stop.** Orders that would have happened anyway do not count — those buyers had already decided to purchase, and the ad was only in front of them when they searched.

[→ Without the ads, would these orders have happened?](../../1-report-overview/06-incrementality-chart/en.md) splits the same orders into two ledgers: one for the whole funnel, one for the orders that go missing. **To count the missing orders, you need a slice of the map where no ads ran at all.**

### Three conditions make a test valid

**Random assignment.** The two sides have to be split at random, not picked by hand.

**A slice that truly received nothing.** Not "a bit less advertising" — **none.** If half the ads still ran, you cannot tell whether missing orders vanished because of the ads or because a neighbour picked them up.

**Enough time.** Miss any of the three and the output is a well-presented guess.

**Randomness is the hard part.** Offline you know which city each store sits in. With ads you hold orders and no record of who saw an ad. Every method below hits the same wall: **you have to be sure the control group was never advertised to.**

## Three ways to hold back a slice

**All three split something in half at random. What gets split is what differs.**

### Split the map into regions

**How it works: assign regions at random to two groups. One keeps running the ads, the other receives none.** This is the approach in Google's 2011 paper *Measuring Ad Effectiveness Using Geo Experiments*, and the basis of today's geo-lift products. It needs two things: **ads targetable by geography**, and **an outcome metric measurable by region**. In the US the unit is the 210 Nielsen DMAs — designated market areas, the TV-market geography. The design runs a pre-test period where both sides are identical, then a test period where only the treatment side changes.

**The cost is granularity.** The smaller the region, the fewer units get randomised and the wider the interval. The larger the region, the more people fall into the control group, and the more the advertiser hates it. Google rules out the postal-code level outright: the ads do not target accurately enough, and people cross the boundaries anyway.

### Ghost ads

**How it works: the control group still enters the auction, but its ads never win a slot.** Google's Conversion Lift and Meta's Conversion Lift both work this way, and they are finer-grained: the randomised unit is the person, so the sample can be large and the interval narrow.

**The cost is money.** The platform bills for the control group's impressions as usual. You pay, and the ad does not run — that bill is the ghost ad spend.

**All three methods share one precondition: you can measure the outcome.** For a channel that produces conversions but no sales, you can measure the incrementality of clicks, but not of money.

### Split the timeline

**How it works: the same audience, two periods. Ads run in the first, stop in the second, and you compare the audience against itself.** This is the cheapest of the three and the weakest. **It is not random.** The two periods see different market conditions: seasonality, competitor promotions, holidays. The gap you measure is part ad effect and part "these two periods were different anyway." **The timeline split ranks last.**

## The numbers it produces

**One experiment, two entirely different numbers.** The platform bill in the Google paper's search ads experiment showed a CPC of 2.40 dollars. The experiment measured a CPIC — cost per incremental click — of 3.00 dollars.

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9ACPC%202.40%20%E7%BE%8E%E5%85%83%EF%BC%8CCPIC%203.00%20%E7%BE%8E%E5%85%83%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%2C%22%E5%AE%9E%E9%AA%8C%E6%B5%8B%E5%87%BA%E7%9A%84%20CPIC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%24%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9ACPC%202.40%20%E7%BE%8E%E5%85%83%EF%BC%8CCPIC%203.00%20%E7%BE%8E%E5%85%83%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%2C%22%E5%AE%9E%E9%AA%8C%E6%B5%8B%E5%87%BA%E7%9A%84%20CPIC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%24%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9ACPC%202.40%20%E7%BE%8E%E5%85%83%EF%BC%8CCPIC%203.00%20%E7%BE%8E%E5%85%83%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%2C%22%E5%AE%9E%E9%AA%8C%E6%B5%8B%E5%87%BA%E7%9A%84%20CPIC%5Cn%EF%BC%88%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E7%9A%84%E9%92%B1%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%24%7Bc%7D%22%7D%7D%5D%7D&w=760&h=420" width="760" alt="geo_cpc_vs_cpic"></a>

**The platform's CPC understates the true incremental cost by 20%.** 20% of paid clicks came away from organic search, and stealing them added no click to the market. **That 20% is the size of an entire category of error:** every number in a platform report assumes the extra click is there because the ad bought it.

**One of Facebook's 15 field experiments was a checkout experiment.** Same campaign, same people: the observational method advertisers use every day (exposed versus unexposed) returned **316%**, the randomised experiment **73%**.

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E5%90%8C%E4%B8%80%E4%B8%AA%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E8%A7%82%E6%B5%8B%E5%8F%A3%E5%BE%84%20316%25%20%E5%AF%B9%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%2073%25%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%5Cn%EF%BC%88%E5%B9%BF%E5%91%8A%E4%B8%BB%E5%B8%B8%E7%94%A8%E7%9A%84%E5%8F%A3%E5%BE%84%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%5Cn%EF%BC%88%E5%88%86%E6%88%90%E4%B8%A4%E7%BB%84%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8F%90%E5%8D%87%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B316%2C73%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="fb_checkout_316_vs_73"></a>

**More than five times.** The finding from that paper: the observational method frequently fails to recover the effect a randomised experiment measures. Matching, regression and propensity score were all tried, and none won reliably.

## Four ways it goes wrong

**Ordered by how often they bite.**

### The two sides were different to begin with

Geographic splits hit this hardest: the treatment side is a university town, the control side an industrial district, and the customer mix differs at the root. **Random assignment fixes most of it, but not all of it** — it spreads known differences evenly, but it cannot rule out unknown ones. The Google paper's fix: sort all DMAs by size, cut them into equal-sized groups, then draw one per group at random for the treatment side. **This narrows the interval by about 10%.**

### The sample is too small

**A wide interval is the same as no measurement.** Geographic splits start with few units: the DMA granularity in the US is 210 regions, so two groups of 105 is the whole randomised sample available. The paper's shortcut: take the pre-test historical data, **manufacture a fake pre-test period and a fake test period, and push them through the variance formula** to get the interval width. **This costs nothing, and it tells you before you launch whether the design can detect anything at all.**

### The test did not run long enough

**This is the one people overlook, and it is the most expensive.** Search ad clicks are instant: the moment the spend stops, incremental clicks stop. **Offline sales do not.** After the treatment group's spend returned to pre-test levels, the Google paper's chart shows incremental sales still climbing before they faded. **The test period has to outlast the entire response lag.** Ending the test halfway gives you a truncated number, and it is **the smaller** one — the one that looks good on a dashboard.

### The treatment leaked into the control

**Did the control group really receive nothing?** All three methods have this hole. In geographic splits the ads do not target accurately and people cross regional boundaries. In ghost ads the platform may still have served other campaigns to the control group. In timeline splits the two periods face different competitor activity. **This is the hardest hole to close, because you cannot see it.**

## When it is worth running, and what the number is good for

**Incrementality tests are expensive. They earn their cost in two situations: using the number to decide where the money goes, or using it to calibrate the observational method you rely on every day.** A few tens of thousands a month, or a question of "is this channel any good" rather than "is it worth more money" — none of those justify one. **One cost that does not appear on the invoice: the held-back slice really did receive no ads.** That is the price of the answer.

**The number answers one question, and only for one run.** It is far smaller than the observational one and far truer — 316% against 73% in the Facebook experiment, more than four times apart. **The platform's number is not fake, and it answers a different question.** A test measures one period, spend level and population, so change the budget, the creative, the season or the audience and the incrementality changes with it. A 73% increment **cannot be multiplied straight into next month's budget.**

[→ Without the ads, would these orders have happened?](../../1-report-overview/06-incrementality-chart/en.md) · [→ A control group is not merely "the people you did not target"](../../3-experiment-design/01-what-a-control-group-is/en.md)

**Data**: Vaver & Koehler, *Measuring Ad Effectiveness Using Geo Experiments*, Google Inc., 2011 (the design and power analysis for geo experiments; 210 Nielsen DMAs; stratified assignment narrows the interval by about 10%; CPC 2.40 dollars against CPIC 3.00 dollars); Gordon, Zettelmeyer, Bhargava & Chapsky, *Marketing Science* 38(2), 2019 (Facebook's 15 field experiments; checkout experiment, 316% from the observational method against 73% from the randomised experiment). **Reproduce**: the numbers in the charts are the results reported in those two papers, and no x-cmd command re-runs them; to substitute your own, edit the series data array in the link's d= parameter.
