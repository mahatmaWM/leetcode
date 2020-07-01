#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
# https://leetcode-cn.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (67.37%)
# Likes:    330
# Dislikes: 0
# Total Accepted:    42K
# Total Submissions: 62.2K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
  '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
#
# 说明:
#
#
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串。
#
#
#

# @lc code=start
class Trie:
    # 嵌套使用dict创建简单的trie树结构。
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree: tree[a] = {}
            tree = tree[a]
        # 单词结束标志
        tree["#"] = "#"


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.lookup
        for a in word:
            if a not in tree: return False
            tree = tree[a]
        if "#" in tree: return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.lookup
        for a in prefix:
            if a not in tree: return False
            tree = tree[a]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

