import collections
'''
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有next 指针都被设置为 NULL



'''
class Solution:
    def connect(self, root) :
        if not root:
            return root
        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])
        # 外层的 while 循环迭代的是层数
        while Q:
            # 记录当前队列大小
            size = len(Q)
            # 遍历这一层的所有节点
            for i in range(size):
                # 从队首取出元素
                node = Q.popleft()
                # 连接
                if i < size - 1:
                    node.next = Q[0]
                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root

'''
ver 2
从根节点开始，由于第 0 层只有一个节点，所以不需要连接，直接为第 1 层节点建立 next 指针即可。
该算法中需要注意的一点是，当我们为第 N 层节点建立 next 指针时，处于第 N-1 层。
当第 N层节点的 next 指针全部建立完成后，移至第 N 层，建立第 N+1 层节点的 next 指针。
遍历某一层的节点时，这层节点的 next 指针已经建立。因此我们只需要知道这一层的最左节点，就可以按照链表方式遍历，不需要使用队列。

'''
class Solution:
    def connectNodes2(self, root):
        if not root:
            return root
        # 从根节点开始
        leftmost = root
        while leftmost.left:
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                # CONNECTION 1
                head.left.next = head.right
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                # 指针向后移动
                head = head.next
            # 去下一层的最左的节点
            leftmost = leftmost.left
        return root
