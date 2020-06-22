# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
#
# 示例 1: 
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3. 
#
# 示例 2: 
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3. 
# Related Topics 链表

# 1、如果链表为空，或者有1个节点，2个节点的时候，直接返回。
# 2、把链表等分为前后两段head1、head2，快慢指针。
# 3、反转head2。
# 4、合并两个链表。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None or head.next.next is None:
            return head

        # break linked list into two equal length
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        # reverse linked list head2
        dummy = ListNode(0)
        dummy.next = head2
        p = head2.next
        head2.next = None
        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        head2 = dummy.next

        # merge two linked list head1 and head2
        p1 = head1
        p2 = head2
        while p2:
            tmp1 = p1.next
            tmp2 = p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2

# leetcode submit region end(Prohibit modification and deletion)
