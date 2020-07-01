#
# @lc app=leetcode.cn id=673 lang=python3
#
# [673] 最长递增子序列的个数
#
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (35.55%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    8.9K
# Total Submissions: 25.1K
# Testcase Example:  '[1,3,5,4,7]'
#
# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
# 示例 1:
#
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
#
#
# 示例 2:
#
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
#
#
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。
#
# https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/solution/dong-tai-gui-hua-jie-zui-chang-zi-xu-lie-zi-chua-4/


# @lc code=start
class Solution:
    # 假设对于以 nums[i] 结尾的序列，我们知道其最长序列的长度为 length[i]，以及具有该长度的序列的个数为 count[i]。
    # 对于每一个 i<j 且 nums[i]<nums[j] ，我们可以将 nums[j] 附加到以 nums[i] 结尾的子序列上。
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n
        dp = [0] * n  #dp[i] = longest ending in nums[i]
        counts = [1] * n  #count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in range(j):
                # 说明无论如何，位置j处的最长长度dp[j]至少可+1
                if nums[i] < nums[j]:
                    # 位置j之前的长度更小，说明位置j的最长长度可以+1，但是其个数可以由位置i的个数继承而来
                    if dp[i] + 1 > dp[j]:
                        dp[j] = 1 + dp[i]
                        counts[j] = counts[i]
                    # 如果位置j之前的长度已经是dp[i] + 1，说明找到了新的长度，这是counts应该相加起来
                    elif dp[i] + 1 == dp[j]:
                        counts[j] += counts[i]

        longest = max(dp)
        return sum(c for i, c in enumerate(counts) if dp[i] == longest)


# @lc code=end
