#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
# https://leetcode-cn.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (71.26%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    22.3K
# Total Submissions: 31.3K
# Testcase Example:  '3\n7'
#
# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
#
# 说明：
#
#
# 所有数字都是正整数。
# 解集不能包含重复的组合。 
#
#
# 示例 1:
#
# 输入: k = 3, n = 7
# 输出: [[1,2,4]]
#
#
# 示例 2:
#
# 输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#
#
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backtrack(start, k, tmp_sum, tmp_res):
            nonlocal res
            if k == 0 and tmp_sum == 0:
                res.append(copy.deepcopy(tmp_res))

            # 组合中一个数字只能出现一次，所以从下一位开始选i
            for i in range(start + 1, 10):
                tmp_res.append(i)
                backtrack(i, k - 1, tmp_sum - i, tmp_res)
                tmp_res.pop()

        backtrack(0, k, n, [])
        return res
# @lc code=end

