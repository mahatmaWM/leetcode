#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.39%)
# Likes:    298
# Dislikes: 0
# Total Accepted:    62.4K
# Total Submissions: 186.9K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
#
#
#
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#
#
#

# @lc code=start
class Solution:
    # 和62题类似的思路。
    # dp[i][j] = 0  # if grid[i][j] == 1
    # dp[i][j] = dp[i-1][j] + dp[i][j-1]  # if grid[i][j] == 0
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * m for _ in range(n)]
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0

        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 0:
                    # 更新下面的方格
                    if i + 1 < n: dp[i + 1][j] += dp[i][j]
                    # 更新右边的方格
                    if j + 1 < m: dp[i][j + 1] += dp[i][j]
                else:  # 如果有障碍物，则标记为0
                    dp[i][j] = 0
        return dp[n - 1][m - 1]
# @lc code=end

