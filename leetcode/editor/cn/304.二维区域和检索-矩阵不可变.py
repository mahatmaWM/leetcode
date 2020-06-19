#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (44.34%)
# Likes:    86
# Dislikes: 0
# Total Accepted:    9.1K
# Total Submissions: 20.5K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
#   '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
#
#
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
#
# 示例:
#
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
#
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
#
#
# 说明:
#
#
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2。
#
# 思路：对于快速求出一位数组任意[beg, end]位置的和，先会计算好每个位置cur_sum。
# 类似本题就是在二维上做相似操作，假设dp就存在这样的值，则
# sumRegion(row1, col1, row2, col2) = dp[row2][col2] - dp[row2][col1 - 1] - dp[row1 - 1][col2] + dp[row1 - 1][col1 - 1]

#

# @lc code=start
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            pass
        else:
            row = len(matrix)
            col = len(matrix[0])
            self.dp = [[ 0 ] * (col + 1) for _ in range(row + 1)]

            # 求行的前缀和
            for i in range(1, row + 1):
                for j in range(1 ,col + 1):
                    self.dp[i][j] = self.dp[i][j - 1] + matrix[i - 1][j - 1]

            # 求列的前缀和
            for j in range(1, col + 1):
                for i in range(1, row + 1):
                    self.dp[i][j] += self.dp[i - 1][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

