#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#
# https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (44.92%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    12.3K
# Total Submissions: 27.3K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search","search","search","search"]\n' +
  '[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# 设计一个支持以下两种操作的数据结构：
#
# void addWord(word)
# bool search(word)
#
#
# search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
#
# 示例:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# 说明:
#
# 你可以假设所有单词都是由小写字母 a-z 组成的。
#
#

# @lc code=start
class WordDictionary:
    # trie树
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        t = self.d
        for c in word:
            if c not in t: t[c] = {}
            t = t[c]
        t['end'] = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        """
        cut = False
        #深搜，参数为：当前子字典，当前串
        def f(td, s):
            nonlocal cut
            if cut: return True
            t = td
            for i, c in enumerate(s):
                if c == '.': return any(f(t[j], s[i + 1: ]) for j in t if j != 'end')    #深搜扩展
                if c not in t: return False
                t = t[c]
            cut = 'end' in t
            return cut
        return f(self.d, word)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

