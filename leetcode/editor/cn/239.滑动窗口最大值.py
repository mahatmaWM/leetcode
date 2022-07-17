#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#
# https://leetcode-cn.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (47.89%)
# Likes:    396
# Dislikes: 0
# Total Accepted:    54.1K
# Total Submissions: 112.9K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
#
#
# 进阶：
#
# 你能在线性时间复杂度内解决此题吗？
#
#
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
# ⁠ 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
#


# @lc code=start
class Solution_baoli:
    # 直接模拟因为find_max_in_window是线性时间，当窗口长度很大的时候会超时
    # 如果这里能logN找到即可解决问题，所以队列里面的元素要有序（这里求最大值，如果有序可以O1时间）
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 特殊情况
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums

        def find_max_in_window(window):
            return max(window)
        import collections
        window = collections.deque()
        max_idx = 0
        for i in range(k):
            window.append(nums[i])
            if nums[i] > nums[max_idx]: max_idx = i
        ans = [nums[max_idx]]

        for i in range(k, n):
            window.append(nums[i])
            window.popleft()
            ans.append(find_max_in_window(window))
        return ans

class Solution1:
    # 思路：见上面暴力方法，只要保证window里面有序，即可O1时间找到
    # 但是由于SortedList内部的list要维护值移动拷贝（实际上还是很耗时的，不快能过）
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) * k == 0: return []
        if k == 1: return nums
        from sortedcontainers import SortedList
        window = SortedList()
        res = []
        left = 0
        for right in range(len(nums)):
            window.add(nums[right])
            while len(window) > k:
                window.remove(nums[left])
                left += 1
            if len(window) == k: res.append(window[-1])
        return res

class Solution:
    # 队列是最合适的数据结构，但是要想办法维护队列的有序性，所以用单调队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) * k == 0: return []
        if k == 1: return nums
        import collections
        deq = collections.deque()

        # 单调队列，索引index放入队列，并保证队首位置对应的元素为最大元素
        def adjust_deq_order(index):
            if deq and deq[0] == index - k:
                deq.popleft()
            while deq and nums[index] > nums[deq[-1]]:
                deq.pop()
            deq.append(index)

        # 初始化队列，并计算nums[:k]的最大值
        max_idx = 0
        for i in range(k):
            adjust_deq_order(i)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, len(nums)):
            adjust_deq_order(i)
            output.append(nums[deq[0]])
        return output
# @lc code=end
