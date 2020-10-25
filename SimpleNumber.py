#数组中的全部元素的异或运算结果即为数组中只出现一次的数字。
def singleNumber(nums):
    x = 0
    for i in nums:
        x ^= i
    return  x

print(singleNumber([2,3,2,6,8,6,3]))