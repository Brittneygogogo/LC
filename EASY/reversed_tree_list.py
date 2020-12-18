import collections

'''

为了降低在结果列表的头部添加一层节点值的列表的时间复杂度，结果列表可以使用链表的结构，在链表头部添加一层节点值的列表的时间复杂度是 O(1)O(1)。
在 Java 中，由于我们需要返回的 List 是一个接口，这里可以使用链表实现；
而 C++ 或 Python 中，我们需要返回一个 vector 或 list，它不方便在头部插入元素（会增加时间开销），
所以我们可以先用尾部插入的方法得到从上到下的层次遍历列表，然后再进行反转。

'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def levelOrderBottom(self, root) :
        levelOrder = list()
        if not root:
            return levelOrder

        q = collections.deque([root])
        while q:
            level = list()
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            levelOrder.append(level)

        return levelOrder[::-1]


root = TreeNode(3)
root.left  = TreeNode(9)
root.right  = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(root.levelOrderBottom(root))