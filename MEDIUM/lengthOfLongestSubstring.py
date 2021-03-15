
'''
在每一步的操作中，我们会将左指针向右移动一格，表示 我们开始枚举下一个字符作为起始位置，然后我们可以不断地向右移动右指针，但需要保证这两个指针对应的子串中没有重复的字符。
在移动结束后，这个子串就对应着 以左指针开始的，不包含重复字符的最长子串。我们记录下这个子串的长度；
在枚举结束后，我们找到的最长的子串的长度即为答案。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，记录每个字符是否出现过
        occ = set()
        n = len(s)
        # 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                # 左指针向右移动一格，移除一个字符
                occ.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in occ:
                # 不断地移动右指针
                occ.add(s[rk + 1])
                rk += 1
            # 第 i 到 rk 个字符是一个极长的无重复字符子串
            ans = max(ans, rk - i + 1)
        return ans


class Solution:
    def lengthOfLongestSubstring(self, s: str):
        n = len(s)
        if len(s) < 1:
            return 0
        max_length = 1
        for i in range(n):
            head_ele = s[i]
            tmp_list = [head_ele]
            for ele in s[i + 1:]:
                if ele not in tmp_list:
                    tmp_list.append(ele)
                    max_length = max(len(tmp_list), max_length)
                else:
                    break
            return "".join(tmp_list)


x = Solution()
print(x.lengthOfLongestSubstring("ebcadcabc"))


x = Solution()
print(x.lengthOfLongestSubstring("abcabcbb"))