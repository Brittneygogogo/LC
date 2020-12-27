from typing import List

'''
什么时候使用 used 数组，什么时候使用 begin 变量
有些朋友可能会疑惑什么时候使用 used 数组，什么时候使用 begin 变量。这里为大家简单总结一下：

排列问题，讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为不同列表时），需要记录哪些数字已经使用过，此时用 used 数组；
组合问题，不讲究顺序（即 [2, 2, 3] 与 [2, 3, 2] 视为相同列表时），需要按照某种顺序搜索，此时使用 begin 变量。


'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return

            for index in range(begin, size):
                residue = target - candidates[index]
                if residue < 0:
                    break

                dfs(candidates, index, size, path + [candidates[index]], res, residue)

        size = len(candidates)
        if size == 0:
            return []
        #排序提高速度
        candidates.sort()
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


x = Solution()
print(x.combinationSum([2,3,6,7], 7))