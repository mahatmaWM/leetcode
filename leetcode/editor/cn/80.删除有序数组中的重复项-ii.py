#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    # 26题一样方法，因为允许出现两个相同的，所以从2开始
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)
        left, right = 2, 2
        while right < len(nums):
            if nums[right] == nums[left - 1] == nums[left - 2]:
                right += 1
            else:
                nums[left] = nums[right]
                left += 1
                right += 1
        return left
# @lc code=end

