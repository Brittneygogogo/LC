'''
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。（只能買賣一次）

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0
不用dp 最小值是是min
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
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
在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。
由于全部交易结束后，持有股票的收益一定低于不持有股票的收益，因此这时候 dp[n−1][0] 收益必然是大于 dp[n−1][1] 最后的答案即为 dp[n−1][0]
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/
'''

def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n):
        if i - 1 == -1:
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue
        dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
        dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
    return dp[n - 1][0]


'''
手續費
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
                #   dp[i][1]
                # = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
                # = max(dp[-1][1], dp[-1][0] - prices[i] - fee)
                # = max(-inf, 0 - prices[i] - fee)
                # = -prices[i] - fee
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[n - 1][0]


'''
冷冻期
冷冻期为 1 天
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
'''

# 原始版本
def maxProfit_with_cool(prices: List[int]) -> int:
    n = len(prices)
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n):
        if i - 1 == -1:
            # base case 1
            dp[i][0] = 0
            dp[i][1] = -prices[i]
            continue
        if i - 2 == -1:
            # base case 2
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            # 当 i = 1 时，dp[i-2] 不合法，所以只能从 dp[i-1][1] 转移过来 第一次买入没有冷冻限制
            dp[i][1] = max(dp[i-1][1], -prices[i])
            # 解释如上
            continue
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
    return dp[n-1][0]

'''
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iii/description/
对 k 进行穷举，k的次数变化只跟i有关系
第 0 天开始，而且还没有进行过买卖，所以最大交易次数限制 k 应该是 max_k；而随着「状态」的推移，你会进行交易，那么交易次数上限 k 应该不断减少，这样一想，k = max_k, k-- 的方式是比较合乎实际场景的。
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_k = 2
        n = len(prices)
        dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(n)]
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


'''
你最多可以完成 k 笔交易。也就是说，你最多可以买 k 次，卖 k 次。
内存超限的错误，原来是传入的 k 值会非常大，dp 数组太大了。那么现在想想，交易次数 k 最多有多大呢？

一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，如果超过，就没有约束作用了，相当于 k 没有限制的情况，而这种情况是之前解决过的。


https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-iv/description/?company_slug=bytedance
'''
class Solution:
    def maxProfit(self, max_k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0:
            return 0
        if max_k > n // 2:
            # 交易次数 k 没有限制的情况
            return self.maxProfit_k_inf(prices)

        # base case：
        # dp[-1][...][0] = dp[...][0][0] = 0
        # dp[-1][...][1] = dp[...][0][1] = -infinity
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        # k = 0 时的 base case
        for i in range(n):
            dp[i][0][1] = float('-inf')
            dp[i][0][0] = 0

        for i in range(n):
            for k in range(max_k, 0, -1):
                if i - 1 == -1:
                    # 处理 i = -1 时的 base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                # 状态转移方程
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][max_k][0]


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




print(maxProfit_k_inf([3,5,1,4,8]))