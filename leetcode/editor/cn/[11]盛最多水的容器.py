# 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且 n 的值至少为 2。 
#
# 
#
# 图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。 
#
# 
#
# 示例: 
#
# 输入: [1,8,6,2,5,4,8,3,7]
# 输出: 49
# Related Topics 数组 双指针

# 使用一左一后的双指针，不断增加left&减小right指针。
# 1、更新最大值
# 2、如果左边高度小于右边高度，则移动左指针；否则移动有指针

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = 0, n - 1
        max_water = min(height[left], height[right]) * right
        while left < right:
            cur = min(height[left], height[right]) * (right - left)
            if cur > max_water:
                max_water = cur
            elif height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water

# leetcode submit region end(Prohibit modification and deletion)
