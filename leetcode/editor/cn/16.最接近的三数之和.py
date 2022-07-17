#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
# https://leetcode-cn.com/problems/3sum-closest/description/
#
# algorithms
# Medium (44.28%)
# Likes:    447
# Dislikes: 0
# Total Accepted:    108.2K
# Total Submissions: 244.3K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target
# 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
#
#
# 示例：
#
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 10^3
# -10^3 <= nums[i] <= 10^3
# -10^4 <= target <= 10^4
#
#
#


# @lc code=start
class Solution:
    # 思路：先数组排序，再遍历数组，
    # 对于当前位置i，使用两个指针left&right来判断三数字的和，根据和来移动左右指针，并更新结果。
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if abs(sum_3 - target) < abs(res - target):
                    res = sum_3

                if sum_3 == target:
                    return sum_3
                elif sum_3 < target:
                    left += 1
                elif sum_3 > target:
                    right -= 1
        return res


# @lc code=end
