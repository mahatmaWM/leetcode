#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#
# https://leetcode-cn.com/problems/combination-sum/description/
#
# algorithms
# Medium (68.98%)
# Likes:    716
# Dislikes: 0
# Total Accepted:    100.6K
# Total Submissions: 145.9K
# Testcase Example:  '[2,3,6,7]\n7'
#
# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。
#
# 说明：
#
#
# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#
#

# @lc code=start
class Solution:
    # 回溯法思路是：条件，无重复元素，且每个数字可以无限使用。
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        # 路径：记录在 tmp_list 中
        # 选择列表：start 和 candidates 之间的元素
        # 结束条件：left_sum
        def backtrack(start, candidates, left_sum, tmp_list):
            nonlocal res
            # 终止条件
            if left_sum < 0: return
            if left_sum == 0:
                res.append(copy.deepcopy(tmp_list))
                return

            for i in range(start, len(candidates)):
                if left_sum < candidates[i]: continue
                # 选择
                tmp_list.append(candidates[i])
                # 因为每个数字都可以使用无数次，所以还可以从当前元素i开始
                backtrack(i, candidates, left_sum - candidates[i], tmp_list)
                # 取消选择
                tmp_list.pop()

        backtrack(0, candidates, target, [])
        return res
# @lc code=end

