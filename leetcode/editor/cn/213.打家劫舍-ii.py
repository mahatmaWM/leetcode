#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
# https://leetcode-cn.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (38.23%)
# Likes:    291
# Dislikes: 0
# Total Accepted:    38.5K
# Total Submissions: 100.6K
# Testcase Example:  '[2,3,2]'
#
#
# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [2,3,2]
# 输出: 3
# 解释: 你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
#
# 示例 2:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
# 偷窃到的最高金额 = 1 + 3 = 4 。
#
## 这个题多了环的条件，在这个约束下就多了个不同时偷第一个和最后一个就可以了。
# 所以，两种偷的情况：
# 第一种不偷最后一个房间，
# 第二种不偷第一个房间，求这两种偷法能获得的最大值。
# 所以只多了一个切片的过程。


# @lc code=start
class Solution:

    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            if not nums: return 0
            if len(nums) == 1: return nums[0]

            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[-1]

        if not nums: return 0
        if len(nums) == 1: return nums[0]
        return max(helper(nums[0:-1]), helper(nums[1:]))


# @lc code=end
