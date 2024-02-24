
'''
只求是否跳出，限制在起跳点范围内跳
'''
from typing import List

class Solution:
    def canJump(self, nums) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost > n:
                    return True
        return False
'''
https://leetcode.cn/problems/jump-game-ii/solutions/230241/tiao-yue-you-xi-ii-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked

贪心 求最少跳的次数
「贪心」地进行正向查找，每次找到可到达的最远位置，就可以在线性时间内得到最少的跳跃次数。
在遍历数组时，我们不访问最后一个元素，这是因为在访问最后一个元素之前，我们的边界一定大于等于最后一个位置 否则就无法跳到最后一个位置了。
如果访问最后一个元素，在边界正好为最后一个位置的情况下，我们会增加一次「不必要的跳跃次数」，因此我们不必访问最后一个元素。
'''
class Solution:
    def jumpn(self, nums: List[int]) -> int:
        n = len(nums)
        #maxPos目前能跳到的最远位置, end:跳跃可达范围右边界
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if i <= maxPos:
                maxPos = max(maxPos, i + nums[i])
                #到达上次跳跃能到达的右边界了
                if i == end:
                    #目前能跳到的最远位置变成了下次起跳位置的右边界
                    end = maxPos
                    step += 1
        return step

x = Solution()
# print(x.canJump([2, 3, 1, 1, 4]))
print(x.jumpn([2, 3, 1, 1, 4]))
