#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode-cn.com/problems/sort-colors/description/
#
# algorithms
# Medium (55.09%)
# Likes:    459
# Dislikes: 0
# Total Accepted:    88.5K
# Total Submissions: 160.6K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 注意:
# 不能使用代码库中的排序函数来解决这道题。
#
# 示例:
#
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
#
# 进阶：
#
#
# 一个直观的解决方案是使用计数排序的两趟扫描算法。
# 首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
#
#
#


# @lc code=start
class Solution:
    # 思路：三色荷兰国旗排序问题。
    # [0,p0, curr, p2,end]前面放0，后面放2，相当于使用 p0, curr, p2 3个指针
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, curr, p2 = 0, 0, len(nums) - 1

        while curr <= p2:
            # 如果curr指向的元素为0，则交换curr,p0两个元素，同时curr p0均右移
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            # 如果curr指向的元素为2，则交换curr,p2两个元素，同时p2左移
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            # 否则curr指向的元素为1
            else:
                curr += 1


# @lc code=end
