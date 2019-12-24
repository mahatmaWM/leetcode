# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例： 
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 
#
# 说明： 
#
# 给定的 n 保证是有效的。 
#
# 进阶： 
#
# 你能尝试使用一趟扫描实现吗？ 
# Related Topics 链表 双指针

# 思路：
# 间隔长度为n的前后指针遍历链表即可。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p_right = p_left = dummy

        for i in range(n):
            p_right = p_right.next
        while p_right.next:
            p_right = p_right.next
            p_left = p_left.next
        p_left.next = p_left.next.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
