import collections


class Solution:
    def groupAnagrams(self, strs):
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)

        return list(mp.values())


x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))