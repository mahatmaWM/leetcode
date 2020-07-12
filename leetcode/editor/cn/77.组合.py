#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#
# https://leetcode-cn.com/problems/combinations/description/
#
# algorithms
# Medium (73.84%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    55K
# Total Submissions: 74.5K
# Testcase Example:  '4\n2'
#
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 示例:
#
# 输入: n = 4, k = 2
# 输出:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#
#


# @lc code=start
class Solution:

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        # 路径：记录在 tmp 中
        # 选择列表：start位置 到 n 之间的元素
        # 结束条件：剩余k
        def backtrack(start, k, tmp):
            if k == 0: res.append(tmp[:])
            # 组合中一个数字只能出现一次，所以从下一位开始选i
            for i in range(start + 1, n + 1):
                tmp.append(i)
                backtrack(i, k - 1, tmp)
                tmp.pop()

        backtrack(0, k, [])
        return res


# @lc code=end
