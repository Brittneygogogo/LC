'''
cur.adj() 泛指 cur 相邻的节点，比如说二维数组中，cur 上下左右四面的位置就是相邻节点；

visited 的主要作用是防止走回头路，大部分时候都是必须的，但是像一般的二叉树结构，没有子节点到父节点的指针，不会走回头路就不需要 visited。

'''

# 计算从起点 start 到终点 target 的最近距离
def  BFS(start, target):
    q = [] # 核心数据结构
    visited = [] # 避免走回头路

    q.append(start) # 将起点加入队列
    visited.append(start)
    step = 0 # 记录扩散的步数

    while q: 
        sz = len(q)
        # 将当前队列中的所有节点向四周扩散 */
        for i in range(sz):
            cur = q[0]
            # 划重点：这里判断是否到达终点 */
            if (cur is target):
                return step
            # 将 cur 的相邻节点加入队列 */
            for x in cur.adj():
                if (x not in visited):
                    q.append(x)
                    visited.append(x)
                
        
        # 划重点：更新步数在这里 */
        step += 1
    
