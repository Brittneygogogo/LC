
def rotateKList(nums, k):
    nums[:] = reversed(nums[:])
# 或 nums.reverse()
    print(nums)
    nums[:k] = reversed(nums[:k])
    print(nums)
    nums[k:] = reversed(nums[k:])
    print(nums)
    return nums

print(rotateKList([1,2,3,4,5,6,7], 4))