#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (50.02%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    40.6K
# Total Submissions: 81K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意：
#
#
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
#
#
#

# @lc code=start
class Solution:
    # itertools.zip_longest 这个函数能将两个字符串转换为每位对应的tuple，不够的可以补齐你指定的字符
    def addStrings(self, num1: str, num2: str) -> str:
        res, jinwei = "", 0
        for (x, y) in itertools.zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            s = (int(x) + int(y) + jinwei)
            d, jinwei = s % 10, s // 10
            res = str(d) + res
        if jinwei > 0: res = str(jinwei) + res
        return res

# @lc code=end

