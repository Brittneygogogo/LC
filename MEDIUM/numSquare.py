import math


# class Solution(object):
#     def numSquares(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
#
#         print(square_nums)
#         dp = [float('inf')] * (n + 1)
#         # bottom case
#         dp[0] = 0
#
#         for i in range(1, n + 1):
#             for square in square_nums:
#                 if i < square:
#                     break
#                 dp[i] = min(dp[i], dp[i - square] + 1)
#
#         return dp[-1]


class Solution:
    def numSquares(self, n):

        def is_divided_by(n, count):
            """
                return: true if "n" can be decomposed into "count" number of perfect square numbers.
                e.g. n=12, count=3:  true.
                     n=12, count=2:  false
            """
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])
        print(square_nums)

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count



x = Solution()
print(x.numSquares(12))