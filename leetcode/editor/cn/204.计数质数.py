#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (33.98%)
# Likes:    367
# Dislikes: 0
# Total Accepted:    60.8K
# Total Submissions: 178.8K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
#
#

# @lc code=start
class Solution:
    # 设置长度为n的hash数组，不断用2和根号n中的数字去尝试更改hash数组的true&false值。
    # 素数筛选算法
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]: primes[2 * i: n: i] = [False] * len(primes[2 * i: n: i])
        return sum(primes)
# @lc code=end

