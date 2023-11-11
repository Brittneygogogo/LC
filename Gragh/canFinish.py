import collections
'''
207 
拓扑排序 dfs递归遍历每一个节点，全部完成再进栈
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已完成
        visited = [0] * numCourses
        # 用数组来模拟栈，下标 0 为栈底，n-1 为栈顶
        result = list()
        # 判断有向图中是否有环
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            # 将节点标记为「搜索中」
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果「未搜索」那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果「搜索中」说明找到了环
                elif visited[v] == 1:
                    valid = False
                    return
            # 将节点标记为「已完成」
            visited[u] = 2
            # 将节点入栈
            result.append(u)

        # 每次挑选一个「未搜索」的节点，开始进行深度优先搜索

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid

'''
广度排序
初始时，所有入度为 0 的节点都被放入队列中，它们就是可以作为拓扑排序最前面的节点，并且它们之间的相对顺序是无关紧要的。
在广度优先搜索的每一步中，我们取出队首的节点 u：
我们将 u 放入答案中；
我们移除 u 的所有出边，也就是将 u 的所有相邻节点的入度减少 1。如果某个相邻节点 v 的入度变为 0，那么我们就将 v 放入队列中。
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

        #遍历储存邻接边
        for cur, pre in prerequisites:
            edges[pre].append(cur)
            indeg[cur] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        visited = 0

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses


x = Solution()
print(x.canFinish(2, [[1,0]]))