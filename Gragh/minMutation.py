class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1
        q = deque([(start, 0)])
        while q:
            cur, step = q.popleft()
            #cur 'AGTCGTA'
            # i 0 x A
            #依次尝试改变一个字符
            for i, x in enumerate(cur):
                for y in "ACGT":
                    #
                    if y != x:
                        nxt = cur[:i] + y + cur[i + 1:]
                        if nxt in bank:
                            if nxt == end:
                                return step + 1
                            #变换后在bank中 但不是end
                            bank.remove(nxt)
                            #
                            q.append((nxt, step + 1))
        return -1
