#
# @lc app=leetcode.cn id=994 lang=python3
#
# [994] 腐烂的橘子
#
# https://leetcode-cn.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (50.66%)
# Likes:    230
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 59.4K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# 在给定的网格中，每个单元格可以有以下三个值之一：
#
#
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
#
#
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。
#
#
#
# 示例 1：
#
#
#
# 输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#
#
# 示例 2：
#
# 输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#
#
# 示例 3：
#
# 输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#
#
#
#
# 提示：
#
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] 仅为 0、1 或 2
#
#
#


# @lc code=start
class Solution:
    # 官方解答，使用BFS，每一轮，腐烂将会从每一个烂橘子蔓延到与其相邻的新鲜橘子上。
    # 一开始，腐烂的橘子的深度为 0，每一轮腐烂会从腐烂橘子传染到之相邻新鲜橘子上，并且设置这些新的腐烂橘子的深度为自己深度 +1，我们想知道完成这个过程之后的最大深度值是多少。
    # 因为我们总是选择去使用深度值最小的（且之前未使用过的）腐烂橘子去腐化新鲜橘子，如此保证每一个橘子腐烂时的深度标号也是最小的（即耗时最少）
    # 我们还应该检查最终状态下，是否还有新鲜橘子。
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        A = grid

        # 东南西北生成器，4个方向传播一次
        def surrounding(r, c):
            for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
                if 0 <= nr < R and 0 <= nc < C: yield nr, nc

        # 把所有腐烂的橘子加入队列中
        import collections
        queue = collections.deque()
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                if val == 2: queue.append((r, c, 0))
        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in surrounding(r, c):
                if A[nr][nc] == 1:
                    A[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        # 如果还有没腐烂的橘子，返回-1
        if any(1 in row for row in A): return -1
        return d


# @lc code=end
