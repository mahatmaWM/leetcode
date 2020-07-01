#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
# https://leetcode-cn.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (42.58%)
# Likes:    294
# Dislikes: 0
# Total Accepted:    46.7K
# Total Submissions: 109.8K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s
# 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。
#
# 示例: 
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
#
#
# 进阶:
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
#
#

# @lc code=start
class Solution:
    # 双指针left, right
    # 移动right累加total, 当total >= s时, 右移left找出最短的sub array, 跳出内层循环后right继续往右走, 直到刷完nums
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s: return 0
        res = len(nums)
        left, total = 0, 0
        for right, i in enumerate(nums):
            total += i
            while total >= s:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
        return res
# @lc code=end

