# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。
# 机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？ 
#
# 
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？ 
#
# 说明：m 和 n 的值均不超过 100。 
#
# 示例 1: 
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 
#
# 示例 2: 
#
# 输入: m = 7, n = 3
# 输出: 28
# Related Topics 数组 动态规划

# 思路：
# 标准的动态规划，因为当前状态只需依赖上一次的状态，dp[i][j]可以做成pre cur两个一维数组做空间优化。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[n - 1][m - 1]

# leetcode submit region end(Prohibit modification and deletion)
