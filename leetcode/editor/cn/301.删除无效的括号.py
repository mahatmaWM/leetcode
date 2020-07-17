#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#
# https://leetcode-cn.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (47.18%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    11.9K
# Total Submissions: 25K
# Testcase Example:  '"()())()"'
#
# 删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。
#
# 说明: 输入可能包含了除 ( 和 ) 以外的字符。
#
# 示例 1:
#
# 输入: "()())()"
# 输出: ["()()()", "(())()"]
#
#
# 示例 2:
#
# 输入: "(a)())()"
# 输出: ["(a)()()", "(a())()"]
#
#
# 示例 3:
#
# 输入: ")("
# 输出: [""]
#
#

# @lc code=start
class Solution:
    # 1、检查原始字符串中合法的左右括号数目。
    # 2、递归回溯，尝试删除与不删除每一个符号，构造合法结果。
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = set()
        # 找字符串最长有效括号的长度
        def longestVaildParentheses(s):
            res = 0
            stack = []
            for a in s:
                if a == '(':
                    stack.append('(')
                elif a == ')':
                    if stack:
                        res += 2
                        stack.pop()
            return res

        def helper(s, left_p, right_p, open, tmp):
            nonlocal res
            # 当都小于0 都不满足条件
            if left_p < 0 or right_p < 0 or open < 0: return
            # s剩余的括号都不够组成的
            if s.count("(") < left_p or s.count(")") < right_p: return

            if not s:
                # 输出
                if left_p == 0 and right_p == 0 and open == 0: res.add(tmp)
                return

            if s[0] == "(":
                # 用 "("
                helper(s[1:], left_p - 1, right_p, open + 1, tmp + "(")
                # 不用 "("
                helper(s[1:], left_p, right_p, open, tmp)
            elif s[0] == ")":
                # 用 ")"
                helper(s[1:], left_p, right_p - 1, open - 1, tmp + ")")
                # 不用 ")"
                helper(s[1:], left_p, right_p, open, tmp)
            else:
                # 其他字符
                helper(s[1:], left_p, right_p, open, tmp + s[0])

        l = longestVaildParentheses(s)
        # 因为l是最长的, 所以左括号和右括号各一半, 再用open表示左右括号抵消多少
        helper(s, l // 2, l // 2, 0, "")
        return list(res)

# @lc code=end

