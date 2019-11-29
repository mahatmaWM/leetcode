# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明: 
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例: 
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
# Related Topics 链表

# 1、找到开始反转的节点m，记录m节点以及前面节点
# 2、反转m到n之间的节点
# 3、重新连接链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy, partial_len = ListNode(0), n - m
        dummy.next = head
        prev, curr = dummy, dummy.next
        # 取出mn之间的结点，并反转
        while m > 1:  # pre是开始反转的结点
            prev, curr = curr, curr.next
            m -= 1
        last_unswapped, first_swapped = prev, curr

        while curr and partial_len >= 0:  # pre是结束反转的结点
            curr.next, prev, curr = prev, curr, curr.next
            partial_len -= 1
        # 重新连接结点
        last_unswapped.next, first_swapped.next = prev, curr
        return dummy.next


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
    S.reverseBetween(head, 2, 4)
