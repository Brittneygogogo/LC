import collections


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

'''
https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/solutions/2361613/103-er-cha-shu-de-ju-chi-xing-ceng-xu-bi-qz2q/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, deque = [], collections.deque([root])
        while deque:
            tmp = collections.deque()
            for _ in range(len(deque)):
                node = deque.popleft()
                if len(res) % 2 == 0:
                    tmp.append(node.val) # 奇数层 -> 插入队列尾部
                else:
                    tmp.appendleft(node.val) # 偶数层 -> 插入队列头部
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            res.append(list(tmp))
        return res

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

x = Solution()
print(x.averageOfLevels(root))