# class Solution(object):
#     def nextGreatestLetter(self, letters, target):
#         index = bisect.bisect(letters, target)
#         return letters[index % len(letters)]

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        seen = set(letters)
        for i in range(1, 26):
            cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
            if cand in seen:
                return cand


x = Solution()
print(x.nextGreatestLetter(["c", "f", "j"], "a"))