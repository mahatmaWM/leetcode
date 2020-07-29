#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (53.75%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    28.7K
# Total Submissions: 53.3K
# Testcase Example:  '[1,2,3,0,2]'
#
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
#
#
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
#
#


# @lc code=start
class Solution:
    # dp[i][j]代表 第i天 不持有或者持有 股票的最大收益
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[1][0] = 0
        dp[1][1] = -prices[0]

        # 不限制交易次数
        for i in range(2, n + 1):
            # 第i天不持有股票
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            # 第i天持有股票
            if i > 2:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i - 1])
            else:
                # 第2天有股票的最大收益
                dp[i][1] = max(dp[i - 1][1], -prices[i - 1])
        return dp[-1][0]

# @lc code=end
if __name__ == "__main__":
    print(Solution().maxProfit(prices=[1, 2, 4]))
