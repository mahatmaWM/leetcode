#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#
# https://leetcode-cn.com/problems/palindrome-number/description/
#
# algorithms
# Easy (58.29%)
# Likes:    1106
# Dislikes: 0
# Total Accepted:    368.5K
# Total Submissions: 632.1K
# Testcase Example:  '121'
#
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
#
#
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？
#
#

# @lc code=start
class Solution:
    # 直接反转数字，注意符号与数字合法性判断
    def isPalindrome(self, x: int) -> bool:
        def reverseNumber(num):
            flag = 1 if num >= 0 else -1
            new_num, num = 0, abs(num)
            while num:
                new_num = 10 * new_num + num % 10
                num = num // 10
            new_num = flag * new_num
            return new_num if 2**31 > new_num >= -2**31 else 0

        return False if x < 0 else x == reverseNumber(x)
# @lc code=end

