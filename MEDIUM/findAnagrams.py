class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        '''
        解法1：滑动窗口
        '''
        res = []
        window = {}     # 记录窗口中各个字符数量的字典
        needs = {}      # 记录目标字符串中各个字符数量的字典
        for c in p: needs[c] = needs.get(c, 0) + 1  # 统计目标字符串的信息

        length, limit = len(p), len(s)
        left = right = 0                    # 定理两个指针，分别表示窗口的左、右界限

        while right < limit:
            c = s[right]
            if c not in needs:              # 当遇到不需要的字符时
                window.clear()              # 将之前统计的信息全部放弃
                left = right = right + 1    # 从下一位置开始重新统计
            else:
                window[c] = window.get(c, 0) + 1            # 统计窗口内各种字符出现的次数
                if right-left+1 == length:                  # 当窗口大小与目标字符串长度一致时
                    if window == needs: res.append(left)    # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    window[s[left]] -= 1                    # 并将移除的字符数量减一
                    left += 1                               # left右移

                right += 1                                  # right右移
        return res

'''

        while right < len(listS):
            curR = listS[right]
            #将右窗口当前访问到的元素curR的个数加1
            if curR not in window:
                window[curR] = 1
            else:
                window[curR] += 1
            right += 1

            #当window数组中curR比needs数组中对应元素的个数要多的时候就应该移动左窗口的指针，因为这样肯定就不满足要求了
            #这一步是最关键的
            while window[curR] > needs.setdefault(curR, 0):
                curL = listS[left]
                left += 1
                #将左窗口当前访问到的元素curL个数减一
                window[curL] -= 1

            #如果窗口的长度和p的长度相等，这个时候一定就是满足提议的字母异位词了，之所以这样是因为上面的那个while循环决定的
            if right - left == len(listP):
                ans.append(left)
        return ans

'''