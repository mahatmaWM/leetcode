# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
#
# 说明：不要使用任何内置的库函数，如 sqrt。 
#
# 示例 1： 
#
# 输入：16
# 输出：True
#
# 示例 2： 
#
# 输入：14
# 输出：False
# 
# Related Topics 数学 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1
        high = num
        while low < high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return low * low == num

# leetcode submit region end(Prohibit modification and deletion)
