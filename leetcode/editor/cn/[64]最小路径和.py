# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。 
#
# 示例: 
#
# 输入:
# [
#  [1,3,1],
#  [1,5,1],
#  [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# Related Topics 数组 动态规划

# 设置好保存结果的dp数组。
# 依次遍历原始数组，在dp中保存最优结果即可。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
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

# leetcode submit region end(Prohibit modification and deletion)
