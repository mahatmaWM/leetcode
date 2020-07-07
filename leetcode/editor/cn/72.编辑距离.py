#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#
# https://leetcode-cn.com/problems/edit-distance/description/
#
# algorithms
# Hard (59.35%)
# Likes:    922
# Dislikes: 0
# Total Accepted:    62.7K
# Total Submissions: 105.6K
# Testcase Example:  '"horse"\n"ros"'
#
# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#
#
#
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#
#
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#
#
#


# @lc code=start
class Solution:
    # 思路，设置一个dp[m+1][n+1]的数组，dp[i][j]用来保存word1的(0到i)位变成word2的(0到j)位的最小变化次数。
    # 每次计算的时候，选取删除，插入，交换中的最小值。
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if word1 == word2 or m == n == 0: return 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 第一列和第一行的初始化
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 分别为删除1位、插入1位、交换1位
                    delete = dp[i - 1][j]
                    insert = dp[i][j - 1]
                    swap = dp[i - 1][j - 1]
                    dp[i][j] = min(delete, insert, swap) + 1
        return dp[i][j]


# @lc code=end
