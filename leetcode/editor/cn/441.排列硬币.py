#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#
# https://leetcode-cn.com/problems/arranging-coins/description/
#
# algorithms
# Easy (40.90%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    23.8K
# Total Submissions: 58K
# Testcase Example:  '5'
#
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
#
# 给定一个数字 n，找出可形成完整阶梯行的总行数。
#
# n 是一个非负整数，并且在32位有符号整型的范围内。
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
#
#


# @lc code=start
class Solution:
    # 二分查找，直接迭代n寻找会超时
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n + 1
        while low < high:
            mid = low + (high - low) // 2
            # print('low={},mid={},high={}'.format(low, mid, high))
            coin_left = n - (mid + 1) * mid // 2
            if 0 <= coin_left < mid + 1: return mid
            if coin_left >= mid + 1:
                low = mid + 1
            elif coin_left < 0:
                high = mid


# @lc code=end
