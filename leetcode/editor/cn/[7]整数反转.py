# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1: 
#
# 输入: 123
# 输出: 321
# 
#
# 示例 2: 
#
# 输入: -123
# 输出: -321
# 
#
# 示例 3: 
#
# 输入: 120
# 输出: 21
# 
#
# 注意: 
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
# Related Topics 数学

# 思路：
# 直接反转数字，注意符号与数字合法性判断

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1 if x >= 0 else -1
        new_x, x = 0, abs(x)
        while x:
            new_x = 10 * new_x + x % 10
            x = x // 10
        new_x = flag * new_x
        return new_x if 2147483648 > new_x >= -2147483648 else 0


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().reverse(x=121))
