#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (44.52%)
# Likes:    757
# Dislikes: 0
# Total Accepted:    105.7K
# Total Submissions: 237.5K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例:
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明:
#
#
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
#
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
#
#


# @lc code=start
class Solution:
    # 动态规划，dp[i] 表示 i 位置的最大上升子序列长度
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        len_nums = len(nums)
        dp = [1] * len_nums

        for i in range(1, len_nums):
            for j in range(i):
                if nums[j] < nums[i]: dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)


class Solution1:
    # 思路二：有点像贪心 + 二分查找，总体约O(NlogN)。
    #
    # 假设有一个临时数组tmp（用于存放当前找到的最长上升子列），首先将nums[0]插入其中
    # 然后遍历数组nums[1:]
    # 如果val > tmp[-1]，新元素 比 当前最长上升子序列中的最后一个元素大，那么必然构成解，直接加入tmp末尾。
    # 如果val <= tmp[-1]，那么在tmp中找到第一个 >=val 的元素，然后用val替换掉它。
    # 由于tmp是有序的，这一步可以用二分搜索。
    # 最后tmp中存放的就是最长上升子序列。
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        mem = list()
        n = len(nums)
        for i in range(n):
            index = bisect.bisect_left(mem, nums[i])
            if len(mem) == index:
                mem.append(nums[i])
            else:
                mem[index] = nums[i]
        return len(mem)


# @lc code=end
