# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例: 
#
# 输入:
# [
#  ["1","0","1","0","0"],
#  ["1","0","1","1","1"],
#  ["1","1","1","1","1"],
#  ["1","0","0","1","0"]
# ]
# 输出: 6
# Related Topics 栈 数组 哈希表 动态规划

# 对于这个矩阵，对于每一行，我们按照上一道题84的算法求解一遍，最后得出的就是最大的矩阵。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def largestRectangleArea(self, heights):
        res = 0
        stack = [0]
        heights.append(0)
        heights.insert(0, 0)
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        del heights[0]
        del heights[-1]
        return res

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        height = [0] * len(matrix[0])
        res = 0
        for i in range(len(matrix)):
            for j in range(len((matrix[0]))):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            res = max(res, self.largestRectangleArea(height))
        return res

# leetcode submit region end(Prohibit modification and deletion)
