import collections
'''
207
初始时，所有入度为 0 的节点都被放入队列中，它们就是可以作为拓扑排序最前面的节点，并且它们之间的相对顺序是无关紧要的。
在广度优先搜索的每一步中，我们取出队首的节点 u：
我们将 u 放入答案中；
我们移除 u 的所有出边，也就是将 u 的所有相邻节点的入度减少 1。如果某个相邻节点 v 的入度变为 0，那么我们就将 v 放入队列中。
'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses

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

#
#
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites) -> bool:
#         edges = collections.defaultdict(list)
#         visited = [0] * numCourses
#         result = list()
#         valid = True
#
#         for info in prerequisites:
#             edges[info[1]].append(info[0])
#
#         def dfs(u: int):
#             nonlocal valid
#             visited[u] = 1
#             for v in edges[u]:
#                 if visited[v] == 0:
#                     dfs(v)
#                     if not valid:
#                         return
#                 elif visited[v] == 1:
#                     valid = False
#                     return
#             visited[u] = 2
#             result.append(u)
#
#         for i in range(numCourses):
#             if valid and not visited[i]:
#                 dfs(i)
#
#         return valid

x = Solution()
print(x.canFinish(2, [[1,0]]))