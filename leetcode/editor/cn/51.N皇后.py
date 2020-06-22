# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
#
# 
#
# 上图为 8 皇后问题的一种解法。 
#
# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。 
#
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。 
#
# 示例: 
#
# 输入: 4
# 输出: [
# [".Q..",  // 解法 1
#  "...Q",
#  "Q...",
#  "..Q."],
#
# ["..Q.",  // 解法 2
#  "Q...",
#  "...Q",
#  ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。
# 
# Related Topics 回溯算法

# 解题思路：
# 递归回溯，也可以叫做对解空间树的深度优先搜索（dfs）
#
# N皇后问题有个技巧在于棋盘的表示方法，这里使用一个数组就可以表达了。比如board=[1, 3, 0, 2]，
# 这是4皇后问题的一个解，意思是：在第0行，皇后放在第1列；在第1行，皇后放在第3列；在第2行，皇后放在第0列；在第3行，皇后放在第2列。
#
# check函数用来检查深度为第k行时，皇后是否可以放置在第j列。
#   board[i] - j == 0 表示第i行的皇后也放在j列。
#   k - i == abs(board[i] - j) 表示(k,j)(i,board[i])两个皇后可以对角线相遇。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [-1] * n
        self.res = []

        def check(k, j):
            for i in range(k):
                if board[i] == j or k - i == abs(board[i] - j):
                    return False
            return True

        def backtrack(depth, tmp_list):
            if depth == n:
                self.res.append(tmp_list[:])
                return
            for j in range(n):
                if check(depth, j):
                    board[depth] = j
                    s = '.' * n
                    tmp_list.append([s[:j] + 'Q' + s[j + 1:]])
                    backtrack(depth + 1, tmp_list)
                    tmp_list.pop()

        backtrack(0, [])
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().solveNQueens(n=4))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
