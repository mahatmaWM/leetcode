# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
#
# 示例 1: 
#
# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
#
# 示例 2: 
#
# 输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# Related Topics 数组 动态规划

# 因为可能包含负数，如果前面一个子序列的乘积为负数 而 当前元素为负数，则可以得到一个正数，所以必须记录pre连续子数组乘积的最大值、最小值。
# 其转移方程如下：
# cur_max = max(pre_max * num, pre_min * num, num)
# cur_min = min(pre_max * num, pre_min * num, num)

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return

        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]

        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res

# leetcode submit region end(Prohibit modification and deletion)
