#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#
# https://leetcode-cn.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (52.68%)
# Likes:    39
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 28.8K
# Testcase Example:  '4'
#
# 泰波那契序列 Tn 定义如下：
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
#
#
#
# 示例 1：
#
# 输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
#
# 示例 2：
#
# 输入：n = 25
# 输出：1389537
#
#
#
#
# 提示：
#
#
# 0 <= n <= 37
# 答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
#
#
#


# @lc code=start
class Solution:
    # 备忘录加速
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1

        res = [0] * (n + 1)
        res[1] = 1
        res[2] = 1
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2] + res[i - 3]
        return res[n]


class Solution:
    # 递归解法会超时（重复计算太多）
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n == 1 or n == 2: return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)


# @lc code=end
