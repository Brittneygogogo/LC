'''
子集问题可以利用数学归纳思想，假设已知一个规模较小的问题的结果，思考如何推导出原问题的结果。也可以用回溯算法，要用 start 参数排除已选择的数字。

组合问题利用的是回溯思想，结果可以表示成树结构，我们只要套用回溯算法模板即可，关键点在于要用一个 start 排除已经选择过的数字。从后面的开始算

'''


res = []
def subsets(nums):
    track = []
    backtrack(nums, 0, track)
    return res

def backtrack(nums, start, track):
    res.append(track.copy())

    for i in range(start, len(nums)):
        if nums[i] in track:
            continue
        track.append(nums[i])
        backtrack(nums, i+1 , track)
        track.pop()


print(subsets([1,2,3]))
