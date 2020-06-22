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


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList1(self, head):
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

    # 递归反转
    def reverseList(self, head):
        def reverse(node):
            if not node.next:
                return node
            new_head = reverse(node.next)
            # 把node放到已反转的子链表的尾部
            tmp_node = node.next
            tmp_node.next = node
            node.next = None
            return new_head

        return reverse(head)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    S = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None
    head = S.reverseList(head)
    while head:
        print(head.val)
        head = head.next
