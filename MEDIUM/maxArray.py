

def maxSubArray(nums):
    n = len(nums)
    if (n == 0):return 0
    dp_0 = nums[0]
    res = dp_0
    for i in range(n):
        dp_1 = max(nums[i], nums[i] + dp_0)
        dp_0 = dp_1
        res = max(res, dp_1)

    return res

print(maxSubArray([1,-1,3]))