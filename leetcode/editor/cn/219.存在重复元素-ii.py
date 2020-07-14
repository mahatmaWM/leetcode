#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (39.12%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    47.9K
# Total Submissions: 122.5K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的
# 绝对值 至多为 k。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
#
#


# @lc code=start
class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = collections.defaultdict(int)
        for index in range(len(nums)):
            if nums[index] in hash:
                if index - hash[nums[index]] <= k: return True
            # 可以把其index更新为最大的位置
            hash[nums[index]] = index
        return False


# @lc code=end
