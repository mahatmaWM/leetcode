# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。 
#
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。 
#
# 示例 1: 
#
# 输入: nums = [2,5,6,0,0,1,2], target = 0
# 输出: true
# 
#
# 示例 2: 
#
# 输入: nums = [2,5,6,0,0,1,2], target = 3
# 输出: false
#
# 进阶: 
#
# 
# 这是 搜索旋转排序数组 的延伸题目，本题中的 nums 可能包含重复元素。 
# 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？ 
# 
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
        :rtype: bool
        """
        N = len(nums)
        left, right = 0, N - 1
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False


# leetcode submit region end(Prohibit modification and deletion)
def main():
    s = Solution()
    print(s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
