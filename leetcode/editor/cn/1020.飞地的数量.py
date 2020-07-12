#
# @lc app=leetcode.cn id=1020 lang=python3
#
# [1020] 飞地的数量
#
# https://leetcode-cn.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (50.88%)
# Likes:    30
# Dislikes: 0
# Total Accepted:    4.4K
# Total Submissions: 8.6K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# 给出一个二维数组 A，每个单元格为 0（代表海）或 1（代表陆地）。
#
# 移动是指在陆地上从一个地方走到另一个地方（朝四个方向之一）或离开网格的边界。
#
# 返回网格中无法在任意次数的移动中离开网格边界的陆地单元格的数量。
#
#
#
# 示例 1：
#
# 输入：[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# 输出：3
# 解释：
# 有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
#
# 示例 2：
#
# 输入：[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# 输出：0
# 解释：
# 所有 1 都在边界上或可以到达边界。
#
#
#
# 提示：
#
#
# 1 <= A.length <= 500
# 1 <= A[i].length <= 500
# 0 <= A[i][j] <= 1
# 所有行的大小都相同
#
#
#


# @lc code=start
class Solution:
    # 把与边界相连的陆地都设置为-1，然后找所剩下的为1的陆地数目，dfs遍历图即可
    def numEnclaves(self, A: List[List[int]]) -> int:
        if not A: return 0
        row = len(A)
        col = len(A[0])
        res = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            # 不合法 或者 已经走过，返回
            if x < 0 or x >= row or y < 0 or y >= col: return
            if A[x][y] != 1: return

            A[x][y] = -1
            for _x, _y in directions:
                dfs(x + _x, y + _y)

        # 从边界为1的格子触发，把与之相连的格子都赋值为-1
        for i in range(row):
            for j in range(col):
                if i in [0, row - 1] or j in [0, col - 1] and A[i][j] == 1: dfs(i, j)

        # 找内陆中格子为1的数目
        for i in range(row):
            for j in range(col):
                if A[i][j] == 1: res += 1
        return res


# @lc code=end
