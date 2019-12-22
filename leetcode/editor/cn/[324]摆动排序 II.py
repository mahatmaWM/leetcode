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


# 思路：
# 如果是有序数组的话，这个问题就很好处理了。
# 直接两个指针调整为摆动排序，其中：0 2的位置放小的一半数字，1 3放大的一半数字。

# 无序数组要快也可以借鉴二分查找的方法找到第K（中位数）大的元素，将左右两边的数字调整好。
# but 这个时候再按照有序的方式去调整的话，结果是错的。
# 因为不能保证两边的子数组是有序的，这个时候要借用三色荷兰国旗排序方法进行调整。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    # 先排序的做法
    def wiggleSort1(self, nums):
        n = len(nums)
        nums = sorted(nums, reverse=True)
        p1, p2 = 0, (n + 1) // 2
        res = [float('-inf')] * n
        for i in range(n):
            if i % 2 == 0:
                res[i] = nums[p2]
                p2 += 1
            else:
                res[i] = nums[p1]
                p1 += 1
        return res

    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 返回索引下标
        def partition(num, low, high):
            # 选取low位置为pivot
            pivot = num[low]
            while low < high:
                while low < high and num[high] <= pivot:
                    high -= 1
                num[low] = num[high]
                while low < high and num[low] >= pivot:
                    low += 1
                num[high] = num[low]
            num[low] = pivot
            return low

        def kth_largest(num, low, high, k):
            index = partition(num, low, high)
            if index == k - 1:
                return num[index]
            if index < k - 1:
                return kth_largest(num, index + 1, high, k)
            else:
                return kth_largest(num, low, index - 1, k)

        n = len(nums)
        if n <= 1:
            return
        mid = kth_largest(nums, 0, n - 1, (n + 1) // 2)
        # print((n + 1) // 2)
        # print(mid)
        # print(nums)

        # O(n)时间原地修改，类似75题的三色荷兰国旗排序算法。
        # 但数组是全部奇数位下标和偶数位下标的拼接
        p0 = curr = 0
        p2 = n - 1
        n |= 1  # 取向上离n最近的奇数

        while curr <= p2:
            ii, jj, kk = map(lambda x: (x * 2 + 1) % n, [p0, curr, p2])
            if nums[jj] > mid:
                nums[jj], nums[ii] = nums[ii], nums[jj]
                p0 += 1
                curr += 1
            elif nums[jj] < mid:
                nums[jj], nums[kk] = nums[kk], nums[jj]
                p2 -= 1
            else:
                curr += 1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [3, 2, 1, 2, 1, 3, 1, 2, 1, 2]
    print(Solution().wiggleSort1(nums=nums))
    print(nums)
