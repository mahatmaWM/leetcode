# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
#
# 
# 数字 1-9 在每一行只能出现一次。 
# 数字 1-9 在每一列只能出现一次。 
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
# 
#
# 
#
# 上图是一个部分填充的有效的数独。 
#
# 数独部分空格内已填入了数字，空白格用 '.' 表示。 
#
# 示例 1: 
#
# 输入:
# [
#  ["5","3",".",".","7",".",".",".","."],
#  ["6",".",".","1","9","5",".",".","."],
#  [".","9","8",".",".",".",".","6","."],
#  ["8",".",".",".","6",".",".",".","3"],
#  ["4",".",".","8",".","3",".",".","1"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".","6",".",".",".",".","2","8","."],
#  [".",".",".","4","1","9",".",".","5"],
#  [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true
# 
#
# 示例 2: 
#
# 输入:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
#     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。 
#
# 说明: 
#
# 
# 一个有效的数独（部分已被填充）不一定是可解的。 
# 只需要根据以上规则，验证已经填入的数字是否有效即可。 
# 给定数独序列只包含数字 1-9 和字符 '.' 。 
# 给定数独永远是 9x9 形式的。 
# 
# Related Topics 哈希表

# 思路：
# 如果只判断有效的话，实现三个函数分别对应三个条件即可：判断行，判断列，判断9宫格。
# 把要判断的这些位置的数字取出来，然后用set后的长度是否等于原长度就能知道是不是有重复数字了。
# 题目中已经说了给出的数字只有1~9，所以省掉了很多事。
# 判断之前需要把’.‘给去掉，因为数字只允许出现一次，而'.'可能出现多次。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isValidRow(self, board):
        n = len(board)
        for r in range(n):
            row = [x for x in board[r] if x != '.']
            if len(set(row)) != len(row):
                return False
        return True

    def isValidCol(self, board):
        n = len(board)
        for c in range(n):
            col = [board[r][c] for r in range(n) if board[r][c] != '.']
            if len(set(col)) != len(col):
                return False
        return True

    def isValidNineCell(self, board):
        n = len(board)
        for r in range(0, n, 3):
            for c in range(0, n, 3):
                cell = []
                for i in range(3):
                    for j in range(3):
                        num = board[r + i][c + j]
                        if num != '.':
                            cell.append(num)
                if len(set(cell)) != len(cell):
                    return False
        return True

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidRow(board) and self.isValidCol(
            board) and self.isValidNineCell(board)

# leetcode submit region end(Prohibit modification and deletion)
