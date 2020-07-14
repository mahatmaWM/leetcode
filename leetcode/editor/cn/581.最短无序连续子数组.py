#
# @lc app=leetcode.cn id=581 lang=python3
#
# [581] 最短无序连续子数组
#
# https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (34.64%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 90.1K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# 给定一个整数数组，你需要寻找一个连续的子数组，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
#
# 你找到的子数组应是最短的，请输出它的长度。
#
# 示例 1:
#
#
# 输入: [2, 6, 4, 8, 10, 9, 15]
# 输出: 5
# 解释: 你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
#
#
# 说明 :
#
#
# 输入的数组长度范围在 [1, 10,000]。
# 输入的数组可能包含重复元素 ，所以升序的意思是<=。
#
#
#

# @lc code=start
class Solution:
    # 思路：数组排序后和原数组比对，去掉前后相同的部分后，不相同的数段。
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        s = e = -1
        nums_sort = sorted(nums)
        for i in range(len(nums)):
            # s为第一个不等的index，e为最后一个不等的index
            if nums_sort[i] != nums[i]:
                if s == -1: s = i
                e = i
        return e - s + 1 if e != s else 0

# @lc code=end

