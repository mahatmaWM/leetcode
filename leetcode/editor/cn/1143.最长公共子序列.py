#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#
# https://leetcode-cn.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (59.75%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    25.7K
# Total Submissions: 43K
# Testcase Example:  '"abcde"\n"ace"'
#
# 给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
#
# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde"
# 的子序列。两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
#
# 若这两个字符串没有公共子序列，则返回 0。
#
#
#
# 示例 1:
#
# 输入：text1 = "abcde", text2 = "ace"
# 输出：3
# 解释：最长公共子序列是 "ace"，它的长度为 3。
#
#
# 示例 2:
#
# 输入：text1 = "abc", text2 = "abc"
# 输出：3
# 解释：最长公共子序列是 "abc"，它的长度为 3。
#
#
# 示例 3:
#
# 输入：text1 = "abc", text2 = "def"
# 输出：0
# 解释：两个字符串没有公共子序列，返回 0。
#
#
#
#
# 提示:
#
#
# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# 输入的字符串只含有小写英文字符。
#
#
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # dp[i][j]代表text1的i位置，和 text2的j位置 为止，的最长公共子序列
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[m][n]

# 最长公共子串
# def find_lcsubstr(text1, text2):
#     m = len(text1)
#     n = len(text2)
#     tail_index = 0
#     mmax = 0  #最长匹配的长度
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
#     for i in range(m):
#         for j in range(n):
#             if text1[i] == text2[j]:
#                 dp[i + 1][j + 1] = dp[i][j] + 1
#                 if dp[i + 1][j + 1] > mmax:
#                     mmax = dp[i + 1][j + 1]
#                     tail_index = i + 1
#     return text1[tail_index - mmax:tail_index], mmax


# print(find_lcsubstr('abdfgc', 'abdfg'))


# @lc code=end

