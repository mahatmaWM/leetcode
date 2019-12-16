# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 示例 1: 
#
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
#
# 示例 2: 
#
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
#
# 说明: 
#
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。 
# Related Topics 堆 分治算法

# 求第K个最大元素的方法。
# 1.排序算法，复杂度就是对应的排序算法复杂度。比如快速排序也就NlogN.

# 2.python中默认小顶堆，建立K个尺寸的小顶堆，
# 然后遍历数组中后面的所有数，当前数大于堆顶元素，则替换当前堆顶元素，维护堆的特性（logk的复杂度），这样遍历完数组，堆中的元素就是前K个最大元素。
# 最大元素建立最小堆，同理即可。这种方法总的时间复杂度为nlogk，实际应用中时效率将非常高。
# 3.利用快排的思想，每次确定第p个数的位置，这里只需要利用这里的特性，让左边小于第k个数，右边全部大于它，但是这里求取的一堆数据时无序的。时间复杂度0(N)。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        heap = nums[0:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        return heap[0]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
