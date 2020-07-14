#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#
# https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (38.29%)
# Likes:    2765
# Dislikes: 0
# Total Accepted:    209.8K
# Total Submissions: 548K
# Testcase Example:  '[1,3]\n[2]'
#
# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。
#
# 请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
#
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
#
#
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
#
#


# @lc code=start
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 找arr1 arr2 两个有序序列合在一起的有序中的第K个元素，K从1开始
        #
        # 假设arr2更长，所以每次更新决定丢弃多少时，主要依据K和arr1长度，二分减半K值。
        #
        # 根据每次找到的pa值，把两个数组分段：
        # arr1[0:pa-1] arr1[pa:]
        # arr2[0:pb-1] arr2[pb:]
        #
        # 如果 A[pa-1] <= B[pb-1]，删去A的前几个元素A[0:pa-1]，并找到第k-pa个元素即可
        #                         否则去掉B的前pb个B[0:pb-1]，并找到新链表第pa个元素即可

        def getKth(arr1, arr2, k):
            l1 = len(arr1)
            l2 = len(arr2)
            # 假设我们需要arr2更长一些
            if l1 > l2: return getKth(arr2, arr1, k)
            # 递归的终止条件
            if l1 == 0: return arr2[k - 1]
            if k == 1: return min(arr1[0], arr2[0])

            pa = min(k // 2, l1)
            pb = k - pa

            
            if arr1[pa - 1] <= arr2[pb - 1]:
                return getKth(arr1[pa:], arr2, pb)
            else:
                return getKth(arr1, arr2[pb:], pa)

        # 忽略奇数 偶数 的区别
        mid1 = (len(nums1) + len(nums2)) // 2 + 1
        mid2 = (len(nums1) + len(nums2) - 1) // 2 + 1
        return (getKth(nums1, nums2, mid1) + getKth(nums1, nums2, mid2)) * 0.5


# @lc code=end
