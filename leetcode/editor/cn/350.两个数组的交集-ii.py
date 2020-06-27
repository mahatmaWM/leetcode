#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (48.66%)
# Likes:    285
# Dislikes: 0
# Total Accepted:    90.3K
# Total Submissions: 185.5K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
#
# 示例 1:
#
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
#
#
# 示例 2:
#
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
#
# 说明：
#
#
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
#
#
# 进阶:
#
#
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
#
#
# 思路：
# 考虑到数组中元素可能重复，所以需要记录元素出现次数。
#
# 1、如果数组已经有序，那么就是求有序数组的交集问题，两个指针分别遍历数组即可。
# 2、如果nums1比nums2小很多，那么用小的那个来做hash表，遍历长的nums2。
# 3、

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter = set(nums1) & set(nums2)
        from collections import defaultdict
        dd1 = defaultdict(int)
        dd2 = defaultdict(int)
        for a in nums1:
            if a in inter:
                dd1[a] += 1
        for b in nums2:
            if b in inter:
                dd2[b] += 1

        res = []
        for i in inter:
            res.extend([i] * min(dd1[i], dd2[i]))
        return res

# @lc code=end

