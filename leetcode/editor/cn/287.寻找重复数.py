#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#
# https://leetcode-cn.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (65.69%)
# Likes:    715
# Dislikes: 0
# Total Accepted:    79.5K
# Total Submissions: 121K
# Testcase Example:  '[1,3,4,2,2]'
#
# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和
# n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1:
#
# 输入: [1,3,4,2,2]
# 输出: 2
#
#
# 示例 2:
#
# 输入: [3,1,3,4,2]
# 输出: 3
#
#
# 说明：
#
#
# 不能更改原数组（假设数组是只读的）。
# 只能使用额外的 O(1) 的空间。
# 时间复杂度小于 O(n^2) 。
# 数组中只有一个重复的数字，但它可能不止重复出现一次。
#
#
#


# @lc code=start
class Solution:
    # 先排序再遍历一样，都是NlogN
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: return nums[i]


class Solution1:
    # 思路：如果可以使用额外空间，那么用hash计数是最简单的，但是这里不能用额外空间，所以只能用比较。
    # 上面是先排序再遍历的方式。
    #
    # 下面借鉴二分查找的思路，已知所有数字的范围是1到n，就可以把left设为1，right设为n，mid设为left和right的中间值。
    # 不断二分left&right，逼近目标值重复数。
    # 每得到一个候选值mid时，用count记录一下有多少个小于等于mid的值。
    # 如果count>mid，代表重复的数字落在mid左侧的区间，更新right；反之就更新right。
    # 这种方法相当于二分猜数字，然后判断该数字是否满足条件。
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            # 遍历记录 <= mid的数字，如果小于等于mid本身，说明重复数字一定出现在[mid+1 right]的区间
            count = 0
            for num in nums:
                if num <= mid: count += 1
            if count > mid:
                right = mid
            else:
                left = mid + 1
        return left


# @lc code=end
