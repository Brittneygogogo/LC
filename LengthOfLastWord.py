def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    space = 0
    l = 0
    for i in range(len(s)):
        if s[i] != " ":
            l += 1
        else:
            l = 0
    return l

# print(lengthOfLastWord("hello world"))
print(lengthOfLastWord("a"))
