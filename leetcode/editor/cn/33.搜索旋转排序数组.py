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
        # 左右闭合的方式
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right + left) // 2
            # print('mid={}'.format(mid))
            if nums[mid] == target: return mid
            # 说明右边是升序的
            if nums[mid] < nums[right]:
                # target在右边，下一次找区间[mid right]，否则找区间[left mid-1]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 说明左边是升序的
            elif nums[mid] > nums[right]:
                if nums[left] <= target <= nums[mid - 1]:
                    right = mid - 1
                else:
                    left = mid + 1
        # while结束，left与right指向一起
        if nums[left] == target: return left
        return -1


# @lc code=end
