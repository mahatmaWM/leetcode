# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
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
# 说明： 
#
# 
# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。 
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。 
# 
# Related Topics 堆 哈希表


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        return [item[0] for item in collections.Counter(nums).most_common(k)]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().topKFrequent(nums=[1], k=1))
