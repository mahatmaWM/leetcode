#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (47.93%)
# Likes:    290
# Dislikes: 0
# Total Accepted:    49.2K
# Total Submissions: 102.7K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
#
#
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution1:
    # 第一次遍历的时候，记录数字出现的次数。
    # 第二次遍历的时候，查找下个节点的值出现的次数如果不是1次，那么就删除下个节点。
    # 修改这个节点的下个指针指向下下个节点，这是指向该节点位置的指针不要动，因为还要判断新的next值。
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        cnt = collections.Counter(val_list)

        head = dummy
        while head and head.next:
            if cnt[head.next.val] != 1:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next
class Solution:
    # slow fast指针一次遍历，fast用于处理重复的情况，slow用于拼接链表
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(-1000)
        dummy.next = head

        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    # 递归的方式
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head: return head
        if head.next and head.val == head.next.val:
            while head.next != None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head


# @lc code=end
