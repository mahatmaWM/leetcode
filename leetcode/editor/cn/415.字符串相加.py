# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
#
# 注意： 
#
# 
# num1 和num2 的长度都小于 5100. 
# num1 和num2 都只包含数字 0-9. 
# num1 和num2 都不包含任何前导零。 
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。 
# 
# Related Topics 字符串


# itertools.izip_longest 这个函数能将两个字符串转换为每位对应的tuple，不够的可以补齐你指定的字符，这个方法简直太好用了.

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        import itertools
        res, jinwei = "", 0
        for (x, y) in itertools.izip_longest(num1[::-1], num2[::-1], fillvalue='0'):
            s = (int(x) + int(y) + jinwei)
            d, jinwei = s % 10, s // 10
            res = str(d) + res

        if jinwei > 0:
            res = str(jinwei) + res

        return res

# leetcode submit region end(Prohibit modification and deletion)
