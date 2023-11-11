from typing import List
'''
https://leetcode.cn/problems/basic-calculator/solutions/465311/chai-jie-fu-za-wen-ti-shi-xian-yi-ge-wan-zheng-j-2/?envType=study-plan-v2&envId=top-interview-150
'''

def calculate(s: str) -> int:
    def helper(s: List) -> int:
        stack = []
         # 记录num前的符号，初始化为 +
        sign = '+'
        num = 0
        # print(s)
        while len(s) > 0:
            c = s.pop(0)
            # 如果是数字，连续读取到 num
            if c.isdigit():
                num = 10 * num + int(c)
            # 遇到左括号开始递归计算 num
            if c == '(':
                num = helper(s)
                # print(num)
            # 如果不是数字，就是遇到了下一个符号，之前的数字和符号就要存进栈中
            if (not c.isdigit() and c != ' ') or len(s) == 0:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack[-1] = stack[-1] * num
                elif sign == '/':
                    # python 除法向 0 取整的写法
                    stack[-1] = int(stack[-1] / float(num))

                num = 0
                sign = c
            # 遇到右括号返回递归结果
            if c == ')': break
            # print(stack)
        return sum(stack)

    return helper(list(s))

print(calculate("1 + 1"))