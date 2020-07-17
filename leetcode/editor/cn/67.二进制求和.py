#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.79%)
# Likes:    431
# Dislikes: 0
# Total Accepted:    112K
# Total Submissions: 206.3K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
#
# 输入为 非空 字符串且只包含数字 1 和 0。
#
#
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#
#
#
# 提示：
#
#
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
#
#
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        i, j, plus = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or plus == 1:
            plus += int(a[i]) if i >= 0 else 0
            plus += int(b[j]) if j >= 0 else 0
            res = str(plus % 2) + res
            i, j, plus = i - 1, j - 1, plus / 2
        return res

# @lc code=end

