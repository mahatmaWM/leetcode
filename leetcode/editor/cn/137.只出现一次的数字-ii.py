#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (67.22%)
# Likes:    359
# Dislikes: 0
# Total Accepted:    32.5K
# Total Submissions: 48.3K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 示例 1:
#
# 输入: [2,2,3,2]
# 输出: 3
#
#
# 示例 2:
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
#
#


# @lc code=start
class Solution1:

    def singleNumber(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for k, v in count.items():
            if v == 1: return k


class Solution:
    # 与136题类似，异或 操作可以看成不进位的加法，所以本题对每位看成相加后对3取模
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += (num >> i) & 1
            ans = ans | ((sum % 3) << i)
        # Python是动态类型语言，在这种情况下其会将符号位置的1看成了值，而不是当作符号“负数”
        return ans - 2**32 if ans > 2**31 - 1 else ans


# @lc code=end
