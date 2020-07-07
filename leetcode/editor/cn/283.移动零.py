#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (61.15%)
# Likes:    614
# Dislikes: 0
# Total Accepted:    159.4K
# Total Submissions: 260.6K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例:
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明:
#
#
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
#
#
#

# @lc code=start
class Solution:
    # 思路：原位操作都是双指针
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in nums:
            if right != 0:
                nums[left] = right
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0
# @lc code=end

