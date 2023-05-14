import collections

'''
叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
当 root 节点左右孩子都为空时，返回 1
当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值

 
'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
    # 深度优先 递归 1
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)
        #
        # if root.left == None or root.right ==None:
        #     return left + right + 1
        # else:
        #     return min(left, right) + 1

    # 深度优先 递归 2
        min_depth = 10 ** 9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth)

        return min_depth + 1

#广度优先搜索

# 同样，我们可以想到使用广度优先搜索的方法，遍历整棵树。
#
# 当我们找到一个叶子节点时，直接返回这个叶子节点的深度。广度优先搜索的性质保证了最先搜索到的叶子节点的深度一定最小。

        # q = collections.deque([root])
        # # root 本身就是一层，depth 初始化为 1
        # depth = 1
        # while q:
        #     # ![](https://labuladong.github.io/pictures/dijkstra/1.jpeg)
        #     sz = len(q)
        #     ## 遍历当前层的节点
        #     for i in range(sz):
        #         cur = q.popleft()
        #         ## 判断是否到达叶子结点
        #         if not cur.left and not cur.right:
        #             return depth
        #         ## 将下一层节点加入队列
        #         if cur.left:
        #             q.append(cur.left)
        #         if cur.right:
        #             q.append(cur.right)
        #     ## 这里增加步数
        #     depth += 1
        # return depth





x = Solution()

tree_lst = [2,None,3,None,4,None,5,None,6]
# for i in tree_lst:

root = TreeNode(2)
# root.left = TreeNode()
root.right = TreeNode(3)
# root.right.left = TreeNode(15)
root.right.right = TreeNode(4)
root.right.right = TreeNode(4)


print(x.minDepth(root))