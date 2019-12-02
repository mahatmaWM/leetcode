# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。 
#
# 示例: 
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
# 
# Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = head
        dummyA = ListNode(0)
        p1 = dummyA
        dummyB = ListNode(0)
        p2 = dummyB
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = dummyB.next
        p2.next = None
        return dummyA.next

# leetcode submit region end(Prohibit modification and deletion)
