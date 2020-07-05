#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (36.31%)
# Likes:    305
# Dislikes: 0
# Total Accepted:    32.2K
# Total Submissions: 88.6K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
#
# 示例 1:
#
# 输入: [10,2]
# 输出: 210
#
# 示例 2:
#
# 输入: [3,30,34,5,9]
# 输出: 9534330
#
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
#
#


# @lc code=start
class Solution:

    def largestNumber(self, nums: List[int]) -> str:

        class compare(str):

            def __lt__(x, y):
                return x + y > y + x

        largest = ''.join(sorted([str(v) for v in nums], key=compare))
        return '0' if largest[0] == '0' else largest


# @lc code=end
