#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words/description/
#
# algorithms
# Hard (30.77%)
# Likes:    278
# Dislikes: 0
# Total Accepted:    35.1K
# Total Submissions: 113.9K
# Testcase Example:  '"barfoothefoobarman"\n["foo","bar"]'
#
# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
#
#
#
# 示例 1：
#
# 输入：
# ⁠ s = "barfoothefoobarman",
# ⁠ words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
#
#
# 示例 2：
#
# 输入：
# ⁠ s = "wordgoodgoodgoodbestword",
# ⁠ words = ["word","good","best","word"]
# 输出：[]
#
#
#


# @lc code=start
class Solution:
    # 通过滑动窗口来取子字符串，并通过字典对象比较单词的出现次数可以求解这个问题
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) <= 0 or len(words) == 0: return []

        res = []
        dic_words = {}
        for w in words:
            dic_words[w] = dic_words.get(w, 0) + 1

        len_word = len(words[0])
        target_len = len_word * len(words)
        left = 0
        while left + target_len <= len(s):
            dic_substr = {}
            substr = s[left:left + target_len]
            # 检查子串合法性
            k = 0
            while k + len_word <= len(substr):
                temp_word = substr[k:k + len_word]
                if temp_word not in dic_words: break
                dic_substr[temp_word] = dic_substr.get(temp_word, 0) + 1
                k = k + len_word
            if dic_words == dic_substr: res.append(left)
            left = left + 1
        return res


# @lc code=end
