# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        # 按区间的 start 升序排列 [(1, 0), (2, 5), (3, 1)] 比较x[1]大小再合并
        intervals.sort(key=lambda a: a[0])

        res.append(intervals[0])
        for curr in intervals[1:]:
            # res 中最后一个元素的引用
            last = res[-1]
            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                # 处理下一个待合并区间
                res.append(curr)
        return res

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        merged = []
        for interval in intervals:
            # 如果列表为空，或者当前区间与上一区间不重合，直接添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 否则的话，我们就可以与上一区间进行合并
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

x = Solution()
print(x.merge([[1,3],[2,6],[8,10],[15,18]]))