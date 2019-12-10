# 给定一个无序的数组 nums，将它重新排列成 nums[0] < nums[1] > nums[2] < nums[3]... 的顺序。
#
# 示例 1: 
#
# 输入: nums = [1, 5, 1, 1, 6, 4]
# 输出: 一个可能的答案是 [1, 4, 1, 5, 1, 6]
#
# 示例 2: 
#
# 输入: nums = [1, 3, 2, 2, 3, 1]
# 输出: 一个可能的答案是 [2, 3, 1, 3, 1, 2]
#
# 说明: 
# 你可以假设所有输入都会得到有效的结果。
#
# 进阶: 
# 你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？
# Related Topics 排序

# 思路
# 0 2 4的位置放小的一半数字，1 3 5放大的一半数字，所以问题转化为将数组分为两部分A,B，A中每个元素都比B大，然后分别从AB中挑选元素即可。
# 也就是找到数组的中间数，并且将nums数组

# 在有序数组lst中查找val值的位置，二分查找递归和循环的两种方式。
# def binary_search_recursion(lst, val, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
#     if lst[mid] < val:
#         return binary_search_recursion(lst, val, mid + 1, end)
#     if lst[mid] > val:
#         return binary_search_recursion(lst, val, start, mid - 1)
#     return mid
#
#
# def binary_search_loop(lst, val):
#     start, end = 0, len(lst) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if lst[mid] < val:
#             start = mid + 1
#         elif lst[mid] > val:
#             end = mid - 1
#         else:
#             return mid
#     return None

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 循环二分查找第K大元素
    def find_kth_largest(self, nums, k):
        import random
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = self.partition_around_pivot(left, right, pivot_idx,
                                                        nums)
            if new_pivot_idx == k - 1:
                return nums[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1

    # 在nums数组的[left，right]区间，挑选nums[pivot_idx]位置的数字，比其大的元素放在左边，
    # 返回new_pivot_idx的值，也就是这个区间中第new_pivot_idx大的元素位置
    def partition_around_pivot(self, left, right, pivot_idx, nums):
        pivot_value = nums[pivot_idx]
        new_pivot_idx = left
        nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
        for i in range(left, right):
            if nums[i] > pivot_value:
                nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                new_pivot_idx += 1
        nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
        return new_pivot_idx

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = len(nums) // 2
        self.find_kth_largest(nums, k)
        print(nums)
        print(nums[k])
        # 根据奇数，偶数来确定right的位置
        left, right = 0, len(nums) - 1 if len(nums) % 2 == 0 else len(nums) - 2
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 2
            right -= 2


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 3, 2, 2, 3, 1]
    print(Solution().wiggleSort(nums=nums))
    print(nums)


    # 测试结果: [1, 3, 2, 2, 1, 3]
    [3, 3, 2, 2, 1, 1]
    # 期望结果: [2, 3, 1, 3, 1, 2]
