# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
# 你只可以看到在滑动窗口内的 k 个数字。
# 滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。 
#
# 
#
# 示例: 
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#  滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7      3
# 1 [3  -1  -3] 5  3  6  7       3
# 1  3 [-1  -3  5] 3  6  7       5
# 1  3  -1 [-3  5  3] 6  7       5
# 1  3  -1  -3 [5  3  6] 7       6
# 1  3  -1  -3  5 [3  6  7]      7 
#
# 
#
# 提示： 
#
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。 
#
# 
#
# 进阶： 
#
# 你能在线性时间复杂度内解决此题吗？ 
# Related Topics 堆 Sliding Window

# 思路：
# 使用双向队列来表示窗口，队列中的元素保持从大到小排序。
# 当窗口右移的时候
# 1、判断移除去的最左端元素是否是最大的元素。
# 2、如队列的元素需要和队列中的元素保持有序。（这和单调栈很类似，叫单调队列）
#
# 队列中的最大元素的索引始终为队首元素。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        import collections
        deq = collections.deque()

        def push_index_to_dq(index):
            if deq and deq[0] == index - k:
                deq.popleft()
            while deq and nums[index] > nums[deq[-1]]:
                deq.pop()
            deq.append(index)

        # 初始化队列，并计算nums[:k]的最大值
        max_idx = 0
        for i in range(k):
            push_index_to_dq(i)
            # print(i, deq)
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        for i in range(k, n):
            push_index_to_dq(i)
            # print(i, deq)
            output.append(nums[deq[0]])
        return output


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
