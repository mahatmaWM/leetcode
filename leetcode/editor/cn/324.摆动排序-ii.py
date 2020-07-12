#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#
# https://leetcode-cn.com/problems/wiggle-sort-ii/description/
#
# algorithms
# Medium (35.53%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    12.1K
# Total Submissions: 34.1K
# Testcase Example:  '[1,5,1,1,6,4]'
#
# 给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
#
# 示例 1:
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
# 你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
#
#
# 思路：
#
# 如果是有序数组的话，这个问题就很好处理了。
# 直接两个指针调整为摆动排序，其中：0 2的位置放小的一半数字，1 3放大的一半数字。
#    # 先排序的做法
#     def wiggleSort1(self, nums):
#         n = len(nums)
#         nums = sorted(nums, reverse=True)
#         p1, p2 = 0, (n + 1) // 2
#         res = [float('-inf')] * n
#         for i in range(n):
#             if i % 2 == 0:
#                 res[i] = nums[p2]
#                 p2 += 1
#             else:
#                 res[i] = nums[p1]
#                 p1 += 1
#         return res
# @lc code=start
class Solution:
    # 找到中位数，然后将大于或者小于中位数数字调整好。
    # but 这个时候再按照有序的方式去调整的话，结果是错的。
    # 因为不能保证两边的子数组是有序的，这个时候要借用三色荷兰国旗排序方法进行调整。
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # [left, right]两边都是闭区间，且从0开始，返回索引下标
        def partition(num, left, right):
            # 选取left位置为pivot
            pivot = num[left]
            while left < right:
                while left < right and num[right] <= pivot:
                    right -= 1
                num[left] = num[right]
                while left < right and num[left] >= pivot:
                    left += 1
                num[right] = num[left]
            num[left] = pivot
            return left

        # [left, right]两边都是闭区间，且从0开始，k从1开始
        def kth_largest(num, left, right, k):
            index = partition(num, left, right)
            if index == k - 1: return num[index]
            if index < k - 1:
                return kth_largest(num, index + 1, right, k)
            else:
                return kth_largest(num, left, index - 1, k)

        n = len(nums)
        if n <= 1: return
        mid = kth_largest(nums, 0, n - 1, (n + 1) // 2)

        # O(n)时间原地修改，类似75题的三色荷兰国旗排序算法。
        # 但数组是全部奇数位下标和偶数位下标的拼接
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


# @lc code=end
