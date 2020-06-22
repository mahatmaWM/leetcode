# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1: 
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
#
# 示例 2: 
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# Related Topics 排序 链表

# 思路：
# 用归并排序的思想，将链表用快慢指针分成两半，然后两半排好序，最后归并。
# 注意快慢指针把链表拆成等长两段的做法，设置一个dummy节点。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 空 或者 只有一个节点
        if head is None or head.next is None:
            return head

        # 等分为两段 a a 或者 a a+1 两段
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None

        # 字段链表排序
        tmp1, tmp2 = self.sortList(head1), self.sortList(head2)

        # 有序链表排序
        ans = ListNode(0)
        p = ans
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                p.next, tmp1 = tmp1, tmp1.next
            else:
                p.next, tmp2 = tmp2, tmp2.next
            p = p.next
        if tmp1:
            p.next = tmp1
        if tmp2:
            p.next = tmp2
        return ans.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    l1 = ListNode(-1)
    l2 = ListNode(5)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(0)
    head = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = None

    head = Solution().sortList(head)
    while head:
        print(head.val)
        head = head.next
