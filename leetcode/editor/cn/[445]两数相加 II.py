# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
#
# 
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。 
#
# 进阶: 
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。 
#
# 示例: 
#
# 
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7
# 
# Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

# leetcode submit region end(Prohibit modification and deletion)
