# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1: 
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 
#
# 示例 2: 
#
# 输入: 1->1->1->2->3
# 输出: 2->3
# Related Topics 链表


# 第一次遍历的时候，记录数字出现的次数。
# 第二次遍历的时候，查找下个节点的值出现的次数如果不是1次，那么就删除下个节点。
# 修改这个节点的下个指针指向下下个节点，这是指向该节点位置的指针不要动，因为还要判断新的next值。

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
        root = ListNode(0)
        root.next = head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        import collections
        counter = collections.Counter(val_list)
        head = root
        while head and head.next:
            if counter[head.next.val] != 1:
                head.next = head.next.next
            else:
                head = head.next
        return root.next

# leetcode submit region end(Prohibit modification and deletion)
