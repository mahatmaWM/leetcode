# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 示例: 
#
# 输入: 3
# 输出:
# [
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
# ]
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.matrix = [[0] * n for _ in range(n)]
        self.num = 1

        def changeInCircle(start):
            endX = n - 1 - start
            endY = n - 1 - start
            # 从左到右改变一行
            for i in range(start, endX + 1):
                self.matrix[start][i] = self.num
                self.num += 1
            # 从上到下改变一列
            for i in range(start + 1, endY + 1):
                self.matrix[i][endX] = self.num
                self.num += 1
            # 从右到左打印一行
            for i in range(endX - 1, start - 1, -1):
                self.matrix[endY][i] = self.num
                self.num += 1
            # 从下到上打印一列：
            for i in range(endY - 1, start, -1):
                self.matrix[i][start] = self.num
                self.num += 1

        start = 0
        while n > start * 2:
            changeInCircle(start)
            start += 1
        return self.matrix

# leetcode submit region end(Prohibit modification and deletion)
