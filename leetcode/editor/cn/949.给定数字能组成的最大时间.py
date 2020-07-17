#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 给定数字能组成的最大时间
#
# https://leetcode-cn.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (35.29%)
# Likes:    44
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 15.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
#
# 最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
#
# 以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,4]
# 输出："23:41"
#
#
# 示例 2：
#
# 输入：[5,5,5,5]
# 输出：""
#
#
#
#
# 提示：
#
#
# A.length == 4
# 0 <= A[i] <= 9
#
#
#


# @lc code=start
class Solution:

    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort()
        for h in range(23, -1, -1):
            for m in range(59, -1, -1):
                t = [h // 10, h % 10, m // 10, m % 10]
                ts = sorted(t)
                if ts == A: return str(t[0]) + str(t[1]) + ":" + str(t[2]) + str(t[3])
        return ""


# @lc code=end
