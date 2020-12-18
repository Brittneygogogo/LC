
'''
寻找回文串的核心思想是从中心向两端扩展
因为回文串长度可能为奇数也可能是偶数，长度为奇数时只存在一个中心点，而长度为偶数时存在两个中心点，所以上面这个函数需要传入l和r。



??????????
0 4
Traceback (most recent call last):
  File "/Users/brittney/PycharmProjects/LC/palinfrome.py", line 17, in <module>
    print(palindrome("abcba", 2, 2))
  File "/Users/brittney/PycharmProjects/LC/palinfrome.py", line 11, in palindrome
    print(s[l + 1, r - 1])
TypeError: string indices must be integers



'''

def palindrome(s, l, r):
    # 防止索引越界
    while (l >= 0 and r < len(s) and s[l] == s[r]):
        # 向两边展开
        l -= 1
        r += 1
    # 返回以 s[l] 和 s[r] 为中心的最长回文串
    print(l+1, r-1)
    # print(s[l + 1, r - 1])
    return s[l + 1, r - l- 1]




print(palindrome("abcba", 2, 2))