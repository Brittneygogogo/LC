res = []

def permute(nums):
    track = []
    backtrack(nums, track)
    return res

def backtrack(nums, track):
    if len(track) == len(nums):
        res.append(track)
        return 1
    for i in range(len(nums)):
        if nums[i] in track:
            continue
        track.append(nums[i])
        backtrack(nums, track)
        track.pop()


print(permute([1,2,3]))