#
# @lc app=leetcode.cn id=686 lang=python3
#
# [686] 重复叠加字符串匹配
#
# https://leetcode-cn.com/problems/repeated-string-match/description/
#
# algorithms
# Easy (34.04%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 32.4K
# Testcase Example:  '"abcd"\n"cdabcdab"'
#
# 给定两个字符串 A 和 B, 寻找重复叠加字符串A的最小次数，使得字符串B成为叠加后的字符串A的子串，如果不存在则返回 -1。
#
# 举个例子，A = "abcd"，B = "cdabcdab"。
#
# 答案为 3， 因为 A 重复叠加三遍后为 “abcdabcdabcd”，此时 B 是其子串；A 重复叠加两遍后为"abcdabcd"，B 并不是其子串。
#
# 注意:
#
# A 与 B 字符串的长度在1和10000区间范围内。
#
#

# @lc code=start
class Solution:
    # 子串必须是连续的
    # 1、刚好是倍数
    # 2、前面叠加一次
    # 3、前后都叠加一次
    def repeatedStringMatch(self, A: str, B: str) -> int:
        m = len(B) // len(A)
        if B in A * m: return m
        if B in A * (m + 1): return m + 1
        if B in A * (m + 2): return m + 2
        return -1

# @lc code=end

