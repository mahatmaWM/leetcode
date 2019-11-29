# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1: 
#
# 输入: 1->1->2
# 输出: 1->2
# 
#
# 示例 2: 
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
# Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
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

# leetcode submit region end(Prohibit modification and deletion)
