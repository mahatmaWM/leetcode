# 给定一个整数矩阵，找出最长递增路径的长度。
#
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
#
# 示例 1:
#
# 输入: nums =
# [
#  [9,9,4],
#  [6,6,8],
#  [2,1,1]
# ]
# 输出: 4
# 解释: 最长递增路径为 [1, 2, 6, 9]。
#
# 示例 2:
#
# 输入: nums =
# [
#  [3,4,5],
#  [3,2,6],
#  [2,2,1]
# ]
# 输出: 4
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
#
# Related Topics 深度优先搜索 拓扑排序 记忆化

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # 思路：使用深度优先dfs，memo[i][j]记录从i j节点能走的最长路径。
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0

        row = len(matrix)
        col = len(matrix[0])
        memo = [[0] * col for _ in range(row)]

        def dfs(i, j):
            if memo[i][j] != 0: return memo[i][j]
            res = 1
            for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                tmp_i = x + i
                tmp_j = y + j
                if 0 <= tmp_i < row and 0 <= tmp_j < col and matrix[tmp_i][tmp_j] > matrix[i][j]:
                    res = max(res, 1 + dfs(tmp_i, tmp_j))
            memo[i][j] = max(res, memo[i][j])
            return memo[i][j]

        return max(dfs(i, j) for i in range(row) for j in range(col))


# leetcode submit region end(Prohibit modification and deletion)
