# A good fit does not mean a trustworthy number

An MMM report hands you two numbers: **"social ads contributed 21%"** and **"R² = 0.91"**.

The first answers *how big the contribution is*. The second answers *how well the model explains the past*. Two different rulers, two different things, and plenty of readers treat them as one. **A model can fit history well while the number that matters sits inside an interval so wide it says nothing.**

## The interval grades one number, the fit grades the whole model

### The interval: how precise is this one number?

**In plain terms: a confidence interval is the band of values the true number is likely to fall in.**

You estimate that social ads contributed 21%, and the 95% interval runs from 15% to 27%. A narrow band means the estimate is sharp. A wide band means the estimate barely happened.

**Sample size drives the width.** More observations, narrower band.

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%95%88%E5%BA%94%EF%BC%8C%E4%B8%89%E7%A7%8D%E6%A0%B7%E6%9C%AC%E9%87%8F%E7%BB%99%E5%87%BA%E7%9A%84%E5%8C%BA%E9%97%B4%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%2C%22%23dc2626%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%A0%B7%E6%9C%AC%202000%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B19%25%EF%BC%89%22%2C%22%E6%A0%B7%E6%9C%AC%20200%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B129%25%EF%BC%89%22%2C%22%E6%A0%B7%E6%9C%AC%2050%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B156%25%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%2295%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E7%9A%84%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B9%2C29%2C56%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%95%88%E5%BA%94%EF%BC%8C%E4%B8%89%E7%A7%8D%E6%A0%B7%E6%9C%AC%E9%87%8F%E7%BB%99%E5%87%BA%E7%9A%84%E5%8C%BA%E9%97%B4%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%2C%22%23dc2626%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%A0%B7%E6%9C%AC%202000%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B19%25%EF%BC%89%22%2C%22%E6%A0%B7%E6%9C%AC%20200%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B129%25%EF%BC%89%22%2C%22%E6%A0%B7%E6%9C%AC%2050%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B156%25%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%2295%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E7%9A%84%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B9%2C29%2C56%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E4%B8%AA%E6%95%88%E5%BA%94%EF%BC%8C%E4%B8%89%E7%A7%8D%E6%A0%B7%E6%9C%AC%E9%87%8F%E7%BB%99%E5%87%BA%E7%9A%84%E5%8C%BA%E9%97%B4%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23f59e0b%22%2C%22%23dc2626%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E6%A0%B7%E6%9C%AC%202000%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B19%25%EF%BC%89%22%2C%22%E6%A0%B7%E6%9C%AC%20200%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B129%25%EF%BC%89%22%2C%22%E6%A0%B7%E6%9C%AC%2050%20%E4%BA%BA%5Cn%EF%BC%88%E5%8C%BA%E9%97%B4%20%C2%B156%25%EF%BC%89%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%2295%25%20%E7%BD%AE%E4%BF%A1%E5%8C%BA%E9%97%B4%E7%9A%84%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A90%2C%22right%22%3A50%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B9%2C29%2C56%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%25%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=430" width="760" alt="ci_width_by_sample_size"></a>

**Same effect, same true value, six times the width.** The 50-observation case gets ±56%. That is not a measurement; it is a shrug.

**Intervals are symmetric around the estimate, so they always have a chance of containing zero.** If a channel's contribution is 8% with an interval of −3% to 19%, that channel is **statistically indistinguishable from zero**. You cannot say it contributed, and you cannot say it did not.

### The fit: how well does the model explain the past?

**In plain terms: R² is the share of the historical variation in sales that the model's predictions account for.**

R² = 0.91 means the model's predicted sales explain 91% of the variation around actual sales. **It is a property of the whole table, not of any one channel.**

**A good fit says one thing: the model can reproduce history. It says nothing about whether the causal story inside that history is right.**

## Neither one covers for the other

**One grades a parameter, the other grades a model.** And the most important fact is this: **a high fit does not make the parameters accurate.**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%8B%9F%E5%90%88%E5%BA%A6%E9%AB%98%E4%B8%8D%E7%AD%89%E4%BA%8E%E5%8C%BA%E9%97%B4%E7%AA%84%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8B%9F%E5%90%88%E5%BA%A6%20R%C2%B2%EF%BC%88%25%EF%BC%89%22%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%85%B3%E9%94%AE%E5%8F%82%E6%95%B0%E7%9A%84%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A16%2C%22data%22%3A%5B%7B%22value%22%3A%5B92%2C3%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20A%22%7D%2C%7B%22value%22%3A%5B88%2C18%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20B%22%7D%2C%7B%22value%22%3A%5B61%2C4%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20C%22%7D%2C%7B%22value%22%3A%5B55%2C25%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20D%22%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=440
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%8B%9F%E5%90%88%E5%BA%A6%E9%AB%98%E4%B8%8D%E7%AD%89%E4%BA%8E%E5%8C%BA%E9%97%B4%E7%AA%84%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8B%9F%E5%90%88%E5%BA%A6%20R%C2%B2%EF%BC%88%25%EF%BC%89%22%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%85%B3%E9%94%AE%E5%8F%82%E6%95%B0%E7%9A%84%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A16%2C%22data%22%3A%5B%7B%22value%22%3A%5B92%2C3%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20A%22%7D%2C%7B%22value%22%3A%5B88%2C18%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20B%22%7D%2C%7B%22value%22%3A%5B61%2C4%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20C%22%7D%2C%7B%22value%22%3A%5B55%2C25%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20D%22%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=440"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%8B%9F%E5%90%88%E5%BA%A6%E9%AB%98%E4%B8%8D%E7%AD%89%E4%BA%8E%E5%8C%BA%E9%97%B4%E7%AA%84%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%2C%22%2364748b%22%2C%22%23f59e0b%22%2C%22%230891b2%22%2C%22%238b5cf6%22%2C%22%2365a30d%22%2C%22%23db2777%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E6%8B%9F%E5%90%88%E5%BA%A6%20R%C2%B2%EF%BC%88%25%EF%BC%89%22%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%85%B3%E9%94%AE%E5%8F%82%E6%95%B0%E7%9A%84%E5%8C%BA%E9%97%B4%E5%8D%8A%E5%AE%BD%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A16%2C%22data%22%3A%5B%7B%22value%22%3A%5B92%2C3%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20A%22%7D%2C%7B%22value%22%3A%5B88%2C18%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20B%22%7D%2C%7B%22value%22%3A%5B61%2C4%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20C%22%7D%2C%7B%22value%22%3A%5B55%2C25%5D%2C%22name%22%3A%22%E6%A8%A1%E5%9E%8B%20D%22%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=440" width="760" alt="fit_vs_interval_width"></a>

**Model B has an R² of 88%. Model A has 92%.** On fit alone, both look fine.

**But the half-width of the key parameter's interval is 18% in Model B and 3% in Model A.**

**Model A sits in the top-right corner: highest fit, narrowest interval. That is the one worth using.**

**Now look at Models C and D.** C fits at only 61% yet its interval half-width is 4%. D fits at 55% and its half-width is 25%.

**Here is the counterintuitive result: fit and parameter precision can come apart completely.** A model can reproduce history perfectly while having no confidence at all in the one parameter that matters.

**The reason:** fit asks whether predictions line up with actuals. Parameter precision asks whether the data contains enough information to pin the number down. **A model can fit beautifully when two variables are highly correlated** — it knows those two weeks of sales were 1000, but not whether search ads or social ads produced them. **The better it fits, the more it looks like it knows.**

### A test that beats the R² number

**Look for systematic pattern in the residuals.** The residual is the gap between what the model predicted and what actually happened.

In a good model the residuals are random: sometimes high, sometimes low, no persistent lean either way.

**When residuals lean the same way across a whole range** — say the model stays too high during a high-spend stretch — the model's shape does not match reality. **A high fit is fake in that case**, because it was fitted with the wrong shape.

**This is a third ruler for fit, and a more useful one than the R² number itself.**

## Where both numbers stop holding up

### A high fit is not a causal claim

**This is the blind spot both rulers share.**

A model with R² = 0.95 can rest on a wrong relationship. Say social ad spend tracks the season tightly and the model leaves out the seasonal term — the whole effect gets charged to social ads. **The model fits well because the season really does drive sales, but the ads did not.**

**Causation comes from experiments, not from a better fit.** See [→ Incrementality testing: run one region as the control](../02-incrementality-testing/en.md).

### The interval only covers the assumptions the model already believes

**A confidence interval answers: "if the model's form is right, where is the true value?"**

**It does not answer: "is the model's form right?"** Swap the saturation curve or the baseline and the whole interval can move.

**So a narrow interval can be worthless**: the model is wrong, and confidently wrong.

**The usual move is to re-run with several settings and watch whether the interval moves.** That comes up in [→ MMM contribution breakdown](../03-mmm-contribution/en.md), and it is worth repeating here because it applies here too

### Extrapolation breaks

**Both the fit and the interval are computed over the range the data covers.**

If your history spans 0 to 500,000 in search ad spend, a prediction at 600,000 comes with an interval that suddenly widens, **because nothing in the data supports it.**

**R² behaves the same way.** R² = 0.95 describes the past well. **It promises nothing about tomorrow.**

**Extrapolating a saturation curve is the dangerous case.** The ceiling k in a Hill curve is itself estimated. Push past k and the model keeps telling you there is a little more to win, when in fact you hit the wall a while ago.

### Many models tried, only the best one reported

**You tried 5 parameter settings, reported the best-fitting one, and attached its narrow interval.**

**That interval is not honest.** You have already spent the luck that would have produced the widest interval — the one reflecting all your attempts rather than the single luckiest one.

**The fix is to lay out every model you tried and report a range of intervals**, instead of picking the tightest.

## How to use the two numbers

**Confidence interval and fit are two different rulers.** The interval grades one estimate. The fit grades the model around it. **Neither substitutes for the other, and they routinely come apart.** A model can fit very well and still have no confidence in its own key parameter, because it cannot tell two highly correlated variables apart.

**So when a model hands you output, look at both, and look at them together:** is the number precise (how wide is the interval), and is the model sound (what is the fit, are the residuals systematic)?

**One floor under all of it: a good fit means the model reproduces history, not that the causality inside that history is right.** For causation, run an experiment.

[→ Every number needs an interval](../../3-experiment-design/04-confidence-intervals/en.md) · [→ Too small a sample flips the result](../../3-experiment-design/02-sample-size-and-power/en.md) · [→ MMM contribution breakdown: unpacking the long-term contributions](../03-mmm-contribution/en.md)

**Data**: the numbers in the charts are general definitions plus one worked example (how sample size drives interval width, and four models compared on fit against parameter interval half-width); they are not the output of any one company's model. **Reproduce**: the chart numbers are worked examples and no x-cmd command re-runs them; to substitute your own, edit the series data array in the link's d= parameter.
