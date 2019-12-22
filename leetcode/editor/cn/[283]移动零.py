# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
#
# 示例: 
#
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
#
# 说明: 
#
# 
# 必须在原数组上操作，不能拷贝额外的数组。 
# 尽量减少操作次数。 
# 
# Related Topics 数组 双指针

# 思路：
# 原位操作都是双指针

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in nums:
            if right != 0:
                nums[left] = right
                left += 1
        for i in range(left, len(nums)):
            nums[i] = 0

# leetcode submit region end(Prohibit modification and deletion)
