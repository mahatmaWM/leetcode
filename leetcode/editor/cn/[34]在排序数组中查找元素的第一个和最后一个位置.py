# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。 
#
# 如果数组中不存在目标值，返回 [-1, -1]。 
#
# 示例 1: 
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
#
# 示例 2: 
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
# Related Topics 数组 二分查找

# 数组已升序排序。
# 1、使用二分查找寻找开始位置。
# 2、使用二分查找寻找结束位置。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return -1, -1
        start, end = -1, -1

        # 采用[left, right)区间
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
        if nums[left] == target:
            start = left

        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        # right为开区间，所以要right-1
        if nums[right - 1] == target:
            end = right - 1

        return start, end


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
