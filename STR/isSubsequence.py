'''
，sss 是否是 ttt 的子序列，因此只要能找到任意一种 sss 在 ttt 中出现的方式，即可认为 sss 是 ttt 的子序列。
可断
输入：s = "abc", t = "ahbgdc"
输出：true
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n
