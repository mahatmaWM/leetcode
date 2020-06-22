# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
#
# 示例 1: 
#
# 输入: 16
# 输出: true
# 
#
# 示例 2: 
#
# 输入: 5
# 输出: false
#
# 进阶： 
# 你能不使用循环或者递归来完成本题吗？
# Related Topics 位运算

# num & (num - 1) == 0判断是否是2的幂次方；同时如果bin表示中0的个数为偶数。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num & (num - 1) == 0 and str(bin(num)[2:]).count('0') % 2 == 0

# leetcode submit region end(Prohibit modification and deletion)
