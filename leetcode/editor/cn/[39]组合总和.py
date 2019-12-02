# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
#
# candidates 中的数字可以无限制重复被选取。 
#
# 说明： 
#
# 
# 所有数字（包括 target）都是正整数。 
# 解集不能包含重复的组合。 
# 
#
# 示例 1: 
#
# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#  [7],
#  [2,2,3]
# ]
# 
#
# 示例 2: 
#
# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
# Related Topics 数组 回溯算法


# 回溯法思路的简单描述是：把问题的解空间转化成了图或者树的结构表示，然后使用深度优先搜索策略进行遍历，遍历的过程中记录和寻找所有可行解或者最优解。
# 本题不停从candidates获取元素，添加至sublist结果，返回的条件：如果候选集中最小的值都比目标值大，则跳出。另外如果本次跳出的数字num比上一轮选中的last小，则继续，否则挑出集合会与之前的重复。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def dfs(self, candidates, sublist, target, last):
        if target == 0:
            self.res.append(sublist)
        if target < candidates[0]:
            return
        for num in candidates:
            if num > target:
                return
            if num < last:
                continue
            self.dfs(candidates, sublist + [num], target - num, num)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        if len(candidates) <= 0:
            return self.res
        candidates.sort()
        self.dfs(candidates, [], target, 0)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
