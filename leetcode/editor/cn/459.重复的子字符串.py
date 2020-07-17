#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#
# https://leetcode-cn.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (47.03%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    20.6K
# Total Submissions: 43.5K
# Testcase Example:  '"abab"'
#
# 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
#
# 示例 1:
#
#
# 输入: "abab"
#
# 输出: True
#
# 解释: 可由子字符串 "ab" 重复两次构成。
#
#
# 示例 2:
#
#
# 输入: "aba"
#
# 输出: False
#
#
# 示例 3:
#
#
# 输入: "abcabcabcabc"
#
# 输出: True
#
# 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
#
#
#

# @lc code=start
class Solution:
    # 不断截取子串，尝试是否可以由其组成。
    def repeatedSubstringPattern(self, s: str) -> bool:
        s_length = len(s)
        for i in range(1, s_length // 2 + 1):
            if s_length % i == 0:
                sub_s = s[:i]
                if sub_s * (s_length // i) == s: return True
        return False

# @lc code=end

