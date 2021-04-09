'''
首先考虑最简单的情况。如果只有一间房屋，则偷窃该房屋，可以偷窃到最高总金额。
如果只有两间房屋，则由于两间房屋相邻，不能同时偷窃，只能偷窃其中的一间房屋，因此选择其中金额较高的房屋进行偷窃，可以偷窃到最高总金额。

'''
class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]

        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[size - 1]

x = Solution()
print(x.rob([1,2,3,1,3]))

'''
考虑到每间房屋的最高总金额只和该房屋的前两间房屋的最高总金额相关，因此可以使用滚动数组，在每个时刻只需要存储前两间房屋的最高总金额。
滚动数组
'''
def rob1(nums) -> int:
    if not nums:
        return 0

    size = len(nums)
    if size == 1:
        return nums[0]

    first, second = nums[0], max(nums[0], nums[1])
    for i in range(2, size):
        first, second = second, max(first + nums[i], second)

    return second

print(rob1([1,2,3,1,3]))

'''
环：
此题中的房间是环状排列的（即首尾相接），而 198.题中的房间是单排排列的；而这也是此题的难点。
在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1 
1 在不偷窃最后一个房子的情况下（即 nums[:n-1]），最大金额是 p2
2 综合偷窃最大金额： 为以上两种情况的较大值，即 max(p1,p2) 。

'''
def rob3(nums:[int]) -> int:
    def my_rob(nums):
        cur, pre = 0, 0
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
        return cur
    return max(my_rob(nums[:-1]), my_rob(nums[1:])) if len(nums) != 1 else nums[0]

print(rob3([1,2,3,1,5]))
#
# def rob3(nums) -> int:
#     if not nums:
#         return 0
#
#     size = len(nums)
#     if size == 1:
#         return nums[0]
#
#     dp = [0] * size
#     dp[0] = nums[0]
#     dp[1] = max(nums[0], nums[1])
#     for i in range(2, size):
#         dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
#
#     return dp[size - 1]
#
# x = [1,2,3,1,5]
# print(max(rob3(x[1:]), rob3(x[:-1])))

'''
路径是二叉树
ls(rob)表示当前结点被选中时候可以抢劫的最大值
ln(rob)表示当前结点不被选择时候可以抢劫的最大值
子树根结点被rob时,ls(left) + ln(right)
子树根结点不rob时，max(ls(left),ls(left)) + max(ln(right),n(right))
时间复杂度为O(n)
空间复杂度为O(logn)

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rob4(root: TreeNode) -> int:
    def _rob(root):
        if not root: return 0, 0

        ls, ln = _rob(root.left)
        rs, rn = _rob(root.right)

        return root.val + ln + rn, max(ls, ln) + max(rs, rn)

    return max(_rob(root))
