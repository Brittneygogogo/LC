temp = []
ans = []


class Solution:
    def combine(self,n, k):
        self.dfs(1, n, k, temp)
        return ans

    def dfs(self, cur, n, k, temp):
        # 剪枝：temp 长度加上区间 [cur, n] 的长度小于 k，不可能构造出长度为 k 的 temp
        if (k==0):
            ans.append(temp.copy())
            return

        while cur <= n - k + 1:
            # 考虑选择当前位置
            temp.append(cur)
            self.dfs(cur+1, n, k-1, temp)
            temp.pop()
            cur += 1

#
# class Solution:
#
#     def combine(self, n, k):
#         self.dfs(1, n, k)
#         return ans
#
#     def dfs( self, cur,  n,  k):
#         # 剪枝：temp 长度加上区间 [cur, n] 的长度小于 k，不可能构造出长度为 k 的 temp
#         if (len(temp) + (n - cur + 1) < k):
#             return
#
#         # 记录合法的答案
#         if (len(temp) == k):
#             ans.append(temp.copy())
#             return
#
#         # 考虑选择当前位置
#         temp.append(cur)
#         self.dfs(cur + 1, n, k)
#         temp.pop()
#         # 考虑不选择当前位置
#         self.dfs(cur + 1, n, k)
#


x = Solution()
print(x.combine(4,2))