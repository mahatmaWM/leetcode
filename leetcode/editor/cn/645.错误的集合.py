#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#
# https://leetcode-cn.com/problems/set-mismatch/description/
#
# algorithms
# Easy (42.20%)
# Likes:    95
# Dislikes: 0
# Total Accepted:    15.7K
# Total Submissions: 37.1K
# Testcase Example:  '[1,2,2,4]'
#
# 集合 S 包含从1到 n
# 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。
#
# 给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。
#
# 示例 1:
#
#
# 输入: nums = [1,2,2,4]
# 输出: [2,3]
#
#
# 注意:
#
#
# 给定数组的长度范围是 [2, 10000]。
# 给定的数组是无序的。
#
# 转化一下题目，暂且将 nums 中的元素变为 [0..N-1]，这样每个元素就和一个数组索引完全对应了，这样方便理解一些。
# 思路：通过将每个索引对应的元素变成负数，以表示这个索引被对应过一次了
#


# @lc code=start
class Solution:

    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # 遍历一遍数组，将数值对应的下标变为负数，如果遇到已经为负的元素，说明此元素重复了
        dup = -1
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index] = nums[index] * -1

        # 递增下标，找到大于0的那个，说明对应的元素是缺失的
        missing = -1
        for i in range(n):
            if nums[i] > 0: missing = i + 1
        return [dup, missing]


# @lc code=end
