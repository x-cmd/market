# The platform's number and the ad's real effect are two different numbers

ROAS 4.0 in the dashboard. 0.3 in the experiment. Same ad spend.

**They are not two answers to one question. They are answers to two questions.** The platform ledger books the orders that touched an ad. The incrementality ledger books the orders that disappeared when the spend stopped. **Neither number can be added to the other, and neither one corrects the other.**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%90%8C%E4%B8%80%E6%89%B9%E5%B9%BF%E5%91%8A%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%E4%B8%89%E4%B8%AA%E6%8F%90%E5%8D%87%E5%80%BC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%E5%B9%B4%E9%BE%84%E6%80%A7%E5%88%AB%22%2C%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%E6%8F%90%E5%8D%87%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B73%2C222%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```
<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Facebook%20%E7%BB%93%E8%B4%A6%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%90%8C%E4%B8%80%E6%89%B9%E5%B9%BF%E5%91%8A%EF%BC%8C%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%E4%B8%89%E4%B8%AA%E6%8F%90%E5%8D%87%E5%80%BC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%EF%BC%88%E7%9C%9F%E5%80%BC%EF%BC%89%22%2C%22%E7%B2%BE%E7%A1%AE%E5%8C%B9%E9%85%8D%E5%B9%B4%E9%BE%84%E6%80%A7%E5%88%AB%22%2C%22%E6%9B%9D%E5%85%89%20vs%20%E6%9C%AA%E6%9B%9D%E5%85%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%BD%AC%E5%8C%96%E7%8E%87%E6%8F%90%E5%8D%87%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B73%2C222%2C316%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="facebook_lift_three_ways"></a>

**In one line: platform numbers tune campaigns inside the platform. Incremental numbers decide whether the money keeps flowing.**

## How to hold two numbers without mixing them up

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%B9%B3%E5%8F%B0%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%20vs%20%E5%A2%9E%E9%87%8F%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%AE%A2%E5%8D%95%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E8%B4%A6%EF%BC%9A%E6%B2%BE%E8%BF%87%E5%B9%BF%E5%91%8A%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%85%B6%E4%B8%AD%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E4%BC%9A%E6%B6%88%E5%A4%B1%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%A2%9E%E9%87%8F%E8%B4%A6%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E5%B0%91%E6%8E%89%E7%9A%84%E8%AE%A2%E5%8D%95%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A60%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1000%2C250%2C250%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```
<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%B9%B3%E5%8F%B0%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%20vs%20%E5%A2%9E%E9%87%8F%E9%82%A3%E6%9C%AC%E8%B4%A6%E8%AE%B0%E7%9A%84%E8%AE%A2%E5%8D%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E8%AE%A2%E5%8D%95%E6%95%B0%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E8%B4%A6%EF%BC%9A%E6%B2%BE%E8%BF%87%E5%B9%BF%E5%91%8A%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%85%B6%E4%B8%AD%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E4%BC%9A%E6%B6%88%E5%A4%B1%E7%9A%84%E8%AE%A2%E5%8D%95%22%2C%22%E5%A2%9E%E9%87%8F%E8%B4%A6%EF%BC%9A%E5%81%9C%E6%8A%95%E5%90%8E%E5%B0%91%E6%8E%89%E7%9A%84%E8%AE%A2%E5%8D%95%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A60%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B1000%2C250%2C250%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="platform_vs_incremental_containment"></a>

**Holding both numbers, the common mistake is not picking the wrong one. It is adding them into a single figure.** The platform report and your own experiment each say their own thing, and then both get typed into the same column.

### The two ledgers do not record the same thing

**The platform ledger starts at the impression.** Impression, click, add-to-cart, purchase. Every order that touched an ad in that session is booked to the ad.

**The incrementality ledger has one line item: the orders that stopped converting once the spend stopped.**

**The two numerators are not the same kind of quantity.** One is an order count. The other is a difference between two order counts. Drop both into one formula and you are adding sales revenue to profit margin.

**They are nested, not parallel.** In the chart above, the 250 incremental orders sit inside the 1,000 platform orders. Stack them and 250 of your 1,250 were counted twice. The platform ledger is addition; the incrementality ledger is subtraction.

**Both hold up. They answer different questions.** The platform ledger answers "how many orders that touched this ad came out of it." The incrementality ledger answers "would those orders have happened without the money."

**The first question needs no control group. The second cannot do without one.** Read the same 4.0 ROAS either way and you get two different things.

## What each ledger actually records

### The platform ledger claims the whole funnel

**The platform method has one practical advantage: it captures the entire chain.** Advertisers have no access to the delivery side. No impressions, no clicks, no carts. They see the purchase, and only the purchase.

**The attribution window is this ledger's time boundary.** An order placed 7 days after the click counts. So does one placed 14 days later, or 30. The longer the window, the more orders get claimed, and the higher the ROAS on the report.

**None of the money changes when the window changes.** Same campaign, same spend, window moved from 7 days to 30. The number moves a long way. The budget does not. That is also why two advertisers' reports cannot be compared directly.

### The incrementality ledger records only what disappeared

**Incrementality has a one-sentence definition: the orders that no longer happen once this ad stops.**

**It has nothing to do with ad spend, and nothing to do with the attribution window.** Incrementality is a difference, not a ratio, and not the credit for one particular click.

**The price is a control group.** Where the ads stop, you need a set of places that keeps running. Otherwise you know the total fell, but not whether the missing orders were ones the ads bought or ones that were coming anyway.

## Where the gap comes from

### Exposure is not random: the platform shows the ad to people who were already going to buy

**In Facebook's 2019 paper, one ad campaign measured a true lift of 73% in the randomized experiment.** The observational method advertisers use every day reported 316%. Even with exact matching, it reported 222%.

**The gap comes from the delivery itself.** The algorithm picks well, and what it picks is the audience with the strongest intent. Those people were already more likely to buy. The ad arrives, they convert, and the ledger calls it the ad's doing. The crude seen-versus-not-seen comparison overstates the lift four times over.

### The attribution window: every extra day claims a few more orders

**The longer the window, the bigger the platform ledger.** For the same campaign, a 7-day window and a 30-day window can differ enormously. Change the window and the same flight of ads gives a different number.

### Demand that already existed gets claimed

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22eBay%20%E9%9D%9E%E5%93%81%E7%89%8C%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%9A%E5%9B%9E%E6%8A%A5%E7%8E%87%E7%9A%84%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%EF%BC%88%E6%97%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%EF%BC%88%E5%8A%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E5%9C%B0%E5%9F%9F%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```
<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22eBay%20%E9%9D%9E%E5%93%81%E7%89%8C%E8%AF%8D%E6%90%9C%E7%B4%A2%E5%B9%BF%E5%91%8A%EF%BC%9A%E5%9B%9E%E6%8A%A5%E7%8E%87%E7%9A%84%E4%B8%89%E7%A7%8D%E7%AE%97%E6%B3%95%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%9B%9E%E5%BD%92%EF%BC%88%E6%97%A0%E6%8E%A7%E5%88%B6%E5%8F%98%E9%87%8F%EF%BC%89%22%2C%22%E5%9B%9E%E5%BD%92%EF%BC%88%E5%8A%A0%E6%97%B6%E9%97%B4%E4%B8%8E%E5%9C%B0%E5%9F%9F%E6%8E%A7%E5%88%B6%EF%BC%89%22%2C%22%E9%9A%8F%E6%9C%BA%E5%AE%9E%E9%AA%8C%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22ROI%20%25%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B4100%2C1400%2C-63%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="ebay_roi_three_ways"></a>

**In the eBay experiments from 2015, ROI on non-brand search ads came out three different ways.** Regression said 4100%. Adding time and geography as controls still gave 1400%. The randomized experiment said **−63%**, with a 95% confidence interval from −124% to −3%.

**The sign flipped.** The money did not buy orders. It intercepted people who had already decided to buy and charged them an ad fee.

## Write them side by side, never add them

### One table, two columns, each labelled with its own method

**The header needs to name the method the column uses and the date the data runs through.**

| Method | Platform report (7-day click attribution) | Incrementality experiment (geo random control) |
|---|---|---|
| Orders attributed | 4,000 | 300 |
| Ad spend | 48,000 dollars | 48,000 dollars |
| Revenue brought in | 192,000 dollars | 14,400 dollars |
| Return | 4.0 | 0.3 |
| Data as of | 2026-10-31 | 2026-10-31 |

**Two columns side by side, each standing on its own, neither one editing the other.** When someone asks "which one is right," the question itself is wrong. The left column answers optimization inside the platform. The right column answers whether the spend continues.

**Do not add the two numbers.** Adding them sells the same orders twice. And using the platform number to infer incrementality invents a channel contribution that does not exist.

## Which one to use, and when

### Talking about optimization inside the platform: the platform method

**Bids, targeting, creative, audience lists — all of these happen inside the platform's rules.** The platform's numbers are the scoreboard for those actions. Creative A versus creative B, the platform method answers that directly.

**But it only compares the platform's own things against each other.** It tells you creative A beat creative B. It cannot tell you whether the channel deserves to keep running.

### Talking about whether the money keeps paying: the incremental method

**To decide whether to renew the spend, and whether the ROI can carry the channel, use the incremental method.**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20vs%20%E6%B5%8B%E5%87%BA%E7%9A%84%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%22%2C%22%E6%B5%8B%E5%87%BA%E7%9A%84%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20CPIC%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400
```
<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E4%B8%80%E6%AC%A1%20geo%20%E5%AE%9E%E9%AA%8C%EF%BC%9A%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%E6%AF%8F%E6%AC%A1%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20vs%20%E6%B5%8B%E5%87%BA%E7%9A%84%E6%AF%8F%E6%AC%A1%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B9%B3%E5%8F%B0%E6%8A%A5%E7%9A%84%20CPC%22%2C%22%E6%B5%8B%E5%87%BA%E7%9A%84%E5%A2%9E%E9%87%8F%E7%82%B9%E5%87%BB%E6%88%90%E6%9C%AC%20CPIC%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E7%BE%8E%E5%85%83%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B2.4%2C3.0%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=400" width="760" alt="geo_cpc_vs_cpic"></a>

**In one geo experiment, the platform reported a cost per click of $2.4. The measured cost per incremental click was $3.0.**

**One in five paid clicks came from organic search, not from anything new.** The platform's CPC runs systematically low, because the denominator mixes in clicks that would have happened anyway.

### When neither set is enough

**If all you have is the platform number, with no control to compare against, you can write neither one.** The incremental column reads "not measured." It does not get a coefficient applied to the platform number.

**Miss the test this quarter and there is no second ledger later.** The platform ledger can be pulled any time. The incrementality ledger exists only while a control group is running.

## Two ledgers, each kept separate

**The platform number and the incremental number are not competing on accuracy. They answer different questions.**

**Put them side by side, label the method and the date, and add nothing.** Platform numbers for optimization inside the platform. Incremental numbers for whether the spend continues.

[→ Without the ads, would these orders have happened?](../../1-report-overview/06-incrementality-chart/en.md) · [→ Attribution: how the platform assigns an order to an ad](../../8-analysis-toolbox/01-attribution/en.md) · [→ Incrementality testing: measuring what disappears when the spend stops](../../8-analysis-toolbox/02-incrementality-testing/en.md) · [→ ROI ranking is not a budget allocation order](../02-roi-ranking-vs-budget-allocation/en.md)

**Data**: Facebook's 73% / 222% / 316% come from Gordon, Zettelmeyer, Bhargava & Chapsky, *Marketing Science* 38(2), 2019 (25.5 million people in the experiment, only 25% of whom actually saw the ad). eBay's 4100% / 1400% / −63% come from Blake, Nosko & Tadelis, *Econometrica* 83(1), 2015 (95% CI −124% to −3%). The geo experiment's $2.4 and $3.0 and the "one in five paid clicks came from organic search" come from Vaver & Koehler, *Measuring Ad Effectiveness Using Geo Experiments*, Google Inc., 2011. The table's 4,000 / 300 orders and the chart's 1,000 / 250 orders are **worked examples**. **Reproduce**: the papers have no public API. `curl -sL -A 'Mozilla/5.0' https://www.nber.org/papers/w20171` fetches the eBay abstract page, `curl -sL -A 'Mozilla/5.0' https://pubsonline.informs.org/doi/10.1287/mksc.2018.1135` the Facebook one. The raw values for the metric cards `paid_search_roi_observed_vs_randomized`, `ad_lift_observed_vs_rct` and `geo_incremental_click_cost` are in `spec/metric-cards.yml`.
