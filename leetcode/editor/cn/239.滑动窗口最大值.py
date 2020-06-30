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
# 思路：
# 使用双向队列来表示窗口，队列中保存索引，其对应元素值保持从大到小排序。这和单调栈很类似，叫单调队列
# 当窗口右移的时候，入队列的元素需要和队列中的元素保持有序。
# 队列中的最大元素的索引始终为队首元素。
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # base cases
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums

        import collections
        deq = collections.deque()

        # 把元素的索引index放入队列，并保证队首为最大元素
        def push_index_to_dq(index):
            # 直接挤出队首的元素的index
            if deq and deq[0] == index - k:
                deq.popleft()
            # 从队尾去掉那些更小的元素的index
            while deq and nums[index] > nums[deq[-1]]:
                deq.pop()
            deq.append(index)

        # 初始化队列，并计算nums[:k]的最大值
        max_idx = 0
        for i in range(k):
            push_index_to_dq(i)
            if nums[i] > nums[max_idx]:
                max_idx = i

        output = [nums[max_idx]]
        for i in range(k, n):
            push_index_to_dq(i)
            output.append(nums[deq[0]])
        return output
# @lc code=end

