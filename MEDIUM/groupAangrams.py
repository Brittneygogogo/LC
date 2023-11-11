import collections
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())


x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))