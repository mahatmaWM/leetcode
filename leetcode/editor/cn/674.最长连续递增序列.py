#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (45.17%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    31K
# Total Submissions: 68.6K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未经排序的整数数组，找到最长且连续的的递增序列，并返回该序列的长度。
#
#
#
# 示例 1:
#
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
#
#
# 示例 2:
#
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
#
#
#
#
# 注意：数组长度不会超过10000。
#
#

# @lc code=start
class Solution:
    # 遍历数组，查看所有的连续递增子序列，并及时记录连续递增子序列的最大值，
    # 这里需要注意遍历的范围和变量的初始化。
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0

        ans, cur_len = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur_len += 1
                ans = max(cur_len, ans)
            else:
                cur_len = 1
        return ans

# @lc code=end

