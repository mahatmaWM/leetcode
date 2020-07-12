# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，
# 然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。
# 如果可以变为 1，那么这个数就是快乐数。
#
# 示例:
#
# 输入: 19
# 输出: true
# 解释:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1
#
# Related Topics 哈希表 数学

# 按照定义的过程处理，并用mem来记录每次出现的数字，防止出现死循环。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()
        while n != 1:
            n = sum([int(i) ** 2 for i in str(n)])
            if n in mem: return False
            mem.add(n)
        else:
            return True

# leetcode submit region end(Prohibit modification and deletion)
