# 给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
#
# 示例 1: 
#
# 输入: nums = [1, 5, 1, 1, 6, 4]
# 输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
#
# 示例 2: 
#
# 输入: nums = [1, 3, 2, 2, 3, 1]
# 输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
#
# 说明: 
# 你可以假设所有输入都会得到有效的结果。
#
# 进阶: 
# 你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
# Related Topics 排序

# ==========================================================================================
# 有序数组，这个问题就很好处理了。
#
# 思路：二分查找的方法找到第K大的元素，将左右两边的数字调整好，然后两个指针调整为摆动排序。
# 其中：0 2 4的位置放小的一半数字，1 3 5放大的一半数字。
# ==========================================================================================
# 在有序数组lst中查找val值的位置，二分查找递归和循环的两种方式。
# def binary_search_recursion(lst, val, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if lst[mid] < val:
#         return binary_search_recursion(lst, val, mid + 1, end)
#     if lst[mid] > val:
#         return binary_search_recursion(lst, val, start, mid - 1)
#     return mid
#
#
# def binary_search_loop(lst, val):
#     start, end = 0, len(lst) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if lst[mid] < val:
#             start = mid + 1
#         elif lst[mid] > val:
#             end = mid - 1
#         else:
#             return mid
#     return None
# ==========================================================================================


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 返回索引下标i，i左边的数字都比num[p0]小，右边的都比它大
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

        def median(arr, n):
            return kth_smallest(arr, 0, n - 1, n // 2)

        n = len(nums)
        if n <= 1: return
        mid = median(nums, n)
        print(mid)
        print(nums)

        # O(n)时间原地修改，类似三色荷兰国旗排序算法，但数组是全部奇数位下标和偶数位下标的拼接
        # 这里的逻辑没有看懂？？
        p0 = curr = 0
        p2 = n - 1
        n |= 1  # 取向上离n最近的奇数
        while curr <= p2:
            ii, jj, kk = map(lambda x: (x * 2 + 1) % n, [p0, curr, p2])
            if nums[jj] > mid:
                nums[jj], nums[ii] = nums[ii], nums[jj]
                p0 += 1
                curr += 1
            elif nums[jj] < mid:
                nums[jj], nums[kk] = nums[kk], nums[jj]
                p2 -= 1
            else:
                curr += 1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [4,5,5,6]
    print(Solution().wiggleSort(nums=nums))
    print(nums)
    #
    # [1, 3, 2, 2, 2, 1, 1, 3, 1, 1, 2]
    # 测试结果: [3, 2, 1, 2, 1, 3, 1, 2, 1, 2, 1]
    # 期望结果: [2, 3, 1, 3, 1, 2, 1, 2, 1, 2, 1]
