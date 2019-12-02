# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
#
# 
#
# 示例: 
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre, curr = dummy, head

        while curr and curr.next:  # curr=1, curr.next=2
            pre.next = curr.next  # 0 --> 2
            curr.next = pre.next.next  # 1 --> 3  # curr.next.next
            pre.next.next = curr  # 2 --> 1
            pre, curr = curr, curr.next  # pre = 1, curr= 3
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
