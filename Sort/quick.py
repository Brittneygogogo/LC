def quick_sort1(ls, start, end):
    """
        快速排序-1
        low 和 high 分别指向序列的头和尾
        low += 1， high -= 1
        在low自增过程中，直到找到大于 mid_val 的下标
        在high自增减过程中，直到找到小于 mid_val 的小标
        然后将这两个值交换
    """

    # 递归退出条件
    if start >= end:
        return

    low = start
    high = end
    mid_val = ls[low]

    while low < high:
        while low < high and ls[high] > mid_val:
            high -= 1
        ls[low] = ls[high]

        while low < high and ls[low] < mid_val:
            low += 1
        ls[high] = ls[low]

    ls[low] = mid_val

    print("mid:", mid_val, ls)

    quick_sort1(ls, start, low - 1)  # 左边的子序列
    quick_sort1(ls, low + 1, end)  # 右边的子序列

    return ls


def quick_sort2(ls):
    """快速排序-2"""

    # 递归退出条件
    if len(ls) <= 1:
        return ls

    left_ls, right_ls = [], []
    mid_val = ls[0]
    for i in range(1, len(ls)):
        if ls[i] < mid_val:
            left_ls.append(ls[i])
        else:
            right_ls.append(ls[i])

    print(left_ls, mid_val, right_ls)

    # 递归调用，左右子列表
    left_res = quick_sort2(left_ls)
    right_res = quick_sort2(right_ls)

    return left_res + [mid_val] + right_res


if __name__ == "__main__":
    ls1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    ls2 = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print("before：", ls1)
    res1 = quick_sort1(ls1, 0, len(ls1) - 1)
    print("quick sort1: ", res1)

    # print("-" * 50)
    # print("before: ", ls2)
    # res2 = quick_sort2(ls2)
    # print("quick sort2：", res2)