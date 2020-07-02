#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (48.45%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 52.5K
# Testcase Example:  '[1,3,5]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 注意数组中可能存在重复的元素。
#
# 示例 1：
#
# 输入: [1,3,5]
# 输出: 1
#
# 示例 2：
#
# 输入: [2,2,2,0,1]
# 输出: 0
#
# 说明：
#
#
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
#
#
#


# @lc code=start
class Solution:

    def findMin(self, nums: List[int]) -> int:
        # 如果长度为1或者本身还是升序
        if len(nums) == 1 or nums[0] < nums[-1]: return nums[0]

        # 采用左右闭合的方式
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            # 位置mid与左右两边的值大小，看mid是否出现在拐点处
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] < nums[mid - 1]:
                return nums[mid]

            # 位置mid与位置right比较，看拐点在右边 或者 左边
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
            # 元素可能相等，不断的前移动right指针
            elif nums[mid] == nums[right]:
                right = right - 1
        return nums[left]


# @lc code=end
