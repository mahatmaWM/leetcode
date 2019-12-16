# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例: 
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# Related Topics 堆 链表 分治算法

# 本题可以使用最小堆结构进行代码实现。
# 首先将每个list里面的第一个元素，也就是每个list的最小元素（因为list都是已排序），共K个指放入大小为K的堆中，将其维护成最小堆结构。
# 堆里面每个元素为（val, node）
# 每次将堆顶的元素，也就是最小元素放到结果中，然后取出该元素原先所处的list中的下一个元素放入队中，维护最小堆结构。
# 当所有元素读取完，所有的元素就按照从小到大放到结果链表中。

# heapq使用说明
# a为普通列表
# - heapq.heapify(a) 调整a，使得其满足最小堆
# - heapq.heappop(a) 从最小堆中弹出最小的元素
# - heapq.heappush(a,b) 向最小堆中压入新的元素

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for ln in lists:
            if ln:
                heap.append((ln.val, ln))

        dummy = curr = ListNode(0)
        heapq.heapify(heap)
        while heap:
            _, ln_index = heapq.heappop(heap)
            curr.next = ln_index
            curr = curr.next
            if ln_index.next:
                heapq.heappush(heap, (ln_index.next.val, ln_index.next))
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
