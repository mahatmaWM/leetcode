# 给定一个整数数组 nums，返回区间和在 [lower, upper] 之间的个数，包含 lower 和 upper。
# 区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
# 说明: 
# 最直观的算法复杂度是 O(n2) ，请在此基础上优化你的算法。
#
# 示例: 
#
# 输入: nums = [-2,5,-1], lower = -2, upper = 2,
# 输出: 3
# 解释: 3个区间分别是: [0,0], [2,2], [0,2]，它们表示的和分别为: -2, -1, 2。
# 
# Related Topics 排序 树状数组 线段树 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        from bisect import bisect_left, bisect_right, insort
        if not nums or upper < lower:
            return 0

        p = [0]
        for a in nums:
            p.append(p[-1] + a)

        walked = []
        ans = 0
        for a in p[::-1]:
            l, r = a + lower, a + upper
            i, j = bisect_left(walked, l), bisect_right(walked, r)
            ans += j - i
            insort(walked, a)
            # print walked
        return ans

# leetcode submit region end(Prohibit modification and deletion)
