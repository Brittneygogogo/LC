import collections

'''
在S中寻找T子串
https://leetcode.cn/problems/minimum-window-substring/solutions/258513/tong-su-qie-xiang-xi-de-miao-shu-hua-dong-chuang-k/?envType=study-plan-v2&envId=top-100-liked
每次都是新的needcnt和need dict
'''
class Solution():
    def minWindow(self, s: str, t: str) -> str:
        need = collections.defaultdict(int)
        # for c in t:
        #     need[c] += 1
        l = len(s)
        ans = ''
        for i in range(l):
            needcnt = len(t)
            for c in t:
                need[c] += 1
            j = i
            while needcnt != 0 and j < l:
                if need[s[j]] > 0:
                    need[s[j]] -= 1
                    needcnt -= 1
                j += 1
            if needcnt == 0:
                if len(ans) > j - i:
                    ans = s[i:j]
                if i == 0:
                    ans = s[i:j]
        return ans

x = Solution()
print(x.minWindow("bba", "ab"))
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         need = collections.defaultdict(int)
#         for c in t:
#             need[c] += 1
#         needCnt = len(t)
#         i = 0
#         res = (0,float('inf'))
#         for j,c in enumerate(s):
#             if need[c] > 0:
#                 needCnt -= 1
#             need[c] -= 1
#             if needCnt == 0:       #步骤一：滑动窗口包含了所有T元素
#                 while True:      #步骤二：增加i，排除多余元素
#                     c = s[i]
#                     if need[c] == 0:
#                         break
#                     need[c] += 1
#                     i += 1
#                 if j-i < res[1] - res[0]:   #记录结果
#                     res = (i,j)
#                 need[s[i]] += 1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
#                 needCnt += 1
#                 i += 1
#         return '' if res[1] > len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果
