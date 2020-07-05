#
# @lc app=leetcode.cn id=556 lang=python3
#
# [556] 下一个更大元素 III
#
# https://leetcode-cn.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (30.86%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    5.1K
# Total Submissions: 16.5K
# Testcase Example:  '12'
#
# 给定一个32位正整数 n，你需要找到最小的32位整数，其与 n 中存在的位数完全相同，并且其值大于n。如果不存在这样的32位整数，则返回-1。
#
# 示例 1:
#
#
# 输入: 12
# 输出: 21
#
#
# 示例 2:
#
#
# 输入: 21
# 输出: -1
#
#
#


# @lc code=start
class Solution:
    # 和31题思路一样
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def reverse(nums, i, j):
            for k in range(i, (i + j) // 2 + 1):
                swap(nums, k, i + j - k)

        i = len(nums) - 1
        # 从后开始遍历数组，找到第一个降序的位置i
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        # 将位置i至n-1的数字反转
        reverse(nums, i, len(nums) - 1)
        # 遍历i到n-1的数字，找到第一个比i-1大的数字，交换彼此即可
        if i > 0:
            for j in range(i, len(nums)):
                if nums[j] > nums[i - 1]:
                    swap(nums, i - 1, j)
                    break
        m = int(''.join(nums))
        # print('m={},n={}'.format(m,n))
        return -1 if m > 2**31 - 1 or m <= n else m


# @lc code=end
