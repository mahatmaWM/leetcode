#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (69.34%)
# Likes:    1009
# Dislikes: 0
# Total Accepted:    255.9K
# Total Submissions: 369K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
#
#
# def reverseList1(self, head):
#     """
#     :type head: ListNode
#     :rtype: ListNode
#     """
#     dummy = ListNode(0)
#     dummy.next = head
#     p = head.next
#     head.next = None

#     while p:
#         tmp = p
#         p = p.next
#         tmp.next = dummy.next
#         dummy.next = tmp
#     return dummy.next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(node):
            if not node.next: return node
            new_head = reverse(node.next)
            # 把node放到已反转的子链表的尾部
            node.next.next = node
            node.next = None
            return new_head

        return reverse(head)
# @lc code=end
