# 给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
# 示例: 
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。 
#
# 进阶： 
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
# Related Topics 数组

# 考虑先正反两次遍历，一次遍历求每个数左侧的所有数的积，一次遍历求每个数右侧的所有数的积，最后两部分积相乘即得所求。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)

        # 左边的乘积
        tmp = 1
        for i in range(len(nums)):
            res[i] = tmp
            tmp *= nums[i]

        # 右边的乘积
        tmp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= tmp
            tmp *= nums[i]
        return res

# leetcode submit region end(Prohibit modification and deletion)
