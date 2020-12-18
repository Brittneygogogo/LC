class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def averageOfLevels(self, root: TreeNode):
        def dfs(root: TreeNode, level: int):
            if not root:
                return
            if level < len(totals):
                totals[level] += root.val
                counts[level] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        counts = list()
        totals = list()
        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

x = Solution()
print(x.averageOfLevels(root))