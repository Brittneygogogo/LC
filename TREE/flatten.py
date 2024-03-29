class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = None
        self.right = None

'''
后序
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            if root == None: return
            helper(root.left)
            helper(root.right)
            if root.left != None: # 后序遍历
                pre = root.left # 令 pre 指向左子树
                while pre.right:
                    pre = pre.right # 找到左子树中的最右节点
                pre.right = root.right # 令左子树中的最右节点的右子树 指向 根节点的右子树
                root.right = root.left # 令根节点的右子树指向根节点的左子树
                root.left = None # 置空根节点的左子树
            root = root.right # 令当前节点指向下一个节点
        helper(root)


'''
https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/solutions/356853/er-cha-shu-zhan-kai-wei-lian-biao-by-leetcode-solu/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while (root != None):
            if root.left != None:
                most_right = root.left
                while most_right.right != None:
                    most_right = most_right.right
                most_right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return



root = TreeNode(1, TreeNode(2, TreeNode(3, None, None), TreeNode(4, None, None)), TreeNode(5, None, 6))
flatten(root)