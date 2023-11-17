'''
所以求直径（即求路径长度的最大值）等效于求路径经过节点数的最大值减一。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def __init__(self):
    #     self.maxDiameter = 0
    #
    # def diameterOfBinaryTree(self, root: TreeNode) -> int:
    #     self.maxDepth(root)
    #     return self.maxDiameter
    #
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     leftMax = self.maxDepth(root.left)
    #     rightMax = self.maxDepth(root.right)
    #
    #     self.maxDiameter = max(self.maxDiameter, leftMax + rightMax)
    #     return 1 + max(leftMax, rightMax)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R 并更新ans
            self.ans = max(self.ans, L + R)
            # 需比较，比如左子树有多条路径，需取最大
            return max(L, R) + 1

        depth(root)
        return self.ans


x = Solution()


print(x.diameterOfBinaryTree())