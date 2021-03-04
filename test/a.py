def max_heapify(heap, heapsize, root):
    left = root * 2 + 1
    right = left + 1
    largest = root
    if left < heapsize and heap[left] > heap[largest]:
        largest = left
    if right < heapsize and heap[right] > heap[largest]:
        largest = right
    if largest != root:
        heap[largest], heap[root] = heap[root], heap[largest]
        max_heapify(heap, heapsize, largest)


def build_max_heap(heap):
    heapsize = len(heap)
    for i in range((heapsize - 2) // 2, -1, -1):
        max_heapify(heap, heapsize, i)


def heap_sort(heap):
    build_max_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)

if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    # print(a)
    heap_sort(a)
    print(a)