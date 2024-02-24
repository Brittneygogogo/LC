class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
图
https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solutions/2023872/fen-lei-tao-lun-luan-ru-ma-yi-ge-shi-pin-2r95/?envType=study-plan-v2&envId=top-interview-150

递归寻找p q节点，根据寻找情况判断

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right:
            return None
        if left and right:
            return root
        return right if not left else left


x = Solution()
print(x.lowestCommonAncestor(root))