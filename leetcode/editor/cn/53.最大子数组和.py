#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
class Solution1:
    # 动态规划，空间复杂度为O(n)
    # 转移方程，当前位置i的最大子序列和为: dp[i] = max(dp[i - 1] + nums[i], nums[i])
    # 可以继续优化空间复杂度为O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

class Solution:
    # 分治法，注意在原位操作nums
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        # 递归计算中点两边最大子序和，[l,r)
        mid = len(nums) // 2
        max_left = self.maxSubArray(nums[0:mid])
        max_right = self.maxSubArray(nums[mid:len(nums)])

        # 从mid-1往前计算最大子序和
        max_l = nums[mid - 1]
        tmp = 0
        for i in range(mid - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        # 从mid往后计算最大子序列和
        max_r = nums[mid]
        tmp = 0
        for i in range(mid, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)

        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)
# @lc code=end

