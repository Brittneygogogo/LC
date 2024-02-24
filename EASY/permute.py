'''
数组是动态改变的，原track随着添加和删除元素，最后res添加的时候会添加为空。
如果用数组需要最后copy一下track

回溯算法

'''
from typing import List

res = []
def permute(nums):
    track = []
    backtrack(nums, track, [False] * len(nums))
    return res
# def backtrack(nums, track):
#     if len(track) == len(nums):
#         res.append(track.copy())
#         return
#
#     for i in range(len(nums)):
#         if nums[i] in track:
#             continue
#         track.append(nums[i])
#         backtrack(nums, track)
#         track.remove(nums[i])
def backtrack(nums: List[int], track: List[int], used: List[bool]):
    # 触发结束条件
    if len(track) == len(nums):
        res.append(track.copy())
        return

    for i in range(len(nums)):
        # 排除不合法的选择
        if used[i]:
            # nums[i] 已经在 track 中，跳过
            continue
        # 做选择
        track.append(nums[i])
        used[i] = True
        # 进入下一层决策树
        backtrack(nums, track, used)
        # 取消选择
        track.pop()
        used[i] = False

print(permute([1,2,3]))
