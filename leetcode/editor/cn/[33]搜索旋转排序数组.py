# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
#
# 你可以假设数组中不存在重复的元素。 
#
# 你的算法时间复杂度必须是 O(log n) 级别。 
#
# 示例 1: 
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
#
# 示例 2: 
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# Related Topics 数组 二分查找

# 把中位数标记出来。
# 如果中位数比左边大，说明左边是递增的，断点在右边：
#     如果target在左边递增的区间，就在左边查找；
#     否则，在右边查找
# 如果中位数比左边小，说明右边是递增的，断点在左边：
#     如果target在右边的递增区间，就在右边查找；
#     否则，在左边查找。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            m = (left + right) // 2
            mid = nums[m]
            if mid == target:
                return m
            if mid > nums[left]:
                if nums[left] < target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if nums[m] < target < nums[right]:
                    left = m + 1
                else:
                    right = m - 1
        else:
            return -1


# leetcode submit region end(Prohibit modification and deletion)
def main():
    s = Solution()
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
