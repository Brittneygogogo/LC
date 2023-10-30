def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    space = 0
    l = 0
    for i in range(len(s)-1, -1 , -1):
        if s[i] != " ":
            l += 1
        else:
            return l

# print(lengthOfLastWord("hello world"))
print(lengthOfLastWord("a bb"))
