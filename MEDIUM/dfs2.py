class Solution:
    def subsets(self, nums) :
        ans = []
        # 存储符合要求的子集
        track = []
        n = len(nums)

        def backtrack(idx):
            # 先添加子集
            ans.append(track[:])

            for i in range(idx, n):
                track.append(nums[i])
                # 避免重复，每次递归，从下一个索引开始
                backtrack(i + 1)
                # 回溯
                track.pop()

        backtrack(0)
        return ans

x = Solution()
print(x.subsets([1,2,3]))