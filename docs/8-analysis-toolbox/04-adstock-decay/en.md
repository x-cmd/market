# Your ads keep working after you stop paying for them

The TV spot that ran last week produced the orders that landed this week.

Pair this week's spend with this week's sales and the spot is credited to the week it had no effect. Sales look flat, the campaign looks useless.

**Adstock exists for this: it accumulates past spend along a decay curve up to today, then pairs that value with today's outcome.**

## An ad's effect is not spent in a day

An impression, a click, a view leaves a trace in the buyer's mind. The trace fades but does not vanish overnight, so today's result is partly caused by today's spend and partly by last week's.

To answer "what drove this sale," the model lines up past inputs in time order, converts each into "how much is still working today," and adds them up. **The converted number is the Adstock value.** The usual form: 100 spent today keeps 80% of its effect for tomorrow; yesterday's 100 keeps 64%; the day before keeps 51.2%. Three days ago, half.

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Adstock%EF%BC%9A%E6%98%A8%E5%A4%A9%E7%9A%84%20100%20%E5%9D%97%EF%BC%8C%E4%BB%8A%E5%A4%A9%E8%BF%98%E5%89%A9%E5%A4%9A%E5%B0%91%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AC%AC0%E5%A4%A9%22%2C%22%E7%AC%AC1%E5%A4%A9%22%2C%22%E7%AC%AC3%E5%A4%A9%22%2C%22%E7%AC%AC7%E5%A4%A9%22%2C%22%E7%AC%AC14%E5%A4%A9%22%2C%22%E7%AC%AC21%E5%A4%A9%22%2C%22%E7%AC%AC30%E5%A4%A9%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%89%A9%E4%BD%99%E6%95%88%E6%9E%9C%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22line%22%2C%22data%22%3A%5B100%2C80%2C51.2%2C20.97%2C4.4%2C0.92%2C0.12%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Adstock%EF%BC%9A%E6%98%A8%E5%A4%A9%E7%9A%84%20100%20%E5%9D%97%EF%BC%8C%E4%BB%8A%E5%A4%A9%E8%BF%98%E5%89%A9%E5%A4%9A%E5%B0%91%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AC%AC0%E5%A4%A9%22%2C%22%E7%AC%AC1%E5%A4%A9%22%2C%22%E7%AC%AC3%E5%A4%A9%22%2C%22%E7%AC%AC7%E5%A4%A9%22%2C%22%E7%AC%AC14%E5%A4%A9%22%2C%22%E7%AC%AC21%E5%A4%A9%22%2C%22%E7%AC%AC30%E5%A4%A9%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%89%A9%E4%BD%99%E6%95%88%E6%9E%9C%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22line%22%2C%22data%22%3A%5B100%2C80%2C51.2%2C20.97%2C4.4%2C0.92%2C0.12%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22Adstock%EF%BC%9A%E6%98%A8%E5%A4%A9%E7%9A%84%20100%20%E5%9D%97%EF%BC%8C%E4%BB%8A%E5%A4%A9%E8%BF%98%E5%89%A9%E5%A4%9A%E5%B0%91%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AC%AC0%E5%A4%A9%22%2C%22%E7%AC%AC1%E5%A4%A9%22%2C%22%E7%AC%AC3%E5%A4%A9%22%2C%22%E7%AC%AC7%E5%A4%A9%22%2C%22%E7%AC%AC14%E5%A4%A9%22%2C%22%E7%AC%AC21%E5%A4%A9%22%2C%22%E7%AC%AC30%E5%A4%A9%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%89%A9%E4%BD%99%E6%95%88%E6%9E%9C%EF%BC%88%25%EF%BC%89%22%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%22%2C%22type%22%3A%22line%22%2C%22data%22%3A%5B100%2C80%2C51.2%2C20.97%2C4.4%2C0.92%2C0.12%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22stack%22%3Anull%7D%5D%7D&w=760&h=420" width="760" alt="adstock_daily_decay_curve"></a>

**Adstock does not change the effect itself. It changes which day the effect is booked on.** Two models with different lag settings credit the same campaign to different weeks: the accounting period differs, not the advertising.

## One number sets the whole curve

**A decay curve has one parameter:** how much survives each day, so every day takes a discount. The convenient name is **half-life** — how many days it takes for the effect to fall to half. A 2-day half-life is short: the effect is down to one eighth by day three.

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%9D%A1%E6%9B%B2%E7%BA%BF%EF%BC%8C%E8%A1%B0%E5%87%8F%E7%8E%87%E4%B8%8D%E5%90%8C%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AC%AC0%E5%A4%A9%22%2C%22%E7%AC%AC1%E5%A4%A9%22%2C%22%E7%AC%AC3%E5%A4%A9%22%2C%22%E7%AC%AC7%E5%A4%A9%22%2C%22%E7%AC%AC14%E5%A4%A9%22%2C%22%E7%AC%AC21%E5%A4%A9%22%2C%22%E7%AC%AC30%E5%A4%A9%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%89%A9%E4%BD%99%E6%95%88%E6%9E%9C%EF%BC%88%25%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E5%BF%AB%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%202%20%E5%A4%A9%EF%BC%89%22%2C%22%E6%85%A2%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%207%20%E5%A4%A9%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%BF%AB%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%202%20%E5%A4%A9%EF%BC%89%22%2C%22data%22%3A%5B100%2C70.71%2C35.36%2C8.84%2C0.78%2C0.07%2C0.01%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E6%85%A2%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%207%20%E5%A4%A9%EF%BC%89%22%2C%22data%22%3A%5B100%2C90.57%2C74.3%2C50%2C25%2C12.5%2C5.13%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%9D%A1%E6%9B%B2%E7%BA%BF%EF%BC%8C%E8%A1%B0%E5%87%8F%E7%8E%87%E4%B8%8D%E5%90%8C%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AC%AC0%E5%A4%A9%22%2C%22%E7%AC%AC1%E5%A4%A9%22%2C%22%E7%AC%AC3%E5%A4%A9%22%2C%22%E7%AC%AC7%E5%A4%A9%22%2C%22%E7%AC%AC14%E5%A4%A9%22%2C%22%E7%AC%AC21%E5%A4%A9%22%2C%22%E7%AC%AC30%E5%A4%A9%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%89%A9%E4%BD%99%E6%95%88%E6%9E%9C%EF%BC%88%25%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E5%BF%AB%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%202%20%E5%A4%A9%EF%BC%89%22%2C%22%E6%85%A2%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%207%20%E5%A4%A9%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%BF%AB%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%202%20%E5%A4%A9%EF%BC%89%22%2C%22data%22%3A%5B100%2C70.71%2C35.36%2C8.84%2C0.78%2C0.07%2C0.01%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E6%85%A2%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%207%20%E5%A4%A9%EF%BC%89%22%2C%22data%22%3A%5B100%2C90.57%2C74.3%2C50%2C25%2C12.5%2C5.13%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E5%90%8C%E4%B8%80%E6%9D%A1%E6%9B%B2%E7%BA%BF%EF%BC%8C%E8%A1%B0%E5%87%8F%E7%8E%87%E4%B8%8D%E5%90%8C%22%7D%2C%22color%22%3A%5B%22%23dc2626%22%2C%22%232563eb%22%5D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E7%AC%AC0%E5%A4%A9%22%2C%22%E7%AC%AC1%E5%A4%A9%22%2C%22%E7%AC%AC3%E5%A4%A9%22%2C%22%E7%AC%AC7%E5%A4%A9%22%2C%22%E7%AC%AC14%E5%A4%A9%22%2C%22%E7%AC%AC21%E5%A4%A9%22%2C%22%E7%AC%AC30%E5%A4%A9%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%89%A9%E4%BD%99%E6%95%88%E6%9E%9C%EF%BC%88%25%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A80%2C%22bottom%22%3A60%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E5%BF%AB%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%202%20%E5%A4%A9%EF%BC%89%22%2C%22%E6%85%A2%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%207%20%E5%A4%A9%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%BF%AB%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%202%20%E5%A4%A9%EF%BC%89%22%2C%22data%22%3A%5B100%2C70.71%2C35.36%2C8.84%2C0.78%2C0.07%2C0.01%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%2C%7B%22name%22%3A%22%E6%85%A2%E8%A1%B0%EF%BC%88%E5%8D%8A%E8%A1%B0%E6%9C%9F%207%20%E5%A4%A9%EF%BC%89%22%2C%22data%22%3A%5B100%2C90.57%2C74.3%2C50%2C25%2C12.5%2C5.13%5D%2C%22type%22%3A%22line%22%2C%22smooth%22%3Atrue%2C%22connectNulls%22%3Atrue%7D%5D%7D&w=760&h=420" width="760" alt="adstock_two_half_lives"></a>

**The same 100 spent on the same day is down to 8.84% after seven days on the fast curve, and still holds 50% on the slow one.**

### Once the parameter is fixed, the accumulated number is fixed too

Take a channel spending 100 a day with a 7-day half-life, so 90.57% survives daily.

| Days elapsed | Today's spend, remaining | Plus the days before it | Total |
|---|---|---|---|
| 0 | 100.00 | — | 100.00 |
| 1 | 90.57 | 100.00 | 190.57 |
| 7 | 50.00 | the balance from the previous 7 days | 580.36 |
| 14 | 25.00 | the balance from the previous 14 days | 820.53 |

**That stack of numbers is the model's input variable.** It sits closer to "how much the ads really pushed this week's sales" than "how much did we spend this week," because it counts earlier weeks that have not faded.

### Why every channel gets its own curve

**Because media really do fade at different speeds.** Search ads are close to same-day: the user searches today, clicks today, buys today. TV and outdoor are different — two or three weeks can pass between seeing an ad and buying. So the standard approach is **one decay curve per channel, each with its own half-life**. One shared curve asserts all channels remember equally long.

**There is a second reason: channels cover for each other.** A user searches your brand name, which puts you on their mind, and two days later sees your short video ad, whose effect the earlier search props up. So the classic Adstock both **decays on its own** and **gets propped up by others** (channel order matters).

## Where the estimate breaks

### Decaying too fast undervalues slow channels

**A half-life estimated too short cuts off the effect that drags on.** Say a channel's real half-life is 21 days but the model estimates 3. The true accumulated value is then more than three times the model's, and the regression coefficient is pushed down to compensate — the same sales need a smaller slope.

**That channel's contribution ends up badly understated.** Overestimating does the opposite, inflating short-lived channels.

### The parameter is fitted, not measured

**Half-life is not observed. It is searched for.** Run the model with different candidates (say 1, 3, 7, 14 days) and pick the one with the best fit and no leftover autocorrelation in the residuals.

**Here is the trap: a better fit does not mean a better parameter.** Stretching the half-life a little often smooths the curve and flatters the fit metric while absorbing noise with signal. So the parameter usually gets a prior range, or a Bayesian treatment.

### The parameter and saturation cancel each other out

Look at [→ MMM contribution breakdown](../../8-analysis-toolbox/03-mmm-contribution/en.md): a saturation curve plus an Adstock curve, both devices for translating spend into effective input. Saturation handles **quantity** (the more you spend, the less each unit is worth); Adstock handles **time** (past effect fades).

**In practice they compensate for each other.** Estimate the half-life longer and the Adstock value grows, so the coefficient shrinks. Estimate the saturation point lower and the effective input shrinks too, so the coefficient shrinks again. **Move both parameters and the model still fits well, while "this channel's contribution" may have shifted 30%.** **You have to see how it was decomposed.**

### Cutting spend lingers longer than adding it

**When you stop, the accumulated effect does not zero out in a day.** You pulled the TV ads last week. Under Adstock, this week's sales still carry last week's residual warmth. Read the lift and you conclude "stopping changed nothing, the ads were useless."

**Experiments refuse to conclude before the decay has run its course.** That is why an incrementality test needs enough runway — not because the ad takes that long to work, but because **you have to wait for the residual to fade before you know what it contributed.**

## When Adstock is worth the trouble

**It is not a curve. It is a modeling step**, and whether to use it depends on whether your data has lag.

| Your situation | Use it? |
|---|---|
| Spend daily, buy the same day (search) | Worth using, but the half-life is short and the gain limited |
| Clear decision cycle (TV, outdoor, offline) | Required — without it the numbers are wrong |
| Spend once a week, weekly data | Use it, but daily data is steadier |
| Budget shifts repeatedly inside a one-month campaign cycle | Required — otherwise the shifts register as effects |

**There is a second test: how long is your history.** If your model covers 26 weeks of weekly data and the channel's real half-life is 8 weeks, the Adstock value gets dragged by history that has not faded. **When the history is too short, Adstock makes the model look more precise and less trustworthy at once.**

**Three things to hold onto.** Estimate each channel separately, read the parameter together with saturation, and match your history length to the half-life you estimate.

[→ MMM contribution breakdown](../../8-analysis-toolbox/03-mmm-contribution/en.md) · [→ Where effect hits the ceiling](../../8-analysis-toolbox/05-hill-saturation-curve/en.md)

**Data**: The charts use the general definition of adstock decay plus one worked example (80% surviving per day, curves at 2-day and 7-day half-lives, and the rolling accumulation table computed from r = 0.8 and r = 0.5^(1/7)). **Reproduce**: no single x-cmd command re-runs them. To use your own half-life, edit the series data array in the link's d= parameter so it follows r^t.
