# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。 
#
# 判断你是否能够到达最后一个位置。 
#
# 示例 1: 
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 
#
# 示例 2: 
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
# 
# Related Topics 贪心算法 数组

# 思路：
# 1、设置最远距离为0。
# 2、遍历数组，如果当前位置能到达，并且当前位置+跳数>最远位置，就更新最远位置。
# 3、最后比较最远位置和数组长度。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_i = 0
        for i, jump in enumerate(nums):
            if i <= max_i < i + jump:
                max_i = i + jump
        return max_i >= i

# leetcode submit region end(Prohibit modification and deletion)
