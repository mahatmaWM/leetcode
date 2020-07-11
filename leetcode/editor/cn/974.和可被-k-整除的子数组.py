#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (45.66%)
# Likes:    173
# Dislikes: 0
# Total Accepted:    22.3K
# Total Submissions: 48.8K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
#
#
#
# 示例：
#
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
#
#
#

# @lc code=start
from itertools import combinations


class Solution:

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A or not K: return 0
        l, result = len(A), 0
        for i in range(l):
            if A[i] % K == 0: result += 1
        # print('res={}'.format(result))
        curr_sum = [0] * (l+1)
        for i in range(1, l+1):
            curr_sum[i] = curr_sum[i - 1] + A[i-1]
        for it1, it2 in list(combinations(curr_sum, 2)):
            if (it2 - it1) % K == 0:
                # print('it2={},it1={}'.format(it2,it1))
                result += 1
        return result


# @lc code=end
