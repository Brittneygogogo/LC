# p初始化为0，q初始化为1，遍历当前输出外观res以获得下一输出；
# q向右移动，直至q指向的值不等于p指向的值，此时q-p为p所指向的值的重复个数；
# p指向下一个不同的数字即让p=q，q重复上述步骤2.
# 加上特殊边界位置的处理：当q == len(res)刚好溢出。
#

def countAndSay( n):
    res = ["1"]  # 当前输出外观数列
    r = 1 # r初始为一，表示输出外观数列的第一项
    # 使用while进行循环，当找到输出外观数列第n项时结束。
    while r < n:
        r += 1              # 每进入一次while，就将r加1
        p, q = 0, 1         # p初始化为0，q初始化为1，遍历当前输出外观res以获得下一输出
                            # q向右移动，直至q指向的值不等于p指向的值，此时q-p为p所指向的值的重复个数
        tmp = []            # 用于存储下一输出外观数列
        while q <= len(res):
            if q == len(res):# 特殊边界位置的处理：当q == len(res)刚好溢出时
                tmp.extend([str(q-p),res[p]])
            elif res[q] != res[p]:
                tmp.extend([str(q-p),res[p]])
                p = q
            q += 1
        res = tmp
    return "".join(res)


print(countAndSay(6))