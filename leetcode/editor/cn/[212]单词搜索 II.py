# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
#
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
# 同一个单元格内的字母在一个单词中不允许被重复使用。
#
# 示例: 
#
# 输入: 
# words = ["oath","pea","eat","rain"] and board =
# [
#  ['o','a','a','n'],
#  ['e','t','a','e'],
#  ['i','h','k','r'],
#  ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
#
# 说明: 
# 你可以假设所有输入都由小写字母 a-z 组成。
#
# 提示: 
#
# 
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？ 
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。
# 什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？
#
# Related Topics 字典树 回溯算法


# 思路：
# 1 把words中的word存入前缀树
# 2 对board进行深度优先搜索
# dfs三个核心部分：
# 1 新的字符不在搜索范围内，退出
# 2 新的字符在搜索范围内，且该字符与之前的字符串为words中的一个word,加入结果集，并将word结束标志置0，放置重复搜索
# 3 按深度优先递归搜索

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.res = []

        def dfs(i, j, t, s):
            # 递归结束
            ch = board[i][j]
            if ch not in t:
                return
            t = t[ch]
            if "end" in t and t["end"] == 1:
                self.res.append(s + ch)
                t["end"] = 0
            # 开始回溯i j位置
            board[i][j] = "#"
            # down
            if i + 1 < m and board[i + 1][j] != "#":
                dfs(i + 1, j, t, s + ch)
            # up
            if i - 1 >= 0 and board[i - 1][j] != "#":
                dfs(i - 1, j, t, s + ch)
            # right
            if j + 1 < n and board[i][j + 1] != "#":
                dfs(i, j + 1, t, s + ch)
            # left
            if j - 1 >= 0 and board[i][j - 1] != "#":
                dfs(i, j - 1, t, s + ch)
            board[i][j] = ch

        # 将word存入前缀树
        trie = {}
        for word in words:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t["end"] = 1

        m = len(board)
        n = len(board[0])
        # 对board进行深度优先搜索
        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, "")
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    print(Solution().findWords(board=board, words=words))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
