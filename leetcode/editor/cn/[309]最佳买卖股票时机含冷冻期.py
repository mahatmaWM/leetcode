# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。
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
# Related Topics 动态规划

# 参考 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/#comment
# 思路：由于没有交易次数限制，那么dp[i][0]代表第i天没有股票，dp[i][1]代表第i天持有股票
# dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
# dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
# 解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
# 可以优化dp空间


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp_0, dp_1 = [0] * n, [0] * n

        for i in range(0, n):
            dp_0[i] = max(dp_0[i-1], dp_1[i - 1] + prices[i])
            if i >=2:
                dp_1[i] = max(dp_1[i-1], dp_1[i - 2] - prices[i])
        print(dp_0, dp_1)
        return dp_0[n-1]



# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().maxProfit(prices=[1,2,3,0,2]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
