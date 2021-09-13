# coding=utf-8
'''
最优O(n)
最坏O(n^2)
平均O(n^2)
空间O(1)
稳定
'''

def insert_sort(ls):
    """插入排序"""
    # 假设左边已排序，右边为未排序，每次从右边取一个数，遍历已排序的子序列，直到找到次数的位置。
    print("before: ", ls)
    #假设第一个已排序
    for j in range(1, len(ls)):
        for i in range(j, 0, - 1):
            if ls[i] < ls[i - 1]:
                ls[i], ls[i - 1] = ls[i - 1], ls[i]
        print(ls)
    print("after: ", ls)


if __name__ == "__main__":
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    insert_sort(ls)