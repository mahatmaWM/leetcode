#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (49.51%)
# Likes:    681
# Dislikes: 0
# Total Accepted:    72.2K
# Total Submissions: 145.9K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' + '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得关键字 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得关键字 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
#
#


# @lc code=start
class DLinkedNode():

    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    # Least recently used，最近最少使用
    # 1、查找需要O1，需要hashmap保存。
    # 2、最近最少使用特性，如果可以在O1时间内找到最新&最旧的，即可。
    # 使用双向链表保存（这里 前面的热度高后面的热度低，这里只会涉及到头尾的操作，所以是O1时间） 注意双向链表设置了 伪头部和伪尾部 ，链表的常用技巧
    # self.head, self.tail = DLinkedNode(), DLinkedNode()
    # python库函数中，orderdict的设计思路也是这样

    def _add_node_to_head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node_to_head(node)

    def _pop_last_node(self):
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity: int):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        # 伪头部 和 伪尾部
        self.head, self.tail = DLinkedNode(), DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key, None)
        if not node: return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key, None)
        if node:
            node.value = value
            self._move_to_head(node)
        else:
            # 生成新的节点，放入双向链表并更新
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node_to_head(newNode)
            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_last_node()
                del self.cache[tail.key]
                self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
