# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。 
#
# 示例 1: 
#
# 输入: nums: [1, 1, 1, 1, 1], S: 3
# 输出: 5
# 解释:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# 一共有5种方法让最终目标和为3。
# 
#
# 注意: 
#
# 
# 数组非空，且长度不会超过20。 
# 初始的数组的和不会超过1000。 
# 保证返回的最终结果能被32位整数存下。 
# 
# Related Topics 深度优先搜索 动态规划

# 思路1：
# 深度优先搜索的方法比较直观。
#
# 思路2：
# 动态规划，借鉴0-1背包问题的思路，dp[i][j]表示从前i个物品中挑选元素是否能填满容量为j的背包，但原始的背包问题
#
# 是 选 或者 不选，而本题的要求是选+ 或者 选-，因此转移方程变为：
# dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
# 注意转移方程里面有j-nums[i]这一项，说明下标有可能为负数，最大为-1000，所以第二位统一右移1000


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # 深度优先搜索，枚举所有情况，O(2^N)
    def findTargetSumWays1(self, nums: List[int], S: int) -> int:
        self.res = 0

        def dfs(nums, i, tmp_sum, target):
            if i == len(nums):
                if tmp_sum == target:
                    self.res += 1
            else:
                dfs(nums, i + 1, tmp_sum + nums[i], target)
                dfs(nums, i + 1, tmp_sum - nums[i], target)

        dfs(nums, 0, 0, S)
        return self.res

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 使用dp字典来代替dp数组，可以不用去考虑数组边界的问题，这里会方便很多

        # dp初始状态
        length, dp = len(nums), {(0, 0): 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                # 第i个数字选+或者-
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + \
                             dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((length, S), 0)


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], S=3))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
