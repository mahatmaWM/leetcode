#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
# https://leetcode-cn.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (50.27%)
# Likes:    390
# Dislikes: 0
# Total Accepted:    54.3K
# Total Submissions: 108.1K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL
#
#
# 1、找到开始反转的节点m，记录m节点以及前面节点
# 2、反转m到n之间的节点
# 3、重新连接链表
# def reverseBetween(self, head, m, n):
#     dummy, partial_len = ListNode(0), n - m
#     dummy.next = head
#     prev, curr = dummy, dummy.next
#     # 取出mn之间的结点，并反转
#     while m > 1:  # pre是开始反转的结点
#         prev, curr = curr, curr.next
#         m -= 1
#     last_unswapped, first_swapped = prev, curr

#     while curr and partial_len >= 0:  # pre是结束反转的结点
#         curr.next, prev, curr = prev, curr, curr.next
#         partial_len -= 1
#     # 重新连接结点
#     last_unswapped.next, first_swapped.next = prev, curr
#     return dummy.next

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        def reverseN(head, n):
            if n == 1:
                successor = head.next  # 拿到后继节点
                return head, successor
            last, successor = reverseN(head.next, n - 1)
            head.next.next = head
            head.next = successor
            return last, successor

        if m == 1:  # 递归终止条件
            res, _ = reverseN(head, n)
            return res
        # 如果不是第一个，那么以下一个为头结点开始递归，直到触发条件
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head


# @lc code=end
