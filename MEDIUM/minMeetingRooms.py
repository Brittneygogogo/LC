class Solution:
    def minMeetingRooms(self, intervals) -> int:
        events = [(iv[0], 1) for iv in intervals] + [(iv[1], -1) for iv in intervals]
        events.sort()
        print(events)
        ans = cur = 0
        for _, e in events:
            cur += e
            ans = max(ans, cur)
        return ans

x = Solution()
print(x.minMeetingRooms([[0,30],[5,10],[15,20]]))