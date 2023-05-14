'''
cur.adj() 泛指 cur 相邻的节点，比如说二维数组中，cur 上下左右四面的位置就是相邻节点；

visited 的主要作用是防止走回头路，大部分时候都是必须的，但是像一般的二叉树结构，没有子节点到父节点的指针，不会走回头路就不需要 visited。

'''

# # 计算从起点 start 到终点 target 的最近距离
# def  BFS(start, target):
#     q = [] # 核心数据结构
#     visited = [] # 避免走回头路
#
#     q.append(start) # 将起点加入队列
#     visited.append(start)
#     step = 0 # 记录扩散的步数
#
#     while q:
#         sz = len(q)
#         # 将当前队列中的所有节点向四周扩散 */
#         for i in range(sz):
#             cur = q[0]
#             # 划重点：这里判断是否到达终点 */
#             if (cur is target):
#                 return step
#             # 将 cur 的相邻节点加入队列 */
#             for x in cur.adj():
#                 if (x not in visited):
#                     q.append(x)
#                     visited.append(x)
#
#
#         # 划重点：更新步数在这里 */
#         step += 1
#
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode):
        res = []
        if not root:
            return res

        q = []
        q.append(root)
        # while 循环控制从上向下一层层遍历
        while q:
            sz = len(q)
            # 记录这一层的节点值
            level = []
            # for 循环控制每一层从左向右遍历
            for i in range(sz):
                cur = q.pop(0)
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(level)
        return res