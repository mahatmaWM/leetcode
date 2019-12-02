# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。 
#
# 示例 1: 
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2: 
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        i, j, plus = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0 or plus == 1:
            plus += int(a[i]) if i >= 0 else 0
            plus += int(b[j]) if j >= 0 else 0
            res = str(plus % 2) + res
            i, j, plus = i - 1, j - 1, plus / 2
        return res

# leetcode submit region end(Prohibit modification and deletion)
