#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (37.74%)
# Likes:    490
# Dislikes: 0
# Total Accepted:    84K
# Total Submissions: 222.6K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
#
#
#


# @lc code=start
class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def nSumTarget(nums, n, start, target):
            res = list(list())
            if n < 2 or len(nums) < n: return res
            # 处理2数和的情况
            if n == 2:
                low, hig = start, len(nums) - 1
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
                while i < len(nums):
                    sub = nSumTarget(nums, n - 1, i + 1, target - nums[i])
                    for item in sub:
                        item.append(nums[i])
                        res.append(item)
                    # 跳过相等的元素
                    while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                        i += 1
                    i += 1
            return res

        nums.sort()
        return nSumTarget(nums, 4, 0, target)


class Solution1:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                # 求剩余两数字之和
                left, right = j + 1, len(nums) - 1
                while left < right:
                    sum_4 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_4 == target:
                        if [nums[i], nums[j], nums[left], nums[right]] not in res:
                            res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    if sum_4 < target: left += 1
                    if sum_4 > target: right -= 1
        return res


# @lc code=end
