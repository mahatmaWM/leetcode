#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#
# https://leetcode-cn.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (40.85%)
# Likes:    775
# Dislikes: 0
# Total Accepted:    68.6K
# Total Submissions: 167.1K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
#
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
#
#
#
#
#
# 以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。
#
#
#
#
#
# 图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。
#
#
#
# 示例:
#
# 输入: [2,1,5,6,2,3]
# 输出: 10
#
#


# @lc code=start
class Solution:
    # 第i位置最大面积是以i为中心，向左找第一个小于heights[i]的位置left_i；向右找第一个小于heights[i]的位置right_i，
    # 即最大面积为heights[i]*(right_i-left_i-1)
    # 比如：只有一个元素时，left_i=0,right_i=2,2-0-1=1,也就是柱状图本身。
    # 注意这种方法，需要在柱状图数组前后添加两个0元素占位。
    # 然后向左向右找第一个更小值的位置，可以用单调栈在线性时间解决。
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        heights = [0] + heights + [0]
        n = len(heights)

        def find_pre_min_index(heights):
            stack = []
            left_i = [0] * n
            for i in range(n):
                h = heights[i]
                while stack and heights[stack[-1]] >= h:
                    stack.pop()
                if stack: left_i[i] = stack[-1]
                stack.append(i)
            return left_i

        def find_next_min_index(heights):
            stack = []
            right_i = [0] * n
            for i in range(n - 1, -1, -1):
                h = heights[i]
                while stack and heights[stack[-1]] >= h:
                    stack.pop()
                if stack: right_i[i] = stack[-1]
                stack.append(i)
            return right_i

        left_i = find_pre_min_index(heights)
        right_i = find_next_min_index(heights)
        res = 0
        for i in range(n):
            res = max(res, (right_i[i] - left_i[i] - 1) * heights[i])
        return res


# @lc code=end
