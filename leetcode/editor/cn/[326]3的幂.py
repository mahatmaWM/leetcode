# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1: 
#
# 输入: 27
# 输出: true
# 
#
# 示例 2: 
#
# 输入: 0
# 输出: false
#
# 示例 3: 
#
# 输入: 9
# 输出: true
#
# 示例 4: 
#
# 输入: 45
# 输出: false
#
# 进阶： 
# 你能不使用循环或者递归来完成本题吗？
# Related Topics 数学

# 思路：
# 整数范围内最大的3的幂次，即 3^19=1162261467，所以如果这个数字能被n整除，则n是3的幂

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 1162261467 % n == 0

# leetcode submit region end(Prohibit modification and deletion)
