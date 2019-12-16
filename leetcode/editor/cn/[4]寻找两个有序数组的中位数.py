# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
#
# 你可以假设 nums1 和 nums2 不会同时为空。 
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
# Related Topics 数组 二分查找 分治算法

# getKth方法比较重要，使用递归和二分法查找两个有序链表任意位置的元素，
# 假设B更长
# A[0:pa] A[pa:]
# B[0:pb] B[pb:]
# 在递归时判断A[pa - 1] <= B[pb - 1]则可以删去A的前几个元素A[0:pa]，并找到新链表第k-pa个元素即可，对应return self.getKth(A[pa:], B, pb)。
# 否则去掉B的前pb个B[0:pb]，并找到新链表第pa个元素即可，对应return self.getKth(A, B[pb:], pa)
# findMedianSortedArrays方法分了奇偶情况。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    # 找A B两个有序链表合在一起的第K个元素（合起来有序后的）
    def getKth(self, A, B, k):
        k = int(k)
        lenA = len(A)
        lenB = len(B)
        # 假设B链表更长
        if lenA > lenB:
            return self.getKth(B, A, k)
        # 递归的终止条件
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])

        pa = int(min(k // 2, lenA))
        pb = k - pa
        if A[pa - 1] <= B[pb - 1]:
            return self.getKth(A[pa:], B, pb)
        else:
            return self.getKth(A, B[pb:], pa)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lenA = len(nums1)
        lenB = len(nums2)
        if (lenA + lenB) % 2 == 1:
            return self.getKth(nums1, nums2, (lenA + lenB) / 2 + 1)
        else:
            return (self.getKth(nums1, nums2, (lenA + lenB) / 2) + self.getKth(
                nums1, nums2, (lenA + lenB) / 2 + 1)) * 0.5


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(Solution().findMedianSortedArrays(nums1, nums2))
