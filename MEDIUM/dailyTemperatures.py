'''
https://leetcode.cn/problems/daily-temperatures/solutions/283196/mei-ri-wen-du-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
找右侧最近的比当前大的值
'''
class Solution:
    def dailyTemperatures(self, T):
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            #清栈里面所有小的，比栈顶大直接计算出来了，小的不管
            while stack and temperature > T[stack[-1]]:
            # while stack and temperature <= T[stack[-1]]:

                prev_index = stack.pop()
                ans[prev_index] = i - prev_index

            #都进栈
            stack.append(i)
        return ans

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))