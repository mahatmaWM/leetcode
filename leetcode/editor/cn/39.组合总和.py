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


# 回溯法思路是：
# 条件，无重复元素，且每个数字可以无限使用。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []

        def backtrack(start, candidates, left_sum, tmp_list):
            # 终止条件
            if left_sum < 0:
                return
            if left_sum == 0:
                # 这里要用深拷贝或者切片，不能用tmp_list；
                # 区别是前面是深拷贝或者切片浅拷贝，后面是对象指代（会在回溯过程中被更改掉）
                self.res.append(tmp_list[:])
                return
            else:
                for i in range(start, len(candidates)):
                    if left_sum < candidates[i]:
                        continue
                    tmp_list.append(candidates[i])
                    # 因为每个数字都可以使用无数次，所以还可以从当前元素i开始
                    backtrack(i, candidates, left_sum - candidates[i], tmp_list)
                    tmp_list.pop()

        backtrack(0, candidates, target, [])
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().combinationSum(candidates=[2,3,5], target=8))
