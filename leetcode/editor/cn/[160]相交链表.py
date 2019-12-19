# 编写一个程序，找到两个单链表相交的起始节点。
#
# 如下面的两个链表： 
#
# 
#
# 在节点 c1 开始相交。 
#
# 
#
# 示例 1： 
#
# 
#
# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# 
#
# 
#
# 示例 2： 
#
# 
#
# 输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
# 
#
# 
#
# 示例 3： 
#
# 
#
# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 解释：这两个链表不相交，因此返回 null。
# 
#
# 
#
# 注意： 
#
# 
# 如果两个链表没有交点，返回 null. 
# 在返回结果后，两个链表仍须保持原有的结构。 
# 可假定整个链表结构中没有循环。 
# 程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。 
# 
# Related Topics 链表

# 1.分别遍历两个链表，如果尾节点不同则不相交，返回None，如果尾节点相同则求相交结点。 
# 2.求相交结点的方法是，求出链表长度的差值，长链表的指针先想后移动lenA-lenB。然后两个链表一起往后走，若结点相同则第一个相交点。 
# 3.求链表的长度，在遍历的时候就计算，并将每个结点放在字典中。 
# 该题中不让修改链表结构。所以只考虑以上思路。还有另一种方法是： 
# 先遍历第一个链表到他的尾部，然后将尾部的next指针指向第二个链表(尾部指针的next本来指向的是null)。这样两个链表就合成了一个链表，判断原来的两个链表是否相交也就转变成了判断新的链表是否有环的问题了：即判断单链表是否有环？



# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # len_a, len_b = 0, 0
        # ptr_a, ptr_b = headA, headB
        # while ptr_a:
        #     ptr_a = ptr_a.next
        #     len_a += 1
        # while ptr_b:
        #     ptr_b = ptr_b.next
        #     len_b += 1
        #
        # if len_a > len_b:
        #     temp = len_a - len_b
        #     ptr_a = headA
        #     ptr_b = headB
        #     while temp > 0:
        #         ptr_a = ptr_a.next
        #     while ptr_a != ptr_b:
        #         ptr_a = ptr_a.next
        #         ptr_b = ptr_b.next
        #     return ptr_a
        # else:
        #     temp = len_b - len_a
        #     ptr_a = headA
        #     ptr_b = headB
        #     while temp > 0:
        #         ptr_b = ptr_b.next
        #     while ptr_a != ptr_b:
        #         ptr_a = ptr_a.next
        #         ptr_b = ptr_b.next
        #     return ptr_a
        if not headA or not headB:
            return None
        pa = headA
        pb = headB
        while pa is not pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next
        return pa

# leetcode submit region end(Prohibit modification and deletion)
