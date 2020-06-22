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
# 示例 2： 
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
# Related Topics 排序 链表

# 插入排序，N^2复杂度：
# 将一个记录插入到已排好序的序列中，从而得到一个新的有序序列（将序列的第一个数据看成是一个有序的子序列，然后从第二个记录逐个向该有序的子序列进行有序的插入，直至整个序列有序）。
# 注意使用哨兵，用于临时存储和判断数组边界。

# 在链表中运用插入排序有一定技巧性。

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # dummy节点相当于是哨兵
        dummy = ListNode(0)
        dummy.next = head
        # head指针一直移动到最后一个节点
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                # 否则head.next指向的节点应该被插入到之前有序链表中
                # 先把head.next节点断开，前后链表继续相连
                temp = head.next
                head.next = head.next.next

                # 在前面dummy指向的有序链表中找到应该插入的位置q之后
                q = dummy
                while q.next and q.next.val < temp.val:
                    q = q.next
                temp.next = q.next
                q.next = temp
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
