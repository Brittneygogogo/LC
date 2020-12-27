
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        f = [0] * m
        f[0] = (obstacleGrid[0][0] == 0)

        for i in range(n):
            for j in range(m):
                if (obstacleGrid[i][j] == 1):
                    f[j] = 0
                    continue
                if (j - 1 >= 0 and obstacleGrid[i][j - 1] == 0):
                    f[j] +=f[j - 1]

        return f[-1]

x = Solution()
print(x.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
