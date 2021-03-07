def quick_sort1(ls, start, end):
    """
        快速排序
        left 和 right 分别指向序列的头和尾
        left += 1， right -= 1
        在left自增过程中，直到找到大于 mid_val 的下标
        在right自增减过程中，直到找到小于 mid_val 的小标
        然后将这两个值交换
    """
    # start=end ,证明要处理的数据只有一个
    # start>end ,证明右边没有数据
    # 递归退出条件
    if start >= end:
        return

    left = start
    right = end
    # 把0位置的数据，认为是中间值
    mid_val = ls[left]

    while left < right:
        # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
        while left < right and ls[right] > mid_val:
            right -= 1
        ls[left] = ls[right]
        # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
        while left < right and ls[left] < mid_val:
            left += 1
        ls[right] = ls[left]
    # while结束后，把mid放到中间位置，left=right
    ls[left] = mid_val

    print("mid:", mid_val, ls)
    # print("ls", ls)
    quick_sort1(ls, start, left - 1)  # 左边的子序列
    quick_sort1(ls, left + 1, end)  # 右边的子序列

    return ls


def quick_sort2(ls):
    """快速排序"""

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

def quick_sort3(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

L = [5, 9, 1, 11, 6, 7, 2, 4]

# print(quick_sort3(L))


if __name__ == "__main__":
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    print("before：", ls)
    res1 = quick_sort1(ls, 0, len(ls) - 1)
    print("quick sort1: ", res1)

    print("-" * 50)
    print("before: ", ls)
    res2 = quick_sort2(ls)
    print("quick sort2：", res2)
    print("-" * 50)
    print("quick sort3：", quick_sort3(ls))