# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
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
# 输出: 2
# 解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 
# Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
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
        return len(self.res)


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().totalNQueens(n=4))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
