# 给定两个整数，被除数 dividend 和除数 divisor。
# 将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。 
#
# 示例 1: 
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
#
# 示例 2: 
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
#
# 说明: 
#
# 
# 被除数和除数均为 32 位有符号整数。 
# 除数不为 0。 
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231, 231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。 
# 
# Related Topics 数学 二分查找

# 思路：
# 这道题换句话说，就是除数能减去多少个被除数。
# 但是除数如果太小，则容易超时，这是要考虑除数的不断倍增。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = 0
        # 正数与正数做异或一定是正数，正数与负数做异或一定是负数
        sign = 1 if dividend ^ divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)

# leetcode submit region end(Prohibit modification and deletion)
