#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode-cn.com/problems/jump-game/description/
#
# algorithms
# Medium (40.13%)
# Likes:    692
# Dislikes: 0
# Total Accepted:    118.8K
# Total Submissions: 296K
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
#
#
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
#
#
#


# @lc code=start
class Solution:
    # 思路：
    # 1、设置最远距离为0。
    # 2、遍历数组，如果当前位置能到达并且当前位置+跳数>目前的最远位置，就更新最远位置。
    # 3、最后比较最远位置和数组长度。
    def canJump(self, nums: List[int]) -> bool:
        max_i = 0
        for i, jump in enumerate(nums):
            if i <= max_i < i + jump: max_i = i + jump
        return max_i >= len(nums) - 1


# @lc code=end
