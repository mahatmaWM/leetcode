# 不使用运算符 + 和 - ，计算两整数 a 、b 之和。
#
# 示例 1: 
#
# 输入: a = 1, b = 2
# 输出: 3
# 
#
# 示例 2: 
#
# 输入: a = -2, b = 3
# 输出: 1
# Related Topics 位运算

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().getSum(a=-2, b=3))
