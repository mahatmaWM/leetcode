#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#
# https://leetcode-cn.com/problems/count-binary-substrings/description/
#
# algorithms
# Easy (52.38%)
# Likes:    157
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 21.8K
# Testcase Example:  '"00110"'
#
# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。
#
# 重复出现的子串要计算它们出现的次数。
#
# 示例 1 :
#
#
# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。
#
# 请注意，一些重复出现的子串要计算它们出现的次数。
#
# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
#
#
# 示例 2 :
#
#
# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
#
#
# 注意：
#
#
# s.length 在1到50,000之间。
# s 只包含“0”或“1”字符。
#
#
#

# @lc code=start
class Solution:
    # 思路：我们可以把一个字符串分组，来记录数字出现了多少次。
    # 比如 00111 我们可以分成groups=[2,3]，11110可以分成groups=[4,1]。
    # 这样当最后计数的时候，对每一个值取min(groups[i-1], groups[i])。
    #
    # 这是为什么呢？  
    # 试想groups=[2,3]的情况，要么是00111要么是11000，无论是哪一种情况都只有 0011 、01或是1100、10两个子串符合条件，也就是groups中相邻两数的最小值。
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i - 1], groups[i])
        return ans

# @lc code=end

