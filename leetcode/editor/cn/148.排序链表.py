#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (65.74%)
# Likes:    580
# Dislikes: 0
# Total Accepted:    66.6K
# Total Submissions: 101.4K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
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
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 147题用的插入排序，这里用归并方法
    # 用归并排序的思想，将链表用快慢指针分成两半，然后两半排好序，最后归并。
    # 注意快慢指针把链表拆成等长两段的做法，设置一个dummy节点。
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        # 合并两个有序链表
        def mergeTwoSortList(l1, l2):
            dummy = cur = ListNode(-1)
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1: cur.next = l1
            if l2: cur.next = l2
            return dummy.next

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

        head1, head2 = splitList(head)
        sort1, sort2 = self.sortList(head1), self.sortList(head2)
        return mergeTwoSortList(sort1, sort2)


# @lc code=end
