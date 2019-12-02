# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
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
#  [-1,  0, 0, 1],
#  [-2, -1, 1, 2],
#  [-2,  0, 0, 2]
# ]
# 
# Related Topics 数组 哈希表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        console = []
        length = len(nums)
        for i in range(0, length - 3):
            for j in range(i + 1, length - 2):
                left, right = j + 1, length - 1
                while left < right:
                    sum_4 = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum_4 == target:
                        if [nums[i], nums[j], nums[left],
                            nums[right]] not in console:
                            console.append(
                                [nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                    if sum_4 < target:
                        left += 1
                    if sum_4 > target:
                        right -= 1
        return console

# leetcode submit region end(Prohibit modification and deletion)
