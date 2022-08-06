#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
# https://leetcode-cn.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (22.30%)
# Likes:    275
# Dislikes: 0
# Total Accepted:    20.2K
# Total Submissions: 90.5K
# Testcase Example:  '[4,2,3]'
#
# 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
#
#
#
# 示例 1:
#
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
#
#
# 示例 2:
#
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#
#
#
#
# 说明：
#
#
# 1 <= n <= 10 ^ 4
# - 10 ^ 5 <= nums[i] <= 10 ^ 5
#
#
#

# @lc code=start
class Solution:
    # 4，2，3
    # -1，4，2，3
    # 2，3，3，2，4
    # 当我们发现当前的数字i小于前面的数字i-1产生冲突后，
    # 有时候需要修改前面i-1较大的数字，有时候却要修改当前i数字为更小的
    # 那么有什么内在规律吗？是有的，判断修改哪个数字其实跟再前面i-2数的大小有关系，
    # 首先如果再前面的数不存在，我们直接修改前面i-1的数字为当前的数字即可。
    # 而当再前面的数字存在，并且小于当前数时，我们还是需要修改前面的数字；
    # 如果再前面的数大于当前数，我们需要修改当前数为前面的数


    def checkPossibility(self, nums: List[int]) -> bool:
        count = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if count == 0: return False
                if i == 1 or nums[i] >= nums[i - 2]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                count -= 1
        return True


# @lc code=end
