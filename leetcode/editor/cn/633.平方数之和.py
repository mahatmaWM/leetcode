#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode-cn.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (33.42%)
# Likes:    122
# Dislikes: 0
# Total Accepted:    24.3K
# Total Submissions: 72.4K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c。
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
#
#


# @lc code=start
class Solution:
    # 双指针，从[0 根号c]范围内依次前后找合适的数字
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c**0.5)

        while left <= right:
            tmp = left**2 + right**2
            if tmp == c: return True
            if tmp < c:
                left += 1
            else:
                right -= 1
        return False


# @lc code=end
