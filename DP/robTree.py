
'''
除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。

给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。

'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        # 利用备忘录消除重叠子问题
        if root in self.memo:
            return self.memo[root]

        # 抢，然后去下下家
        do_it = root.val
        if root.left:
            do_it += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            do_it += self.rob(root.right.left) + self.rob(root.right.right)

        # 不抢，然后去下家
        not_do = self.rob(root.left) + self.rob(root.right)

        res = max(do_it, not_do)
        self.memo[root] = res
        return res
# 详细解析参见：
# https://labuladong.github.io/article/?qno=
