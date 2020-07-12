#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
# https://leetcode-cn.com/problems/maximal-square/description/
#
# algorithms
# Medium (42.47%)
# Likes:    455
# Dislikes: 0
# Total Accepted:    56K
# Total Submissions: 131.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
#
# 示例:
#
# 输入:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# 输出: 4
#
#


# @lc code=start
class Solution:
    # dp[i][j]表示以第i行，第j列处为右下角的最大正方形的边长。
    # 那么若当前位置matrix[i][j]为1，则此处可以构成的最大正方形的边长，
    # 是其正上方，左侧，和左上界三者共同约束的，且为三者中的最小值加1（这个需要作图就可以观察出这个规律）
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(dp[i][j], res)
        return res * res


# @lc code=end
