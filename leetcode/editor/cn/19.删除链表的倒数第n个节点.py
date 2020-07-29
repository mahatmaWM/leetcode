#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (38.78%)
# Likes:    853
# Dislikes: 0
# Total Accepted:    181.9K
# Total Submissions: 469.1K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
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
# 给定的 n 保证是有效的。
#
# 进阶：
#
# 你能尝试使用一趟扫描实现吗？
#
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 思路：间隔长度为n的前后指针遍历链表即可。
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode('#')
        dummy.next = head

        p_right = p_left = dummy
        for _ in range(n):
            p_right = p_right.next
        while p_right.next:
            p_right = p_right.next
            p_left = p_left.next
        p_left.next = p_left.next.next
        return dummy.next
# @lc code=end

