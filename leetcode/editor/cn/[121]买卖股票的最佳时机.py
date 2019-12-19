# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。 
#
# 注意你不能在买入股票前卖出股票。 
#
# 示例 1: 
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 
#
# 示例 2: 
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# Related Topics 数组 动态规划

# 思路：遍历数组，对于位置i，与i之前最小的购入价格比较即可。
# min_buy记录位置i左边的最小值。
# profit为遍历到位置i时的最大收益。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit, pre_min_buy = 0, prices[0]
        for i in prices:
            pre_min_buy = min(i, pre_min_buy)
            max_profit = max(i - pre_min_buy, max_profit)
        return max_profit

# leetcode submit region end(Prohibit modification and deletion)
