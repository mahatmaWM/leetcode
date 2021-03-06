#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#
# https://leetcode-cn.com/problems/water-and-jug-problem/description/
#
# algorithms
# Medium (35.09%)
# Likes:    219
# Dislikes: 0
# Total Accepted:    24.1K
# Total Submissions: 68.6K
# Testcase Example:  '3\n5\n4'
#
# 有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？
#
# 如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。
#
# 你允许：
#
#
# 装满任意一个水壶
# 清空任意一个水壶
# 从一个水壶向另外一个水壶倒水，直到装满或者倒空
#
#
# 示例 1: (From the famous "Die Hard" example)
#
# 输入: x = 3, y = 5, z = 4
# 输出: True
#
#
# 示例 2:
#
# 输入: x = 2, y = 6, z = 5
# 输出: False
#
#
#

# @lc code=start
import math


class Solution:

    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x + y: return False
        t = math.gcd(x, y)
        if t == 0:
            return True if z == x or z == y else False
        else:
            return True if z % t == 0 else False

# @lc code=end
