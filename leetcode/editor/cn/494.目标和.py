#
# @lc app=leetcode.cn id=494 lang=python3
#
# [494] 目标和
#
# https://leetcode-cn.com/problems/target-sum/description/
#
# algorithms
# Medium (44.37%)
# Likes:    287
# Dislikes: 0
# Total Accepted:    30.7K
# Total Submissions: 69.3K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或
# -中选择一个符号添加在前面。
#
# 返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
#
#
#
# 示例：
#
# 输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
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
#
#
# 提示：
#
#
# 数组非空，且长度不会超过 20 。
# 初始的数组的和不会超过 1000 。
# 保证返回的最终结果能被 32 位整数存下。
#
#


# @lc code=start
# 思路一：回溯的思路，但是会超时
# 存在很多子问题，比如下面代码中，如果某一个nums[i]=0，就能一眼看出相同的backtrack函数被多次调用
# 所以先用备忘录来优化，就得到思路二的动态规划版本
class Solution1:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.res = 0

        def backtrack(nums, i, cur_sum, target):
            # 退出情况
            if i == len(nums):
                if cur_sum == target:
                    self.res += 1
                return
            # 选择列表
            # 选择 + 号
            cur_sum += nums[i]
            backtrack(nums, i + 1, cur_sum, target)
            cur_sum -= nums[i]
            # 选择 - 号
            cur_sum -= nums[i]
            backtrack(nums, i + 1, cur_sum, target)
            cur_sum += nums[i]

        if len(nums) == 0: return 0
        backtrack(nums, 0, 0, S)
        return self.res


# 思路二：使用备忘录来优化，避免递归回溯的过程中重复计算
class Solution2:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        memo = dict()

        def dp(nums, i, cur_sum, target):
            if i == len(nums):
                if cur_sum == target:
                    return 1
                return 0
            key = str(i) + '|' + str(cur_sum)
            if key in memo:
                return memo[key]
            res = dp(nums, i + 1, cur_sum + nums[i], target) + dp(nums, i + 1, cur_sum - nums[i], target)
            memo[key] = res
            return res

        if len(nums) == 0: return 0
        return dp(nums, 0, 0, S)


# 思路三，转化原始问题为标准的动态规划问题（0-1背包问题）
# dp[i][j]表示从前i个物品中挑选元素是否能填满容量为j的背包，
# 原始的背包问题是 选 或者 不选，而本题的要求是选+ 或者 选-，因此转移方程变为：
# dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
# 注意转移方程里面有j-nums[i]这一项，说明下标有可能为负数，最大为-1000，所以第二位统一右移1000
#
class Solution:

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # dp初始状态，使用dp字典来代替dp数组，可以不用去考虑数组边界的问题，会方便很多
        length = len(nums)
        dp = {(0, 0): 1}
        for i in range(1, length + 1):
            for j in range(-sum(nums), sum(nums) + 1):
                # 第i个数字选 + 或 -
                dp[(i, j)] = dp.get((i - 1, j - nums[i - 1]), 0) + dp.get((i - 1, j + nums[i - 1]), 0)
        return dp.get((length, S), 0)


# @lc code=end
