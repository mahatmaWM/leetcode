#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# https://leetcode-cn.com/problems/keyboard-row/description/
#
# algorithms
# Easy (69.05%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 26.3K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
#
#
#
#
#
#
#
# 示例：
#
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
#
#
#
#
# 注意：
#
#
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。
#
#


# @lc code=start
class Solution:

    def findWords(self, words: List[str]) -> List[str]:
        T = []
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')

        def match(set0, str0):
            if not (set(str0.lower()) - set0): return True
            return False

        for i in range(len(words)):
            if match(set1, words[i]) or match(set2, words[i]) or match(set3, words[i]):
                T.append(words[i])
        return T


# @lc code=end
