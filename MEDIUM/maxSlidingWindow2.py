

def maxSlidingWindow2(nums, k):
    n = len(nums)
    m =[]
    for i in range(n-k+1):
        l = nums[i:i+k]
        print(l)
        print(max(l))
        m.append(max(l))
    return m


# print(maxlength([1,3,-1,-3,5,3,6,7], 3))
print(maxSlidingWindow2([9,11], 2))
