#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
# https://leetcode-cn.com/problems/integer-break/description/
#
# algorithms
# Medium (56.09%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    28.8K
# Total Submissions: 51.4K
# Testcase Example:  '2'
#
# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。
#
# 示例 1:
#
# 输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。
#
# 示例 2:
#
# 输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
#
# 说明: 你可以假设 n 不小于 2 且不大于 58。
#
#

# @lc code=start
class Solution:
    # 动态规划，dp[i]表示对数字i拆分，能得到的最大乘积
    # 那么对j < i，可以拆成j与i-j两个数字，dp[j]*dp[i-j]两个可以继续拆分，j*dp[i-j] 三种情况
    def integerBreak(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[j] * dp[i - j], j * (i - j), j * dp[i - j]))
        return dp[-1]

# @lc code=end
