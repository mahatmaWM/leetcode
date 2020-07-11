#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# https://leetcode-cn.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (48.05%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    137.1K
# Total Submissions: 285.4K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
#
# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
#
# L   C   I   R
# E T O E S I I G
# E   D   H   N
#
#
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
#
# 请你实现这个将字符串进行指定行数变换的函数：
#
# string convert(string s, int numRows);
#
# 示例 1:
#
# 输入: s = "LEETCODEISHIRING", numRows = 3
# 输出: "LCIRETOESIIGEDHN"
#
#
# 示例 2:
#
# 输入: s = "LEETCODEISHIRING", numRows = 4
# 输出: "LDREOEIIECIHNTSG"
# 解释:
#
# L     D     R
# E   O E   I I
# E C   I H   N
# T     S     G
#
#


# @lc code=start
class Solution:
    # 1、res[row] += c： 把每个字符 c 填入对应行 res[row]
    # 2、row += direction： 更新当前字符 c 对应的行索引；
    # 3、direction = - direction： 在达到 ZZ 字形转折点时，执行反向。
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ['' for _ in range(numRows)]
        # 当前行和移动方向
        row, direction = 0, -1
        for c in s:
            res[row] += c
            # 换方向
            if row == 0 or row == numRows - 1:
                direction = -direction
            row += direction
        return ''.join(res)


# @lc code=end
