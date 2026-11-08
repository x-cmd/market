DATA = {
    'id': 'x-market-8-analysis-toolbox-07-equal-marginal-returns-principle',
    'reference': 'docs/8-analysis-toolbox/07-equal-marginal-returns-principle/cn.md',
    'groups': [
        {
            'name_en': 'what the principle says',
            'name_cn': '等边际原则说了什么',
            'qa': [
                {
                    'id': 'the-principle-in-one-line',
                    'q_en': 'What does the equal marginal returns principle say?',
                    'q_cn': '等边际原则说了什么？',
                    'a_en': """
                        Under a fixed total budget, total return is maximised when every channel's marginal return is equal. Marginal return is what the last unit of money buys, not what the average unit bought. So if one channel still has a higher marginal return than another, moving money there raises the total. You keep moving until no move helps, and at that point the marginal returns are equal by construction.
                        """,
                    'a_cn': """
                        总量固定的时候，各渠道的边际回报相等，总回报最大。边际回报说的是最后一块钱能换回什么，不是平均一块钱换回什么。所以只要有一个渠道的边际比另一个高，把钱挪过去总回报就上升。一直挪到挪不动为止，那个点上各渠道的边际就相等了。
                        """,
                    'confidence': 10,
                },
                {
                    'id': 'not-the-same-as-roi-ranking',
                    'q_en': 'Is the equal marginal returns principle the same as ranking channels by ROI?',
                    'q_cn': '等边际原则跟按 ROI 排渠道排名是一回事吗？',
                    'a_en': """
                        No, and this is the point most often missed. ROI is an average: total return divided by total spend. It counts the return earned on all the money you have already put into that channel. The channel with the highest ROI is often the one you have already funded heavily, which is exactly the channel whose marginal return has already fallen. The money belongs in the channel you have not funded enough, and that channel often has a mediocre ROI. The chart of a worked example shows one channel earning 10 units on its first unit of spend and 1 unit on its tenth, so the total and marginal lines tell you very different stories.
                        """,
                    'a_cn': """
                        不是，这是最容易搞错的一点。ROI 是平均：总回报除以总花费。它把已经投进去的钱挣的回报也算进了分子。ROI 最高的那个渠道，往往恰恰是你已经投得最多的那个，也就是边际早就掉下来的那个。钱该去的地方是你还没投够的渠道，而那个渠道的 ROI 往往平平。一个算例里，同一条渠道第一个 1 万带回 10 万销售，第十个 1 万只带回 1 万，总回报和边际回报这两条线讲的是完全不同的故事。
                        """,
                    'confidence': 9,
                },
            ],
        },
        {
            'name_en': 'how the principle is derived',
            'name_cn': '它怎么推出来的',
            'qa': [
                {
                    'id': 'the-whole-argument',
                    'q_en': 'How does the principle follow from a single move?',
                    'q_cn': '这个原则是怎么推出来的？',
                    'a_en': """
                        From one observation: if a unit of money can be moved, move it to wherever it earns more. Suppose channel A has a marginal return of 3 and channel B has 5. Moving one unit from A to B adds 2 to the total. After the move A's marginal rises slightly, because it now has less spend and sits further left on its curve, and B's marginal falls slightly, because it now has more. Keep moving until the two are equal, and any further move raises one side by as much as it lowers the other. That is the whole derivation. There is no deeper mathematics, just the rule that you keep moving while there is room to move.
                        """,
                    'a_cn': """
                        靠一个想法：只要有一块钱可以挪，就挪到回报更高的那边。假设 A 渠道的边际是 3，B 渠道的边际是 5，把 1 万从 A 挪到 B，总回报增加 2 万。挪完之后 A 的边际升一点（它少投了，往曲线左边移，读数更高），B 的边际降一点（它多投了）。一直挪到两边相等，再挪任何一块钱都是这边涨多少那边就跌多少。推导到这里就完了，没有更深的数学，就是有余地就挪、挪到挪不动为止。
                        """,
                    'confidence': 9,
                },
                {
                    'id': 'two-conditions',
                    'q_en': 'What two conditions does the principle need?',
                    'q_cn': '这个原则需要哪两个条件？',
                    'a_en': """
                        A fixed total and independent channels. The total must be capped, otherwise the question is not how to split but how much to spend, and if the marginal return stays positive you would spend forever. Independence means that adding money to one channel does not change the effect of another. That second one is the easiest to miss. When brand keyword search and non-brand search compete for the same people, adding to one changes the other's marginal, and the equal-marginal reading stops holding.
                        """,
                    'a_cn': """
                        总量固定，各渠道互相独立。总量要封顶，不然问题就不是怎么分而是花多少，边际回报一直为正的话就会一直花下去。独立是指给一个渠道加钱不会改变另一个渠道的效果。第二条最容易漏：品牌词搜索和非品牌词搜索抢同一批人的时候，给一边加钱会改变另一边的边际，等边际那个解就不成立了。
                        """,
                    'confidence': 9,
                },
            ],
        },
        {
            'name_en': 'what an equal-marginal split looks like',
            'name_cn': '等边际长什么样',
            'qa': [
                {
                    'id': 'marginals-equal-spend-not',
                    'q_en': 'What does an equal-marginal allocation look like?',
                    'q_cn': '等边际的分配长什么样？',
                    'a_en': """
                        Every channel shows the same marginal return, but the budgets behind them differ. In a worked example with a total of one million across four channels, every channel ends up with a marginal return of 3.2 units per unit spent, yet the split is 42, 28, 19 and 11 units. Search has been funded to the point where another unit buys only 3.2, while out-of-home is still on the lower slope of its curve, so it needs less money to reach the same marginal. The ROI of these four channels can differ threefold and it changes nothing about the allocation.
                        """,
                    'a_cn': """
                        每个渠道的边际回报一样，但背后的花费差很多。一个 100 万分给四个渠道的算例里，四个渠道的边际回报都落在 3.2，但分到的钱是 42、28、19、11 万。搜索已经投到再加一块只赚回 3.2 的位置，户外还在曲线的前半段，所以它用更少的钱就达到了同一个边际。这四个渠道的 ROI 可以差三倍，但那不影响分配结果。
                        """,
                    'confidence': 9,
                },
            ],
        },
        {
            'name_en': 'when it does not hold',
            'name_cn': '它什么时候不靠谱',
            'qa': [
                {
                    'id': 'marginals-cannot-be-estimated',
                    'q_en': 'What if the marginal return cannot be estimated?',
                    'q_cn': '边际回报估不出来怎么办？',
                    'a_en': """
                        Then the principle cannot be applied as a calculation, only as a direction. The marginal return is the slope of a curve at one point, not the line between two points, so it has to come from splitting spend into bands and looking at the return of each band separately. Many teams hold a single number for a month, total spend and total sales, and dividing those gives an average ROI rather than a marginal. This is the most practical limitation of the whole approach: without banding, there is no marginal to equalise.
                        """,
                    'a_cn': """
                        那这个原则只能当方向用，不能当计算用。边际回报是曲线在某一点的斜率，不是两个点的连线，只能靠把花费分档、每档单独看回报来估。很多团队手里只有「这个月花了多少、带来多少销售」这一个总数，除出来的是平均 ROI，不是边际。这是整个办法最实际的限制：不分档，就算不出边际。
                        """,
                    'confidence': 9,
                },
                {
                    'id': 'hard-constraints',
                    'q_en': 'What happens when there are hard constraints?',
                    'q_cn': '有硬约束的时候会怎么样？',
                    'a_en': """
                        The equal-marginal solution may not exist. A contract that fixes the budget, inventory that only supports so much exposure, a team with no spare capacity, or a channel with brand restrictions all put a wall in front of the optimum. When a wall is there, the best allocation sits on the boundary of the constraint rather than at the point where marginals are level. The order of work matters: list the constraints first, then optimise, because doing it the other way round produces a number that cannot be used.
                        """,
                    'a_cn': """
                        等边际的解可能不存在。合同锁死了预算、库存只够投这么多、投放团队排期满了、某些渠道有品牌调性要求——这些都在最优解前面竖了墙。有墙的时候，最好的分配落在约束的边界上，而不是边际拉平的那个点上。所以顺序要紧：先列约束，再谈优化。反过来做，算出来的东西用不了。
                        """,
                    'confidence': 9,
                },
                {
                    'id': 'total-not-fixed',
                    'q_en': 'What if the budget is not capped?',
                    'q_cn': '总量不封顶的时候呢？',
                    'a_en': """
                        The question changes. If one more unit still earns 3.2, the answer is not how to split the total but how much to spend in total, and the condition to look for becomes a marginal return of zero rather than marginal returns being equal to each other. In practice budgets are usually capped, and the cap is usually imposed by the fact that returns turn negative before the money runs out: pushing ads harder can lower price, cannibalise organic traffic and annoy the marginal customer.
                        """,
                    'a_cn': """
                        问题就变了。如果再多花一块钱还能赚 3.2，那答案不是怎么分，而是总共该花多少，判据也从「彼此相等」变成「边际等于零」。现实里预算一般有上限，而且通常是回报先转负、钱还没花完就到了上限：广告推得太猛会压低价格、会挤占自然流量、会让边际客户反感。
                        """,
                    'confidence': 8,
                },
                {
                    'id': 'channels-interact',
                    'q_en': 'What if the channels affect each other?',
                    'q_cn': '渠道之间互相影响怎么办？',
                    'a_en': """
                        The net effect of a move is no longer the difference of the two marginals, and the numbers the principle produces have to be discounted. Brand and non-brand search compete for the same people, television can take volume away from search rather than add to it, and multi-touch attribution can count the same sale twice if the same customer meets several channels. The intuition still points the right way, but the arithmetic needs the interaction subtracted out before it can be trusted.
                        """,
                    'a_cn': """
                        挪一块钱的净效果就不再是两个边际的差，原则算出来的数得打折。品牌词搜索和非品牌词搜索抢同一批人，电视广告可能把搜索的量拿走而不是加上，自己做的多触点归因还可能把同一笔销售算两次。直觉还是指对方向，但算术得先把中间那块互动减掉才靠得住。
                        """,
                    'confidence': 8,
                },
            ],
        },
        {
            'name_en': 'how to use it',
            'name_cn': '怎么把它用起来',
            'qa': [
                {
                    'id': 'three-steps',
                    'q_en': 'How do you actually apply the principle?',
                    'q_cn': '这个原则具体怎么用？',
                    'a_en': """
                        Three steps, in this order. Estimate the marginal returns rather than the ROI, by banding spend. List the constraints, including which channels cannot move and which have caps. Then find the point where nothing can move: repeatedly shift a unit from the lower marginal to the higher one, updating the marginals as you go. This is a converging process rather than a formula, and most teams are in fact doing budget optimisation this way without calling it that. There is also a free check: recompute every marginal under the new allocation, and if they are still not level, the marginals were estimated wrong or a constraint was missed.
                        """,
                    'a_cn': """
                        三步，按这个顺序。先估边际而不是估 ROI，靠分档。再列约束，包括哪些渠道不能动、哪些有上限。然后找那个挪不动的点：反复把一块钱从边际低的挪到边际高的，边际变了就更新。这个过程是收敛的，不是一个公式，很多团队实际上就是这么在做预算优化，只不过没人这么叫。还有一条不花钱的检查：按新分配重算每个渠道的边际，如果还是拉不平，说明前面的边际估错了，或者有约束没列全。
                        """,
                    'confidence': 9,
                },
            ],
        },
    ],
}
