# 请判断一个链表是否为回文链表。
#
# 示例 1: 
#
# 输入: 1->2
# 输出: false
#
# 示例 2: 
#
# 输入: 1->2->2->1
# 输出: true
# 
#
# 进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
# Related Topics 链表 双指针

# 1、先把链表断开成等长的两个链表。
# 2、反转第二个链表。
# 3、两个链表对比。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        def reverse_linklist(p):
            res = None
            while p:
                curr = p
                p = p.next
                curr.next = res
                res = curr
            return res

        if not head:
            return True

        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None

        new_head2 = reverse_linklist(head2)

        while new_head2 and new_head2.val == head1.val:
            new_head2, head1 = new_head2.next, head1.next
        return not new_head2

# leetcode submit region end(Prohibit modification and deletion)
