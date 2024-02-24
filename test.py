from typing import List
from typing import List
from bisect import bisect_left
'''
按照大佬思路实现的代码，找n中前缀长度x，满足前x个位数都在nums中且nums中也存在小于第x+1个位数。
对于本题而言，证明的方法是从解的性质反推，归纳。

首先，小于n的数字有什么性质？显然可以分为两类：

位数和n相同，但是字典序小

位数比n小

对于情形1，我们要找字典序小的数，那么什么条件下字典序小？

两个字符串有一段相同的前缀（可以长度为0）；

在这段前缀后的第一个字符更小。

我们只需枚举前述第一个更小的位置即可。对于这个更小的字符，我们应当让它尽可能大，但是不能等于或超过限值；对于其余字符，则没有限制，取可选的最大即可。这就得出了前面的构造方法。

对于情形2，位数小于 n 的数字中，最大的显然就是位数-1，但所有数位都最大的数字。

这样就推出了解法，同时从推理的过程中验证了解的正确性。

'''
def max_num(nums, n):
    nums = list(map(str,nums))
    nums.sort()
    s = str(n)
    maxx = -1
    for x in range(len(s)):
        idx = bisect_left(nums, s[x])
        if idx != 0:
            maxx = x
        if s[x] not in nums:
            break
    print(nums, n)
    if maxx != -1:
        idx = bisect_left(nums, s[maxx])
        return int(s[:maxx] + nums[idx-1] + nums[-1]*(len(s)-maxx-1))
    else:
        return int(nums[-1]*(len(s)-1)) if len(s) > 1 else -1


def solve(nums: List[int], n: int) -> int:
    """
    由nums数组中的元素组成的小于n的最大数
    """
    nums = sorted(nums)
    nums = list(map(int, str(n)))  # 拆分位数
    k = len(nums)
    # 前x位数相等，第x+1位数更小，剩下的数字尽可能大。
    # 因此枚举x(0<=x<k)，若
    #   1.n的前x位数字都在数组nums中
    #   2.数组nums中存在比 n的第x+1位数字 更小的数字，
    x = 0  # 前缀长度非索引
    while x < k - 1:
        # 当前nums[x]能选入条件一：nums中存在<nums[x+1]的数
        idx = bisect_left(nums, nums[x+1])
        # nums[0,idx-1] < target <= nums[idx,]
        if idx == 0:
            break
        # 当前nums[x]能选入条件二：nums[x]在nums中
        if nums[x] not in nums:
            break
        x += 1
    # print(nums, x)
    # 答案与n等位数：数组nums中存在比n的第x+1位数字更小数字
    idx = bisect_left(nums, nums[x])
    if idx > 0:  # 等位数
        # nums[0,x-1] + nums[idx-1] + nums[-1]*(k-(x+1))
        return nums[:x] + [nums[idx-1]] + [nums[-1]] * (k - (x + 1))
    # 答案的位数比n的位数少，从nums中重复k-1次取最大数
    else:  
        return [nums[-1]] * (k - 1)

 


# x =Solution()
# print(x.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(x.minWindow("numsDOBECODEBnumsNC", "numsBC"))
print(max_num([2,4,9], 23121))
#22999