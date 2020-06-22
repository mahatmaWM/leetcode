# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明: 
#
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。 
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。 
# 
#
# 示例: 
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]
# Related Topics 数组 双指针

# 思路：
# nums1 保存最终结果，原位处理的话必然涉及到元素位置移动的操作，


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ptr_1, ptr_2, ptr_res = m - 1, n - 1, m + n - 1

        while ptr_1 >= 0 and ptr_2 >= 0:
            if nums1[ptr_1] >= nums2[ptr_2]:
                nums1[ptr_res] = nums1[ptr_1]
                ptr_1 -= 1
            else:
                nums1[ptr_res] = nums2[ptr_2]
                ptr_2 -= 1
            ptr_res -= 1
        # if ptr_2 > 0:
        #     nums1[:ptr_2] = nums2[:ptr_2]


# leetcode submit region end(Prohibit modification and deletion)
def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print(Solution().merge(nums1, m, nums2, n))
    print(nums1)


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
