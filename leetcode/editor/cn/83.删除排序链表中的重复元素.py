#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (50.49%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    107.5K
# Total Submissions: 212.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
#
#
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        cur_ptr = head
        next_ptr = head.next
        while cur_ptr and next_ptr:
            if cur_ptr.val == next_ptr.val:
                next_ptr = next_ptr.next
                cur_ptr.next = next_ptr
            else:
                cur_ptr = next_ptr
                next_ptr = next_ptr.next
        return head
# @lc code=end

