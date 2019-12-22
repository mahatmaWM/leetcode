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

# 思路：
# 第一步找到旋转点，左右两边都分别是升序的，然后左右两边分别二分查找即可。
# 寻找旋转点也可以借鉴二分查找的思路。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def find_rotate_index(left, right):
            if nums[left] < nums[right]:
                return 0
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] > nums[pivot + 1]:
                    return pivot + 1
                else:
                    if nums[pivot] < nums[left]:
                        right = pivot - 1
                    else:
                        left = pivot + 1

        def b_search(left, right):
            while left <= right:
                pivot = (left + right) // 2
                if nums[pivot] == target:
                    return pivot
                elif target < nums[pivot]:
                    right = pivot - 1
                else:
                    left = pivot + 1
            return -1

        # 数组为空或者只有一个元素
        if not nums:
            return -1
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        rotate_index = find_rotate_index(0, n - 1)
        if rotate_index == 0:
            return b_search(0, n - 1)
        else:
            # 决定在旋转点左边找还是右边找
            if nums[0] <= target:
                return b_search(0, rotate_index - 1)
            else:
                return b_search(rotate_index, n - 1)


# leetcode submit region end(Prohibit modification and deletion)
def main():
    s = Solution()
    print(s.search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
