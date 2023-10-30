'''
不同的二叉搜索树
G(n)  长度为 n的序列能构成的不同二叉搜索树的个数。

F(i,n)F(i, n)F(i,n): 以 iii 为根、序列长度为 nnn 的不同二叉搜索树个数 (1≤i≤n)(1 \leq i \leq n)(1≤i≤n)。


'''


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

x = Solution()
print(x.numTrees(4))