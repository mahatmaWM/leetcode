# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
# 
# 每行中的整数从左到右按升序排列。 
# 每行的第一个整数大于前一行的最后一个整数。 
# 
#
# 示例 1: 
#
# 输入:
# matrix = [
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
# 
#
# 示例 2: 
#
# 输入:
# matrix = [
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
# ]
# target = 13
# 输出: false
# Related Topics 数组 二分查找

# 思路：
# 1、可以直接遍历找，复杂度m*n。
# 2、可以行间遍历找，行内二分查找，复杂度m*logn。
# 3、因为矩阵按照Z字形是严格升序的，所以如果按照Z字形排序好，可以原地二分查找。
# 可以使用额外空间把它降维再二分；这里的技巧是通过计算将mid索引转化为矩阵的行列值索引。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2

            # 一维索引转化为二维索引的技巧
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

# leetcode submit region end(Prohibit modification and deletion)
