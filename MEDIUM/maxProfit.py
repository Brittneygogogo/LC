'''
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。（只能買賣一次）

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0
不用dp 最小值是是min
'''
from typing import List


def maxProfit(prices):
    inf = int(1e9)
    minprice = float('inf')
    maxprofit = 0
    for price in prices:
        maxprofit = max(price - minprice, maxprofit)
        minprice = min(price, minprice)
    return maxprofit

'''
尽可能地完成更多的交易（可多次买卖一支股票）
no fee
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''
# 卖出有利可图
def maxrofit2(stocks):
        if not stocks: return 0
        ans = 0
        for i in range(1, len(stocks)):
            if (stocks[i] > stocks[i-1]):
                ans += (stocks[i] - stocks[i-1])
        return ans

'''
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
由于全部交易结束后，持有股票的收益一定低于不持有股票的收益，因此这时候 dp[n−1][0] 收益必然是大于 dp[n−1][1] 最后的答案即为 dp[n−1][0]


'''
def maxProfit_k_inf(prices: List[int]) -> int:
    n = len(prices)
    dp_i_0, dp_i_1 = 0, float('-inf')
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i])
    return dp_i_0


'''
手續費
'''
def maxProfit_with_fee(prices: List[int], fee: int) -> int:
    n = len(prices)
    dp_i_0, dp_i_1 = 0, float('-inf')
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i] - fee)
    return dp_i_0

'''
手續費滾動數組
sell表示第i天交易完后手里没有股票的最大利润
buy 表示第i天交易完后手里持有一支股票的最大利润（i 从 0 开始）。

'''
# class Solution:
#     def maxProfit3(self, prices, fee: int) -> int:
#         n = len(prices)
#         sell, buy = 0, -prices[0]
#         for i in range(1, n):
#             sell, buy = max(sell, buy + prices[i] - fee), max(buy, sell - prices[i])
#         return sell

'''
手續費貪心
方法一中，我们将手续费放在卖出时进行计算。如果我们换一个角度考虑，将手续费放在买入时进行计算，那么就可以得到一种基于贪心的方法。
我们用 buy 表示在最大化收益的前提下，如果我们手上拥有一支股票，那么它的最低买入价格是多少。在初始时，buy 的值为 prices[0] 加上手续费 fee。那么当我们遍历到第 i~(i>0) 天时：
如果当前的股票价格 prices[i] 加上手续费 fee 小于 buy，那么与其使用 buy 的价格购买股票，我们不如以prices[i]+fee 的价格购买股票，因此我们将 buy 更新为 prices[i]+fee
如果当前的股票价格 prices[i] 大于 buy，那么我们直接卖出股票并且获得 prices[i]−buy 的收益。
但实际上，我们此时卖出股票可能并不是全局最优的（例如下一天股票价格继续上升），因此我们可以提供一个反悔操作，看成当前手上拥有一支买入价格为 prices[i] 的股票，将 buy 更新为 prices[i]。
这样一来，如果下一天股票价格继续上升，我们会获得 prices[i+1]−prices[i] 的收益，加上这一天prices[i]−buy 的收益，恰好就等于在这一天不进行任何操作，而在下一天卖出股票的收益；
对于其余的情况，prices[i] 落在区间 [buy−fee,buy] 内，它的价格没有低到我们放弃手上的股票去选择它，也没有高到我们可以通过卖出获得收益，因此我们不进行任何操作。
上面的贪心思想可以浓缩成一句话，即当我们卖出一支股票时，我们就立即获得了以相同价格并且免除手续费买入一支股票的权利。在遍历完整个数组 prices 之后之后，我们就得到了最大的总收益。

'''
# class Solution:
#     def maxProfit3(self, prices, fee: int) -> int:
#         n = len(prices)
#         buy = prices[0] + fee
#         profit = 0
#         for i in range(1, n):
#             if prices[i] + fee < buy:
#                 buy = prices[i] + fee
#             elif prices[i] > buy:
#                 profit += prices[i] - buy
#                 buy = prices[i]
#         return profit

'''
冷冻期
冷冻期为 1 天
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
'''

def maxProfit_with_cool(prices: List[int]) -> int:
    n = len(prices)
    dp_i_0, dp_i_1, dp_pre_0 = 0, float('-inf'), 0
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
        dp_pre_0 = temp
    return dp_i_0




# k 无限制，包含手续费和冷冻期
def maxProfit_k_inf_fee_cooldown(prices: List[int], cooldown: int, fee: int) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n):
        if i - 1 == -1:
            # base case 1
            dp[i][0] = 0
            dp[i][1] = -prices[i] - fee
            continue

        # 包含 cooldown 的 base case
        if i - cooldown - 1 < 0:
            # base case 2
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # 别忘了减 fee
            dp[i][1] = max(dp[i - 1][1], -prices[i] - fee)
            continue
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        # 同时考虑 cooldown 和 fee
        dp[i][1] = max(dp[i - 1][1], dp[i - cooldown - 1][0] - prices[i] - fee)
    return dp[n - 1][0]





'''

由于我们最多可以完成2笔交易，因此在任意一天结束之后，我们会处于以下五个状态中的一种：

未进行过任何操作；

只进行过一次买操作；

进行了一次买操作和一次卖操作，即完成了一笔交易；

在完成了一笔交易的前提下，进行了第二次买操作；

完成了全部两笔交易。

'''

# class Solution:
#     def maxProfit5(self, prices) -> int:
#         n = len(prices)
#         buy1 = buy2 = -prices[0]
#         sell1 = sell2 = 0
#         for i in range(1, n):
#             buy1 = max(buy1, -prices[i])
#             sell1 = max(sell1, buy1 + prices[i])
#             buy2 = max(buy2, sell1 - prices[i])
#             sell2 = max(sell2, buy2 + prices[i])
#         return sell2

'''
你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''


# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码不保证正确性，仅供参考。如有疑惑，可以参照我写的 java 代码对比查看。

# 原始版本
def maxProfit_k_2(prices: List[int]) -> int:
    max_k = 2
    n = len(prices)
    dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
    for i in range(n):
        for k in range(max_k, 0, -1):
            if i - 1 == -1:
                # 处理 base case
                dp[i][k][0] = 0
                dp[i][k][1] = -prices[i]
                continue
            dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
            dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
    # 穷举了 n × max_k × 2 个状态，正确。
    return dp[n - 1][max_k][0]


# def maxProfit(self, k: int, prices) -> int:
#     if not prices:
#         return 0
#
#     n = len(prices)
#     k = min(k, n // 2)
#     buy = [0] * (k + 1)
#     sell = [0] * (k + 1)
#
#     buy[0], sell[0] = -prices[0], 0
#     for i in range(1, k + 1):
#         buy[i] = sell[i] = float("-inf")
#
#     for i in range(1, n):
#         buy[0] = max(buy[0], sell[0] - prices[i])
#         for j in range(1, k + 1):
#             buy[j] = max(buy[j], sell[j] - prices[i])
#             sell[j] = max(sell[j], buy[j - 1] + prices[i])
#
#     return max(sell)



print(maxProfit_k_inf([3,5,1,4,8]))