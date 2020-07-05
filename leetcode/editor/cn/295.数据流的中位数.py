#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (46.30%)
# Likes:    209
# Dislikes: 0
# Total Accepted:    17.9K
# Total Submissions: 38.4K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n' +
  '[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
#
# 例如，
#
# [2,3,4] 的中位数是 3
#
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
#
# 设计一个支持以下两种操作的数据结构：
#
#
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
#
#
# 示例：
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
#
# 进阶:
#
#
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
#
#
#

# @lc code=start
class MedianFinder:
    # 思路：本题的难点是在动态增加数字的过程中，需求是要快速的找到中位数。
    # 使用两个堆，一个是小顶堆（保存后一半大小的数字，大的那部分），
    # 一个大顶堆（保存前一半大小的数字，小的那部分，多出的一个处理奇数的情况）。
    # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，才能模拟出大顶堆的效果
    #
    # 先将新元素压入大顶堆，大顶堆顶弹出的元素在压入小顶堆；
    # 注意如果此时count为奇数，则将落单的元素放入大顶堆
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count = 0
        self.max_heap = []
        self.min_heap = []


    def addNum(self, num: int) -> None:
        self.count += 1
        import heapq
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))


    def findMedian(self) -> float:
        if self.count & 1: return self.max_heap[0][1]
        return (self.min_heap[0] + self.max_heap[0][1]) / 2



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

