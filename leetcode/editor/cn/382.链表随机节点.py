#
# @lc app=leetcode.cn id=382 lang=python3
#
# [382] 链表随机节点
#
# https://leetcode-cn.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (57.04%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 9.3K
# Testcase Example:  '["Solution","getRandom"]\n[[[1,2,3]],[]]'
#
# 给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。
#
# 进阶:
# 如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？
#
# 示例:
#
#
# // 初始化一个单链表 [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
# solution.getRandom();
#
# 思路叫蓄水池抽样算法，主要用来解决如下问题。
# 给定一个数据流，数据流长度N很大，且N直到处理完所有数据之前都不可知，请问如何在只遍历一遍数据（O(N)）的情况下，能够随机选取出m个不重复的数据。

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res = None
        cur = self.head
        c = 0
        while cur:
            if not random.randint(0, c): res = cur.val
            c += 1
            cur = cur.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end
