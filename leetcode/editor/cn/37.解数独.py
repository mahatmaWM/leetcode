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

# set + 回溯

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 用来记录每行、每列、每个grid应该放置的数字
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]

        empty = []

        # 遍历一遍数独，去除已经出现的数字，并记录需要填补的空格
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    block[(i // 3) * 3 + j // 3].remove(val)
                else:
                    empty.append((i, j))

        # 从空格列表中获取空格，一个一个的回溯放置数字
        def backtrack(iter=0):
            if iter == len(empty):
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if backtrack(iter + 1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False

        backtrack()


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(Solution().solveSudoku(board=board))

    print('\n'.join([' '.join(item) for item in board]))
