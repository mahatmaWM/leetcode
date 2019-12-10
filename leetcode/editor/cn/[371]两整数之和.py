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
        if b == 0:
            return a
        else:
            return self.getSum(a ^ b, (a & b) << 1)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().getSum(a = -2, b = 3))
