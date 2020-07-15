#
# @lc app=leetcode.cn id=41 lang=python3
#
# [41] 缺失的第一个正数
#
# https://leetcode-cn.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (38.40%)
# Likes:    542
# Dislikes: 0
# Total Accepted:    54.9K
# Total Submissions: 143K
# Testcase Example:  '[1,2,0]'
#
# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。
#
#
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
#
#
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
#
#
#
#
# 提示：
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。
#
#


# @lc code=start
class Solution1:
    # 数组长度为n，说明里面没有出现的最小正整数一定<=n，
    # 那么定义一个长度为n的hash记录一遍数组，在递增遍历整数n以内的数字，类似桶排序，这种方法的空间为O(N)
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        hash = [0] * len(nums)
        for i in range(len(nums)):
            if 0 < nums[i] <= len(nums): hash[nums[i] - 1] += 1
        for i in range(len(nums)):
            if hash[i] == 0: return i + 1
        return len(nums) + 1


class Solution:
    # nums[nums[i] - 1] != nums[i]，这一步是关键，代表当前数字nums[i]应该放在nums[i]-1的位置
    # 按照这个思想，数组[3,1,4,-1]可以变成[1,-1,3,4]，遍历这个数组，发现第一个 i+1 != nums[i]的i+1即是结果。
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        for i in range(len(nums)):
            # 这里要用while，代表一直交换，直到位置i满足条件
            while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for index, num in enumerate(nums):
            if num != index + 1: return index + 1
        return len(nums) + 1


# @lc code=end
