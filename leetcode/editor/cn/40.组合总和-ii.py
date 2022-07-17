#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
# https://leetcode-cn.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (61.76%)
# Likes:    285
# Dislikes: 0
# Total Accepted:    61.6K
# Total Submissions: 99.7K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。
#
# 说明：
#
#
# 所有数字（包括目标数）都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# 示例 2:
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
# [1,2,2],
# [5]
# ]
#
#

# @lc code=start
class Solution:
    # 条件：数组有重复数字，但每个数字只能被使用一次。
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        # 路径：记录在 tmp_path 中
        # 选择列表：start 和 candidates 之间的元素
        # 结束条件：left_sum
        def backtrack(candidates, tmp_path, start, tmp_sum):
            nonlocal res
            if tmp_sum < 0: return
            if tmp_sum == 0:
                import copy
                res.append(copy.deepcopy(tmp_path))
                return
            for i in range(start, len(candidates)):
                if tmp_sum < candidates[i]: break
                # 前一个相同的元素已经被选中
                if i > start and candidates[i] == candidates[i - 1]: continue
                # 选择
                tmp_path.append(candidates[i])
                # 因为每个数字不能重复使用，所以从下一个元素开始
                backtrack(candidates, tmp_path, i + 1, tmp_sum - candidates[i])
                # 取消选择
                tmp_path.pop()

        backtrack(candidates, [], 0, target)
        return res
# @lc code=end

