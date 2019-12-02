# 给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。
#
# 定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。 
#
# 找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。 
#
# 示例 1: 
#
# 输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# 输出: [1,2],[1,4],[1,6]
# 解释: 返回序列中的前 3 对数：
#     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
#
# 示例 2: 
#
# 输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# 输出: [1,1],[1,1]
# 解释: 返回序列中的前 2 对数：
#      [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
#
# 示例 3: 
#
# 输入: nums1 = [1,2], nums2 = [3], k = 3 
# 输出: [1,3],[2,3]
# 解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]
# 
# Related Topics 堆

# 最小堆。
# 把所有的点对加入到最小堆，然后输出前k个。
# 但没有利用到“两个数组都有序”这个条件，就算数组无序，也可以利用这个方法。
# 要利用有序这个条件，可以借助mergesort的思路，pair的第一个元素至多包含了nums1数组的前k个元素，k以后的可以不用考虑。
# 所以，这形成了k个list，每一个list都包含了nums2的元素。每一次取所有list中的最小值，然后该list下一个元素入队。

# leetcode submit region begin(Prohibit modification and deletion)
from heapq import heappush, heappop


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        pairs = []
        if len(nums1) > len(nums2):
            tmp = self.kSmallestPairs(nums2, nums1, k)
            for pair in tmp:
                pairs.append([pair[1], pair[0]])
            return pairs

        min_heap = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heappush(min_heap, [nums1[i] + nums2[j], i, j])

        push(0, 0)
        while min_heap and len(pairs) < k:
            _, i, j = heappop(min_heap)  # j 由上一次pop出来的数字产生
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)  # j=j+1,   只会越来越大，不会浪费时间
            if j == 0:
                push(i + 1, 0)  # at most queue min(n, m) space
        return pairs

# leetcode submit region end(Prohibit modification and deletion)
