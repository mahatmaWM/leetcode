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

# getKth方法比较重要，使用递归和二分法查找两个有序链表任意位置的元素，在递归时判断A[pa - 1] <= B[pb - 1]（A链表的前几个元素小于B链表的那些）所以可以删去A的前几个元素，并找到新链表k-pa（pb）个元素即可对应代码return self.getKth(A[pa:], B, pb)。
# findMedianSortedArrays与findMedianSortedArrays2都可以寻找中位数，findMedianSortedArrays方法分了奇偶情况，而findMedianSortedArrays2分别找第 (m+n+1) / 2 个，和 (m+n+2) / 2 个，然后求其平均值即可，这对奇偶数均适用。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def getKth(self, A, B, k):
        k = int(k)
        lenA = len(A)
        lenB = len(B)
        if lenA > lenB:
            return self.getKth(B, A, k)
        if lenA == 0:
            return B[k - 1]
        if k == 1:
            return min(A[0], B[0])
        pa = int(min(k / 2, lenA))
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
