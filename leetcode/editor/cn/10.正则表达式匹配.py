#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (28.24%)
# Likes:    1237
# Dislikes: 0
# Total Accepted:    81.8K
# Total Submissions: 289.6K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
#
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#
#
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
#
# 说明:
#
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
#
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#
#
# 示例 3:
#
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#
#
# 示例 4:
#
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#
#
# 示例 5:
#
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
#
#


# @lc code=start
class Solution0:
    # 如果不考虑有正则的情况，仅仅比较两个字符串是否相等，很容易写出递归解法。
    def isMatch(self, s, p):
        if not p: return not s
        first = bool(s) and p[0] == s[0]
        return first and self.isMatch(s[1:], p[1:])

class Solution:
    # 以下正则递归版本只是在__isMatch基础上改进得到
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        # 判断s和p的第一位是否匹配成功，条件：s不能为空且p[0]==s[0] or "."
        first = bool(s) and (p[0] == s[0] or p[0] == '.')

        # 看子问题中是否有*号，准备递归
        if len(p) >= 2 and p[1] == '*':
            # 对应（字符+*）出现0次 或者 多次
            return self.isMatch(s, p[2:]) or (first and self.isMatch(s[1:], p))
        else:
            return first and self.isMatch(s[1:], p[1:])

class Solution1:
    # 动态规划版本，在递归树的基础上添加了一个备忘录减少计算
    def isMatch(self, s, p):
        S = len(s)
        P = len(p)
        # 存储s[0:i], p[0:j] 是否能匹配 (i, j)
        memo = {}

        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]
            if j == P: return i == S

            pre = i < S and p[j] in {s[i], "."}
            if j <= P - 2 and p[j + 1] == "*":
                tmp = dp(i, j + 2) or (pre and dp(i + 1, j))
            else:
                tmp = pre and dp(i + 1, j + 1)
            memo[(i, j)] = tmp
            return tmp

        return dp(0, 0)


# @lc code=end
