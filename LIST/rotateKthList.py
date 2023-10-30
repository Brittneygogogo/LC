
def rotateKList(nums, k):
    nums[:] = reversed(nums[:])
# 或 nums.reverse()
    print(nums)
    nums[:k] = reversed(nums[:k])
    print(nums)
    nums[k:] = reversed(nums[k:])
    return nums


'''def reverseX(nums):
    j = len(nums) - 1
    i = 0
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums'''

# print(reverseX([1,2,3,4,5,6,7]))


print(rotateKList([1,2,3,4,5,6,7], 4))