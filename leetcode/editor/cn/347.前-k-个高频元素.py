#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#
# https://leetcode-cn.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (60.64%)
# Likes:    363
# Dislikes: 0
# Total Accepted:    59.1K
# Total Submissions: 97.4K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
#
#
#
# 示例 1:
#
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
#
#
# 示例 2:
#
# 输入: nums = [1], k = 1
# 输出: [1]
#
#
#
# 提示：
#
#
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
#
#
#


# @lc code=start
class Solution1:
    # 注意本题评率相同的元素要么全部包含在结果中，要么都不在。
    # 不会出现部分在部分不在的情况，否则本题解法是不成立的，692题就有breaking tail的情况
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in collections.Counter(nums).most_common(k)]


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


# @lc code=end
