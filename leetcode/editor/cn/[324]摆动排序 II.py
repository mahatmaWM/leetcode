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


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findKthLargest(self, nums, k):
        import random
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = self.partition_around_pivot(left, right, pivot_idx,
                                                        nums)
            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:  # new_pivot_idx < k - 1.
                left = new_pivot_idx + 1

    def partition_around_pivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1
        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

# leetcode submit region end(Prohibit modification and deletion)
