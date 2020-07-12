#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.20%)
# Likes:    746
# Dislikes: 0
# Total Accepted:    139.3K
# Total Submissions: 182.8K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
#
#


# @lc code=start
class Solution:
    # 标准的回溯套路 + 备忘录
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        memo = dict.fromkeys(nums, False)  # 保存数字是否使用过

        # 路径：记录在 tmp_res 中
        # 选择列表：nums 中不存在于 memo 的那些元素
        # 结束条件：nums 中的元素全都在 tmp_res 中出现
        def backtrack(tmp_res, memo):
            if len(tmp_res) == len(nums):
                results.append(tmp_res[:])
                return

            for x in nums:
                if not memo[x]:
                    memo[x] = True
                    tmp_res.append(x)
                    backtrack(tmp_res, memo)
                    tmp_res.pop()
                    memo[x] = False

        backtrack([], memo)
        return results


# @lc code=end
