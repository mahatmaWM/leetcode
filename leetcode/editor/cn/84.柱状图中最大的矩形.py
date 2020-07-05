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
    # 这个题是单调栈的运用，使用一个单调递增栈来维护已经出现了的矩形高度。
    #   如果后面新来的元素高度比栈里的最后的元素大，那么需要入栈，因为面积最大的元素会出现在后面。
    #   如果后面新来的元素高度比栈里的最后的元素小，那么需要弹出栈里的元素，并且，每次弹出的时候都要对计算目前的宽度，相乘得到面积。
    #
    # 栈里保存索引的方式是需要掌握的，保存索引的方式在最小值栈结构中也有运用。
    # 每次求栈内矩形的高度的时候，其实是求其位置到最右边的距离。
    # 注意即将入栈的元素索引i是一直不变的，另外栈里的每个元素的索引可以认为是矩形的右边界。
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        res = 0
        heights.append(0)
        for i in range(len(heights)):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack[-1]]
                    stack.pop()
                    if not stack:
                        w = i
                    else:
                        w = i - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(i)
        return res
# @lc code=end

