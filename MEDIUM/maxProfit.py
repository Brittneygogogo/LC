class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
            # f[i][0]: 手上持有股票的最大收益
            # f[i][1]: 手上不持有股票，并且处于冷冻期中的累计最大收益
            # f[i][2]: 手上不持有股票，并且不在冷冻期中的累计最大收益

        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            newf0 = max(f0, f2 - prices[i])
            newf1 = f0 + prices[i]
            newf2 = max(f1, f2)
            f0, f1, f2 = newf0, newf1, newf2

        return max(f1, f2)
