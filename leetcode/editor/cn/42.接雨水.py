#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
# https://leetcode-cn.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (51.26%)
# Likes:    1359
# Dislikes: 0
# Total Accepted:    109.7K
# Total Submissions: 214.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
# Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
#
#


# @lc code=start
class Solution1:
    # 暴力求解法，对于位置i，其能装水的最大值 = min(左边最大高度，右边最大高度) - 当前的height
    # 所以对于每个i位置，可以遍历其左右的最大高度，这样两个for循环嵌套即可。
    #
    # 优化：使用备忘录，先遍历两遍数组，记录左右的最大值，pre_max前缀最大值
    # 使用left_max,right_max记录每个位置左右两边的最大值，两次遍历数组即可。
    # 最后遍历每个位置i，它能存放的水量即为左右最大值中的最小值 - 位置i的值。
    def trap(self, height: List[int]) -> int:
        if not height: return 0
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


class Solution:
    # 左右双指针l,r从两头往中间逼近，并用max_l,max_r来记录已经遍历过的左右最大值。
    def trap(self, height: List[int]) -> int:
        if len(height) == 0: return 0
        ans = 0
        l, r = 0, len(height) - 1
        max_l, max_r = height[0], height[-1]
        while l < r:
            if max_l < max_r:
                ans += (max_l - height[l])
                l += 1
                max_l = max(max_l, height[l])
            else:
                ans += (max_r - height[r])
                r -= 1
                max_r = max(max_r, height[r])
        return ans


# @lc code=end
