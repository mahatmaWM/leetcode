#
# @lc app=leetcode.cn id=907 lang=python3
#
# [907] 子数组的最小值之和
#
# https://leetcode-cn.com/problems/sum-of-subarray-minimums/description/
#
# algorithms
# Medium (29.54%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 16.4K
# Testcase Example:  '[3,1,2,4]'
#
# 给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
#
# 由于答案可能很大，因此返回答案模 10^9 + 7。
#
#
#
# 示例：
#
# 输入：[3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
#
#
#
# 提示：
#
#
# 1 <= A <= 30000
# 1 <= A[i] <= 30000
#
#
#
#
#


# @lc code=start
class Solution:
    # 思路：观察规律，针对 [3,1,2,4]，比如包含元素1的子数组，其最小值一定是1，一共有2*3个子数组，1前面1个元素，1后面2个元素，(1+1)*(2+1)。
    # 问题转化为，对于当前元素i，如果求左边第一个小于当前元素的位置left 和 右边第一个小于当前元素的位置right，那么[left+1 right-1]这个区间的最小值就是i
    # 这两个位置就是我们能找到的区间长度最大值，这就需要维护一个严格单调递增的栈。
    #
    # 最大左边长度和最大右边长度？可以通过单调栈
    #
    # 注意一头一尾添加一个为0的元素
    # 这个问题还有一个陷阱就是当包含重复元素的时候我们怎么计算？例如[71,55,82,55]，此时有两种策略
    # nextList包含重复元素，preList不包含
    # nextList不包含重复元素，preList包含
    # 使用的是第二种策略

    # 这里使用递增栈（栈低到栈顶依次递增）
    def sumSubarrayMins(self, A: List[int]) -> int:
        if not A: return 0
        A = [0] + A + [0]

        stack = list()
        next_smaller = [-1] * len(A)
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                pre_index = stack.pop()
                next_smaller[pre_index] = i - pre_index
            stack.append(i)

        stack.clear()
        pre_smaller = [-1] * len(A)
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                stack.pop()
            if stack: pre_smaller[i] = i - stack[-1]
            stack.append(i)

        return sum(i * j * k for i, j, k in zip(A, next_smaller, pre_smaller)) % (10**9 + 7)


# @lc code=end
