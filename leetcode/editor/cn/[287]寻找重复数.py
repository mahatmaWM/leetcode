# 给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
# 假设只有一个重复的整数，找出这个重复的数。
#
# 示例 1: 
#
# 输入: [1,3,4,2,2]
# 输出: 2
# 
#
# 示例 2: 
#
# 输入: [3,1,3,4,2]
# 输出: 3
# 
#
# 说明： 
#
# 
# 不能更改原数组（假设数组是只读的）。 
# 只能使用额外的 O(1) 的空间。 
# 时间复杂度小于 O(n2) 。 
# 数组中只有一个重复的数字，但它可能不止重复出现一次。 
# 
# Related Topics 数组 双指针 二分查找

# 思路：
# 如果可以使用额外空间，那么用hash计数是最简单的，但是这里不能用额外空间，所以只能用比较，而且暴力比较复杂度为O(n2)
# 既然遍历是不能避免的，那么另外的只能借助二分查找了。
#
# 二分查找。
# 已知所有数字的范围是1----n，就可以把left设为1，right设为n，mid设为left和right的中间值，
# 每次循环，用count记录一下有多少个小于等于mid的值，
# 如果count <= mid，就代表重复的数字应该不会落在mid左侧的区间内，于是更新left；反之就更新right。
# 这种方法相当于二分猜数字，然后判断该数字是否满足条件。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 1, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 遍历 记录<= mid的数字，如果小于等于mid本身，说明重复数字一定出现在[mid right]的区间
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            # print mid, count
            if count <= mid:
                left = mid + 1
            else:
                right = mid
        return left

# leetcode submit region end(Prohibit modification and deletion)
