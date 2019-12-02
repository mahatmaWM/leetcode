# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
# 
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。 
#
# 示例: 
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# Related Topics 栈 数组 双指针

# 使用left_max,right_max记录每个位置左右两边的最大值，两次遍历数组即可。
# 最后遍历每个位置i，它能存放的水量即为左右最大值中的最小值 - 位置i的值。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        n, res = len(height), 0
        left_max, right_max = [0] * n, [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])

        for i in range(1, n - 1):
            res += min(left_max[i], right_max[i]) - height[i]
        return res

# leetcode submit region end(Prohibit modification and deletion)
