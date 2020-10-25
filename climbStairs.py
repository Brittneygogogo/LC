# def climbStairs(n):
"""
:type n: int
:rtype: int
"""
# 递归，超时(斐波那契)
# def pa(n, s):
#     if n > 0:
#         s = pa(n - 1, s)
#     if n > 1:
#         s = pa(n - 2, s)
#     if n==0:
#         s += 1
#     return s
#
# s = 0
# s = pa(n, s)
# return s

def climbStairs(n):
    p = 0
    q = 0
    r = 1
    i = 1
    while (i <= n):
        i += 1
        p = q
        q = r
        r = p + q
    return r


print(climbStairs(5))
