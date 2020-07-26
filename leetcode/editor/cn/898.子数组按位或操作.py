#
# @lc app=leetcode.cn id=898 lang=python3
#
# [898] 子数组按位或操作
#
# https://leetcode-cn.com/problems/bitwise-ors-of-subarrays/description/
#
# algorithms
# Medium (28.52%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    2.8K
# Total Submissions: 9.8K
# Testcase Example:  '[0]'
#
# 我们有一个非负整数数组 A。
#
# 对于每个（连续的）子数组 B = [A[i], A[i+1], ..., A[j]] （ i <= j），我们对 B 中的每个元素进行按位或操作，获得结果
# A[i] | A[i+1] | ... | A[j]。
#
# 返回可能结果的数量。 （多次出现的结果在最终答案中仅计算一次。）
#
#
#
# 示例 1：
#
# 输入：[0]
# 输出：1
# 解释：
# 只有一个可能的结果 0 。
#
#
# 示例 2：
#
# 输入：[1,1,2]
# 输出：3
# 解释：
# 可能的子数组为 [1]，[1]，[2]，[1, 1]，[1, 2]，[1, 1, 2]。
# 产生的结果为 1，1，2，1，3，3 。
# 有三个唯一值，所以答案是 3 。
#
#
# 示例 3：
#
# 输入：[1,2,4]
# 输出：6
# 解释：
# 可能的结果是 1，2，3，4，6，以及 7 。
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 50000
# 0 <= A[i] <= 10^9
#
#
#


# @lc code=start
class Solution1:
    # 直接暴力枚举，两个for循环，然后得到[start, end]段，再全部or一下，复杂度是O(N3)
    # 由于[start, end]的信息可以由[start, end-1]和A[end]得到，这里可以用dp空间换时间降低到O(N2)，但还是会超时
    # 另外，由于转移的时候只和上一个状态有关系，dp的空间还可以压缩为1维
    def subarrayBitwiseORs0(self, A: List[int]) -> int:
        n = len(A)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = A[i]
        ans = set(A)
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                end = start + length - 1
                dp[start][end] = dp[start][end - 1] | A[end]
                ans.add(dp[start][end])
        return len(ans)

    def subarrayBitwiseORs(self, A: List[int]) -> int:
        n = len(A)
        dp = [0] * n
        for i in range(n):
            dp[i] = A[i]
        ans = set(A)
        for length in range(2, n + 1):
            for start in range(n - length + 1):
                dp[start] = dp[start] | A[start + length - 1]
                ans.add(dp[start])
        return len(ans)


class Solution:
    # cur记录了到当前位置i-1的所有bitor的结果（去重后），所以到i位置时，只需要i与之前的所有结果做bitor，同时更新ans
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        cur = set([])
        ans = set([])
        for i in range(len(A)):
            cur = {A[i] | b for b in cur} | {A[i]}
            ans |= cur
        return len(ans)


# @lc code=end
