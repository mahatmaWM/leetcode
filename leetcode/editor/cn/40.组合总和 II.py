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

# 条件：数组有重复数字，但每个数字只能被使用一次。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.res = []

        # 路径：记录在 tmp_list 中
        # 选择列表：start 和 candidates 之间的元素
        # 结束条件：left_sum
        def backtrack(start, candidates, tmp_sum, tmp_list):
            # 终止条件
            if tmp_sum < 0:
                return
            if tmp_sum == 0:
                self.res.append(tmp_list[:])
                return
            else:
                for i in range(start, len(candidates)):
                    if tmp_sum < candidates[i]:
                        continue
                    # 前一个相同的元素已经被选中
                    if i > start and candidates[i] == candidates[i - 1]:
                        continue
                    # 因为每个数字不能重复使用，所以递归还可以从下一个元素开始
                    tmp_list.append(candidates[i])
                    backtrack(i + 1, candidates, tmp_sum - candidates[i], tmp_list)
                    tmp_list.pop()

        backtrack(0, candidates, target, [])
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
