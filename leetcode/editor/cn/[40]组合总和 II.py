# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的每个数字在每个组合中只能使用一次。 
#
# 说明： 
#
# 
# 所有数字（包括目标数）都是正整数。 
# 解集不能包含重复的组合。 
# 
#
# 示例 1: 
#
# 输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#  [1, 7],
#  [1, 2, 5],
#  [2, 6],
#  [1, 1, 6]
# ]
# 
#
# 示例 2: 
#
# 输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ]
# Related Topics 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dfs(self, candidates, sublist, target, index):
        if target == 0:
            self.res.append(sublist)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if i != index and candidates[i] == candidates[i - 1]:
                continue
            self.dfs(candidates, sublist + [candidates[i]],
                     target - candidates[i], i + 1)

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # ?????
        if len(candidates) <= 0:
            return []
        candidates.sort()
        self.res = []
        self.dfs(candidates, [], target, 0)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
