#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
# https://leetcode-cn.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (51.38%)
# Likes:    2073
# Dislikes: 0
# Total Accepted:    257.3K
# Total Submissions: 500.8K
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
#
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
#


# @lc code=start
class Solution1:
    # 动态规划，空间复杂度为O(n)
    # 转移方程，当前位置i的最大子序列和为: dp[i] = max(dp[i - 1] + nums[i], nums[i])
    # 可以继续优化空间复杂度为O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


class Solution:
    # 分治法
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算中点两边最大子序和
            mid = len(nums) // 2

            max_left = self.maxSubArray(nums[0:mid])
            max_right = self.maxSubArray(nums[mid:len(nums)])

            # 从mid往前往后的中间最大子序和
            max_l = nums[mid - 1]
            tmp = 0
            for i in range(mid - 1, -1, -1):
                tmp += nums[i]
                max_l = max(tmp, max_l)

            max_r = nums[mid]
            tmp = 0
            for i in range(mid, len(nums)):
                tmp += nums[i]
                max_r = max(tmp, max_r)

            # 返回三个中的最大值
            return max(max_right, max_left, max_l + max_r)


# @lc code=end
