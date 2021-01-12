class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.ans = ""

    def tree2str(self, root: TreeNode) -> str:
        if not root:
            return self.ans

        def convert(root):
            if not root:
                return ""
            elif not root.left and not root.right:
                return str(root.val)
            elif root.right:
                return str(root.val) + "(" + convert(root.left) + ")" + "(" + convert(root.right) + ")"
            else:
                return str(root.val) + "(" + convert(root.left) + ")"

        self.ans += convert(root)
        return self.ans