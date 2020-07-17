#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode-cn.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (63.46%)
# Likes:    1533
# Dislikes: 0
# Total Accepted:    223.2K
# Total Submissions: 351.7K
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
# ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。
#
#
#
#
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
#
#
# 示例：
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
#
#


# @lc code=start
class Solution:
    # 思路：最大面积不仅和高度有关，还和宽度有关。
    # 双指针，不断增加left&减小right指针。
    # 每变化一次的时候，更新最大值，如果左边高度小于右边高度，则移动左指针；否则移动右指针
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_water = min(height[left], height[right]) * (right - left)
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            max_water = max(cur, max_water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


# @lc code=end
