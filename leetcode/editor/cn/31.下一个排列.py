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

class Solution1:
    # 思路：很有技巧的题目。
    # 1、从后向前遍历数组，找到第一个降序的位置i，把i位置后面的数字翻转。
    # 2、这个数字i和后面第一个比它大的位置j交换即可。
    #
    # 首先说一下这题怎么想到的。
    # 有如下的一个数组
    # 1　　2　　7　　4　　3　　1
    # 下一个排列为：
    # 1　　3　　1　　2　　4　　7
    # 观察可以发现，在给出的数组中，2之后的数字都是降序排列的，我们将其反转，得到
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

        # 逆序遍历数组，找到第一个降序的位置i
        i = len(nums) - 1
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


class Solution:
    # 思路：很有技巧的题目。
    # 1、从后向前遍历数组，找到第一个降序的位置i，然后在找i位置后面的刚刚比i位置数字大一点的数字。
    # 2、这个数字i和后面第一个比它大的位置j交换即可。
    # 3、后续的数字再升序排列
    # 和556题一样的方法
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 逆序遍历数组，找到第一个降序的位置i
        i = len(nums) - 1
        while i >= 0 and nums[i] <= nums[i - 1]:
            i -= 1

        if i == 0:
            nums.sort()
        else:
            first = i - 1
            j = first + 1
            second_item = nums[j]
            second_index = j
            while j < len(nums):
                if nums[j] > nums[first] and nums[j] < second_item:
                    second_item = nums[j]
                    second_index = j
                j += 1
            nums[first], nums[second_index] = nums[second_index], nums[first]
            sorted(nums[first + 1:])

# @lc code=end
