

'''
组合
完全背包，不限个数
有几种凑法可以凑成5

dp[i][w]表示：对于前i个物品，当前背包的容量为w时，这种情况下可以装下的最大价值是dp[i][w]。

如果你没有把这第i个物品装入背包，那么很显然，最大价值dp[i][w]应该等于dp[i-1][w]。你不装嘛，那就继承之前的结果。

如果你把这第i个物品装入了背包，那么dp[i][w]应该等于dp[i-1][w-wt[i-1]] + val[i-1]。

首先，由于i是从 1 开始的，所以对val和wt的取值是i-1。

而dp[i-1][w-wt[i-1]]也很好理解：你如果想装第i个物品，你怎么计算这时候的最大价值？换句话说，在装第i个物品的前提下，背包能装的最大价值是多少？

显然，你应该寻求剩余重量w-wt[i-1]限制下能装的最大价值，加上第i个物品的价值val[i-1]，这就是装第i个物品的前提下，背包可以装的最大价值。

'''


def coinChange(coins, amount):
    n = len(coins)
    dp = [[0] * (amount + 1)] * (n + 1)
    # dp[0] = 0
    for i in range(n+1):
        dp[i][0] = 1
    # print(dp)

    for i in range(1, n + 1):
        for j in range(1, amount + 1):
            if j - coins[i - 1] >=0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][amount]


'''
官方
'''
def coinChange2(coins, amount) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


#
# def coinChange3(coins, amount):
#     n = len(coins)
#     dp = [[0] * (amount + 1)] * (n + 1)
#     # dp[0] = 0
#     # for i in range(n+1):
#     #     dp[i][0] = 1
#     # print(dp)
#
#     for i in range(1, n + 1):
#         for j in range(1, amount + 1):
#             if j - coins[i - 1] >=0:
#                 dp[i][j] = max(dp[i - 1][j],
#                                dp[i - 1][j - coins[i - 1]] + wt[i - 1])
#             else:
#                 dp[i][j] = dp[i - 1][j]
#
#     return dp[n][amount]


print(coinChange([2,5,10], 11))
print(coinChange2([2,5,10], 11))
# print(coinChange3([1,2,5], 5))