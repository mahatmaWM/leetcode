# 给定一个正整数数组 w ，其中 w[i] 代表位置 i 的权重，请写一个函数 pickIndex ，它可以随机地获取位置 i，选取位置 i 的概率与 w[i] 成正比。
#
# 说明: 
#
# 
# 1 <= w.length <= 10000 
# 1 <= w[i] <= 10^5 
# pickIndex 将被调用不超过 10000 次 
# 
#
# 示例1: 
#
# 
# 输入:
# ["Solution","pickIndex"]
# [[[1]],[]]
# 输出: [null,0]
# 
#
# 示例2: 
#
# 
# 输入:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# 输出: [null,0,1,1,1,0]
#
# 输入语法说明： 
#
# 输入是两个列表：调用成员函数名和调用的参数。
# Solution 的构造函数有一个参数，即数组 w。
# pickIndex 没有参数。
# 输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。
# Related Topics 二分查找 Random


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def __init__(self, w: List[int]):
        self.N = len(w)
        self.pre_sum = w
        for i in range(1, len(w)):
            self.pre_sum[i] = self.pre_sum[i - 1] + self.pre_sum[i]

    def pickIndex(self) -> int:
        import random
        tmp = random.random() % self.N
        start, end = 0, self.N
        while start < end:
            mid = start + (end - start) / 2
            if self.pre_sum[mid] <= tmp:
                start = mid + 1
            else:
                end = mid
        return start

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# leetcode submit region end(Prohibit modification and deletion)
