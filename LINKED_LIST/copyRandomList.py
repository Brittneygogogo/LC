class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         originToClone = {}
#         # 第一次遍历，先把所有节点克隆出来
#         p = head
#         while p:
#             if p not in originToClone:
#                 originToClone[p] = Node(p.val)
#             p = p.next
#         # 第二次遍历，把克隆节点的结构连接好
#         p = head
#         while p:
#             if p.next:
#                 originToClone[p].next = originToClone[p.next]
#             if p.random:
#                 originToClone[p].random = originToClone[p.random]
#             p = p.next
#         # 返回克隆之后的头结点
#         return originToClone.get(head)
#
# # 用递归的方式进行遍历
# class Solution2:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         self.visited = set()
#         self.originToClone = {}
#         self.traverse(head)
#         return self.originToClone.get(head)
#
#     # DFS 图遍历框架
#     def traverse(self, node):
#         if not node:
#             return
#         if node in self.visited:
#             return
#         # 前序位置，标记为已访问
#         self.visited.add(node)
#         # 前序位置，克隆节点
#         if node not in self.originToClone:
#             self.originToClone[node] = Node(node.val)
#         cloneNode = self.originToClone[node]
#
#         # 递归遍历邻居节点，并构建克隆图
#         # 递归之后，邻居节点一定存在 originToClone 中
#         self.traverse(node.next)
#         cloneNode.next = self.originToClone.get(node.next)
#
#         self.traverse(node.random)
#         cloneNode.random = self.originToClone.get(node.random)
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        cur = head
        m = {}
        while cur != None:
            # p.random = cur.random
            # p.next = cur.next
            m[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur != None:
            if cur.next != None:
                m[cur].next = m[cur.next]
            if cur.random != None:
                m[cur].random = m[cur.random]
            cur = cur.next
        return m[head]



a = Node(1)
b = Node(2)
head = a
head.next = b
head.random = b
b.random = b



x = Solution()
print(x.copyRandomList(head).next.random.val)