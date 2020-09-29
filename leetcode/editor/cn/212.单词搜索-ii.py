#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# https://leetcode-cn.com/problems/word-search-ii/description/
#
# algorithms
# Hard (40.79%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 37.2K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' + '["oath","pea","eat","rain"]'
#
# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
# 示例:
#
# 输入:
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
# 提示:
#
#
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
# 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。
#
#
#

# @lc code=start
class Solution:
    # 思路：
    # 1 把words中的word存入前缀树
    # 2 对board进行深度优先搜索
    #
    # dfs三个核心部分：
    # 1 新的字符不在搜索范围内，退出
    # 2 新的字符在搜索范围内，且该字符与之前的字符串为words中的一个word，加入结果集，并将word结束标志置0，防止重复搜索
    # 3 按深度优先递归搜索
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        def dfs(i, j, t, s):
            nonlocal res
            # 递归结束
            ch = board[i][j]
            if ch not in t: return
            t = t[ch]
            if "end" in t and t["end"] == 1:
                res.append(s + ch)
                t["end"] = 0

            # 开始回溯i j位置
            board[i][j] = "#"
            # down, up, right, left
            if i + 1 < m and board[i + 1][j] != "#": dfs(i + 1, j, t, s + ch)
            if i - 1 >= 0 and board[i - 1][j] != "#": dfs(i - 1, j, t, s + ch)
            if j + 1 < n and board[i][j + 1] != "#": dfs(i, j + 1, t, s + ch)
            if j - 1 >= 0 and board[i][j - 1] != "#": dfs(i, j - 1, t, s + ch)
            board[i][j] = ch

        # 将word存入前缀树
        trie = {}
        for word in words:
            t = trie
            for ch in word:
                if ch not in t: t[ch] = {}
                t = t[ch]
            t["end"] = 1

        m = len(board)
        n = len(board[0])
        # 对board进行深度优先搜索
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
        return res
# @lc code=end

