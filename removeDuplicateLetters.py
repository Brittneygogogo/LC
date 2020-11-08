
'''

要求一、通过inStack这个布尔数组做到栈stk中不存在重复元素。

要求二、我们顺序遍历字符串s，通过「栈」这种顺序结构的 push/pop 操作记录结果字符串，保证了字符出现的顺序和s中出现的顺序一致。

这里也可以想到为什么要用「栈」这种数据结构，因为先进后出的结构允许我们立即操作刚插入的字符，如果用「队列」的话肯定是做不到的。

要求三、我们用类似单调栈的思路，配合计数器count不断 pop 掉不符合最小字典序的字符，保证了最终得到的结果字典序最小。
'''


def removeDuplicateLetters(s):
    stk = []

    # 维护一个计数器记录字符串r中字符的数量
    # 因为输入为 ASCII 字符，大小 256 够用了
    count = dict()
    for i in s:
        count[i] += 1
    

    inStack = {}
    for c in s:
        # 每遍历过一个字符，都将对应的计数减一
        count[c] -= 1

        if inStack[c]: continue

        # 插入之前，和之前的元素比较一下大小
        # 如果字典序比前面的小，pop前面的元素
        while (stk or c < stk.pop()):
            # 若之后不存在栈顶元素了，则停止 pop
            if count[stk.pop()] == 0:
                break
            
            # 若之后还有，则可以 pop
            inStack[stk.pop()] = False
        
        stk.append(c)
        inStack[c] = True
    

    sb= []
    while stk:
        sb.append(stk.pop())
    
    return str(sb.reverse())



print(removeDuplicateLetters("babc"))
