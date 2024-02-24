'''
定义 dp[i] 表示字符串 s 前 i 个字符组成的字符串 s[0..i−1]是否能被空格拆分成若干个字典中出现的单词,
包含位置 i−1 的最后一个单词，看它是否出现在字典中以及除去这部分的字符串是否合法即可。


'''
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]



x = Solution()
print(x.wordBreak("applepenapple", ["apple", "pen"]))