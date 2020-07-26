#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (39.67%)
# Likes:    462
# Dislikes: 0
# Total Accepted:    98.6K
# Total Submissions: 248.5K
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
#


# @lc code=start
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # [left, right)
        def lower_bound(left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target and (mid == 0 or nums[mid - 1] < target): return mid

                # 因为是找下界，所以相等的时候要往前逼近
                if nums[mid] >= target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
            return -1

        # [left, right)
        def upper_bound(left, right):
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] > target): return mid

                # 因为是找上界，所以相等的时候要往后逼近
                if nums[mid] <= target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid
            return -1

        if not nums: return -1, -1
        left, right = 0, len(nums)
        return lower_bound(left, right), upper_bound(left, right)


# @lc code=end
