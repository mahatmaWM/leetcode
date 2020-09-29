#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (41.72%)
# Likes:    439
# Dislikes: 0
# Total Accepted:    63.5K
# Total Submissions: 152.3K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
# 示例:
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
#
#
#
# 提示：
#
#
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
#
#
#


# @lc code=start
class Solution:
    # 搜索，尝试表格的每一个位置为起点dfs递归搜索
    # 注意这里不能往回走，需要记录走过的节点（本题采用原位标注#表示走过的节点，完后再复原）
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(x, y, d, word):
            # 走出边界 或者 当前不等的剪枝
            if x < 0 or x == len(board) or y < 0 or y == len(board[0]) or word[d] != board[x][y]: return False
            if d == len(word) - 1: return True
            tmp = board[x][y]
            board[x][y] = '#'
            found = dfs(x, y - 1, d + 1, word) or dfs(x, y + 1, d + 1, word) or dfs(x + 1, y, d + 1, word) or dfs(
                x - 1, y, d + 1, word)
            board[x][y] = tmp
            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, word): return True
        return False


# @lc code=end
