# class Solution:
#     def isValidBST(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#
#         def helper(node, lower=float('-inf'), upper=float('inf')):
#             if not node:
#                 return True
#
#             val = node.val
#             if val <= lower or val >= upper:
#                 return False
#
#             if not helper(node.right, val, upper):
#                 return False
#             if not helper(node.left, lower, val):
#                 return False
#             return True
        # return helper(root)


class node:
    def __init__(self,x, a = None, b=None):
        self.left = a
        self.right = b
        self.val = x


class Solution:
    def isValidBST(self, root) -> bool:
        return self.helper(root, None, None)

    # 限定以 root 为根的子树节点必须满足 max.val > root.val > min.val
    def helper(self, root, min_node, max_node):
        # base case
        if not root:
            return True
        # 若 root.val 不符合 max 和 min 的限制，说明不是合法 BST
        if min_node and root.val <= min_node.val:
            return False
        if max_node and root.val >= max_node.val:
            return False
        # 限定左子树的最大值是 root.val，右子树的最小值是 root.val
        return self.helper(root.left, min_node, root) and self.helper(root.right, root, max_node)


node2 = node(x = 5, a = node(x = 1), b =node(x = 4))
node5 = node(x = 4, b = node(x = 6))

root = node(x= 4, a = node2, b = node5)

x = Solution()
print(x.isValidBST(root))

