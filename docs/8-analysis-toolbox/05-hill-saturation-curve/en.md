# The extra 100,000 buys you 0 orders, or 30, or 3. The Hill curve says which

"Spend another 100,000 on this channel. How many more orders do we get?"

**The answer is not 100,000, and it is not zero. It depends on where you already are.**

Spending from 0 to 1,000,000 buys market reach. Spending from 1,000,000 to 1,100,000 buys repeated contact with people you have already reached. **That shape — returns shrinking as you spend more — needs a curve.**

## The Hill curve never lets spend run past the ceiling

The curve keeps going up, gets flatter and flatter, and hugs a horizontal line. That line is the ceiling: the most sales this channel can produce, no matter how much money goes in.

```text
effect(x) = x^α / (x^α + k^α)
```

**x is spend, α is elasticity, k is the saturation point.** No matter how large x gets, the effect stays below 1, approaching the ceiling without crossing it. That is why nearly every marketing mix model fits one — **because real channels have a limit and a linear model does not.**

## k sets the ceiling, α sets how fast you get there

### k: the spend level where half the ceiling lands

**k is where the ceiling sits, expressed as a spend level.** When effect(x) reaches 0.5, x is exactly k: **spend to the saturation point and you have half the ceiling.** k is set by market size, reachable audience, and room in the category.

A larger k pushes the ceiling further away. To reach 90% of it, spend has to hit 9^(1/α) times k: 9 times k when α = 1, 3 when α = 2, 2.1 when α = 3. **That multiple travels with α.** The larger α is, the sooner you reach the ceiling. And α is a shape relative to k, so the same α with a different k is a different channel.

### α: the elasticity, which decides where the curve flattens

**α decides at what spend level the curve starts to bend over.** It is set by the nature of the channel: search ads respond fast (small α), brand ads ramp slowly (large α). α = 1 is the plainest version: double the spend, double the effect, though it never gets to 1. At α = 2 the curve is flatter at low spend — **a small budget earns back less**, and the effect only shows up near k.

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Hill%20%E6%9B%B2%E7%BA%BF%EF%BC%9A%E5%90%8C%E6%A0%B7%E7%9A%84%20k%EF%BC%8C%E4%B8%8D%E5%90%8C%E7%9A%84%20%CE%B1%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220%22%2C%22250%22%2C%22500%22%2C%221000%22%2C%221500%22%2C%222000%22%2C%223000%22%2C%224000%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%95%88%E6%9E%9C%EF%BC%88%E5%8D%A0%E5%A4%A9%E8%8A%B1%E6%9D%BF%E7%9A%84%E6%AF%94%E4%BE%8B%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%CE%B1%20%3D%201%EF%BC%88k%3D1000%EF%BC%89%22%2C%22%CE%B1%20%3D%202%EF%BC%88k%3D1000%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%CE%B1%20%3D%201%EF%BC%88k%3D1000%EF%BC%89%22%2C%22data%22%3A%5B0%2C0.2%2C0.33%2C0.5%2C0.6%2C0.67%2C0.75%2C0.8%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%CE%B1%20%3D%202%EF%BC%88k%3D1000%EF%BC%89%22%2C%22data%22%3A%5B0%2C0.06%2C0.2%2C0.5%2C0.69%2C0.8%2C0.9%2C0.94%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=420

```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Hill%20%E6%9B%B2%E7%BA%BF%EF%BC%9A%E5%90%8C%E6%A0%B7%E7%9A%84%20k%EF%BC%8C%E4%B8%8D%E5%90%8C%E7%9A%84%20%CE%B1%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220%22%2C%22250%22%2C%22500%22%2C%221000%22%2C%221500%22%2C%222000%22%2C%223000%22%2C%224000%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%95%88%E6%9E%9C%EF%BC%88%E5%8D%A0%E5%A4%A9%E8%8A%B1%E6%9D%BF%E7%9A%84%E6%AF%94%E4%BE%8B%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%CE%B1%20%3D%201%EF%BC%88k%3D1000%EF%BC%89%22%2C%22%CE%B1%20%3D%202%EF%BC%88k%3D1000%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%CE%B1%20%3D%201%EF%BC%88k%3D1000%EF%BC%89%22%2C%22data%22%3A%5B0%2C0.2%2C0.33%2C0.5%2C0.6%2C0.67%2C0.75%2C0.8%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%CE%B1%20%3D%202%EF%BC%88k%3D1000%EF%BC%89%22%2C%22data%22%3A%5B0%2C0.06%2C0.2%2C0.5%2C0.69%2C0.8%2C0.9%2C0.94%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Hill%20%E6%9B%B2%E7%BA%BF%EF%BC%9A%E5%90%8C%E6%A0%B7%E7%9A%84%20k%EF%BC%8C%E4%B8%8D%E5%90%8C%E7%9A%84%20%CE%B1%22%7D%2C%22color%22%3A%5B%22%2364748b%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%220%22%2C%22250%22%2C%22500%22%2C%221000%22%2C%221500%22%2C%222000%22%2C%223000%22%2C%224000%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%95%88%E6%9E%9C%EF%BC%88%E5%8D%A0%E5%A4%A9%E8%8A%B1%E6%9D%BF%E7%9A%84%E6%AF%94%E4%BE%8B%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%CE%B1%20%3D%201%EF%BC%88k%3D1000%EF%BC%89%22%2C%22%CE%B1%20%3D%202%EF%BC%88k%3D1000%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%CE%B1%20%3D%201%EF%BC%88k%3D1000%EF%BC%89%22%2C%22data%22%3A%5B0%2C0.2%2C0.33%2C0.5%2C0.6%2C0.67%2C0.75%2C0.8%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%CE%B1%20%3D%202%EF%BC%88k%3D1000%EF%BC%89%22%2C%22data%22%3A%5B0%2C0.06%2C0.2%2C0.5%2C0.69%2C0.8%2C0.9%2C0.94%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=420" width="760" alt="hill_curve_alpha_1_vs_2"></a>

**Look at the two lines at 500: α = 1 has reached 0.33, α = 2 is only at 0.2.** Same spend, lower return, because the α = 2 channel climbs slower early on.

**A curve with α above 1 has one more property: unit return starts low, rises through the middle, and turns over.** "Unit return" means effect divided by spend — how much effect one yuan buys. For α = 2 and k = 1000 it peaks at x = k(α−1)^(1/α) = 1000, half the ceiling.

**But the steepest point comes earlier.** The slope is largest at x = k((α−1)/(α+1))^(1/α), which for α = 2 is 1000·(1/3)^0.5 ≈ 577. There, **one extra yuan buys the largest increment in effect.** Above it, effect still climbs, but each extra yuan lifts it less. **Two positions, two meanings:** 577 is where adding money is most efficient, 1000 is where the unit price is best.

**Which is why "test small first, then scale up" is not always the right instinct.** For channels with α > 1 the first few hundred yuan buy a trial run, and the effect really is flattened there — which is also why adding money to an established channel can pay better than starting small. Not every channel behaves this way, but the shape allows it.

## Where the Hill curve stops being trustworthy

### A young channel cannot tell you where its ceiling is

**To estimate a ceiling, you have to climb close to it.** For a channel that has only spent 200, whether k is 500 or 5000 makes no difference to the fit.

**Where the data does not reach, the parameters are guesses.** A guessed k goes straight into the contribution calculation: guess k too high and the model hands that channel more contribution. **So treat MMM contribution numbers for new channels as discounted.** The common practice is to give a new channel a prior borrowed from comparable channels rather than letting it fit freely — but keep track that the number was borrowed.

### α swings wildly when the data is thin

**Fitting the two parameters together is what makes them unstable.** When most of your data sits below 10% of k, the curve is close to a straight line there, and a great many (k, α) pairs fit it well. The software picks one; swap in a different one and the conclusion can reverse.

**How to tell: look at the uncertainty interval.** If the 95% interval for k runs from 300 to 3000, that k has not really been estimated, and neither has the contribution number attached.

### There is more than one curve

**Hill is the most common, not the only one, and not always the right one.** The alternatives — logistic (fits an S shape), Michaelis-Menten (the biochemistry one, shaped much like Hill), plain piecewise linear — produce similar numbers on large samples. The difference shows up when the data is thin. So do not ask "which curve was used". Ask "how good is the fit, and how wide are the parameter intervals". If swapping the curve flips the conclusion, the curve gave it to you.

### The saturation point moves

**k is not a fixed property of a channel. It changes.** A competitor enters and goes after the same people: k falls. The channel expands into new cities or new age groups: k rises. **A k estimated a year ago, used for a budget decision today, is out of date.** As [→ Decomposing MMM contribution](../../8-analysis-toolbox/03-mmm-contribution/en.md) puts it: **a saturation curve describes "at some spend level", not a permanent property.**

## Three checks that cost nothing

**If a channel is already saturated, the model can show it. First, check whether the contribution breakdown shows spend rising while contribution stalls.** Spend up 50% this quarter with contribution up 5% means the channel is already against the ceiling.

**Second, check whether marginal return is falling.** That is the number [→ Marginal ROI versus average ROI](../../8-analysis-toolbox/06-marginal-vs-average-roi/en.md) is about. Average ROI still looks healthy while marginal ROI has dropped to near zero — the saturation signal.

**Third, check whether the residuals have a pattern.** If residuals in the high-spend range all lean the same way, the curve's shape does not match what happened.

**None of these needs a rerun. They are readable from the data you already have.**

## The Hill curve draws a line where the ceiling is, and nothing goes past it

**The Hill saturation curve does one thing: it gives the idea that more spend buys less extra effect a mathematical shape, so spend can never cross the top.** k sets where the ceiling is, α sets how fast you approach it — and both are easier to trust once you can see how far the data reached. A ceiling estimated from data that stops at 10% of k is not a ceiling. It is a guess with a decimal point.

[→ Decomposing MMM contribution](../../8-analysis-toolbox/03-mmm-contribution/en.md) · [→ Marginal ROI versus average ROI](../../8-analysis-toolbox/06-marginal-vs-average-roi/en.md) · [→ The equal marginal returns principle](../../8-analysis-toolbox/07-equal-marginal-returns-principle/en.md)

**Data**: the numbers in the chart are the standard definitions of the Hill curve plus one worked example (two curves, α = 1 and α = 2, k = 1000). **Reproduce**: no x-cmd command re-runs them. To swap in your own k and α, edit the series data arrays in the link's d= parameter and recompute them as x^α / (x^α + k^α).
