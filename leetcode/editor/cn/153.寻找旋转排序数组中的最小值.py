#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (50.95%)
# Likes:    197
# Dislikes: 0
# Total Accepted:    53.1K
# Total Submissions: 104.3K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
#
# 请找出其中最小的元素。
#
# 你可以假设数组中不存在重复元素。
#
# 示例 1:
#
# 输入: [3,4,5,1,2]
# 输出: 1
#
# 示例 2:
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
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
            if  nums[mid] < nums[mid - 1]:
                return nums[mid]
            # 位置mid与位置right比较，看拐点在右边 或者 左边
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid - 1
# @lc code=end

