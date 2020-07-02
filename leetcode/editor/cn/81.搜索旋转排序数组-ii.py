#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (35.63%)
# Likes:    179
# Dislikes: 0
# Total Accepted:    31.1K
# Total Submissions: 87.2K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 示例 1:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
#
#
# 示例 2:
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
# 进阶:
#
#
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums  可能包含重复元素。
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
#
#


# @lc code=start
class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0: return False

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            print('mid={}'.format(mid))
            if nums[mid] == target: return True
            # 说明右边是升序的
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 说明左边是升序的
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] == nums[right]:
                right = right - 1
        if nums[left] == target: return True
        return False


# @lc code=end
