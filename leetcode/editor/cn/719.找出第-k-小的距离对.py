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
class Solution1:
    # 时间复杂度：O((k+N)logN)，k最大可以达到 O(N^2)，因此最坏情况下，时间复杂度为O(N^2logN)，超出了时间限制
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        heap = [(nums[i + 1] - nums[i], i, i + 1) for i in range(len(nums) - 1)]
        heapq.heapify(heap)

        for _ in range(k):
            d, i, j = heapq.heappop(heap)
            if j + 1 < len(nums): heapq.heappush(heap, (nums[j + 1] - nums[i], i, j + 1))
        return d


class Solution:
    # 二分法，类似378题，目标距离一定存在[lo, hi]之间，应该可以二分逼近查找
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0] + 1
        while lo < hi:
            mi = (lo + hi) // 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1
        return lo


# @lc code=end
