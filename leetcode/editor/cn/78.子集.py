#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (77.41%)
# Likes:    600
# Dislikes: 0
# Total Accepted:    96K
# Total Submissions: 124K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#

# @lc code=start
class Solution:
    # 思路：标准回溯套路
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, choose, index):
            nonlocal res
            res.append(copy.deepcopy(choose))
            for i in range(index, len(nums)):
                choose.append(nums[i])
                backtrack(nums, choose, i + 1)
                choose.pop()

        backtrack(nums, [], 0)
        return res
# @lc code=end

