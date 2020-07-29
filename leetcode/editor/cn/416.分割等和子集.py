#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
# https://leetcode-cn.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (47.64%)
# Likes:    340
# Dislikes: 0
# Total Accepted:    42.9K
# Total Submissions: 88.2K
# Testcase Example:  '[1,5,11,5]'
#
# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
#
# 注意:
#
#
# 每个数组中的元素不会超过 100
# 数组的大小不会超过 200
#
#
# 示例 1:
#
# 输入: [1, 5, 11, 5]
#
# 输出: true
#
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#
#
#
#
# 示例 2:
#
# 输入: [1, 2, 3, 5]
#
# 输出: false
#
# 解释: 数组不能分割成两个元素和相等的子集.
#
#
#
#
#

# @lc code=start
class Solution1:
    # 转化为0-1背包问题，dp[i][j]表示能否在前i个物品中 选或者不选 可以装满容量j的背包。
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0: return False
        target = target // 2

        # 初始化，并且把只取一个物品能填的位置 置为True
        dp = [[False] * (target + 1) for _ in range(n)]
        dp[0][0] = True
        for i in range(1, target + 1):
            if nums[0] == i: dp[0][i] = True

        for i in range(1, n):
            for j in range(target + 1):
                # 当前容量大于等于当前物品的重量时，dp[i][j] = dp[i - 1][j]（当前不取）or dp[i - 1][j - nums[i]]（当前要取）
                # 否则当前不取
                if j >= nums[i]:
                    dp[i][j] = dp[i - 1][j] or (dp[i - 1][j - nums[i]])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

class Solution:
    # 考虑到递推公式中dp[i][j] 仅依赖于dp[i - 1][*]的状态，
    # 不会再看之前i-2的状态，所以迭代的过程中就没有必要保存之前的状态了，使用一个pre和curr一维数组来优化空间。
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0: return False
        target //= 2
        pre = [False] * (target + 1)
        cur = [False] * (target + 1)
        pre[0] = True
        for i in range(1, target + 1):
            if nums[0] == i: pre[i] = True
        for i in range(1, n):
            for j in range(target + 1):
                if j >= nums[i]:
                    cur[j] = pre[j] or (pre[j - nums[i]])
                else:
                    cur[j] = pre[j]
            pre = cur[:]
        return cur[-1]
# @lc code=end

