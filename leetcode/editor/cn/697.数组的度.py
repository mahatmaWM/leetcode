#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#
# https://leetcode-cn.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (53.47%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 32.4K
# Testcase Example:  '[1,2,2,3,1]'
#
# 给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。
#
# 你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
#
# 示例 1:
#
#
# 输入: [1, 2, 2, 3, 1]
# 输出: 2
# 解释:
# 输入数组的度是2，因为元素1和2的出现频数最大，均为2.
# 连续子数组里面拥有相同度的有如下所示:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# 最短连续子数组[2, 2]的长度为2，所以返回2.
#
#
# 示例 2:
#
#
# 输入: [1,2,2,3,1,4,2]
# 输出: 6
#
#
# 注意:
#
#
# nums.length 在1到50,000区间范围内。
# nums[i] 是一个在0到49,999范围内的整数。
#
#
#

# @lc code=start
class Solution:
    # 思路:
    # 1、遍历数组,记录每个数值的数量已经最左边和最右边的索引值
    # 2、找出数量最多的数,返回长度
    def findShortestSubArray(self, nums: List[int]) -> int:
        freqDict = {}
        for i in range(len(nums)):
            if nums[i] not in freqDict: freqDict[nums[i]] = [0, i, i]
            freqDict[nums[i]][0] += 1
            freqDict[nums[i]][2] = i

        maxFreq, minLen = 0, len(nums)
        for v in freqDict.values():
            if maxFreq < v[0]:
                maxFreq, minLen = v[0], v[2] - v[1] + 1
            elif maxFreq == v[0]:
                minLen = min(minLen, v[2] - v[1] + 1)

        return minLen

# @lc code=end

