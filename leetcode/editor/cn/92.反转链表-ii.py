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
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 1、找到开始反转的节点m，记录m节点以及前面节点
    # 2、反转m到n之间的节点
    # 3、重新连接链表
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy, fanzhuan_len = ListNode(0), n - m
        dummy.next = head

        pre, curr = dummy, dummy.next
        # 找到开始反转的结点m（pre是开始反转的结点）
        while m > 1:
            pre, curr = curr, curr.next
            m -= 1
        last_unswapped, first_swapped = pre, curr

        # 开始反转m到n之间的节点（pre是反转后的头结点，curr是剩余部分的头结点）
        while curr and fanzhuan_len >= 0:
            curr.next, pre, curr = pre, curr, curr.next
            fanzhuan_len -= 1
        # 重新连接结点
        last_unswapped.next, first_swapped.next = pre, curr
        return dummy.next


class Solution1:

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 反转链表前n个位置（返回反转链表的头指针，）
        def reverseN(head, n):
            if n == 1:
                houji = head.next  # 拿到后继节点
                return head, houji
            last, houji = reverseN(head.next, n - 1)
            # 下面两行画图才好理解
            head.next.next = head
            head.next = houji
            return last, houji

        if m == 1:
            res, _ = reverseN(head, n)
            return res
        # 如果不是第一个，那么以下一个为头结点开始递归，直到触发条件
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head


# @lc code=end
