'''动态规划'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n==0:return 0
        dp = [0]*n
        for i in range(len(s)):
            # i-dp[i-1]-1是与当前)对称的位置
            if s[i]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
               dp[i]=dp[i-1]+dp[i-dp[i-1]-2]+2
        return max(dp)

'''栈'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        length = 0
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    length = i-stack[-1]
                    max_length = max(max_length,length)
        return max_length

'''
正向逆向结合
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n, left, right, maxlength = len(s), 0, 0, 0
        for i in range(n):
            if s[i] =='(':
                left+=1
            else:
                right+=1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        left = right = 0
        for i in range(n-1,-1,-1):
            if s[i] =='(':
                left+=1
            else:
                right+=1
            if left == right:
                maxlength = max(maxlength, 2 * left)
            elif right < left:
                left = right = 0

        return maxlength