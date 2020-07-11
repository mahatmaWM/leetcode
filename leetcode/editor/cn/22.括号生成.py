#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
# https://leetcode-cn.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (75.55%)
# Likes:    1099
# Dislikes: 0
# Total Accepted:    136.6K
# Total Submissions: 180.8K
# Testcase Example:  '3'
#
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
#
#
# 示例：
#
# 输入：n = 3
# 输出：[
# ⁠      "((()))",
# ⁠      "(()())",
# ⁠      "(())()",
# ⁠      "()(())",
# ⁠      "()()()"
# ⁠    ]
#
#
#


# @lc code=start
class Solution:
    # 分别从n个左括号&右括号中选择括号来组成合理的序列。
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []

        # 定义左右还剩余的括号数目，以及当前得到的中间状态
        def dfs(left, right, cur_str):
            if left == 0 and right == 0:
                self.res.append(cur_str)
                return
            # 如果左括号还有剩余，则可以放置左括号，
            if left > 0: dfs(left - 1, right, cur_str + '(')
            # 如果右括号的剩余数大于左括号，则可以放置右括号。
            if right > left and right > 0: dfs(left, right - 1, cur_str + ')')

        dfs(n, n, '')
        return self.res


# @lc code=end
