# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。 
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#  [-1, 0, 1],
#  [-1, -1, 2]
# ]
# 
# Related Topics 数组 双指针

# 1、数组排序
# 2、遍历数组，对于当前位置i，使用两个指针left&right来判断三数字的和，根据和来移动左右指针。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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
                if sum_3 < 0:
                    left += 1
                if sum_3 > 0:
                    right -= 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
