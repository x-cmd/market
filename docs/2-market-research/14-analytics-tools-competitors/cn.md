# 网站分析开源项目里，umami 的 fork 数排第一，star 排第二

你要给团队选一个网站分析。候选名单不难列：umami、PostHog、Matomo、Plausible、Fathom、GoatCounter、Countly、Ackee、Pirsch。

挑的时候容易只看一个数——GitHub star。star 是「收藏」，说的人多不多。**但对自托管这件事来说，fork 比 star 更说明问题**：收藏是「以后可能用」，fork 是「我现在就在改」。

把这九个项目的两个数摆在一起，umami 的位置立刻不一样。

## 九个对得上号的

| 项目 | 定位 | 许可 | star | fork | 建库 | 最近推送 | 定价 |
|---|---|---|---:|---:|---|---|---|
| `posthog` | :hedgehog: PostHog is the leading platform… | NOASSERTION | 40,699 | 3,605 | 2020-01-23 | 2026-11-08 | 未抓到（定价页 JS 渲染） |
| `umami` | Umami is a privacy-first web and product a… | MIT | 39,983 | 8,501 | 2020-07-17 | 2026-11-07 | $0 / $20 / $200 每月（10 万 / 100 万 / 1000 万 events） |
| `analytics` | Open source, privacy-first web analytics. … | AGPL-3.0 | 29,794 | 1,931 | 2018-12-04 | 2026-11-08 | 未抓到（定价页 JS 渲染） |
| `matomo` | Empowering People Ethically 🚀 — Matomo is … | GPL-3.0 | 22,012 | 2,928 | 2011-03-30 | 2026-11-08 | 免费自托管；云端从 €230 每月起 |
| `fathom` | Fathom Lite. Simple, privacy-focused websi… | MIT | 8,034 | 388 | 2016-11-19 | 2026-03-18 | $15 / $25 / $45 / $60 / $100 每月（10 万～200 万 pageviews） |
| `goatcounter` | Easy web analytics. No tracking of persona… | NOASSERTION | 6,150 | 286 | 2019-05-28 | 2026-09-27 | 未抓到（站点未返回可解析内容） |
| `countly-server` | Countly is a privacy-first, AI-powered ana… | NOASSERTION | 5,926 | 985 | 2012-05-28 | 2026-11-06 | 从 $175 每月起（Flex），另有企业自托管版 |
| `Ackee` | Self-hosted, Node.js based analytics tool … | MIT | 4,722 | 388 | 2014-04-16 | 2026-10-23 | 未抓到（站点未返回可解析内容） |
| `pirsch` | Pirsch is a drop-in, server-side, no-cooki… | AGPL-3.0 | 1,033 | 51 | 2020-06-20 | 2026-11-06 | $6 / $12 每月（1 万 / 更多 events） |

**抓取时间**：2026 年 11 月 8 日，取自 GitHub 公开 API（`api.github.com/repos/<owner>/<repo>`）。star 与 fork 是抓取当时的快照，每天都在变。

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BD%91%E7%AB%99%E5%88%86%E6%9E%90%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BC%9AGitHub%20star%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A190%2C%22right%22%3A70%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22star%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22pirsch%22%2C%22Ackee%22%2C%22countly-server%22%2C%22goatcounter%22%2C%22fathom%22%2C%22matomo%22%2C%22analytics%22%2C%22umami%22%2C%22posthog%22%5D%2C%22axisLabel%22%3A%7B%22fontSize%22%3A11%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B1033%2C4722%2C5926%2C6150%2C8034%2C22012%2C29794%2C39983%2C40699%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22itemStyle%22%3A%7B%22color%22%3A%5B%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%232563eb%22%2C%22%23cbd5e1%22%5D%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BD%91%E7%AB%99%E5%88%86%E6%9E%90%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BC%9AGitHub%20star%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A190%2C%22right%22%3A70%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22star%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22pirsch%22%2C%22Ackee%22%2C%22countly-server%22%2C%22goatcounter%22%2C%22fathom%22%2C%22matomo%22%2C%22analytics%22%2C%22umami%22%2C%22posthog%22%5D%2C%22axisLabel%22%3A%7B%22fontSize%22%3A11%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B1033%2C4722%2C5926%2C6150%2C8034%2C22012%2C29794%2C39983%2C40699%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22itemStyle%22%3A%7B%22color%22%3A%5B%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%232563eb%22%2C%22%23cbd5e1%22%5D%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22%E7%BD%91%E7%AB%99%E5%88%86%E6%9E%90%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BC%9AGitHub%20star%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A190%2C%22right%22%3A70%2C%22top%22%3A60%2C%22bottom%22%3A50%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22star%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22pirsch%22%2C%22Ackee%22%2C%22countly-server%22%2C%22goatcounter%22%2C%22fathom%22%2C%22matomo%22%2C%22analytics%22%2C%22umami%22%2C%22posthog%22%5D%2C%22axisLabel%22%3A%7B%22fontSize%22%3A11%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22axis%22%2C%22axisPointer%22%3A%7B%22type%22%3A%22shadow%22%7D%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22bar%22%2C%22data%22%3A%5B1033%2C4722%2C5926%2C6150%2C8034%2C22012%2C29794%2C39983%2C40699%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22right%22%2C%22formatter%22%3A%22%7Bc%7D%22%7D%2C%22itemStyle%22%3A%7B%22color%22%3A%5B%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%23cbd5e1%22%2C%22%232563eb%22%2C%22%23cbd5e1%22%5D%7D%7D%5D%7D&w=760&h=420" width="760" alt="gh_stars"></a>

star 排第二的是 umami，39,983 个，落后 PostHog 的 40,699 不到 **七百个**。这个差距小到可以说「同一梯队」。

## fork 是另一样东西

```text
https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22star%20%E6%98%AF%20star%EF%BC%8Cfork%20%E6%98%AF%E5%8F%A6%E4%B8%80%E6%A0%B7%E4%B8%9C%E8%A5%BF%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22star%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22fork%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A18%2C%22data%22%3A%5B%7B%22value%22%3A%5B40699%2C3605%5D%2C%22name%22%3A%22posthog%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B39983%2C8501%5D%2C%22name%22%3A%22umami%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%2C%7B%22value%22%3A%5B29794%2C1931%5D%2C%22name%22%3A%22analytics%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B22012%2C2928%5D%2C%22name%22%3A%22matomo%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B8034%2C388%5D%2C%22name%22%3A%22fathom%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B6150%2C286%5D%2C%22name%22%3A%22goatcounter%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B5926%2C985%5D%2C%22name%22%3A%22countly-server%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B4722%2C388%5D%2C%22name%22%3A%22Ackee%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B1033%2C51%5D%2C%22name%22%3A%22pirsch%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=420
```

<a href="https://x-cmd.com/draw/explore/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22star%20%E6%98%AF%20star%EF%BC%8Cfork%20%E6%98%AF%E5%8F%A6%E4%B8%80%E6%A0%B7%E4%B8%9C%E8%A5%BF%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22star%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22fork%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A18%2C%22data%22%3A%5B%7B%22value%22%3A%5B40699%2C3605%5D%2C%22name%22%3A%22posthog%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B39983%2C8501%5D%2C%22name%22%3A%22umami%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%2C%7B%22value%22%3A%5B29794%2C1931%5D%2C%22name%22%3A%22analytics%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B22012%2C2928%5D%2C%22name%22%3A%22matomo%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B8034%2C388%5D%2C%22name%22%3A%22fathom%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B6150%2C286%5D%2C%22name%22%3A%22goatcounter%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B5926%2C985%5D%2C%22name%22%3A%22countly-server%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B4722%2C388%5D%2C%22name%22%3A%22Ackee%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B1033%2C51%5D%2C%22name%22%3A%22pirsch%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=420"><img src="https://x-cmd.com/draw/echarts?d=%7B%22title%22%3A%7B%22text%22%3A%22star%20%E6%98%AF%20star%EF%BC%8Cfork%20%E6%98%AF%E5%8F%A6%E4%B8%80%E6%A0%B7%E4%B8%9C%E8%A5%BF%22%7D%2C%22color%22%3A%5B%22%232563eb%22%5D%2C%22grid%22%3A%7B%22left%22%3A80%2C%22right%22%3A40%2C%22top%22%3A60%2C%22bottom%22%3A60%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22star%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%2C%22name%22%3A%22fork%22%2C%22axisLabel%22%3A%7B%22formatter%22%3A%22%7Bvalue%7D%22%7D%7D%2C%22tooltip%22%3A%7B%22trigger%22%3A%22item%22%2C%22formatter%22%3A%22%7Bb%7D%22%7D%2C%22series%22%3A%5B%7B%22type%22%3A%22scatter%22%2C%22symbolSize%22%3A18%2C%22data%22%3A%5B%7B%22value%22%3A%5B40699%2C3605%5D%2C%22name%22%3A%22posthog%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B39983%2C8501%5D%2C%22name%22%3A%22umami%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%23dc2626%22%7D%7D%2C%7B%22value%22%3A%5B29794%2C1931%5D%2C%22name%22%3A%22analytics%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B22012%2C2928%5D%2C%22name%22%3A%22matomo%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B8034%2C388%5D%2C%22name%22%3A%22fathom%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B6150%2C286%5D%2C%22name%22%3A%22goatcounter%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B5926%2C985%5D%2C%22name%22%3A%22countly-server%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B4722%2C388%5D%2C%22name%22%3A%22Ackee%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%2C%7B%22value%22%3A%5B1033%2C51%5D%2C%22name%22%3A%22pirsch%22%2C%22itemStyle%22%3A%7B%22color%22%3A%22%2394a3b8%22%7D%7D%5D%2C%22label%22%3A%7B%22show%22%3Atrue%2C%22position%22%3A%22top%22%2C%22formatter%22%3A%22%7Bb%7D%22%2C%22fontSize%22%3A10%7D%7D%5D%7D&w=760&h=420" width="760" alt="gh_forks"></a>

umami 的 fork 是 **8,501**。第二名 PostHog 3,605，第二是它的 **2.4 倍**；比排第四的 Matomo（2,928）高近三倍；比排在最后的 Pirsch（51）高了一百六十多倍。

star 排第二、fork 排第一，这个组合的意思是：**用的人多，真的动手改的人也多。** 这是自托管选型里最实在的一个信号——你迟早要改点东西（接自己的事件、改看板、加一个内部指标），改的人多，踩过的坑就少。

## 许可那一格

umami 是 MIT，star 39,983；Plausible 是 AGPL-3.0，star 29,794；Matomo 是 GPL-3.0，star 22,012。**star 数最高的 MIT 许可项目，就是 umami**——如果你公司法务对 AGPL 敏感，这一格直接决定选谁。

## 价格：九家里查到五家

| 项目 | 定价 | 怎么查到的 |
|---|---|---|
| umami | $0 / $20 / $200 每月（10 万 / 100 万 / 1000 万 events） | 定价页正文 |
| Fathom | $15 / $25 / $45 / $60 / $100 每月（10 万～200 万 pageviews） | 定价页正文 |
| Pirsch | $6 / $12 每月（1 万 / 更多 events） | 定价页正文 |
| Countly | 从 $175 每月起（Flex），另有企业自托管版 | 定价页正文 |
| Matomo | 免费自托管；云端从 €230 每月起 | 定价页正文 |
| Plausible | — | 定价页是 JS 渲染，没抓到 |
| PostHog | — | 定价页是 JS 渲染，没抓到 |
| GoatCounter | — | 站点没返回可解析内容 |
| Ackee | — | 站点没返回可解析内容 |

**四家留空，不填推算值。** 定价这件事本身有可比性陷阱：umami 按 events 计费，Fathom 按 pageviews 计费，Countly 按 Flex 席位计费。「$20」和「$20」不是一个东西。所以就算都抓到了，还得先对齐计量单位再比。

抓定价页这件事还暴露了一个差别：有些站的价格写在 HTML 里（`curl` 加个浏览器 UA 就能拿到），有些是 JS 渲染的（拿不到，得靠浏览器）。**能不能被脚本读到，本身就是自托管方案的一个隐性成本。**

## 结论

选网站分析的自托管方案时，star 看热度，**fork 看有多少人真的在改**。umami 是这两样里唯一双排第一的（fork 第一，MIT 许可里 star 第一），star 第二但和第一只差七百。

价格那一栏，九家里四家抓不到——不是数据不存在，是抓取方式不对。这件事要写进条目里，别装作查过。

**数据**：GitHub 公开 API，2026-11-08 抓取；定价为各家官网定价页，2026-11-08 抓取。**复现**：`curl -s -H "User-Agent: <you>" https://api.github.com/repos/umami-software/umami`
