# 中序遍历，总是选择中间位置左边的数字作为根节点
# 选择中间位置左边的数字作为根节点，则根节点的下标为 \textit{mid}=(\textit{left}+\textit{right})/2mid=(left+right)/2，此处的除法为整数除法。


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def sortedArrayToBST(self, nums):
        def helper(left, right):
            if left > right:
                return None

            # 总是选择中间位置左边的数字作为根节点
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return helper(0, len(nums) - 1)


root = TreeNode(3)
root.left  = TreeNode(9)
root.right  = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(root.sortedArrayToBST([-10,-3,0,5,9]))