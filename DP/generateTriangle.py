from typing import List


class Solution:
    def generateTriangle(self, numRows: int) -> List[List[int]]:
        result = []
        dp = [[1]] * (numRows)
        for i in range(numRows):
            #个数多一个，行数是0...n-1，每行个数是1，2...i+1
            dp[i] = [1] * (i + 1)
            dp[i][0] = dp[i][-1] = 1
            for j in range(1, i):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            result.append(dp[i])
        return result

