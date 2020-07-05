#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#
# https://leetcode-cn.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (42.11%)
# Likes:    523
# Dislikes: 0
# Total Accepted:    95.5K
# Total Submissions: 226.7K
# Testcase Example:  '[1,2]'
#
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
#
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
#
#
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 1、先把链表断开成等长的两个链表。
    # 2、反转第二个链表。
    # 3、两个链表对比。
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        if not head.next: return True

        # 快慢指针将链表分为两段，长度分别为 a a 或者 a a+1
        # 注意head2会可能更长一个节点
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

        def reverse(node):
            if not node.next: return node
            new_head = reverse(node.next)
            # 把node放到已反转的子链表的尾部
            node.next.next = node
            node.next = None
            return new_head

        head1, head2 = splitList(head)
        head2 = reverse(head2)
        # 判断回文
        while head1 and head2.val == head1.val:
            head2, head1 = head2.next, head1.next
        return not head1


# @lc code=end
