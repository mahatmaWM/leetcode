# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
#
# 示例: 
#
# 输入: 38
# 输出: 2
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 
#
# 进阶: 
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
# Related Topics 数学

# 把num先分解 num = (a[0] * 1 + a[1] * 10 + …a[n] * 10 ^n) (a[i]都在0-9之间)
# 先来看一组mod 9 效果
# 1 % 9 = 1
# 10 % 9 = 1
# 100 % 9 = 1
# ......
# 10^N % 9 = 1
#
# 因此直接把num % 9得到的就是a[0] + a[1] + …a[n],并且如果a[0] + a[1] + …a[n] > 10的话还会继续mod 9下去直到变为个位数
# 就得到一下非常简洁迅速的解法，注意最后非零情况不直接return num % 9 而是 return (num-1)%9+1 是为了避免9%9=0这个错误情况

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 0 if num == 0 else (num - 1) % 9 + 1

# leetcode submit region end(Prohibit modification and deletion)
