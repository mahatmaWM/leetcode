#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (48.89%)
# Likes:    121
# Dislikes: 0
# Total Accepted:    27.7K
# Total Submissions: 56.5K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
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
#
#

# @lc code=start
class Solution:
    # num & (num - 1) == 0判断是否是2的幂次方；同时如果bin表示中0的个数为偶数。
    def isPowerOfFour(self, num: int) -> bool:
        return num & (num - 1) == 0 and str(bin(num)[2:]).count('0') % 2 == 0

# @lc code=end

