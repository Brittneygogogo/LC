
'''
括号问题可以简单分成两类，一类是前文写过的 括号的合法性判断 ，一类是合法括号的生成。对于括号合法性的判断，主要是借助「栈」这种数据结构，而对于括号的生成，一般都要利用回溯递归的思想。

n为生成n对括号

用 left 记录还可以使用多少个左括号，用 right 记录还可以使用多少个右括号

对于递归相关的算法，时间复杂度这样计算（递归次数）*（递归函数本身的时间复杂度）。

我们可以只在序列仍然保持有效时才添加 ‘('  或 ‘)’
如果左括号数量不大于 n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。

'''
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans



# def generateParenthesis(n):
#     if (n == 0):return
#     # 记录所有合法的括号组合
#     res = []
#     # 回溯过程中的路径
#     track = ""
#     # 可用的左括号和右括号数量初始化为 n
#     backtrack(n, n, track, res)
#     return res
#
#
# # 可用的左括号数量为 left 个，可用的右括号数量为 right 个
# def backtrack(left, right, track, res):
#     # 若左括号剩下的多，说明不合法
#     if (right < left):return
#     # 数量小于 0 肯定是不合法的
#     if (left < 0 or right < 0):return
#     # 当所有括号都恰好用完时，得到一个合法的括号组合
#     if (left == 0 and right == 0):
#         res.append(track)
#         return
#

    # # 尝试放一个左括号
    # track += '(' # 选择
    # backtrack(left - 1, right, track, res)
    # track = track[:-1] # 撤消选择
    #
    # # 尝试放一个右括号
    # track += (')') # 选择
    # backtrack(left, right - 1, track, res)
    # track = track[:-1]# 撤消选择

x = Solution()
print(x.generateParenthesis(3))