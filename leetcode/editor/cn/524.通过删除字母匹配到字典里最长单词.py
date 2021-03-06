#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
# https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (45.55%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    15.1K
# Total Submissions: 33K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
#
# 给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。
#
# 示例 1:
#
#
# 输入:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]
#
# 输出:
# "apple"
#
#
# 示例 2:
#
#
# 输入:
# s = "abpcplea", d = ["a","b","c"]
#
# 输出:
# "a"
#
#
# 说明:
#
#
# 所有输入的字符串只包含小写字母。
# 字典的大小不会超过 1000。
# 所有输入的字符串长度不会超过 1000。
#
#
#


# @lc code=start
class Solution:
    # 1、把字典按照单词长度以及字典序排序
    # 2、依次检查排序后的字典中的每个单词是否可以由s得到，找到就返回结果
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))

        def isSubSeq(word, s):
            i = 0
            for c in s:
                if c == word[i]: i += 1
                if i == len(word): return True
            return False

        for word in d:
            if isSubSeq(word, s): return word
        return ''


# @lc code=end
