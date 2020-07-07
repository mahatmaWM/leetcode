#
# @lc app=leetcode.cn id=432 lang=python3
#
# [432] 全 O(1) 的数据结构
#
# https://leetcode-cn.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (34.87%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    3.6K
# Total Submissions: 10.2K
# Testcase Example:  '["AllOne","getMaxKey","getMinKey"]\n[[],[],[]]'
#
# 请你实现一个数据结构支持以下操作：
#
#
# Inc(key) - 插入一个新的值为 1 的 key。或者使一个存在的 key 增加一，保证 key 不为空字符串。
# Dec(key) - 如果这个 key 的值是 1，那么把他从数据结构中移除掉。否则使一个存在的 key 值减一。如果这个 key
# 不存在，这个函数不做任何事情。key 保证不为空字符串。
# GetMaxKey() - 返回 key 中值最大的任意一个。如果没有元素存在，返回一个空字符串"" 。
# GetMinKey() - 返回 key 中值最小的任意一个。如果没有元素存在，返回一个空字符串""。
#
#
#
#
# 挑战：
#
# 你能够以 O(1) 的时间复杂度实现所有操作吗？
#
#


# @lc code=start
# 定义双向节点
class Node:

    def __init__(self, cnt):
        self.cnt = cnt
        # 记录该cnt(计数)下key包括哪些?
        self.keySet = set()
        # 前后指针
        self.prev = None
        self.next = None


class AllOne:
    # 需要O(1)肯定会用到hash，inc和dec容易做到，但getmax和getmin也要常数时间，一定需要在inc和dec的时候做一些工作，
    # 比较常见的思路是使用双向链表，头尾按照顺序存储，方便快速找到max和min。

    # 双向节点的值表示key的计数值，我们同一个计数的key 都挂在同一个节点上，链表升序排。
    # 有head, tail求最大值最小值都在 O(1)时间复杂度了。
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 记录头尾 便于求最小值最大值
        self.head = Node(float("-inf"))
        self.tail = Node(float("inf"))
        # 首尾相连
        self.head.next = self.tail
        self.tail.prev = self.head

        # 保存个数对应的节点
        self.cntKey = {}
        # 某个key对应的个数
        self.keyCnt = {}

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.keyCnt:
            self.__changeKey(key, 1)
        else:
            self.keyCnt[key] = 1
            # 说明没有计数为1的节点,在self.head后面加入
            if self.head.next.cnt != 1:
                self.__addNodeAfter(Node(1), self.head)
            self.head.next.keySet.add(key)
            self.cntKey[1] = self.head.next

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key in self.keyCnt:
            cnt = self.keyCnt[key]
            if cnt == 1:
                self.__keyCnt.pop(key)
                self.__removeFromNode(self.cntKey[cnt], key)
            else:
                self.__changeKey(key, -1)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return "" if self.tail.prev == self.head else next(iter(self.tail.prev.keySet))

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return "" if self.head.next == self.tail else next(iter(self.head.next.keySet))

    # key增加offset，同时要改变链表
    def __changeKey(self, key, offset):
        cnt = self.keyCnt[key]
        self.keyCnt[key] = cnt + offset

        curNode = self.cntKey[cnt]
        newNode = None
        if cnt + offset in self.cntKey:
            newNode = self.cntKey[cnt + offset]
        else:
            newNode = Node(cnt + offset)
            self.cntKey[cnt + offset] = newNode
            self.addNodeAfter(newNode, curNode if offset == 1 else curNode.prev)
        newNode.keySet.add(key)
        self.removeFromNode(curNode, key)

    # 在prevNode后面加入newNode
    def __addNodeAfter(self, newNode, prevNode):
        newNode.prev = prevNode
        newNode.next = prevNode.next
        prevNode.next.prev = newNode
        prevNode.next = newNode

    # 在curNode删除key
    def __removeFromNode(self, curNode, key):
        curNode.keySet.remove(key)
        if len(curNode.keySet) == 0:
            self.removeNodeFromList(curNode)
            self.cntKey.pop(curNode.cnt)

    # 删掉curNode节点
    def __removeNodeFromList(self, curNode):
        curNode.prev.next = curNode.next
        curNode.next.prev = curNode.prev
        curNode.next = None
        curNode.prev = None


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end
