# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
#
# 请找出其中最小的元素。 
#
# 你可以假设数组中不存在重复元素。 
#
# 示例 1: 
#
# 输入: [3,4,5,1,2]
# 输出: 1
#
# 示例 2: 
#
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
# Related Topics 数组 二分查找


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
            mid = left + (right - left) // 2
            # 比较位置mid与左右两边的值大小，看mid是否出现在拐点处
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # 将位置mid与位置right相比较，看mid是位于大的部分？还是小的部分？改变left或者right指针
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findMin(nums=[4,5,6,7,0,1,2]))
