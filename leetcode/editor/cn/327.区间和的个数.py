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

# 思路：
# 首先设计到任务区间和的问题，最好都转化为数组前缀和的表达。
# 如果有了前缀和表达pre_sum[i]，那么对于 lower <= pre_sum[right] - pre_sum[left] <= upper
# 通过上面的不等式 pre_sum[right] - upper <= pre_sum[left] <= pre_sum[right] - lower
# 如果我们逆序访问前缀和数组，当访问pre_sum[left]的时候，在j之前的前缀和中，如果在[pre_sum[right] - upper, pre_sum[right] - lower]区间范围内的，都是满足条件的。
#
# 这时候如果已遍历的前缀和都已经排好序，就能使用二分查找从而找到满足范围的前缀和的数量，也就是以当前节点作为区间右端点满足区间和在[lower,upper]中的区间数量

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

        pre_sum = [0]
        for a in nums:
            pre_sum.append(pre_sum[-1] + a)

        walked = []
        ans = 0
        for a in pre_sum[::-1]:
            # 当前和的上下限
            l, r = a + lower, a + upper

            i, j = bisect_left(walked, l), bisect_right(walked, r)
            ans += j - i
            insort(walked, a)
            # print walked
        return ans


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().countRangeSum(nums=[-2, 5, -1], lower=-2, upper=2))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
