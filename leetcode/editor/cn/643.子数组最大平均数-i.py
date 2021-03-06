#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
# https://leetcode-cn.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (38.70%)
# Likes:    100
# Dislikes: 0
# Total Accepted:    16.1K
# Total Submissions: 41.4K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1:
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
#
# 注意:
#
#
# 1 <= k <= n <= 30,000。
# 所给数据范围 [-10,000，10,000]。
#
#
#

# @lc code=start
class Solution:
    # 采用滑动窗口
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k - 1
        cur_window = sum(nums[0:k])
        res = cur_window
        while right < len(nums) - 1:
            right = right + 1
            cur_window = cur_window - nums[left] + nums[right]
            res = max(res, cur_window)
            left = left + 1
        return float(res) / k

# @lc code=end

