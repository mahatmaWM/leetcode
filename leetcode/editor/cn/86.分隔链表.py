#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#
# https://leetcode-cn.com/problems/partition-list/description/
#
# algorithms
# Medium (58.13%)
# Likes:    214
# Dislikes: 0
# Total Accepted:    39.3K
# Total Submissions: 67.6K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next: return head

        dummy_small = ListNode('#')
        p_small = dummy_small
        dummy_big = ListNode('#')
        p_big = dummy_big
        
        while head:
            if head.val < x:
                p_small.next = head
                p_small = p_small.next
            else:
                p_big.next = head
                p_big = p_big.next
            head = head.next

        p_small.next = dummy_big.next
        p_big.next = None
        return dummy_small.next
# @lc code=end

