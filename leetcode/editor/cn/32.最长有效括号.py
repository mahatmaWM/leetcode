#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (30.74%)
# Likes:    693
# Dislikes: 0
# Total Accepted:    62.5K
# Total Submissions: 203.2K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
#
# 示例 1:
#
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#
#
# 示例 2:
#
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#
#
#


# @lc code=start
class Solution:
    # 动态规划的思路：
    # 1、定义dp[n]为包含s的第i位置，所形成的最长有效括号长度
    # 2、初始状态dp[0]=0
    # 3、寻找递推方程，如果第i位为 ( 符号，显然不合法，则dp[i]=0
    #               如果第i位为 ) 符号，则要看上一位是否是 ( 符号，比如****() + ()，若是则有dp[i] = dp[i - 2] + 2
    #                                   如果上一位为 ) 符号，比如******() + ))，则继续往前面看
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0

        res = 0
        n = len(s)
        dp = [0] * n
        for i in range(1, len(s)):
            if s[i] == "(": dp[i] == 0
            if s[i] == ")":
                # 如果上一位为(
                if s[i - 1] == "(": dp[i] = dp[i - 2] + 2

                # 如果上一位为 ) 时，则需要i-dp[i-1]-1 位置看其是否为)
                if s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    # i-1位的长度加1，并且继续看前面i-dp[i-1]-2位置处再加1
                    dp[i] = (dp[i - 1] + 1) + (dp[i - dp[i - 1] - 2] + 1)
                res = max(res, dp[i])
        return res


# @lc code=end
