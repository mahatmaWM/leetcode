def quick_sort(arr, l, r):
    if l < r:
        q = partition2(arr, l, r)
        quick_sort(arr, l, q - 1)
        quick_sort(arr, q + 1, r)

# 选取一个基准值pivot，小数在左大数在右
def partition(arr, l, r):
    pivot = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 将哨兵交换到i+1位置
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1


def partition1(arr, l, r):
    if l >= r: return 0
    pivot = arr[l]
    i, j = l + 1, r
    while True:
        while arr[i] <= pivot:
            i += 1
            if i == r: break
        while arr[j] > pivot:
            j -= 1
            if j == l: break
        if i >= j: break
        arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[i] = arr[i], arr[l]
    return i

def partition2(array, left, right):
    key = array[left]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[left] = key
    return left

arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
l, r = 0, len(arr) - 1
quick_sort(arr, l, r)
print(arr)