#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (65.75%)
# Likes:    579
# Dislikes: 0
# Total Accepted:    49.8K
# Total Submissions: 75.5K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#

# 思路：
# 如果节点i为根节点，左子树的节点的个数为i-1（为1,…i-1），右子树的个数为n-i（为i+1,…n）
# 对一个根来说，唯一二叉树的个数为左子树结点的个数乘以右子树的个数。
#
# 而根节点可以从1到n中选择。我们可以容易用递归实现，但是提交时间超限。
# 可以进一步思考使用动态规划，基本思路是一致的。
#
# 如n = 3时：
# dp[3] = dp[0] * dp[2]
# dp[3] = dp[1] * dp[1]
# dp[3] = dp[2] * dp[0]
# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n + 1)]
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            # 依次选j为根节点
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
# @lc code=end

