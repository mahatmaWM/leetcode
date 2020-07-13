#
# @lc app=leetcode.cn id=436 lang=python3
#
# [436] 寻找右区间
#
# https://leetcode-cn.com/problems/find-right-interval/description/
#
# algorithms
# Medium (45.59%)
# Likes:    41
# Dislikes: 0
# Total Accepted:    3.5K
# Total Submissions: 7.6K
# Testcase Example:  '[[1,2]]'
#
# 给定一组区间，对于每一个区间 i，检查是否存在一个区间 j，它的起始点大于或等于区间 i 的终点，这可以称为 j 在 i 的“右侧”。
#
# 对于任何区间，你需要存储的满足条件的区间 j 的最小索引，这意味着区间 j 有最小的起始点可以使其成为“右侧”区间。如果区间 j 不存在，则将区间 i
# 存储为 -1。最后，你需要输出一个值为存储的区间值的数组。
#
# 注意:
#
#
# 你可以假设区间的终点总是大于它的起始点。
# 你可以假定这些区间都不具有相同的起始点。
#
#
# 示例 1:
#
#
# 输入: [ [1,2] ]
# 输出: [-1]
#
# 解释:集合中只有一个区间，所以输出-1。
#
#
# 示例 2:
#
#
# 输入: [ [3,4], [2,3], [1,2] ]
# 输出: [-1, 0, 1]
#
# 解释:对于[3,4]，没有满足条件的“右侧”区间。
# 对于[2,3]，区间[3,4]具有最小的“右”起点;
# 对于[1,2]，区间[2,3]具有最小的“右”起点。
#
#
# 示例 3:
#
#
# 输入: [ [1,4], [2,3], [3,4] ]
# 输出: [-1, 2, -1]
#
# 解释:对于区间[1,4]和[3,4]，没有满足条件的“右侧”区间。
# 对于[2,3]，区间[3,4]有最小的“右”起点。
#
#
#


# @lc code=start
class Solution:
    # 首先将左边界排序（记录下索引位置），然后对于每一个候选区间（右边界），在排序结果中二分查找对应的目标区间
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        res = []
        loc = []
        for idx, val in enumerate(intervals):
            loc.append((val[0], idx))
        loc.sort()

        # 二分查找：第一个大于等于右边界的数
        def searchInsert(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] == target: return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        # 取出已排序的左边界
        loc_left = list(map(lambda x: x[0], loc))
        for _, right in intervals:
            index = searchInsert(loc_left, right)
            if index >= len(loc):
                res.append(-1)
            else:
                res.append(loc[index][1])
        return res


# @lc code=end
