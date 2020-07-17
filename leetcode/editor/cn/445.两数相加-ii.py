#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (57.35%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    41.4K
# Total Submissions: 72.1K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
#
#
# 进阶：
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
#
#
# 示例：
#
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 本题的主要难点在于链表中数位的顺序与我们做加法的顺序是相反的，为了逆序处理所有数位，我们可以使用栈：把所有数字压入栈中，再依次取出相加。
    # 计算过程中需要注意进位的情况。
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 遍历两个链表，入栈
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        # 出栈，计算并注意进位符号
        ans = None
        carry = 0
        while stack1 or stack2 or carry != 0:
            a = 0 if not stack1 else stack1.pop()
            b = 0 if not stack2 else stack2.pop()
            cur = a + b + carry
            carry = cur // 10
            cur %= 10
            curnode = ListNode(cur)
            curnode.next = ans
            ans = curnode
        return ans

# @lc code=end

