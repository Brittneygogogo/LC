'''

　　　　最优时间复杂度：O(n)（表示遍历一次发现没有任何可以交换的元素排序结束，在内循环可以做一个标识判断，如果首次循环没有任何交换，则跳出）

　　　　最坏复杂度：O(n2)

　　　　稳定性：稳定
可能需要运行多次
一次不够

'''
#正序
def bubble_sort(ls):
    """冒泡排序"""
    print("before: ", ls)
    #正序
    for i in range(0, len(ls) - 1):
        # i = [0, 1, ...., len(ls) - 2]，每次比较的第一个数的下标
        # j = [i + 1, i + 2, ..., len(ls) - 1]，每次比较的第二个数的下标
        for j in range(i + 1, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
        print(ls)
    print("after: ", ls)



#倒序
def bubble_sort2(ls):
    """冒泡排序"""
    print("before：", ls)
    for j in range(len(ls) - 1, 0, -1):
        # j = [len(ls) - 1, len(ls) - 2, ..., 1], 每次需要比较的次数
        # i = [0, 1, 2, ..., j - 1]，需要比较的下标
        for i in range(j):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
        print(ls)
    print("after：", ls)

if __name__ == "__main__":
    ls1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    ls2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    bubble_sort(ls1)
    print("-" * 50)
    bubble_sort2(ls2)