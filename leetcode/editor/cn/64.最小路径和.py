#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (65.70%)
# Likes:    486
# Dislikes: 0
# Total Accepted:    91.4K
# Total Submissions: 139.1K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
# 示例:
#
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
#
#
#


# @lc code=start
class Solution:
    # 设置好保存结果的dp数组。依次遍历原始数组，在dp中保存最优结果即可。
    def minPathSum(self, grid: List[List[int]]) -> int:
        r_len = len(grid)
        c_len = len(grid[0])
        dp = [[0] * c_len for i in range(r_len)]
        for i in range(r_len):
            for j in range(c_len):
                if i == j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    y = 2147483647 if i - 1 < 0 else dp[i - 1][j]
                    x = 2147483647 if j - 1 < 0 else dp[i][j - 1]
                    dp[i][j] = grid[i][j] + min(x, y)
        return dp[-1][-1]


# @lc code=end
