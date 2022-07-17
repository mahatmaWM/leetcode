#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#

# @lc code=start
class Solution:

    def sortArray(self, nums: List[int]) -> List[int]:
        import random

        def quick_sort(arr, l, r):
            if l < r:
                q = partition2(arr, l, r)
                quick_sort(arr, l, q - 1)
                quick_sort(arr, q + 1, r)

        # 算法导论上比较精妙的分割方法
        # [l,r]两边都闭区间
        def partition(arr, l, r):
            # 设置哨兵
            pivot = arr[r]
            i = l - 1
            for j in range(l, r):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            # 将哨兵交换到i+1位置
            arr[i + 1], arr[r] = arr[r], arr[i + 1]
            return i + 1

        # 比较直观容易理解的分割实现
        def partition2(array, left, right):
            # 选最左为哨兵，就先从右遍历；相反也可以
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

        random.shuffle(nums)
        quick_sort(nums, 0, len(nums) - 1)
        return nums
# @lc code=end
