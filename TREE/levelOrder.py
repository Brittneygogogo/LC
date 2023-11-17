import collections

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        if root==None:  #若是空树则直接返回
            return []

        queue = [root] #创建队列
        ans = [] #储存结果列表

        while queue: #队列非空时
            #上一层的所有节点值
            ans.append([node.val for node in queue])
            # 存储当前层的所有节点
            ll = []
            for node in queue:
                if node.left:
                    ll.append(node.left)
                if node.right:
                    ll.append(node.right)
            queue=ll
        return ans


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
print(x.levelOrder(root))