# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 示例 1: 
#
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
#
# 示例 2: 
#
# 输入: coins = [2], amount = 3
# 输出: -1
#
# 说明: 
# 你可以认为每种硬币的数量是无限的。
# Related Topics 动态规划

# 思路：
# dp[i]表示金额为i时所需要的最少硬币枚数

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(1, amount + 1):
                if i >= coin:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if dp[-1] != float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().coinChange(coins=[1, 2, 5], amount=11))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
