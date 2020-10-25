

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
#         return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))


def romanToInt(s):
    ssss = 0
    d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
    for i, n in enumerate(s):
        print(i,n,s[max(i - 1, 0):i + 1])
        # print(s[max(i - 1, 0):i + 1], d[n])
        print(d.get(s[max(i - 1, 0):i + 1]), d[n])
        if d.get(s[max(i-1, 0):i + 1])!=None:
            ssss += d.get(s[max(i-1, 0):i + 1])
        else:
            ssss +=d [n]
    return ssss




print(romanToInt("MCMXCIV"))
