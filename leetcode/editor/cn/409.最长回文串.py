#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (54.99%)
# Likes:    191
# Dislikes: 0
# Total Accepted:    50.7K
# Total Submissions: 92.2K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
#
# 示例 1:
#
#
# 输入:
# "abccccdd"
#
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#
#
#


# @lc code=start
class Solution:
    # 1、记录s中每个字母出现的次数。
    # 2、出现次数为偶数的字母都可以用来构造回文，出现次数为奇数的，可以用其减1的长度来构造回文。
    # 3、最后再添加一个出现次数为奇数的字符。
    def longestPalindrome(self, s: str) -> int:
        s_cnt = collections.Counter(s)

        res = 0
        left_single = 0
        for k, v in s_cnt.items():
            if v % 2 == 1:
                res += (v - 1)
                left_single += 1
            elif v % 2 == 0:
                res += v

        if left_single > 0:
            return res + 1
        else:
            return res


# @lc code=end
