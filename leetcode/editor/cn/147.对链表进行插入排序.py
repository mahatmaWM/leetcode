#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (64.39%)
# Likes:    181
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 51.3K
# Testcase Example:  '[4,2,1,3]'
#
# 对链表进行插入排序。
#
#
# 插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
# 每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。
#
#
#
# 插入排序算法：
#
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
#
#
#
# 示例 1：
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
#
#
# 示例 2：
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
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
    # 插入排序，时间复杂度O(N^2)
    # 链表操作时注意使用哨兵，用于临时存储和判断数组边界。
    # 在链表中运用插入排序有一定技巧性。
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        # dummy节点相当于是哨兵
        dummy = ListNode(0)
        dummy.next = head

        pre, cur = head, head.next
        while cur:
            if pre.val <= cur.val:
                pre = pre.next
                cur = cur.next
            else:
                # 当前cur节点需要插入到前面有序链表中

                # 1、取出cur节点
                insert_node = cur
                cur = cur.next
                pre.next = cur

                # 2、把cur插入到前面有序链表中
                q = dummy
                while q.next and q.next.val < insert_node.val:
                    q = q.next

                # 3、插入q节点之后
                insert_node.next = q.next
                q.next = insert_node
        return dummy.next


# @lc code=end
