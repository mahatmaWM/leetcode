#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (38.06%)
# Likes:    799
# Dislikes: 0
# Total Accepted:    136.8K
# Total Submissions: 358.3K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#
#
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
#


# @lc code=start
class Solution:
    # 思路，判断目标值是否在升序的子区间内，从而决定前后指针应该怎么移动
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        # [l, r)
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return mid
            # print('l={},mid={},r={}'.format(l, mid, r))
            # 说明右边是升序的
            if nums[mid] < nums[r - 1]:
                # target在右边，下一次找区间[mid+1, r)，否则找区间[l, mid)
                if nums[mid] < target <= nums[r - 1]:
                    l = mid + 1
                else:
                    r = mid
            # 说明左边是升序的
            elif nums[mid] > nums[r - 1]:
                if nums[l] <= target <= nums[mid - 1]:
                    r = mid
                else:
                    l = mid + 1
            elif nums[mid] == nums[r - 1]:
                r = mid
        return -1


# @lc code=end
