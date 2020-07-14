#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode-cn.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (36.62%)
# Likes:    590
# Dislikes: 0
# Total Accepted:    65.1K
# Total Submissions: 177.8K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 说明:
#
# 假设你总是可以到达数组的最后一个位置。
#
#

# @lc code=start
class Solution:
    # 贪心，使用最少的步数到达最后一个位置，则第i步位置为第i−1步前的点中所能达到的最远位置。
    def jump(self, nums: List[int]) -> int:
        step = 0
        pre_end = 0
        max_bound = 0
        for i in range(len(nums) - 1):
            # 位置i能到达的最远边界
            max_bound = max(max_bound, nums[i] + i)
            # 如果当前位置i等于上一层的最远边界，则更新最远边界，并且跳数加1
            if i == pre_end:
                step += 1
                pre_end = max_bound
        return step
# @lc code=end

