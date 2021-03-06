#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (43.92%)
# Likes:    135
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 50.6K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n' +
  '[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# 设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。
#
# 你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，它包含数据流中的初始元素。每次调用
# KthLargest.add，返回当前数据流中第K大的元素。
#
# 示例:
#
#
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
#
#
# 说明:
# 你可以假设 nums 的长度≥ k-1 且k ≥ 1。
#
#

# @lc code=start
import heapq
class KthLargest:
    # 使用Python的堆是小根堆，不需要对其进行转换。
    # 如果一个堆的大小是k的话，那么最小的数字就在其最前面（即为第k大的数字），只要维护当新来的数字和最前面的这个数字比较即可。
    # 所以我们的工作就是维护一个小根堆，这个小根堆保存的是从第K大的数字到最大的数字。
    # 堆的大小即为K。
    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1


    def add(self, val: int) -> int:
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

