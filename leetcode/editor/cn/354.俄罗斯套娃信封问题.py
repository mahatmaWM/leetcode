#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
# https://leetcode-cn.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (35.55%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    11.6K
# Total Submissions: 32.7K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h)
# 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。
#
# 说明:
# 不允许旋转信封。
#
# 示例:
#
# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
#


# @lc code=start
class Solution:
    # 思路：本题是最长递增子序列（Longes Increasing Subsequence，简写为 LIS）的一个变种，300题。
    # 比如先按照信封的W进行升序排序，而当W相同的时候，按照H降序排（这里有贪心的思想，显然当W相同时，如果要选一个信封到最终结果中，肯定是选择H最小的那个，如果H降序排，那么对H找到LIS即可）
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            import bisect
            memo = list()
            n = len(nums)
            for i in range(n):
                index = bisect.bisect_left(memo, nums[i])
                if len(memo) == index:
                    memo.append(nums[i])
                else:
                    memo[index] = nums[i]
            return len(memo)

        return lis([i[1] for i in envelopes])


# @lc code=end
