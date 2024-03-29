'''
堆排序是一种选择排序，它的最坏，最好，平均时间复杂度均为O(nlogn)，空间O(1),它也是不稳定排序。

　　a.将无序序列构建成一个堆，根据升序降序需求选择大顶堆或小顶堆;

　　b.将堆顶元素与末尾元素交换，将最大元素"沉"到数组末端;

　　c.重新调整结构，使其满足堆定义，然后继续交换堆顶元素与当前末尾元素，反复执行调整+交换步骤，直到整个序列有序。

'''
def max_heapify(heap, heapSize, root):  # 调整列表中的元素并保证以root为根的堆是一个大根堆
    '''
    给定某个节点的下标root，这个节点的父节点、左子节点、右子节点的下标都可以被计算出来。
    父节点：(root-1)//2
    左子节点：2*root + 1
    右子节点：2*root + 2  即：左子节点 + 1
    '''
    left = 2 * root + 1
    right = left + 1
    largest = root

    if left < heapSize and heap[largest] < heap[left]:
        largest = left
    if right < heapSize and heap[largest] < heap[right]:
        largest = right
    if largest != root:  # 如果做了堆调整则larger的值等于左节点或者右节点的值，这个时候做堆调整操作
        heap[largest], heap[root] = heap[root], heap[largest]
        # 递归的对子树做调整
        max_heapify(heap, heapSize, largest)

def build_max_heap(heap):  # 构造一个堆，将堆中所有数据重新排序
    heapSize = len(heap)
    for i in range((heapSize-2) // 2, -1, -1):  # 自底向上建堆
        max_heapify(heap, heapSize, i)

def heap_sort(heap):  # 将根节点取出与最后一位做对调，对前面len-1个节点继续进行堆调整过程。
    build_max_heap(heap)
    # 调整后列表的第一个元素就是这个列表中最大的元素，将其与最后一个元素交换，然后将剩余的列表再递归的调整为最大堆
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)

# 测试
if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    # print(a)
    heap_sort(a)
    print(a)
    # b = [random.randint(1,1000) for i in range(1000)]
    # print(b)
    # heap_sort(b)
    # print(b)
#---------------------------------------------------------------------------------------------------------------------------

# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1  # left = 2*i + 1
#     r = 2 * i + 2  # right = 2*i + 2
#
#     if l < n and arr[i] < arr[l]:
#         largest = l
#
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # 交换
#         heapify(arr, n, largest)
#

# def heapSort(arr):
#     n = len(arr)
#
#     # Build a maxheap.
#     for i in range(n, -1, -1):
#         heapify(arr, n, i)
#
#         # 一个个交换元素
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # 交换
#         heapify(arr, i, 0)
#
#
# arr = [12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print("排序后")
# for i in range(n):
#     print("%d" % arr[i]),
