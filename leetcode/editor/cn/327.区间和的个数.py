#
# @lc app=leetcode.cn id=327 lang=python3
#
# [327] 区间和的个数
#
# https://leetcode-cn.com/problems/count-of-range-sum/description/
#
# algorithms
# Hard (34.53%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 11.6K
# Testcase Example:  '[-2,5,-1]\n-2\n2'
#
# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
# 说明:
# 最直观的算法复杂度是 O(n^2) ，请在此基础上优化你的算法。
#
# 示例:
#
# 输入: nums = [-2,5,-1], lower = -2, upper = 2,
# 输出: 3
# 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
#
#
#


# @lc code=start
class Solution:
    # 首先设计到任务区间和的问题，最好都转化为数组前缀和的表达。
    # 如果有了前缀和表达pre_sum[i]，那么对于 lower <= pre_sum[right] - pre_sum[left] <= upper
    # 通过上面的不等式 pre_sum[left] + lower <= pre_sum[right] <= pre_sum[left] + upper
    #
    # 如果我们逆序访问前缀和数组，当访问pre_sum[left]的时候，对于已经访问过的前缀和中pre_sum[right]，在[pre_sum[left] + lower , pre_sum[left] + upper]区间范围内的，都是满足条件的。
    # 我们可以将已经访问过的前缀和pre_sum[right]都排序存好，就能使用二分查找从而找到满足范围的前缀和的数量，也就是以当前节点作为区间右端点满足区间和在[lower,upper]中的区间数量
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums or upper < lower: return 0

        # 计算前缀和
        pre_sum = [0]
        for a in nums:
            pre_sum.append(pre_sum[-1] + a)

        walked = []
        ans = 0
        # 逆序遍历前缀和数组
        for a in pre_sum[::-1]:
            # 更新当前的上下限
            l, r = a + lower, a + upper
            i, j = bisect.bisect_left(walked, l), bisect.bisect_right(walked, r)
            ans += j - i
            bisect.insort(walked, a)
        return ans


# @lc code=end
