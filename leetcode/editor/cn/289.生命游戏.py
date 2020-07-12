#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
# https://leetcode-cn.com/problems/game-of-life/description/
#
# algorithms
# Medium (74.48%)
# Likes:    229
# Dislikes: 0
# Total Accepted:    35.8K
# Total Submissions: 48.1K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# 根据 百度百科 ，生命游戏，简称为生命，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。
#
# 给定一个包含 m × n 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态：1 即为活细胞（live），或 0
# 即为死细胞（dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
#
#
# 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
# 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
# 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
# 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
#
#
#
# 根据当前状态，写一个函数来计算面板上所有细胞的下一个（一次更新后的）状态。下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。
#
#
#
# 示例：
#
# 输入：
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# 输出：
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
#
#
#
# 进阶：
#
#
# 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
# 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
#
#
#


# @lc code=start
class Solution:
    # 思路
    # 第一次遍历，对于每个位置，计算周围的细胞数目，保存
    # 第二次遍历，根据当前位置细胞状态和周围细胞数目，设置最终细胞状态
    # 这里有个问题，如何原地存储细胞数目信息？
    #
    # 用当前位置数字的最后一位储存原来是否有细胞（0，1）
    # 将周围细胞数目的值，左移一位
    # 将这两个值做按位或运算
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 计算x y位置的细胞周围活细胞数目
        def count_cell(x, y):
            points = [
                (x - 1, y - 1),
                (x - 1, y),
                (x - 1, y + 1),
                (x, y - 1),
                (x, y + 1),
                (x + 1, y - 1),
                (x + 1, y),
                (x + 1, y + 1),
            ]
            return sum((board[i][j] & 1) for i, j in points if 0 <= i < max_x and 0 <= j < max_y)

        if not board: return board
        max_x, max_y = len(board), len(board[0])
        # 计算周围细胞数目，并储存
        for i in range(max_x):
            for j in range(max_y):
                count = count_cell(i, j)
                count <<= 1
                board[i][j] |= count

        for i in range(max_x):
            for j in range(max_y):
                count = board[i][j] >> 1  # 右移一位，取出周围细胞数目
                board[i][j] &= 1  # 重新设置原先细胞状态
                if board[i][j] == 1:
                    if count < 2 or count > 3: board[i][j] = 0
                else:
                    if count == 3: board[i][j] = 1
        return board


# @lc code=end
