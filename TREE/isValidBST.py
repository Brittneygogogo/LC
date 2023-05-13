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
#
#         return helper(root)


class node:
    def __init__(self,x, a = None, b=None):
        self.left = a
        self.right = b
        self.val = x

class Solution:
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

node2 = node(x = 2, a = node(x = 1), b =node(x = 3))
node5 = node(x = 5, b = node(x = 6))

root = node(x= 4, a = node2, b = node5)

x = Solution()
print(x.isValidBST2(root))

