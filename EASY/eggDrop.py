'''
2nd：二分优化
首先我们根据 dp(K, N) 数组的定义（有 K 个鸡蛋面对 N 层楼，最少需要扔几次），很容易知道 K 固定时，这个函数随着 N 的增加一定是单调递增的，无论你策略多聪明，楼层增加测试次数一定要增加。

那么注意 dp(K - 1, i - 1) 和 dp(K, N - i) 这两个函数，其中 i 是从 1 到 N 单增的，
如果我们固定 K 和 N，把这两个函数看做关于 i 的函数，前者随着 i 的增加应该也是单调递增的，而后者随着 i 的增加应该是单调递减的：


这时候求二者的较大值，再求这些最大值之中的最小值，其实就是求这两条直线交点，也就是红色折线的最低点嘛。
'''

class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()

        def dp(K, N):
            if K == 1: return N
            if N == 0: return 0
            if (K, N) in memo:
                return memo[(K, N)]

            # for 1 <= i <= N:
            #     res = min(res,
            #             max(
            #                 dp(K - 1, i - 1),
            #                 dp(K, N - i)
            #                 ) + 1
            #             )

            res = float('INF')
            # 用二分搜索代替线性搜索
            lo, hi = 1, N
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(K - 1, mid - 1)  # 碎
                not_broken = dp(K, N - mid)  # 没碎
                # res = min(max(碎，没碎) + 1)
                if broken > not_broken:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, not_broken + 1)

            memo[(K, N)] = res
            return res

        return dp(K, N)


"""
3rd 解法
1、无论你在哪层楼扔鸡蛋，鸡蛋只可能摔碎或者没摔碎，碎了的话就测楼下，没碎的话就测楼上。

2、无论你上楼还是下楼，总的楼层数 = 楼上的楼层数 + 楼下的楼层数 + 1（当前这层楼）。

根据这个特点，可以写出下面的状态转移方程：

dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1

dp[k][m - 1] 就是楼上的楼层数，因为鸡蛋个数 k 不变，也就是鸡蛋没碎，扔鸡蛋次数 m 减一；

dp[k - 1][m - 1] 就是楼下的楼层数，因为鸡蛋个数 k 减一，也就是鸡蛋碎了，同时扔鸡蛋次数 m 减一。

PS：这个 m 为什么要减一而不是加一？之前定义得很清楚，这个 m 是一个允许的次数上界，而不是扔了几次。

int superEggDrop3(int K, int N) {
    // m 最多不会超过 N 次（线性扫描）
    int[][] dp = new int[K + 1][N + 1];
    // base case:
    // dp[0][..] = 0
    // dp[..][0] = 0
    // Java 默认初始化数组都为 0
    int m = 0;
    while (dp[K][m] < N) {
        m++;
        for (int k = 1; k <= K; k++)
            dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1;
    }
    return m;
}
=====
for (int m = 1; dp[K][m] < N; m++)
    for (int k = 1; k <= K; k++)
        dp[k][m] = dp[k][m - 1] + dp[k - 1][m - 1] + 1;
        
"""


x = Solution()
print(x.superEggDrop(2, 8))
