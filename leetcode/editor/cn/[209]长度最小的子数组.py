# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例: 
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
# 
#
# 进阶: 
#
# 如果你已经完成了O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。 
# Related Topics 数组 双指针 二分查找

# 双指针法.
# 用l, r代表左右两个指针, 当右指针走到i时, 累加total, 当total >= s时, 尽量把l往右移, 找出符合题意的最短的subarray, 跳出内层循环后右指针继续往右走, 直到刷完nums.

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        res = len(nums)
        left, total = 0, 0
        for i, n in enumerate(nums):
            total += n
            while total >= s:
                res = min(res, i - left + 1)
                total -= nums[left]
                left += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
