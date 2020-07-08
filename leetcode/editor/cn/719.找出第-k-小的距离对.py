#
# @lc app=leetcode.cn id=719 lang=python3
#
# [719] 找出第 k 小的距离对
#
# https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance/description/
#
# algorithms
# Hard (32.99%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    4.3K
# Total Submissions: 12.8K
# Testcase Example:  '[1,3,1]\n1'
#
# 给定一个整数数组，返回所有数对之间的第 k 个最小距离。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。
#
# 示例 1:
#
#
# 输入：
# nums = [1,3,1]
# k = 1
# 输出：0
# 解释：
# 所有数对如下：
# (1,3) -> 2
# (1,1) -> 0
# (3,1) -> 2
# 因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。
#
#
# 提示:
#
#
# 2 <= len(nums) <= 10000.
# 0 <= nums[i] < 1000000.
# 1 <= k <= len(nums) * (len(nums) - 1) / 2.
#
#
#


# @lc code=start
class Solution:

    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in range(k):
            d, i, j = heapq.heappop(heap)
            if j + 1 < len(nums): heapq.heappush(heap, (nums[j + 1] - nums[i], i, j + 1))
        return d


# @lc code=end
