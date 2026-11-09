# Two numbers on the same ad spend answer two different questions

ROAS 4.0 in the dashboard. 0.3 in the experiment. Both describe the same ad spend.

**These are not two answers to one question. They are answers to two questions.** The platform ledger records the orders that touched an ad. The incrementality ledger records the orders that stopped happening when the ads stopped. **Neither number can be added to the other, and neither one corrects the other.**

__FIG1__

**In one line: platform numbers tune campaigns inside the platform; incremental numbers decide whether the money keeps flowing.**

## Putting the two side by side without mixing them

__FIG2__

**When you hold both numbers, the common mistake is not picking the wrong one. It is combining them into a single figure.**

### The two ledgers do not record the same thing

**The platform ledger starts at the impression.** Impression, click, add-to-cart, purchase — every order that touched an ad during that session is booked to the ad. **The incrementality ledger has exactly one line: the orders that stopped converting once the spend stopped.**

**The numerators are not the same kind of quantity.** One is an order count. The other is a difference between two order counts. Put them in the same formula and you are adding sales revenue to profit margin.

**They are nested, not parallel.** The incremental orders are already inside the platform ledger.

### One number says how much you spent, the other says how much you lost

__FIG3__

**The platform ledger is an addition: ad spend plus the revenue of orders that touched an ad.** The incrementality ledger is a subtraction: the difference in orders between before and after the ads stopped.

**Both ledgers are internally valid. They answer different questions.** The platform ledger answers "how many orders that touched this ad came out of it." The incrementality ledger answers "would those orders have happened without the money."

## What each ledger actually records

### The platform ledger claims the whole funnel

__FIG4__

**The platform's method has one practical advantage: it captures the entire chain.** Advertisers have no access to the ad delivery side. They cannot see impressions, clicks or carts. They see the purchase, and only the purchase.

**The attribution window is this ledger's time boundary.** An order placed 7 days after the click counts. So does one placed 30 days later, or 14. The longer the window, the more orders get claimed.

### The incrementality ledger records only what disappeared

__FIG5__

**Incrementality has a one-sentence definition: the orders that no longer happen once this ad stops.**

**It has nothing to do with ad spend, and nothing to do with the attribution window.** Incrementality is a difference, not a ratio.

## Where the gap comes from

### Exposure is not random: the platform shows the ad to people who were already going to buy

__FIG6__

**In Facebook's 2019 paper, one ad campaign measured a true lift of 73% in the randomized experiment.** The observational method advertisers use every day reported 316%. Even with exact matching, it reported 222%.

**The gap comes from the delivery itself:** the algorithm picks well, and what it picks is the audience with the strongest intent.

**The crude comparison is seen versus not seen.** People who saw the ad were already more likely to buy, and that group gets credited to the ad.

### The attribution window: every extra day claims a few more orders

**The longer the window, the bigger the platform ledger.** For the same campaign, a 7-day window and a 30-day window can differ enormously.

### Demand that already existed gets claimed

__FIG7__

**In the eBay experiments from 2015, ROI on non-brand search ads came out three different ways.** Regression said 4100%. Adding time and geography as controls still gave 1400%. The randomized experiment said **−63%**, with a 95% confidence interval from −124% to −3%.

**The sign flipped.** The money did not buy orders. It intercepted people who had already decided to buy and charged them an ad fee.

## Put them in separate columns and never add them

### One table, two columns, each labelled with its own method

__FIG8__

**The header needs to state three things: which method this column uses, and the date the data runs through.**

### What adding them would cost you

**First, the total of the two numbers means nothing.** The incremental orders are already inside the platform orders.

**Second, using the platform number to infer incrementality invents a channel contribution that does not exist.**

**Third, each column has to stand on its own.**

## Which one to use, and when

### Talking about optimization inside the platform: the platform method

__FIG9__

**Bids, targeting, creative, audience lists — all of these happen inside the platform's rules.** The platform's numbers are the scoreboard for those actions.

**But the platform method only compares the platform's own things against each other.** It can tell you creative A beat creative B. It cannot tell you whether this channel deserves to keep running.

### Talking about whether the money keeps paying: the incremental method

**To decide whether to renew the spend, and whether the ROI can carry the channel, use the incremental method.**

**In one geo experiment, the platform reported a cost per click of $2.4. The measured cost per incremental click was $3.0.** One in five paid clicks came from organic search.

### When neither set is enough

**If all you have is the platform number, with no control to compare against, you can write neither one.**

## Two ledgers, each kept separate

**The platform number and the incremental number are not competing on accuracy. They answer different questions.**

**Put them side by side, label the method and the date, and add nothing.** Platform numbers for optimization inside the platform. Incremental numbers for whether the spend continues.

[→ Without the ads, would these orders have happened?](../../1-report-overview/06-incrementality-chart/en.md) · [→ Attribution: how the platform assigns an order to an ad](../../8-analysis-toolbox/01-attribution/en.md) · [→ Incrementality testing: measuring what disappears when the spend stops](../../8-analysis-toolbox/02-incrementality-testing/en.md) · [→ ROI ranking is not a budget allocation order](../02-roi-ranking-vs-budget-allocation/en.md)

**Data**: __DATA__ **Reproduce**: __REPRO__
