# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
# 
# 每行的元素从左到右升序排列。 
# 每列的元素从上到下升序排列。 
# 
#
# 示例: 
#
# 现有矩阵 matrix 如下： 
#
# [
#  [1,   4,  7, 11, 15],
#  [2,   5,  8, 12, 19],
#  [3,   6,  9, 16, 22],
#  [10, 13, 14, 17, 24],
#  [18, 21, 23, 26, 30]
# ]
# 
#
# 给定 target = 5，返回 true。 
#
# 给定 target = 20，返回 false。 
# Related Topics 二分查找 分治算法

# 从左下角或者右上角开始遍历。
# 这里选右上角开始。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
