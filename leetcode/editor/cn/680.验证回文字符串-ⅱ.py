#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.41%)
# Likes:    214
# Dislikes: 0
# Total Accepted:    43.5K
# Total Submissions: 110.2K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
# 示例 1:
#
#
# 输入: "aba"
# 输出: True
#
#
# 示例 2:
#
#
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
#
#
# 注意:
#
#
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
#
#
#


# @lc code=start
class Solution:

    def validPalindrome(self, s: str) -> bool:
        # 思路：判断回文字符串，使用两个指针，前后各一个，使用闭区间[left, right]。
        # 当遇到前后字符不一致的时候，有两种情况，删除前面字符或者删除后面字符。
        # 由于删除一个字符后剩下的仍旧是字符串，可以直接递归处理了，注意最多删除一个字符
        def isPalindrome(s, left, right, cnt):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    if cnt == 1: return False
                    cnt += 1
                    return isPalindrome(s, left + 1, right, cnt) or isPalindrome(s, left, right - 1, cnt)
            # print('left={},right={}'.format(left, right))
            return True

        return isPalindrome(s, 0, len(s) - 1, 0)


# @lc code=end
