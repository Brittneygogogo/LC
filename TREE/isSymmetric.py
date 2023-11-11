# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def ifSymmetric(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.ifSymmetric(left.left, right.right) and self.ifSymmetric(left.right, right.left)


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.ifSymmetric(root.left, root.right)

    # return self.ifSymmetric(root, root)


