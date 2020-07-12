#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (42.81%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    26.8K
# Total Submissions: 62.4K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
#
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。
#
#


# @lc code=start
class Solution:
    # 把pattern转化为每个字母首次出现的位置，如abba=0110
    # 把str变成list，然后找每个字符串出现的位置，"dog cat cat dog" 变为 0110
    # 然后对比两个数字串
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        if len(words) != len(pattern): return False
        # 字母中每个字符第一次出现的位置
        # list中每个元素第一次出现的位置
        if [i for i in map(pattern.find, pattern)] == [i for i in map(words.index, words)]: return True
        return False


# @lc code=end
