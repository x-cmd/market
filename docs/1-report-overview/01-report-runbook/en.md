# Eight steps turn a market question into a report you can defend

Eight steps. Each answers four questions: what happens here, who does it, what comes out, how you check it.

The flow is built for a human and an AI agent working side by side. The split is one line: **work with a defined input and a defined output goes to the agent; anything needing a human call stays with the human.**

An agent will compute a 4100% and a −63%, draw the charts, draft the paragraphs. It cannot make three decisions: what this round of analysis answers, which definition each number follows, whether the conclusion is safe to say out loud. Get those wrong and the polish downstream carries the error further out.

The four human decisions: set the question, draw the scope, settle the definition, sign off. The rest goes to the agent.

## Step 1: Write down the question

The trade word is **brief** — the short statement of what you want. One page, four lines. The human owns this step; an agent can break a vague prompt into candidate questions, but picking one is yours. Out: one sentence of question, one deliverable, one audience, one deadline. Check it by asking whether that sentence can be answered.

```
We need to answer ________;
the deliverable is ________ (one PPT slide? a document with charts? a table?);
for ________;
needed by ________.
```

A vague deliverable sends every later step back to the drawing board. "A market report" is not one; "one page that settles whether we enter this category" is.

## Step 2: Draw the boundary around what counts

The trade word is **scope** — the boundary of the counting. It turns "market" into something you can point at: which territory, which time window, whether you count yourself. The human sets the boundary; the agent looks up what falls inside it. Out: one line of scope plus the entities in play (which companies, categories, regions). Check it by running the definition, then changing it — if the numbers do not move, the scope line needs another look.

Three things scope definitions leave out most often: **whether you include yourself** (the denominator of a share moves the number a lot), **how you classify** (NACE codes, or your own categories), and **which year you stop at** (data lags).

## Step 3: Pick the one number that counts

The trade word is **source of truth** — the single place a number comes from. One metric, one authoritative source. Any number quoted elsewhere traces back to it. The agent finds candidates, the human picks. Out: one **metric card** per metric, defined in `spec/metric-cards.yml` — the machine-readable version an agent reads directly. Check it by running the card's command: it has to produce the number written there. If not, the card is wrong.

> The field most often left off a card is **caveats** — who the number covers, who it misses, from which year it stops being comparable to earlier ones.

## Step 4: Compute

The trade word is **compute**. Follow the formula on the card; do not invent one. The agent runs this: metric card plus raw series in, computed number plus the parameters used out. Check it against a small sample you can work out by hand, and give a range rather than a point wherever a range is meaningful.

The usual failure is not an arithmetic slip. It is computing a different thing: a share with the wrong denominator, nominal figures read as real, seasonally adjusted data read as raw.

## Step 5: Draw

The trade word is **visualize**. One chart per section, one point per chart. The agent runs this: the computed numbers plus the one thing the section has to show, in; one draw URL out — **the data lives inside the link**, so a human can open it and see every parameter, and an agent can change the numbers and redraw it. Open the URL and check the chart matches the text; swap a number and the chart moves.

> Three endpoints cover three jobs: `/draw/echarts` for data charts, `/draw/mindmap` for structure, `/draw/archmap` for architecture.
> **Structure charts only show things the business actually has** (a report outline, a value chain, an ad funnel), not the author's mind.

## Step 6: Write

The trade word is **narrative**. Each section gets a paragraph in plain language plus one judgement worth carrying away. The agent drafts, the human edits. Out: one paragraph plus a takeaway — the single line the reader keeps. Read it aloud to a colleague; if they cannot repeat it back, rewrite it.

> Three rules for the prose: open with the situation rather than a definition; translate jargon the moment it appears; and **do not teach people how to run a business** — stick to how the number was computed and how to read it.

## Step 7: Check

The trade word is **QA** — quality assurance. Ten checks before anything is filed.

1. Does every number say who measured it?
2. Does every share say what the denominator is?
3. Does every number carry the date it refers to?
4. Does the text say who is covered and who is missed?
5. Is it clear whether figures are nominal or real?
6. Where a range was called for, is there one?
7. Do the chart captions state the definition?
8. Are estimated numbers flagged as estimates?
9. Can the conclusion go straight into a meeting?
10. Can the data be run again from scratch?

The agent checks once, the human checks again, and both passes have to clear. Number 10 gets skipped most often, and it is the one that cannot be.

## Step 8: Ship

The trade word is **deliver**. Three items travel together, and the report is not credible without all three: the report, a data appendix (source, command and as-of date for every number), and the reproduction scripts (the metric cards and fetch commands in `spec/`). Hand the scripts to someone who was not involved. If they get the same numbers, the work holds. If not, what you shipped is paper.

---

## One run through, end to end

A fragment of a completed run, on e-commerce penetration in the EU, from the Eurostat enterprise ICT survey (`isoc_ec_evaln2`), published November 2025.

**Steps 1 and 2 · Brief and scope**

```
We need to answer: what is the EU "e-commerce share" exactly, and which definition do other people quote;
the deliverable is: a share chart that drops straight into a report, plus a paragraph I can read aloud to my boss;
for: the head of marketing;
needed by: this Friday.
```

Scope: EU 27 countries; NACE C-E industries (wholesale and retail, accommodation and food, transport); firms with 10+ employees; 2009–2025. **You are not included** — an industry aggregate, not one company.

**Step 3 · Source of truth**

```yaml
id: ecom_share_of_turnover
label: 网络销售占企业总营业额
value: 19.82          # 2024，欧盟整体
unit: "%"
denominator: 企业总营业额（雇员 10 人及以上，NACE C-E）
source:
  provider: Eurostat
  dataset: isoc_ec_evaln2
  series: A.GE10.C-E.E_AWSVAL.PC_ETURN.EU27_2020
  command: x dbnomics data Eurostat/isoc_ec_evaln2/A.GE10.C-E.E_AWSVAL.PC_ETURN.EU27_2020
caveats:
  - 只覆盖雇员 10 人及以上的企业，小店和个体户不在里面
  - 只覆盖 NACE C-E 行业
  - 2025 的调查覆盖范围有变，跟 2024 不能直接比
```

**Step 5 · Draw**

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E6%AC%A7%E7%9B%9F%202024%EF%BC%9A%E5%90%8C%E4%B8%80%E4%B8%AA%E5%88%86%E6%AF%8D%EF%BC%8C%E6%8D%A2%E4%B8%AA%E5%88%86%E5%AD%90%EF%BC%8C%E5%B7%AE%E4%B8%80%E5%80%8D%22%7D%2C%22color%22%3A%5B%22%232563eb%22%2C%22%23dc2626%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A30%2C%22top%22%3A60%2C%22bottom%22%3A70%7D%2C%22legend%22%3A%7B%22data%22%3A%5B%22%E5%85%A8%E9%83%A8%E7%BD%91%E7%BB%9C%E9%94%80%E5%94%AE%22%2C%22%E5%85%B6%E4%B8%AD%E5%8D%96%E7%BB%99%E6%B6%88%E8%B4%B9%E8%80%85%EF%BC%88B2C%EF%BC%89%22%5D%2C%22top%22%3A30%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E5%B8%8C%E8%85%8A%22%2C%22%E6%B3%A2%E9%BB%91%22%2C%22%E5%85%8B%E7%BD%97%E5%9C%B0%E4%BA%9A%22%2C%22%E4%BF%9D%E5%8A%A0%E5%88%A9%E4%BA%9A%22%2C%22%E5%A1%9E%E6%B5%A6%E8%B7%AF%E6%96%AF%22%2C%22%E7%AB%8B%E9%99%B6%E5%AE%9B%22%2C%22%E6%96%AF%E6%B4%9B%E4%BC%90%E5%85%8B%22%2C%22%E8%A5%BF%E7%8F%AD%E7%89%99%22%2C%22%E7%88%B1%E5%B0%94%E5%85%B0%22%2C%22Hungary%22%5D%2C%22axisLabel%22%3A%7B%22interval%22%3A0%2C%22rotate%22%3A30%2C%22fontSize%22%3A11%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22%E5%8D%A0%E4%BC%81%E4%B8%9A%E6%80%BB%E8%90%A5%E4%B8%9A%E9%A2%9D%EF%BC%88%25%EF%BC%89%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%25%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E5%85%A8%E9%83%A8%E7%BD%91%E7%BB%9C%E9%94%80%E5%94%AE%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B81.0%2C68.8%2C46.9%2C36.7%2C34.8%2C33.0%2C32.3%2C31.8%2C31.2%2C30.9%5D%7D%2C%7B%22name%22%3A%22%E5%85%B6%E4%B8%AD%E5%8D%96%E7%BB%99%E6%B6%88%E8%B4%B9%E8%80%85%EF%BC%88B2C%EF%BC%89%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B42.2%2C40.5%2C10.6%2C6.9%2C31.6%2C15.2%2C7.3%2C18.4%2C18.5%2C0.9%5D%7D%5D%7D&w=760&h=420
```

The data is in the link: open it and every parameter shows; swap in your own numbers and the chart redraws itself. Two bars per country, ten countries — total online sales left, consumer-facing sales right. Greece 81% against 42%, Hungary 31% against 0.9%.

**Step 6 · Write (the takeaway for this section)**

> The same "e-commerce share" is 19.82% for the EU as a whole in 2024; counting only sales to consumers it is 8.49%. Nobody is wrong — the numerator carries B2B. Hungary is the extreme case: 30.85% of turnover comes from online sales, but only 0.92% goes to consumers, the rest almost entirely wholesale flowing to retailers. **So "e-commerce share is 31% in this country" does not mean "three in ten people in this country shop online."**

**Steps 7 and 8 · QA and ship**

Eight of the ten checks passed. Check 4 needs the note spelled out: firms with under 10 employees are not in the survey. Check 9 passed — the paragraph reads aloud to the boss as it stands. What ships: the report, the data appendix, and one reproduction command (the `x dbnomics data …` line above).

---

## The one you rerun every week

**Same shape, new numbers.** The weekly deliverable for the person on the execution desk, and a reusable template for consulting clients.

| What ships | What it looks like | Who does it |
|---|---|---|
| 3 charts | share chart, trend chart, price-band chart | agent |
| 1 table | this week's key numbers and the change from last week | agent |
| 5 sentences | five takeaways, one number each | agent drafts, human edits |
| 1 command | how to rerun it next week | agent |

Each chart's data and definition live on its own page. **The weekly rerun has to be the same set of charts** — a fixed shape lets a reader watch the change instead of re-reading it.

## Three things to hand an agent

1. **What this step is for** (one sentence; do not make it guess)
2. **The metric card** (the one in `spec/metric-cards.yml`; do not let it hunt for numbers on its own)
3. **How to check the result** (one sentence; better still, something a machine can run)

Example:

```
按 spec/metric-cards.yml 里 ecom_share_of_turnover 这张卡取数，
算出 2024 年欧盟整体的网络销售占营业额比重，
和只算 B2C 的那个数并排画成一张双柱图，
用 /draw/echarts，w=760 h=420，alt 用 eu2024_two_numerators。
画完把图里两个数念给我听，对不上卡上的值就别交。
```

The last line is the point: **every job you hand an agent has to carry an acceptance test**, otherwise what comes back is a deliverable that looks right rather than one that is.

[→ What a market share denominator really is](../02-market-share-chart/en.md) · [→ How a category sorts by price, and how hard it discounts](../04-price-band-chart/en.md)

**Data**: Eurostat enterprise ICT survey `isoc_ec_evaln2`, published 2025-11; EU e-commerce share of turnover 19.82% (2024, EU27, NACE C-E, firms with 10+ employees), consumer-facing online sales 8.49%, Hungary 30.85% total and 0.92% B2C.

**Reproduce**: `x dbnomics data Eurostat/isoc_ec_evaln2/A.GE10.C-E.E_AWSVAL.PC_ETURN.EU27_2020` and `x dbnomics data Eurostat/isoc_ec_evaln2/A.GE10.C-E.E_AWSVAL_B2C.PC_ETURN.EU27_2020`
