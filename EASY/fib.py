

'''
方法二：记忆化自底向上的方法
自底向上通过迭代计算斐波那契数的子问题并存储已计算的值，通过已计算的值进行计算。减少递归带来的重复计算。

算法：

如果 N 小于等于 1，则返回 N。
迭代 N，将计算出的答案存储在数组中。
使用数组前面的两个斐波那契数计算当前的斐波那契数。
知道我们计算到 N，则返回它的斐波那契数。


'''

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        cache = {0: 0, 1: 1}

        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]

        return cache[N]

'''
我们先计算存储子问题的答案，然后利用子问题的答案计算当前斐波那契数的答案。我们将递归计算，但是通过记忆化不重复计算已计算的值。

算法：

如果 N <= 1，则返回 N。
调用和返回 memoize(N)。
如果 N 对应的斐波那契数存在，则返回。
否则将计算 N 对应的斐波那契数为 memoize(N-1) + memoize(N-2)。

'''

class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        self.cache = {0: 0, 1: 1}
        return self.memoize(N)

    def memoize(self, N: int) -> {}:
        if N in self.cache.keys():
            return self.cache[N]
        self.cache[N] = self.memoize(N-1) + self.memoize(N-2)
        return self.memoize(N)

