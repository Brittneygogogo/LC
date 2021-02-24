def decodeString(s):
    ans = ""
    multiStack = []
    ansStack = []
    multi = 0
    for c in s:
        if '0' <= c <= '9':
            multi = multi * 10 + int(c)
        elif c == '[':
            ansStack.append(ans)
            multiStack.append(multi)
            ans = ""
            multi = 0
        elif c.isalpha():
            ans += c
        else:
            last_res =ansStack.pop()
            cur_multi=multiStack.pop()
            ans =  last_res + cur_multi * ans

    return str(ans)

print(decodeString("3[a]2[b3[c]]"))