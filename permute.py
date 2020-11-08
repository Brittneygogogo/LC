'''
数组是动态改变的，原track随着添加和删除元素，最后res添加的时候会添加为空。
如果用数组需要最后copy一下track

回溯算法

'''



res = []
def permute(nums):
    track = []
    backtrack(nums, track)
    return res

def backtrack(nums, track):
    if len(track) == len(nums):
        res.append(track.copy())
        return

    for i in range(len(nums)):
        if nums[i] in track:
            continue
        track.append(nums[i])
        backtrack(nums, track)
        track.remove(nums[i])


print(permute([1,2,3]))
