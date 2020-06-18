#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#
# https://leetcode-cn.com/problems/smallest-range-i/description/
#
# algorithms
# Easy (68.30%)
# Likes:    52
# Dislikes: 0
# Total Accepted:    11.5K
# Total Submissions: 16.9K
# Testcase Example:  '[1]\n0'
#
# 给你一个整数数组 A，对于每个整数 A[i]，我们可以选择处于区间 [-K, K] 中的任意数 x ，将 x 与 A[i] 相加，结果存入 A[i] 。
#
# 在此过程之后，我们得到一些数组 B。
#
# 返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
#
#
#
#
#
#
# 示例 1：
#
# 输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
#
#
# 示例 2：
#
# 输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
#
#
# 示例 3：
#
# 输入：A = [1,3,6], K = 3
# 输出：0
# 解释：B = [3,3,3] 或 B = [4,4,4]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 10000
# 0 <= K <= 10000
#
# 思路，新得到的B数组，B_min的最大值 = A_min + K，B_max的最小值 = A_max - K
# 所以得到的新数组B的差值就小为 (A_max - K) - (A_min + K)，当此值小于0的时候，最终结果为0
#

# @lc code=start
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, (max(A) - K) - (min(A) + K))

# @lc code=end
