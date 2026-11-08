DATA = {
    'id': 'x-market-8-analysis-toolbox-04-adstock-decay',
    'reference': 'docs/8-analysis-toolbox/04-adstock-decay/cn.md',
    'groups': [
        {
            'name_en': 'what adstock does',
            'name_cn': 'Adstock 在做什么',
            'qa': [
                {
                    'id': 'what-adstock-does',
                    'q_en': 'What does adstock actually do?',
                    'q_cn': 'Adstock 到底在做什么？',
                    'a_en': """
                        It accumulates past advertising spend into a running stock of effect, discounting it day by day along a decay curve. Each day's spend enters the pool and the pool loses a fixed fraction every day, so what the model sees today is not today's spend but the sum of every past day's spend and whatever effect remains of it. This is the step that keeps a model from crediting last week's money with this week's sales.
                        """,
                    'a_cn': """
                        它把过去的投放按一条衰减曲线累积成一个滚动的效果存量。每天的花费进池子，池子每天倒掉固定的一个比例，所以模型今天看到的不是今天的花费，而是过去每一天的花费各自还剩多少效果、堆在一起的结果。这一步是为了防止模型把上周的钱算到本周的销售头上。
                        """,
                    'confidence': 10,
                },
                {
                    'id': 'why-the-step-matters',
                    'q_en': 'What goes wrong if a model skips adstock?',
                    'q_cn': '模型里跳过 Adstock 会出什么问题？',
                    'a_en': """
                        The time alignment breaks. Pairing this week's spend with this week's sales makes the model credit last week's money with this week's sales, because the effect of an ad arrives after the spend. The coefficients come out wrong because the channels are not lined up against the outcome they actually cause. The damage is not noise, it is a systematic misattribution of one period's effect to another.
                        """,
                    'a_cn': """
                        时点对不上。拿本周的花费配本周的销售，模型就会把上周的钱算成这周的功劳，因为广告的效果是花在之后才到的。回归系数会错，因为渠道没有被摆到它真正造成的结果那一行上。这个错不是噪声，是一个周期的效果被系统性地记到另一个周期头上。
                        """,
                    'confidence': 9,
                },
            ],
        },
        {
            'name_en': 'the geometry of the decay',
            'name_cn': '衰减的几何形状',
            'qa': [
                {
                    'id': 'what-the-curve-looks-like',
                    'q_en': 'What shape does the adstock decay curve take?',
                    'q_cn': 'Adstock 衰减曲线是什么形状？',
                    'a_en': """
                        A geometric decline: a fixed discount rate multiplied in every day. With a rate of 0.7, a single day's spend retains 100% on the day it runs, 70% the next day, 49% the day after, and 8.2% by the seventh day. The curve is the same shape for every channel; what differs is the rate, which sets both how fast it falls and how long the tail runs.
                        """,
                    'a_cn': """
                        一条指数下降的曲线：每天乘一个固定的折扣率。折扣率 0.7 时，一次投放当天留 100%，第二天 70%，第三天 49%，到第七天还剩 8.2%。所有渠道是同一个形状，差的是折扣率，而折扣率同时定下了它掉得多快和尾巴拖多长。
                        """,
                    'confidence': 10,
                },
                {
                    'id': 'how-much-does-a-tail-hold-up',
                    'q_en': 'How much can a long decay tail inflate a small spend?',
                    'q_cn': '一条长尾巴能把一笔小钱撑大多少？',
                    'a_en': """
                        A lot. With a discount rate of 0.3, one day's spend carries a total effect of roughly 3.3 times that day's value. With a rate of 0.9, roughly 10 times. So the tail can make a small spend look like a large effect. This is not a distortion, it is what this does, but you have to know that the number you are deciding on has been inflated by its tail.
                        """,
                    'a_cn': """
                        撑得很多。折扣率 0.3 时，一次投放的总效果大约是当天价值的 3.3 倍；折扣率 0.9 时大约是 10 倍。所以一条长尾巴能把一笔小钱撑成一个看起来很大的效果。这不是失真，这件事本来就是这样，但你得知道你要拿它做决定的那个数，被它的尾巴撑大过。
                        """,
                    'confidence': 9,
                },
                {
                    'id': 'is-the-discount-rate-estimated',
                    'q_en': 'Is the discount rate estimated from the data or chosen in advance?',
                    'q_cn': '折扣率是数据估出来的，还是事先定好的？',
                    'a_en': """
                        Chosen in advance. This is the sharpest difference between adstock and the regression coefficients around it. The coefficients are read out of the data, while the discount rate is put in before the model runs. The common practice is to fix a rate per channel, such as 0.3 for search, 0.7 for social and 0.9 for television, because channels really do respond at different speeds. But fixing it also writes the answer in: a model that reports a large contribution for television may only be reporting that television's tail is long.
                        """,
                    'a_cn': """
                        事先定好的。这是 Adstock 和它周围那些回归系数最尖锐的区别。系数是从数据里读出来的，折扣率是模型跑之前就放进去的。常见做法是给每个渠道定一个固定的率，比如搜索 0.3、社交 0.7、电视 0.9，因为渠道的见效速度确实不一样。但这么定也等于把答案写了进去：模型说电视广告贡献大，很可能只是在说电视的尾巴长。
                        """,
                    'confidence': 9,
                },
            ],
        },
        {
            'name_en': 'when it misleads',
            'name_cn': '它什么时候不靠谱',
            'qa': [
                {
                    'id': 'decay-too-fast-undervalues-long-tail',
                    'q_en': 'What happens when the decay is set too fast?',
                    'q_cn': '衰减定得太快会怎么样？',
                    'a_en': """
                        Long-tail channels get undervalued, and the error points in the direction that leads to a bad decision. A fast rate wipes out television's effect before the people who saw it go shopping, so the model credits those sales to something else, usually organic search or direct visits. You then cut the channel that was quietly working. Google's 2011 geo experiment showed the same effect in the field: after the test group's spend returned to its pre-test level, incremental sales kept rising before they faded. The test period has to outlast the whole response lag, and the same is true of the tail you assign to a channel.
                        """,
                    'a_cn': """
                        长尾渠道被低估，而这个错正好指向一个坏决定。折扣率太快，电视广告的效果在那些看到它的人还没出门买东西之前就被抹掉了，于是那部分销售被记到别的东西名下，多半是自然搜索或直接访问。然后你就会砍掉那个在悄悄起作用的渠道。Google 2011 年那次 geo 实验在实地看到的是同一件事：实验组的花费回到前测水平之后，增量销售还在继续往上走，然后才慢慢消下去。测试期必须长出整个响应滞后期，给你渠道定的尾巴也一样。
                        """,
                    'confidence': 9,
                },
                {
                    'id': 'exponential-may-be-the-wrong-shape',
                    'q_en': 'What if the real decay curve is not exponential?',
                    'q_cn': '真实的衰减曲线不是指数形状怎么办？',
                    'a_en': """
                        Then the shape is wrong and one exponential curve will misprice every channel using it. Some real curves fall fast for the first two days and then slowly, because part of the audience buys on impulse and part takes time to decide. Worse, channels have different shapes, so giving them all one exponential form misprices search and television in opposite directions. A common workaround is to run each channel with one fast and one slow curve and take the number in between, which is an admission that the shape is unknown but known to lie between the two.
                        """,
                    'a_cn': """
                        那形状就错了，一条指数曲线会把所有用它算的渠道都算错。有些真实的曲线是头两天掉得快、之后掉得慢，因为一部分受众是冲动买、一部分要慢慢决定。更麻烦的是不同渠道的形状本来就不同，给它们套同一条指数曲线，会把搜索和电视往相反的方向算错。常见的折中办法是给每个渠道跑一条快曲线和一条慢曲线，取中间那个数——这其实是在承认形状不知道，只知道落在快慢之间。
                        """,
                    'confidence': 8,
                },
                {
                    'id': 'coefficients-are-not-comparable',
                    'q_en': 'Why can you not read the regression coefficient directly once adstock is in the model?',
                    'q_cn': '加了 Adstock 之后为什么不能直接读回归系数？',
                    'a_en': """
                        Because the coefficient multiplies the accumulated stock, not the original spend. Spend might range from zero to 100,000 while the accumulated stock ranges to two million, so the same coefficient produces a number twenty times larger. The model is not wrong, but the units changed. When you read an MMM output, look at the absolute contributions it produces rather than at the coefficient next to a per-unit label.
                        """,
                    'a_cn': """
                        因为系数乘的是累积后的存量，不是原始花费。花费可能在 0 到 10 万之间，累积后的存量能到 200 万，同一个系数乘出来的数就差 20 倍。模型没错，是单位变了。所以看 MMM 的产出，别盯着系数和它旁边的单位标签，要看它拆出来的绝对贡献。
                        """,
                    'confidence': 8,
                },
                {
                    'id': 'measuring-the-tail-without-a-model',
                    'q_en': 'Is there a way to measure a channel’s tail without building a model?',
                    'q_cn': '有没有不建模就能量出效果期有多长的办法？',
                    'a_en': """
                        Yes. Cut the spend on one day by half and watch what happens to sales over the following weeks. A fast drop means the decay is fast, a slow fade means the tail is long. This needs no regression and it is more reliable than the discount rate you assumed inside a model, so it is a good way to check the assumption you are about to bake in.
                        """,
                    'a_cn': """
                        有。把某天的花费砍掉一半，看接下来几周的销售怎么变。掉得快说明衰减快，慢慢消说明尾巴长。这不需要回归，而且比你在模型里假定的折扣率可靠，所以是检验那个假设的好办法——在你把它烤进模型之前先验一遍。
                        """,
                    'confidence': 9,
                },
            ],
        },
    ],
}
