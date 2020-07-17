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

from typing import List


# @lc code=start
class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1) + len(nums2)

        # 找到两个升序数组的第K个元素（K从0开始计数）
        def findKth(nums1, nums2, k):
            if not nums1: return nums2[k]
            if not nums2: return nums1[k]
            i1, i2 = len(nums1) // 2, len(nums2) // 2
            m1, m2 = nums1[i1], nums2[i2]
            # 如果两个数组的中位数个数<K，说明第K个数应该出现在更大的元素中
            # 需要扔掉两个数组前面小的半段（扔掉更小的半段，i2+1个或者i1+1个元素，同时更新k值）
            if i1 + i2 < k:
                if m1 > m2:
                    return findKth(nums1, nums2[i2 + 1:], k - (i2 + 1))
                else:
                    return findKth(nums1[i1 + 1:], nums2, k - (i1 + 1))
            # 如果两个数组的中位数个数>=K，说明第K个数应该出现在更小的元素中
            # 需要扔掉两个数组后面大的半段（扔掉更大的半段，此时不需要更新k值）
            else:
                if m1 > m2:
                    return findKth(nums1[:i1], nums2, k)
                else:
                    return findKth(nums1, nums2[:i2], k)

        if n % 2 == 1:
            return findKth(nums1, nums2, n // 2)
        else:
            return (findKth(nums1, nums2, n // 2) + findKth(nums1, nums2, n // 2 - 1)) / 2.0


# @lc code=end

if __name__ == "__main__":
    nums1 = list([1, 3])
    nums2 = list([2])
    print(Solution().findMedianSortedArrays(nums1, nums2))
