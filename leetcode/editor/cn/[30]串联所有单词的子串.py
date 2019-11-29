# 给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
#
# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。 
#
# 
#
# 示例 1： 
#
# 输入：
#  s = "barfoothefoobarman",
#  words = ["foo","bar"]
# 输出：[0,9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9,0] 也是有效答案。
# 
#
# 示例 2： 
#
# 输入：
#  s = "wordgoodgoodgoodbestword",
#  words = ["word","good","best","word"]
# 输出：[]
# 
# Related Topics 哈希表 双指针 字符串

# 通过滑动窗口来取子字符串，并通过字典对象比较单词的出现次数可以求解这个问题

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if 0 > len(s) or len(s) == 0 or len(words) == 0:
            return res

        dic_words = {}
        for w in words:
            if w in dic_words:
                dic_words[w] += 1
            else:
                dic_words[w] = 1

        len_word = len(words[0])
        str_length = len_word * len(words)

        j = 0
        while j + str_length <= len(s):
            dic_substr = {}
            substr = s[j: j + str_length]
            k = 0
            while k + len_word <= len(substr):
                temp_word = substr[k: k + len_word]
                if temp_word in dic_words:
                    if temp_word in dic_substr:
                        dic_substr[temp_word] += 1
                    else:
                        dic_substr[temp_word] = 1
                    k = k + len_word
                else:
                    break

            if dic_words == dic_substr:
                res.append(j)

            j = j + 1

        return res

# leetcode submit region end(Prohibit modification and deletion)
