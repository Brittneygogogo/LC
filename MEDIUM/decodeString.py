'''
https://leetcode.cn/problems/decode-string/solutions/19447/decode-string-fu-zhu-zhan-fa-di-gui-fa-by-jyd/?envType=study-plan-v2&envId=top-100-liked
括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。
'''
def decodeString(s):
    ans = ""
    multiStack = []
    ansStack = []
    multi = 0
    for c in s:
        #变数字
        if '0' <= c <= '9':
            multi = multi * 10 + int(c)
        elif c == '[':
            #一起进栈并变为空
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