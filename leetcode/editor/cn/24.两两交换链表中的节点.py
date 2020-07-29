#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (65.82%)
# Likes:    517
# Dislikes: 0
# Total Accepted:    112.5K
# Total Submissions: 170.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
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
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode('#')
        dummy.next = head
        pre, curr = dummy, head
        # 对 1->2->3->4 而言
        while curr and curr.next:           # curr=1, curr.next=2
            # 完成 1 2 的交换
            pre.next = curr.next            # 0 --> 2
            curr.next = pre.next.next       # 1 --> 3
            pre.next.next = curr            # 2 --> 1
            pre, curr = curr, curr.next     # pre = 1, curr= 3
        return dummy.next
# @lc code=end

