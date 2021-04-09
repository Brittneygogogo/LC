'''
2者中最长的公共子序列长度/字符串，可不连续

从低至上
由于数组索引从 0 开始，有索引偏移
二维矩阵 列数在里面, 行数在外面
dp = [[0] * (n+1)] * (m+1)

'''
def longestCommonSubsequence(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n+1)] * (m+1)
    # print(dp)
    # 定义：s1[0..i-1] 和 s2[0..j-1] 的 lcs 长度为 dp[i][j]
    # 目标：s1[0..m-1] 和 s2[0..n-1] 的 lcs 长度，即 dp[m][n]
    # base case: dp[0][..] = dp[..][0] = 0
    s = ''
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # 现在 i 和 j 从 1 开始，所以要减一
            if (s1[i - 1] == s2[j - 1]):
                s += s1[i - 1]
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # return dp[m][n]
    return s


# print(longestCommonSubsequence("abcde", "acfe"))
print(longestCommonSubsequence("ace", "aced"))
