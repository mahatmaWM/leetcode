#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# https://leetcode-cn.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (25.94%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 19K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
# 你需要返回给定数组中的重要翻转对的数量。
#
# 示例 1:
#
#
# 输入: [1,3,2,3,1]
# 输出: 2
#
#
# 示例 2:
#
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
#
# 注意:
#
#
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
#
#
#


# @lc code=start
class Solution:
    # 归并排序的过程中，如果前半个数组的元素大于后半个数组的元素，这种组合叫翻转对，时间复杂度 O(NlogN)
    def reversePairs(self, nums: List[int]) -> int:

        # 合并两个有序数组，nums[start:mid] nums[mid+1:end]，都采用前闭后闭的方式，代码更容易理解
        def merge(nums, start, mid, end):
            l, r = start, mid + 1
            res = []
            while l <= mid and r <= end:
                if nums[l] >= nums[r]:
                    res.append(nums[r])
                    r += 1
                else:
                    res.append(nums[l])
                    l += 1
            nums[start:end + 1] = res + nums[l:mid + 1] + nums[r:end + 1]

        def mergesort_and_count(nums, start, end):
            if start >= end: return 0
            mid = (start + end) // 2
            count = mergesort_and_count(nums, start, mid) + mergesort_and_count(nums, mid + 1, end)

            # 统计翻转对
            j = mid + 1
            for i in range(start, mid + 1):
                while j < end + 1 and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            merge(nums, start, mid, end)
            return count

        return mergesort_and_count(nums, 0, len(nums) - 1)


# @lc code=end
