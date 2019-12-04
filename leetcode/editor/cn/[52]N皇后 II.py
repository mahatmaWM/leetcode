#n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
#
# 
#
# 上图为 8 皇后问题的一种解法。 
#
# 给定一个整数 n，返回 n 皇后不同的解决方案的数量。 
#
# 示例: 
#
# 输入: 4
#输出: 2
#解释: 4 皇后问题存在如下两个不同的解法。
#[
# [".Q..",  // 解法 1
#  "...Q",
#  "Q...",
#  "..Q."],
#
# ["..Q.",  // 解法 2
#  "Q...",
#  "...Q",
#  ".Q.."]
#]
# 
# Related Topics 回溯算法



#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(k, j):
            for i in range(k):
                if board[i] - j == 0 or k - i == abs(board[i] - j):
                    return False
            return True

        def dfs(depth, value_list):
            if depth == n:
                res.append(value_list)
                return
            for i in range(n):
                if check(depth, i):
                    board[depth] = i
                    s = '.' * n
                    dfs(depth + 1, value_list + [s[:i] + 'Q' + s[i + 1:]])

        board = [-1 for i in range(n)]
        res = []
        dfs(0, [])
        return len(res)
        
#leetcode submit region end(Prohibit modification and deletion)
