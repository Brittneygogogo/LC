'''
https://leetcode.cn/problems/sliding-window-maximum/solutions/2361228/239-hua-dong-chuang-kou-zui-da-zhi-dan-d-u6h0/?company_slug=bytedance
'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
        res = [nums[deque[0]]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] <= i - k:
                deque.popleft()
            while deque and nums[i] >= nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            res.append(nums[deque[0]])
        return res


print(maxSlidingWindow2([1,3,-1,-3,5,3,6,7], 3))
# print(maxSlidingWindow2([9,11], 2))
