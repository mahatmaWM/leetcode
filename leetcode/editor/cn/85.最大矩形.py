#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (46.58%)
# Likes:    463
# Dislikes: 0
# Total Accepted:    31.1K
# Total Submissions: 66.8K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
#
# 示例:
#
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
#
#


# @lc code=start
class Solution:
    # 对于这个矩阵，对于每一行，我们按照上一道题84的算法求解一遍，最后得出的就是最大的矩阵
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0

        def largestRectangleArea(heights):
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

        height = [0] * len(matrix[0])
        res = 0
        for i in range(len(matrix)):
            for j in range(len((matrix[0]))):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            res = max(res, largestRectangleArea(height))
        return res


# @lc code=end
