'''
最优时间复杂度：O(n^2)
最坏时间复杂度：O(n^2)
稳定性：不稳定（考虑升序每次选择最大的情况）

'''
def selection_sort(ls):
    """选择排序"""
    # 假设左边为已排序，右边为未排序

    print("before：", ls)
    for i in range(0, len(ls) - 1):
        # i = [0, 1, 2,,, len(ls) - 2]
        # j = [i + 1, i + 2,,, len(ls) - 1]
        min_index = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_index]:
                min_index = j
        if min_index != i:
            ls[min_index], ls[i] = ls[i], ls[min_index]
        print(ls)
    print("after：", ls)


if __name__ == "__main__":
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    selection_sort(ls)
