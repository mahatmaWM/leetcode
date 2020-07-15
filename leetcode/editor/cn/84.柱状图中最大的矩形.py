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
class Solution0:
    # 暴力枚举的方式，right指针向右移动，left指针不停往左边移动，每移动一次left指针就尝试计算一次
    # 由于min(heights[left:right + 1]是线性，实际是O(N3)复杂度
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0: return 0
        ans = float('-inf')
        for right in range(len(heights)):
            for left in range(right, -1, -1):
                ans = max(ans, min(heights[left:right + 1]) * (right + 1 - left))
        return ans


class Solution1:
    # https://www.youtube.com/watch?v=GYuBQacXr1A
    # 利用一个严格递增的单调栈，一次遍历找到结果的方法
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        # 栈里初始化-1（为了计算栈中只有一个柱子时的情况）
        stack = [-1]
        ans = float('-inf')
        for i in range(len(heights)):
            # 当栈中有真实索引，且当前待加入索引i位置的柱子 <= 栈顶柱子的时候
            # 栈里元素出栈，这时需要计算出栈的柱子能构成的最大矩阵
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                ans = max(ans, heights[stack.pop()] * (i - 1 - stack[-1]))
            stack.append(i)
        while stack[-1] != -1:
            ans = max(ans, heights[stack.pop()] * (len(heights) - 1 - stack[-1]))
        return ans


class Solution:
    # 第i位置（1开始）最大面积是以i为中心，向左找第一个小于heights[i]的位置left_i；向右找第一个小于heights[i]的位置right_i，
    # 即最大面积为heights[i]*(right_i-(left_i+1))
    #
    # 注意只有一个元素时，left_i=0,right_i=2,2-(0+1)=1，也就是柱状图本身，所以这种方法需要在柱状图数组前后添加两个0元素占位。
    # 然后向左向右找第一个更小值的柱子的位置i，可以用单调栈在线性时间解决。
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        heights = [0] + heights + [0]
        n = len(heights)

        def find_pre_min_index(heights):
            stack = []
            left_i = [0] * n
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack: left_i[i] = stack[-1]
                stack.append(i)
            return left_i

        def find_next_min_index(heights):
            stack = []
            right_i = [0] * n
            for i in range(n - 1, -1, -1):
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                if stack: right_i[i] = stack[-1]
                stack.append(i)
            return right_i

        left_i = find_pre_min_index(heights)
        right_i = find_next_min_index(heights)
        ans = 0
        for i in range(n):
            ans = max(ans, (right_i[i] - left_i[i] - 1) * heights[i])
        return ans


# @lc code=end
