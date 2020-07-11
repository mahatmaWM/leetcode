#
# @lc app=leetcode.cn id=336 lang=python3
#
# [336] 回文对
#
# https://leetcode-cn.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (33.31%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    4.1K
# Total Submissions: 12.4K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
# 给定一组唯一的单词， 找出所有不同 的索引对(i, j)，使得列表中的两个单词， words[i] + words[j] ，可拼接成回文串。
#
# 示例 1:
#
# 输入: ["abcd","dcba","lls","s","sssll"]
# 输出: [[0,1],[1,0],[3,2],[2,4]]
# 解释: 可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
#
#
# 示例 2:
#
# 输入: ["bat","tab","cat"]
# 输出: [[0,1],[1,0]]
# 解释: 可拼接成的回文串为 ["battab","tabbat"]
#
#


# @lc code=start
class Solution:
    # 常规两个遍历枚举所有的pair对，并依次判断每队的方式会超时
    # 以下是对每个word预处理了其 合法前缀 合法后缀，结合hash，能一次遍历数组内完成查找
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # 对word而言，将其分为word[0:i], word[i:], 如果word[i:]本身为回文，则word[0:i]就是一个合法前缀
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]: valid_prefixes.append(word[:i])
            return valid_prefixes

        # 对word而言，将其分为word[0:i], word[i:], 如果word[0:i]本身为回文，则word[i:]就是一个合法后缀
        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i + 1] == word[:i + 1][::-1]: valid_suffixes.append(word[i + 1:])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        solutions = []

        for word_index, word in enumerate(words):
            reversed_word = word[::-1]
            # 情况1，两个单词刚好反序，则合在一起为回文
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                solutions.append([word_index, word_lookup[reversed_word]])
            # 情况2，对word的所有合法后缀而言，如果能找到其逆序word，则能组合成回文
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup: solutions.append([word_lookup[reversed_suffix], word_index])
            # 情况3，对word的所有合法前缀而言，如果能找到其逆序word，则能组合成回文
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup: solutions.append([word_index, word_lookup[reversed_prefix]])
        return solutions


# @lc code=end
