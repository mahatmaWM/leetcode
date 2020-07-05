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
    # 如果正常排序以后再遍历，不能满足线性时间复杂度的要求。

    # 由于元素都是非负整数，所以采用桶排序的方法。
    # 1、求随机数组中的最大元素，最小元素，为线性时间复杂度。
    # 2、在最大元素和最小元素之间，N-1 个间隔，确定每个桶的范围，以及需要桶的个数。
    # 3、每个桶为一个有序实数对 (None,None)，将每个数依次往目标桶里塞，并更新每个桶的上下界。
    # 5、计算每个桶的下界与上一个桶的上界的差值，差值最大值即为最大间隔。
    # （注意：差距最大的两个点一定会被分到不同的桶里面）。
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2 or min(nums) == max(nums): return 0
        min_num, max_num, n = min(nums), max(nums), len(nums)

        # 每个桶的范围大小
        bucket_range = (max_num - min_num) // (n - 1) or 1
        # 需要桶的个数
        cnt = (max_num - min_num) // bucket_range + 1
        # bucket[0] bucket[1] 分别为桶内的下界 上界
        buckets = [[None, None] for _ in range(cnt)]
        for i in nums:
            bucket = buckets[(i - min_num) // bucket_range]
            bucket[0] = i if not bucket[0] else min(bucket[0], i)
            bucket[1] = i if not bucket[1] else max(bucket[1], i)
        # 因为最后要检查 每个桶的下界 与 上一个桶的上届，所以这里要确保桶下界一定有值
        buckets = [b for b in buckets if b[0]]
        return max(buckets[i][0] - buckets[i - 1][1] for i in range(1, len(buckets)))


# @lc code=end
