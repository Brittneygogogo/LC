'''
最好O(n)
最坏O(n^2)
平均O(n^1.3-2)
空间O(1)
不稳定
'''

def shell_sort(ls):
    """希尔排序"""
    print("before: ", ls)

    step = len(ls) // 2  # 初始步长

    while step > 0:
        # 插入排序
        for j in range(step, len(ls)):
            print("j", j, ls[j:])
            for i in range(j, 0, - step):
                print("i", i)
                if ls[i] < ls[i - step]:
                    ls[i], ls[i - step] = ls[i - step], ls[i]
                    # print(ls)
        print("step\t", step)
        step //= 2
        print(ls)
    print("shell_sort ：", ls)


if __name__ == "__main__":
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    shell_sort(ls)