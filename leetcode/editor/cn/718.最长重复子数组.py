#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] 最长重复子数组
#
# https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (50.17%)
# Likes:    177
# Dislikes: 0
# Total Accepted:    12.8K
# Total Submissions: 25.4K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# 给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。
#
# 示例 1:
#
#
# 输入:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出: 3
# 解释:
# 长度最长的公共子数组是 [3, 2, 1]。
#
#
# 说明:
#
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#
#

# @lc code=start
class Solution:
    # 动态规划，dp[i][j]代表A[0:i] B[0:j]能构成的最长子数组
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        res = 0
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                    res = max(dp[i + 1][j + 1], res)
        return res

# @lc code=end
