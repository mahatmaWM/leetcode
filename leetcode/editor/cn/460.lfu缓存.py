#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU缓存
#
# https://leetcode-cn.com/problems/lfu-cache/description/
#
# algorithms
# Hard (41.96%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    14.8K
# Total Submissions: 35.4K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
	'[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。它应该支持以下操作：get 和 put。
#
#
# get(key) - 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。
# put(key, value) -
# 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。
#
#
# 「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。
#
#
#
# 进阶：
# 你是否可以在 O(1) 时间复杂度内执行两项操作？
#
#
#
# 示例：
#
# LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回 1
# cache.put(3, 3);    // 去除 key 2
# cache.get(2);       // 返回 -1 (未找到key 2)
# cache.get(3);       // 返回 3
# cache.put(4, 4);    // 去除 key 1
# cache.get(1);       // 返回 -1 (未找到 key 1)
# cache.get(3);       // 返回 3
# cache.get(4);       // 返回 4
#
# 本题与146区别，这里要记录使用次数，所以不能用LRU的双向列表来存储所谓的热度，O1时间是解决不了的。

# @lc code=start
class LFUCache:
	def __init__(self, capacity: int):
		from collections import OrderedDict, defaultdict
		self.freq = defaultdict(OrderedDict)
		self.key_to_freq = {}
		self.capacity = capacity
		self.min_freq = 0


	def get(self, key: int) -> int:
		if key not in self.key_to_freq: return -1
		key_freq = self.key_to_freq[key]
		res = self.freq[key_freq].pop(key)
		if not self.freq[key_freq] and key_freq == self.min_freq: self.min_freq += 1
		self.freq[key_freq + 1][key] = res
		self.key_to_freq[key] = key_freq + 1
		return res


	def put(self, key: int, value: int) -> None:
		if self.capacity == 0: return
		# key 本身就在其中
		if key in self.key_to_freq:
			key_freq = self.key_to_freq[key]
			self.freq[key_freq].pop(key)
			if not self.freq[key_freq] and key_freq == self.min_freq: self.min_freq += 1
			self.freq[key_freq + 1][key] = value
			self.key_to_freq[key] = key_freq + 1
		else:
			# key不在, 要弹出频率使用次数少的key
			if len(self.key_to_freq) == self.capacity:
				k, v = self.freq[self.min_freq].popitem(last=False)
				self.key_to_freq.pop(k)
			self.key_to_freq[key] = 1
			self.freq[1][key] = value
			self.min_freq = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

