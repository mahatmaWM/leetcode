# 反转一个单链表。
#
# 示例: 
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
#
# 进阶: 
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# Related Topics 链表


# 迭代的方法，直接遍历链表反转。
#
# 递归的方法：
# class Solution:
#     def reverseList(self, head):
#         return reverse(head)
#
#     def reverse(self, node, prev=None):
#         if not node:
#             return prev
#         n = node.next
#         node.next = prev
#         return reverse(n, node)

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = head.next
        head.next = None

        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
