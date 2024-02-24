import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class TreeNode:
#     def __init__(self, x, left, right):
#         self.val = x
#         self.left = None
#         self.right = None

'''
询问是否存在从当前节点 root 到叶子节点的路径，满足其路径和为 sum
'''
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


'''
返回路径和=sum的节点list
'''
class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        res = []
        self.dfs(root, sum, res, [])
        return res

    def dfs(self, root, sum, res, path):
        if not root: # 空节点，不做处理
            return
        if not root.left and not root.right: # 叶子节点
            if sum == root.val: # 剩余的「路径和」恰好等于叶子节点值
                res.append(path + [root.val]) # 把该路径放入结果中
        self.dfs(root.left, sum - root.val, res, path + [root.val]) # 左子树
        self.dfs(root.right, sum - root.val, res, path + [root.val]) # 右子树

x = Solution()
print(x.pathSum(root,))

'''
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
https://leetcode.cn/problems/path-sum-iii/solutions/1021296/lu-jing-zong-he-iii-by-leetcode-solution-z9td/?envType=study-plan-v2&envId=top-100-liked
'''


class Solution:
    def pathNum(self, root: TreeNode, targetSum: int) -> int:
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)

# class Solution:
#     def pathSum(self, root, total: int):
#         ret = list()
#         path = list()
#
#         def dfs(root, total):
#             if not root:
#                 return
#             path.append(root.val)
#             total -= root.val
#             if not root.left and not root.right and total == 0:
#                 ret.append(path[:])
#             dfs(root.left, total)
#             dfs(root.right, total)
#             path.pop()
#
#         dfs(root, total)
#         return ret

x = Solution()
root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3, None, None), TreeNode(-2, None, None)), TreeNode(2, None, TreeNode(1, None, None))), TreeNode(-3, None, TreeNode(11, None, None)))
print(x.pathNum(root, 8))