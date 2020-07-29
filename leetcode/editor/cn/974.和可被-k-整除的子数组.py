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
class Solution:
    # 参考560题的思路，整除转化为同余定理处理
    # 如果A数组，[i,j]的和能被K整除，则位置i的前缀和，位置j的前缀和均能被K整除，这就是同余定理
    # 这样转化可以减少很多重复计算，直接枚举会超时
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # 余数为0的情况，说明当前的前缀和可以被整除，要提前放个1，比如 A=[K]
        hash = {0: 1}
        pre_sum = 0
        res = 0
        for i in range(len(A)):
            pre_sum += A[i]
            m = pre_sum % K
            # 取值 + 更新
            res += hash.get(m, 0)
            hash[m] = hash.get(m, 0) + 1
        return res


# @lc code=end
