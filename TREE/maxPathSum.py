'''
https://leetcode.cn/problems/binary-tree-maximum-path-sum/solutions/297005/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-/?company_slug=bytedance

迭代的返回取left或right其一的最大值
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.maxSum = float("-inf")
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain

            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)

            # 返回节点的最大贡献值
            # 左右二选一
            return node.val + max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum

x = Solution()
root = TreeNode(10, TreeNode(9, None, None), TreeNode(20, TreeNode(10, None, None), TreeNode(7, None, None)))
print(x.maxPathSum(root))