# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。
#
# 示例 1: 
#
# 输入: n = 12
# 输出: 3
# 解释: 12 = 4 + 4 + 4.
#
# 示例 2: 
#
# 输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9.
# Related Topics 广度优先搜索 数学 动态规划

# 动态规划思路：维护一个长度为n+1的数组，第i位存储和为i的最少整数个数。则f(i)只与i之前的数组有关。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        output = [0x7fffffff] * (n + 1)
        output[0] = 0
        output[1] = 1
        for i in range(2, n + 1):
            j = 1
            while j * j <= i:
                output[i] = min(output[i], output[i - j * j] + 1)
                j = j + 1

        return output[n]

# leetcode submit region end(Prohibit modification and deletion)
