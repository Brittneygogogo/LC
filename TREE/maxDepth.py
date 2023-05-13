class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.res = 0
        self.traverse(root, 0)
        return self.res

    # 遍历二叉树
    def traverse(self, root: TreeNode, depth: int) -> None:
        if not root:
            return
        # 前序遍历位置
        depth += 1
        # 遍历的过程中记录最大深度
        self.res = max(self.res, depth)
        self.traverse(root.left, depth)
        self.traverse(root.right, depth)
        # 后序遍历位置
        depth -= 1


x = Solution()
root = TreeNode(3)
root.left  = TreeNode(9)
root.right  = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(x.maxDepth(root))