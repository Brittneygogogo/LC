def dailyTemperatures(T):
    s = []
    ans = []
     # 这里放元素索引，而不是元素
    for i in range(len(T)):
        while ( not s and T[s.top()] <= T[i]):
            s = s[:-1]
        if s:

            ans[i] = s[-1] - i # 得到索引间距
        s   (i) # 加入索引，而不是元素
    
    return ans


