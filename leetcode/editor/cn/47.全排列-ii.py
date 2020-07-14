#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (59.07%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    64K
# Total Submissions: 108.4K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#

# @lc code=start
class Solution:
    # 回溯解法：求解关键：找到重复的原因，对树进行剪枝。
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        nums.sort()
        memo = [False] * len(nums)
        res = []

        # 路径：记录在 tmp_res 中
        # 选择列表：nums 中不存在于 memo 的那些元素
        # 结束条件：nums 中的元素全都在 tmp_res 中出现
        def backtrack(tmp_res, memo):
            if len(tmp_res) == len(nums):
                res.append(tmp_res[:])
                return
            for i in range(len(nums)):
                if memo[i]: continue

                # 有重复元素时的剪枝条件：元素相等时，前一个已被用则当前的就不用
                if i > 0 and nums[i] == nums[i - 1] and memo[i - 1]: continue
                memo[i] = True
                tmp_res.append(nums[i])
                backtrack(tmp_res, memo)
                memo[i] = False
                tmp_res.pop()

        backtrack([], memo)
        return res
# @lc code=end

