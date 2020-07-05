#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#
# https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (72.51%)
# Likes:    243
# Dislikes: 0
# Total Accepted:    32K
# Total Submissions: 44K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
# 示例:
#
# 给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # 处理链表为空或者只有一个节点的情况
        if not head: return None
        if not head.next: return TreeNode(head.val)

        # 利用快慢指针将链表分为两段，长度分别为 a a 或者 a a+1
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

        head1, head2 = splitList(head)
        node = TreeNode(head2.val)
        node.left = self.sortedListToBST(head1)
        node.right = self.sortedListToBST(head2.next)
        return node
# @lc code=end

