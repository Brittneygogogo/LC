class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        def count(itera):
            ans = [0] * 26
            for letter in itera:
                ans[ord(letter) - ord('a')] += 1
            return ans

        def dominates(c1, c2):
            return all(x1 >= x2 for x1, x2 in zip(c1, c2))

        ans = None
        target = count(c.lower() for c in licensePlate if c.isalpha())
        for word in words:
            if ((len(word) < len(ans) or ans is None) and
                    dominates(count(word.lower()), target)):
                ans = word

        return ans

'''

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        def judge(dic, dic_word):
            for c in dic:
                if c not in dic_word:
                    return False
                if dic[c] > dic_word[c]:
                    return False
            return True
        
        dic = defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                dic[c.lower()] += 1
        res = ""
        for word in words:
            if res and len(word) >= len(res):
                continue
            dic_word = Counter(word)
            if judge(dic, dic_word):
                res = word
        return res
    
'''