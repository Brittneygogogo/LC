
'''


[3,4,2,1,2]

'''


def nextGreaterElement(nums):
    res = [0]*len(nums)
    s = []
    nums = nums[::-1]
    # 倒着往栈里放
    for i, value in enumerate(nums):
        # 判定个子高矮
        while (s and s[0] <= value):
            # 矮个起开，反正也被挡着了。。。
            s.pop()
        # nums[i] 身后的 next great number
        if s:
            res[i] = s[-1]
        else:
            res[i] = -1
        #
        s.append(nums[i])

    return res


print(nextGreaterElement([2,1,2,4,3]))