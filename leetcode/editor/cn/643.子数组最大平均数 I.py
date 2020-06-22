# 给定 n 个整数，找出平均数最大且长度为 k 的连续子数组，并输出该最大平均数。
#
# 示例 1: 
#
# 输入: [1,12,-5,-6,50,3], k = 4
# 输出: 12.75
# 解释: 最大平均数 (12-5-6+50)/4 = 51/4 = 12.75
# 
#
# 
#
# 注意: 
#
# 
# 1 <= k <= n <= 30,000。 
# 所给数据范围 [-10,000，10,000]。 
# 
# Related Topics 数组

# 采用滑动窗口。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left, right, n = 0, k - 1, len(nums)
        cur_window = sum(nums[0:k])
        res = cur_window
        while right < n - 1:
            right = right + 1
            cur_window = cur_window - nums[left] + nums[right]
            res = max(res, cur_window)
            left = left + 1
        return float(res) / k


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findMaxAverage(nums=[0,4,0,3,2], k=1))
