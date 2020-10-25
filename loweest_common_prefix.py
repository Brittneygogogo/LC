def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    lxp = ""
    for index, char in enumerate(strs[0]):
        for s in strs[1:]:
            if index == len(s):
                return lxp
            if char == s[index]:
                continue
            else: 
                return lxp
        lxp += char

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))