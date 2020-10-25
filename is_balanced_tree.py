# 一棵二叉树是平衡二叉树，当且仅当其所有子树也都是平衡二叉树，因此可以使用递归的方式判断二叉树是不是平衡二叉树，递归的顺序可以是自顶向下或者自底向上。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # def isBalanced(self, root: TreeNode) -> bool:
    #     def height(root: TreeNode) -> int:
    #         if not root:
    #             return 0
    #         leftHeight = height(root.left)
    #         rightHeight = height(root.right)
    #         if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
    #             return -1
    #         else:
    #             return max(leftHeight, rightHeight) + 1
    #
    #     return height(root) >= 0


    def isBalanced(self, root):
        return self.recur(root) != -1

    def recur(self, root):
        if not root: return 0
        left = self.recur(root.left)
        if left == -1: return -1
        right = self.recur(root.right)
        if right == -1: return -1
        return max(left, right) + 1 if abs(left - right) < 2 else -1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.left.left = TreeNode(10)
root.right.left.right = TreeNode(11)
root.right.right = TreeNode(7)


print(root.isBalanced(root))
