# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。 
#
# 如果数组中不存在目标值，返回 [-1, -1]。 
#
# 示例 1: 
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2: 
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# Related Topics 数组 二分查找

# 数组已升序排序。
# 1、使用二分查找寻找开始位置。
# 2、使用二分查找寻找结束位置。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1, -1
        left, right = -1, -1

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if nums[start] == target:
            left = start

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end + 1) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        if nums[end] == target:
            right = end

        return left, right

# leetcode submit region end(Prohibit modification and deletion)
