def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    i = 0
    j = 0
    for _ in range(len(nums)):
        if nums[j] == val:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    nums = nums[i:]
    print(nums)
    return len(nums)

print(removeElement([3,2,2,3], 3))
print(removeElement([0,1,2,2,3,0,4,2], 2))