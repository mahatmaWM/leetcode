# 编写一个程序，通过已填充的空格来解决数独问题。
#
# 一个数独的解法需遵循如下规则： 
#
# 
# 数字 1-9 在每一行只能出现一次。 
# 数字 1-9 在每一列只能出现一次。 
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
# 
#
# 空白格用 '.' 表示。 
#
# 
#
# 一个数独。 
#
# 
#
# 答案被标成红色。 
#
# Note: 
#
# 
# 给定的数独序列只包含数字 1-9 和字符 '.' 。 
# 你可以假设给定的数独只有唯一解。 
# 给定数独永远是 9x9 形式的。 
# 
# Related Topics 哈希表 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # num是否可以放在pos_row, pos_col位置
        def isAvailable(pos_row, pos_col, num):
            if num in board[pos_row]:
                return False
            for i in range(9):
                if board[i][pos_col] == num:
                    return False
            gird33 = []
            row1 = pos_row // 3 * 3
            row2 = (pos_row // 3 + 1) * 3
            for i in range(row1, row2):
                gird33 += board[i][row1:row2]
            if num in gird33:
                return False
            return True

        def posTry(pos_row, pos_col):
            if pos_row == 9 and pos_col == 0:
                return True
            if board[pos_row][pos_col] == '.':
                for i in range(1, 10):
                    if isAvailable(pos_row, pos_col, str(i)):
                        board[pos_row][pos_col] = str(i)
                        flag = posTry(pos_row + (pos_col + 1) // 9,
                                      (pos_col + 1) % 9)
                        # 如果下一个位置失败了，则回溯到当前位置
                        if not flag:
                            board[pos_row][pos_col] = '.'
                        else:
                            return True
            else:
                return posTry(pos_row + (pos_col + 1) // 9, (pos_col + 1) % 9)

        posTry(0, 0)
        return board

# leetcode submit region end(Prohibit modification and deletion)
