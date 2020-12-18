# class Solution(object):
#     def findLengthOfLCIS(self, nums):
#         ans = anchor = 0
#         for i in range(len(nums)):
#             if i and nums[i-1] >= nums[i]: anchor = i
#             ans = max(ans, i - anchor + 1)
#         return ans
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strPart(s, left)) or isPalindrome(strPart(s, right))
            left += 1
            right -= 1
        return True

'''
分析发现，在找到不相等的元素时，[0, left) 和 (right, len(s) - 1] 这两部分已经判断过是回文的，因此不用再次判断。只用判断 [left, right] 区间中的字符串，即删除 left 或者 right 指向的元素，剩余的区间 (left, right] 或者 [left, right) 是否为回文串。

若 (left, right] 或者 [left, right) 为回文串，则说明删除了一个字符可以构成回文串。

如题目的示例 2 ，当左右指针遇到了不等元素时，删除 left 或者 right 指向元素后， 我们只用判断 c 或者 b 是否为回文串。由于这两者是回文串，所以总体的字符串 s 删除 left 或者 right 指向元素也可以构成回文串。



'''

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda x : x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1 : right + 1]) or isPalindrome(s[left: right])
        return True


x = Solution()
print(x.findLengthOfLCIS([7,8,1,2,3]))