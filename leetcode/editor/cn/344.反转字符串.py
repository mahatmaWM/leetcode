#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
# https://leetcode-cn.com/problems/reverse-string/description/
#
# algorithms
# Easy (70.46%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    147.8K
# Total Submissions: 209.8K
# Testcase Example:  '["h","e","l","l","o"]'
#
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
#
#
# 示例 1：
#
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
#
#
# 示例 2：
#
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
#
#

# @lc code=start
class Solution:
    # 注意这种反转的场景，[left, right]两边闭合的区间会少遍历一次
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
# @lc code=end
