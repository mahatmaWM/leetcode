#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (40.37%)
# Likes:    271
# Dislikes: 0
# Total Accepted:    65.9K
# Total Submissions: 163.3K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
#
#
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 思路：
    # 1、链表为空或者只有一个节点时，直接返回。
    # 2、找到列表长度。
    # 3、找到应该断开的节点。
    # 4、重新连接链表。
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head

        list_length = 1
        node = head
        while node.next:
            node = node.next
            list_length += 1

        # 记录尾巴节点
        tail = node

        # 找到应该断开的节点
        k = list_length - k % list_length
        if k == list_length: return head
        node = head
        list_length = 1
        while list_length < k:
            node = node.next
            list_length += 1

        # 重新连接链表
        new_head = node.next
        tail.next = head
        node.next = None
        return new_head


# @lc code=end
