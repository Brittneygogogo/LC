'''
https://leetcode.cn/problems/largest-rectangle-in-histogram/solutions/266844/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/?envType=study-plan-v2&envId=top-100-liked

在得到了左右两侧的柱子之后，我们就可以计算出每根柱子对应的左右边界，并求出答案了。
'''
class Solution:
    def largestRectangleArea(self, heights) -> int:
        n = len(heights)
        left, right = [0] * n, [0] * n
        ans = 0

        #找左侧最近的比当前小的值
        mono_stack = list()
        for i in range(n):
            # 比栈顶小, 清栈里面所有大的，剩下就是比它小的
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()

            left[i] = mono_stack[-1] if mono_stack else -1

            mono_stack.append(i)

        #找右侧最近的比当前小的值
        mono_stack = list()
        for i in range(n - 1, -1, -1):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()
            right[i] = mono_stack[-1] if mono_stack else n
            mono_stack.append(i)

        if n > 0:
            for i in range(n):
                ans = max(ans, (right[i] - left[i] - 1) * heights[i])
        else:
            ans = 0
        return ans

from typing import List


