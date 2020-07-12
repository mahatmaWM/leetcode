#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 有序数组的平方
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.21%)
# Likes:    102
# Dislikes: 0
# Total Accepted:    39.5K
# Total Submissions: 55.5K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
#
#
#
# 示例 1：
#
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
#
#
# 示例 2：
#
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。
#
#
#

# @lc code=start
class Solution:
    # 双指针left&right一头一尾
    # 比较谁的平方更小，谁就先进入结果
    def sortedSquares(self, A: List[int]) -> List[int]:
        left, right = 0, len(A) - 1
        res = []
        while left <= right:
            S1 = A[left] * A[left]
            S2 = A[right] * A[right]
            if S1 <= S2:
                res.insert(0, S2)
                right -= 1
            elif S1 > S2:
                res.insert(0, S1)
                left += 1
        return res

# @lc code=end

