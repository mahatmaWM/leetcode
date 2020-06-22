# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。
#
# 示例1: 
#
# 
# 输入: 5
# 输出: True
# 解释: 1 * 1 + 2 * 2 = 5
# 
#
# 
#
# 示例2: 
#
# 
# 输入: 3
# 输出: False
# 
# Related Topics 数学

# 思路：
# 从0到根号c范围内依次前后找合适的数字

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            tmp = left ** 2 + right ** 2
            if tmp < c:
                left += 1
            elif tmp == c:
                return True
            else:
                right -= 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = Solution()
    print(a.judgeSquareSum(c=5))
