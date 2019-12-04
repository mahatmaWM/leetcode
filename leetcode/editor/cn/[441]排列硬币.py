# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
#
# 给定一个数字 n，找出可形成完整阶梯行的总行数。 
#
# n 是一个非负整数，并且在32位有符号整型的范围内。 
#
# 示例 1: 
#
# 
# n = 5
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤
#
# 因为第三行不完整，所以返回2.
# 
#
# 示例 2: 
#
# 
# n = 8
#
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# 因为第四行不完整，所以返回3.
# 
# Related Topics 数学 二分查找

# 直接迭代n寻找会超时。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        while low <= high:
            mid = int((low + high) / 2)
            left_coin = n - (mid + 1) * mid / 2
            if 0 <= left_coin < mid + 1:
                return mid
            elif left_coin >= mid + 1:
                low = mid + 1
            elif left_coin < 0:
                high = mid - 1

# leetcode submit region end(Prohibit modification and deletion)
