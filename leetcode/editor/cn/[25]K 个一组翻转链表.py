# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
#
# k 是一个正整数，它的值小于或等于链表的长度。 
#
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
#
# 示例 : 
#
# 给定这个链表：1->2->3->4->5 
#
# 当 k = 2 时，应当返回: 2->1->4->3->5 
#
# 当 k = 3 时，应当返回: 3->2->1->4->5 
#
# 说明 : 
#
# 
# 你的算法只能使用常数的额外空间。 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。 
# 
# Related Topics 链表

# 思路一：
# 用栈，我们把 k 个数压入栈中，然后弹出来的顺序就是翻转的！
#
# 这里要注意几个问题：
# 第一，剩下的链表个数够不够 k 个（因为不够 k 个不用翻转）；
# 第二，已经翻转的部分要与剩下链表连接起来。


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        while True:
            # 先找一段K长度的
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            # 注意,目前tmp所在k+1位置
            # 说明剩下的链表不够k个,跳出循环
            if count:
                p.next = head
                break
            # 翻转操作
            while stack:
                p.next = stack.pop()
                p = p.next
            # 与剩下链表连接起来
            p.next = tmp
            head = tmp

        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
