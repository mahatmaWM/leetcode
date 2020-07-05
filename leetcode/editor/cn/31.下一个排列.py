#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode-cn.com/problems/next-permutation/description/
#
# algorithms
# Medium (33.79%)
# Likes:    551
# Dislikes: 0
# Total Accepted:    70.6K
# Total Submissions: 207.6K
# Testcase Example:  '[1,2,3]'
#
# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
#


# @lc code=start
class Solution:
    # 思路：很有技巧的题目。
    # 1、从后向前遍历数组，找到第一个降序的位置i，把i位置后面的数字翻转。
    # 2、这个数字i和后面第一个比它大的位置j交换即可。
    #
    # 首先说一下这题怎么想到的。
    # 有如下的一个数组
    # 1　　2　　7　　4　　3　　1
    # 下一个排列为：
    # 1　　3　　1　　2　　4　　7
    # 观察可以发现，再给出的数组中，2之后的数字都是降序排列的，我们将其反转，得到
    # 1　　2　　1　　3　　4　　7
    # 然后将1 3 4 7 中第一个比2大的数字3与2交换位置就得到最后结果，和556题一样的方法
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]

        def reverse(nums, i, j):
            for k in range(i, (i + j) // 2 + 1):
                swap(nums, k, i + j - k)

        n = len(nums)
        i = n - 1
        # 从后开始遍历数组，找到第一个降序的位置i
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        # 将位置i至n-1的数字反转
        reverse(nums, i, n - 1)
        # 遍历i到n-1的数字，找到第一个比i-1大的数字，交换彼此即可
        if i > 0:
            for j in range(i, n):
                if nums[j] > nums[i - 1]:
                    swap(nums, i - 1, j)
                    break


# @lc code=end
