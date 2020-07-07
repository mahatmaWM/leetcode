#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode-cn.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (27.83%)
# Likes:    364
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 112.6K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
#
#
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
#
#
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#
# 示例 2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
#
#
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#
#
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#
#
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false
#
#

# @lc code=start
class Solution:
    # 动态规划，定义 dp[i][j]，代表：s[0 i] 是否与 p[0 j] 匹配
    # 初始化:
    # dp[0][0]:什么都没有,所以为true
    # 第一行dp[0][j],换句话说,s为空,与p匹配,所以只要p开始为*才为true
    # 第一列dp[i][0],当然全部为False
    # 转移方程:
    # 如果(s[i] == p[j] || p[j] == "?") && dp[i-1][j-1] ,有dp[i][j] = true
    # 如果p[j] == "*" && (dp[i-1][j] = true || dp[i][j-1] = true) 有dp[i][j] = true
    # ​注意:
    # ​dp[i][j-1],表示*代表是空字符,例如ab,ab*
    # ​dp[i-1][j],表示*代表非空任何字符,例如abcd,ab*
    def isMatch(self, s: str, p: str) -> bool:
        sn,pn = len(s),len(p)
        dp = [[False] * (pn + 1) for _ in range(sn + 1)]
        # 初始化dp，如果p的开始位为*号，则全为true
        dp[0][0] = True
        for j in range(1, pn + 1):
            if p[j - 1] == "*": dp[0][j] = dp[0][j - 1]

        for i in range(1, sn + 1):
            for j in range(1, pn + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        return dp[-1][-1]
# @lc code=end

