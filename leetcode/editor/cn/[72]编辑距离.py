# 给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作： 
#
# 
# 插入一个字符 
# 删除一个字符 
# 替换一个字符 
# 
#
# 示例 1: 
#
# 输入: word1 = "horse", word2 = "ros"
# 输出: 3
# 解释:
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 
#
# 示例 2: 
#
# 输入: word1 = "intention", word2 = "execution"
# 输出: 5
# 解释:
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
# 
# Related Topics 字符串 动态规划

# 设置一个distance[m+1][n+1]的数组，distance[i][j]用来保存word1第i位变成word2第j位的最小变化次数。
# 每次计算的时候，选取删除，插入，交换中的最小值。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if word1 == word2 or m == n == 0:
            return 0
        distance = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            distance[i][0] = i
        for j in range(n + 1):
            distance[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                delete = distance[i - 1][j] + 1
                insert = distance[i][j - 1] + 1
                swap = distance[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    swap += 1
                distance[i][j] = min(delete, insert, swap)
        return distance[i][j]

# leetcode submit region end(Prohibit modification and deletion)
