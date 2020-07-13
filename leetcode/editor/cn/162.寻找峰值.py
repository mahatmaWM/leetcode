#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
# https://leetcode-cn.com/problems/find-peak-element/description/
#
# algorithms
# Medium (46.46%)
# Likes:    232
# Dislikes: 0
# Total Accepted:    46.1K
# Total Submissions: 98.9K
# Testcase Example:  '[1,2,3,1]'
#
# 峰值元素是指其值大于左右相邻值的元素。
#
# 给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。
#
# 数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。
#
# 你可以假设 nums[-1] = nums[n] = -∞。
#
# 示例 1:
#
# 输入: nums = [1,2,3,1]
# 输出: 2
# 解释: 3 是峰值元素，你的函数应该返回其索引 2。
#
# 示例 2:
#
# 输入: nums = [1,2,1,3,5,6,4]
# 输出: 1 或 5
# 解释: 你的函数可以返回索引 1，其峰值元素为 2；
# 或者返回索引 5， 其峰值元素为 6。
#
#
# 说明:
#
# 你的解法应该是 O(logN) 时间复杂度的。
#
#


# @lc code=start
class Solution:
    # 思路，使用二分查找：对比每次中点元素和其右侧元素值的大小：
    # （1）若中点元素值大于右侧元素值，则说明该中点元素位于峰的右侧，将right = mid
    # （2）若中点元素值小于右侧元素值，则说明该中点元素位于峰的左侧，将left = mid + 1
    # 2、当left == right时，打破循环，此时left和right同时指向峰值处
    def findPeakElement(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums + [float('inf')]
        left, right = 1, len(nums) - 2
        while left < right:
            mid = left + (right - left) // 2
            # print('left={},mid={},right={}'.format(left, mid, right))
            if nums[mid] > nums[mid + 1]:
                right = mid
            elif nums[mid] <= nums[mid + 1]:
                left = mid + 1
        return left - 1


# @lc code=end
