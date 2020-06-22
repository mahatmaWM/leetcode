# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
#
# 请找出其中最小的元素。 
#
# 注意数组中可能存在重复的元素。 
#
# 示例 1： 
#
# 输入: [1,3,5]
# 输出: 1
#
# 示例 2： 
#
# 输入: [2,2,2,0,1]
# 输出: 0
#
# 说明： 
#
# 
# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。 
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？ 
# 
# Related Topics 数组 二分查找

# 旋转排序数组nums可以被拆分为2个排序数组nums1,nums2，并且nums1任一元素 > nums2任一元素；
# 因此，考虑二分法寻找此两数组的分界点nums[i](即第2个数组的首个元素)。

# 对比153和154的实现


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 如果长度为1或者本身还是升序
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # 说明分界点在右边
            if nums[mid] > nums[right]:
                left = mid + 1
            # 说明分界点在左边
            elif nums[mid] < nums[right]:
                right = mid
            # 说明右边是全部相等，那么不断的前移动right指针
            else:
                right = right - 1  # key
        return nums[left]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findMin(nums=[2, 2, 2, 0, 1]))
