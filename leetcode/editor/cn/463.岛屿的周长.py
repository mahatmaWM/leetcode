#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# https://leetcode-cn.com/problems/island-perimeter/description/
#
# algorithms
# Easy (66.95%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    18.1K
# Total Submissions: 27K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
#
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
#
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
#
#
#
# 示例 :
#
# 输入:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
#
# 输出: 16
#
# 解释: 它的周长是下面图片中的 16 个黄色的边：
#
#
#
#
#

# @lc code=start
class Solution:
    # 对于两个 水平 或者 垂直 挨着的方块，其周长 = 4*个数 - 2*挨着数（邻居数）
    # 所以只要统计有多少个为1的数目，以及有多少个邻居数即可
    # 由于行列都是递增顺序遍历的，所以邻居只需要统计一次即可
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        counts = 0
        neighbors = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    counts += 1
                    if i < row - 1:
                        if grid[i + 1][j] == 1: neighbors += 1
                    if j < col - 1:
                        if grid[i][j + 1] == 1: neighbors += 1
        return 4 * counts - 2 * neighbors

# @lc code=end

