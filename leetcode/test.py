def quicksort(num, low, high):  # 快速排序
    if low < high:
        location = partition(num, low, high)
        quicksort(num, low, location - 1)
        quicksort(num, location + 1, high)


# 返回索引下标i，i左边的数字都比num[i]小，右边的都比它大
def partition(num, low, high):
    # 选取low位置为pivot
    pivot = num[low]
    while low < high:
        while low < high and num[high] >= pivot:
            high -= 1
        num[low] = num[high]
        while low < high and num[low] <= pivot:
            low += 1
        num[high] = num[low]
    num[low] = pivot
    return low


def kth_smallest(num, low, high, k):
    index = partition(num, low, high)
    if index == k: return num[index]
    if index < k:
        return kth_smallest(num, index + 1, high, k)
    else:
        return kth_smallest(num, low, index - 1, k)


pai = [5, 4, 6, 5]
# quicksort(pai, 0, len(pai) - 1)
# print(pai)
print(kth_smallest(pai, 0, len(pai) - 1, 0))
