# 统计所有小于非负整数 n 的质数的数量。
#
# 示例:
#
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
#
# Related Topics 哈希表 数学

# 设置长度为n的hash数组，不断用2和根号n中的数字去尝试更改hash数组的true&false值。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]: primes[2 * i: n: i] = [False] * len(primes[2 * i: n: i])
        return sum(primes)

# leetcode submit region end(Prohibit modification and deletion)
