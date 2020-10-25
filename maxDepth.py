class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def maxDepth(self, root):
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1


root = TreeNode(3)
root.left  = TreeNode(9)
root.right  = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(root.maxDepth(root))