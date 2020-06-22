# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
#
# 
#
# 示例: 
#
# 输入:
# [
# [ 1, 2, 3 ],
# [ 4, 5, 6 ],
# [ 7, 8, 9 ]
# ]
#
# 输出:  [1,2,4,7,5,3,6,8,9]
#
# 解释:
#
# 
#
# 
#
# 说明: 
#
# 
# 给定矩阵中的元素总数不会超过 100000 。 
# 
#

# 思路：
# 依次遍历，注意方向

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0: return []
        M, N, result = len(matrix), len(matrix[0]), []
        for curve_line in range(M + N - 1):
            row_begin = 0 if curve_line + 1 <= N else curve_line + 1 - N
            row_end = M - 1 if curve_line + 1 >= M else curve_line

            if curve_line % 2 == 1:
                for i in range(row_begin, row_end + 1):
                    result.append(matrix[i][curve_line - i])
            else:
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][curve_line - i])
        return result


# leetcode submit region end(Prohibit modification and deletion)
def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().findDiagonalOrder(matrix=matrix))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
