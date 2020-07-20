#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#
# https://leetcode-cn.com/problems/middle-of-the-linked-list/description/
#
# algorithms
# Easy (69.00%)
# Likes:    236
# Dislikes: 0
# Total Accepted:    67.6K
# Total Submissions: 97.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 给定一个带有头结点 head 的非空单链表，返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。
#
#
#
# 示例 1：
#
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next =
# NULL.
#
#
# 示例 2：
#
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
#
#
#
#
# 提示：
#
#
# 给定链表的结点数介于 1 和 100 之间。
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
    # 快慢指针（慢指针每次走一步，快指针每次走两步）
    def middleNode(self, head: ListNode) -> ListNode:
        slow_ptr, fast_ptr = head, head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr

# @lc code=end
