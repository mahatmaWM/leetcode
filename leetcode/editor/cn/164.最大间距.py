#
# @lc app=leetcode.cn id=164 lang=python3
#
# [164] 最大间距
#
# https://leetcode-cn.com/problems/maximum-gap/description/
#
# algorithms
# Hard (55.14%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    15.8K
# Total Submissions: 28.7K
# Testcase Example:  '[3,6,9,1]'
#
# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。
#
# 示例 1:
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
# 示例 2:
#
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
#
# 说明:
#
#
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
#
#
#


# @lc code=start
class Solution:
    # 首先肯定要先排序，然后遍历。但正常排序不满足线性时间复杂度的要求，所以需要用到O(N)的排序。
    # 由于元素都是非负整数，所以采用桶排序的方法。
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums): return 0
        min_num, max_num, n = min(nums), max(nums), len(nums)
        gap = (max_num - min_num) // (n - 1) or 1
        # 需要桶的个数
        cnt = (max_num - min_num) // gap + 1

        # 桶内的下界 上界
        buckets = [[None, None] for _ in range(cnt)]
        for i in nums:
            bucket = buckets[(i - min_num) // gap]
            bucket[0] = i if not bucket[0] else min(bucket[0], i)
            bucket[1] = i if not bucket[1] else max(bucket[1], i)

        # 因为最后要检查 每个桶的下界 与 上一个桶的上届，所以这里要确保桶下界一定有值
        buckets = [b for b in buckets if b[0]]
        return max(buckets[i][0] - buckets[i - 1][1] for i in range(1, len(buckets)))


# @lc code=end
