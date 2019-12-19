# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
# 
# Related Topics 数组 双指针

# 思路：
# 先数组排序，再遍历数组，对于当前位置i，使用两个指针left&right来判断三数字的和，根据和来移动左右指针，并更新结果。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = sum(nums[:3])
        n = len(nums)

        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                sum_3 = nums[i] + nums[left] + nums[right]
                if abs(sum_3 - target) < abs(res - target):
                    res = sum_3

                if sum_3 < target:
                    left += 1
                elif sum_3 > target:
                    right -= 1
                else:
                    return sum_3
        return res

# leetcode submit region end(Prohibit modification and deletion)
