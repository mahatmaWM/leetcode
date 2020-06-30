#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# https://leetcode-cn.com/problems/n-queens/description/
#
# algorithms
# Hard (69.92%)
# Likes:    427
# Dislikes: 0
# Total Accepted:    44.3K
# Total Submissions: 63.4K
# Testcase Example:  '4'
#
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
#
#
# 上图为 8 皇后问题的一种解法。
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例:
#
# 输入: 4
# 输出: [
# ⁠[".Q..",  // 解法 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
#
# ⁠["..Q.",  // 解法 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
#
#
#
#
# 提示：
#
#
#
# 皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自
# 百度百科 - 皇后 ）
#
#
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # board[i]=j，表示第 i 行 j 列
        self.board = [-1] * n
        self.res = []

        # 检查第 k 行时，是否可以放置在第 j 列
        #   board[i] == j 表示第i行的皇后也放在j列。
        #   k - i == abs(board[i] - j) 表示(k,j)(i,board[i])两个皇后可以对角线相遇。
        def valid(k, j):
            for i in range(k):
                if self.board[i] == j or k - i == abs(self.board[i] - j):
                    return False
            return True

        # 路径：记录在 tmp_list 中
        # 选择列表：depth之外剩余的行
        # 结束条件：depth访问到最低一行
        def backtrack(depth, tmp_list):
            if depth == n:
                self.res.append(tmp_list[:])
                return
            for j in range(n):
                if valid(depth, j):
                    # 选择位置j
                    self.board[depth] = j
                    s = '.' * n
                    tmp_list.append(s[:j] + 'Q' + s[j + 1:])
                    backtrack(depth + 1, tmp_list)
                    # 撤销位置j
                    tmp_list.pop()
                    self.board[depth] = -1

        backtrack(0, [])
        return self.res
# @lc code=end

