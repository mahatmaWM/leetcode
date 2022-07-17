#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    # 思路：这种需要在原位操作的，都是left,right双指针直接遍历数组。
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        left, right = 1, 1
        while right < len(nums):
            if nums[right] == nums[left - 1]:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left
# @lc code=end

