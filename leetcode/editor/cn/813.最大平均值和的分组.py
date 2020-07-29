#
# @lc app=leetcode.cn id=813 lang=python3
#
# [813] 最大平均值和的分组
#
# https://leetcode-cn.com/problems/largest-sum-of-averages/description/
#
# algorithms
# Medium (49.92%)
# Likes:    89
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 5.3K
# Testcase Example:  '[9,1,2,3,9]\n3'
#
# 我们将给定的数组 A 分成 K 个相邻的非空子数组 ，我们的分数由每个子数组内的平均值的总和构成。计算我们所能得到的最大分数是多少。
#
# 注意我们必须使用 A 数组中的每一个数进行分组，并且分数不一定需要是整数。
#
#
# 示例:
# 输入:
# A = [9,1,2,3,9]
# K = 3
# 输出: 20
# 解释:
# A 的最优分组是[9], [1, 2, 3], [9]. 得到的分数是 9 + (1 + 2 + 3) / 3 + 9 = 20.
# 我们也可以把 A 分成[9, 1], [2], [3, 9].
# 这样的分组得到的分数为 5 + 2 + 6 = 13, 但不是最大值.
#
#
# 说明:
#
#
# 1 <= A.length <= 100.
# 1 <= A[i] <= 10000.
# 1 <= K <= A.length.
# 答案误差在 10^-6 内被视为是正确的。
#
#
#


# @lc code=start
class Solution:
    # 动态规划，dp[i][k] 代表将A的前i个数字分成k组得到的最大平均值
    # 则dp[i][k] = max(dp[i][k], dp[j][k-1]+avg(j+1, i))，其中j可变（从k-1到i）
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)

        # 计算avg的时候，使用前缀和加速
        cur_sum = [0]
        for i in A:
            cur_sum.append(cur_sum[-1] + i)

        def avg(i, j):
            return (cur_sum[j] - cur_sum[i]) / float(j - i)

        dp = [[0.0 for _ in range(K + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][1] = avg(0, i)

        for k in range(2, K + 1):
            for i in range(k, n + 1):
                for j in range(k - 1, i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + avg(j, i))
        return dp[-1][-1]


# @lc code=end
