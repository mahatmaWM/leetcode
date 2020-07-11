#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (70.82%)
# Likes:    189
# Dislikes: 0
# Total Accepted:    59.2K
# Total Submissions: 83.6K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
#
# 示例 1:
#
#
# 输入: "Let's take LeetCode contest"
# 输出: "s'teL ekat edoCteeL tsetnoc" 
#
#
# 注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
#
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([item[::-1] for item in s.split()])

# @lc code=end

