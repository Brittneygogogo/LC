def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    if not nums:
        return 0
    # 两个指针i和j
    j = 0
    for cur in range(len(nums)):
        # 当前元素!=0，就把其交换到左边，等于0的交换到右边
       if nums[cur]:
            nums[j],nums[cur] = nums[cur],nums[j]
            j += 1
    return nums

print(moveZeroes([0,1,0,3,0,4,12]))