#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#
# https://leetcode-cn.com/problems/reorder-list/description/
#
# algorithms
# Medium (55.97%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    26.9K
# Total Submissions: 48.1K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
#
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 1、如果链表为空，或者有1个节点，2个节点的时候，直接返回。
    # 2、把链表等分为前后两段head1、head2，快慢指针。
    # 3、反转head2。
    # 4、合并两个链表。
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return head

        # 利用快慢指针将链表分为两段，长度分别为 a a 或者 a a+1
        def splitList(head):
            dummy = ListNode(0)
            dummy.next = head
            slow, fast = dummy, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            head1, head2 = head, slow.next
            slow.next = None
            return head1, head2

        def reverse(node):
            if not node.next: return node
            new_head = reverse(node.next)
            # 把node放到已反转的子链表的尾部
            node.next.next = node
            node.next = None
            return new_head

        # 合并两个链表
        def mergeTwoList(l1, l2):
            dummy = cur = ListNode(-1)
            while l1 and l2:
                cur.next = l1
                l1 = l1.next
                cur = cur.next
                cur.next = l2
                l2 = l2.next
                cur = cur.next
            if l1: cur.next = l1
            if l2: cur.next = l2
            return dummy.next

        head1, head2 = splitList(head)
        head2 = reverse(head2)
        mergeTwoList(head1, head2)


# @lc code=end
