#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (51.90%)
# Likes:    717
# Dislikes: 0
# Total Accepted:    130.9K
# Total Submissions: 252.3K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
#
#

# heapq使用说明
# a为普通列表
# - heapq.heapify(a) 调整a，使得其满足最小堆
# - heapq.heappop(a) 从最小堆中弹出最小的元素
# - heapq.heappush(a,b) 向最小堆中压入新的元素

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 思路：本题可以使用最小堆结构进行代码实现。
    # 首先将每个list里面的第一个元素，也就是每个list的最小元素（因为list都是已排序），共K个指放入大小为K的堆中，将其维护成最小堆结构。
    # 堆里面每个元素为（val, node）
    # 每次将堆顶的元素，也就是最小元素放到结果中，然后取出该元素原先所处的list中的下一个元素放入队中，维护最小堆结构。
    # 当所有元素读取完，所有的元素就按照从小到大放到结果链表中。
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for node in lists:
            if node: heap.append((node.val, node))

        dummy = curr = ListNode(0)
        heapq.heapify(heap)
        while heap:
            _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next: heapq.heappush(heap, (node.next.val, node.next))
        return dummy.next


# @lc code=end

