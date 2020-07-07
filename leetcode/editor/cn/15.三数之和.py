#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (28.07%)
# Likes:    2283
# Dislikes: 0
# Total Accepted:    254.4K
# Total Submissions: 906.3K
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0
# ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#


# @lc code=start
class Solution1:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        length = len(nums)

        for i in range(length):
            left, right = i + 1, length - 1
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if sum_3 == 0:
                    if [nums[i], nums[left], nums[right]] not in res:
                        res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                if sum_3 < 0: left += 1
                if sum_3 > 0: right -= 1
        return res


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums已经被排序
        def nSumTarget(nums, n, start, target):
            res = list(list())
            l = len(nums)
            if n < 2 or l < n: return res
            # 处理2数和的情况（while是为了跳过相等的数字）
            if n == 2:
                low, hig = start, l - 1
                while low < hig:
                    left = nums[low]
                    right = nums[hig]
                    sum = left + right
                    if sum < target:
                        while low < hig and nums[low] == left:
                            low += 1
                    elif sum > target:
                        while low < hig and nums[hig] == right:
                            hig -= 1
                    elif sum == target:
                        res.append([left, right])
                        while low < hig and nums[low] == left:
                            low += 1
                        while low < hig and nums[hig] == right:
                            hig -= 1
            else:
                i = start
                while i < l:
                    sub = nSumTarget(nums, n - 1, i + 1, target - nums[i])
                    for item in sub:
                        item.append(nums[i])
                        res.append(item)
                    # 跳过相等的元素
                    while i < l - 1 and nums[i] == nums[i + 1]:
                        i += 1
                    i += 1
            return res

        nums.sort()
        return nSumTarget(nums, 3, 0, 0)


# @lc code=end
