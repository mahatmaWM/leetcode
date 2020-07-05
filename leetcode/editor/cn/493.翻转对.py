#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#
# https://leetcode-cn.com/problems/reverse-pairs/description/
#
# algorithms
# Hard (25.94%)
# Likes:    99
# Dislikes: 0
# Total Accepted:    4.9K
# Total Submissions: 19K
# Testcase Example:  '[1,3,2,3,1]'
#
# 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
#
# 你需要返回给定数组中的重要翻转对的数量。
#
# 示例 1:
#
#
# 输入: [1,3,2,3,1]
# 输出: 2
#
#
# 示例 2:
#
#
# 输入: [2,4,3,5,1]
# 输出: 3
#
#
# 注意:
#
#
# 给定数组的长度不会超过50000。
# 输入数组中的所有数字都在32位整数的表示范围内。
#
#
#


# @lc code=start
class Solution1:
    # 归并排序的过程中，如果前半个数组的元素大于后半个数组的元素，这种组合叫翻转对，时间复杂度 O(NlogN)
    def reversePairs(self, nums: List[int]) -> int:

        # 合并两个有序数组，nums[start:mid] nums[mid+1:end]，都采用前闭后闭的方式，代码更容易理解
        def merge(nums, start, mid, end):
            l, r = start, mid + 1
            res = []
            while l <= mid and r <= end:
                if nums[l] >= nums[r]:
                    res.append(nums[r])
                    r += 1
                else:
                    res.append(nums[l])
                    l += 1
            nums[start:end + 1] = res + nums[l:mid + 1] + nums[r:end + 1]

        def mergesort_and_count(nums, start, end):
            if start >= end: return 0
            mid = (start + end) // 2
            count = mergesort_and_count(nums, start, mid) + mergesort_and_count(nums, mid + 1, end)

            # 统计翻转对
            j = mid + 1
            for i in range(start, mid + 1):
                while j < end + 1 and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            merge(nums, start, mid, end)
            return count

        return mergesort_and_count(nums, 0, len(nums) - 1)

# 树状数组做法, O(NlogN)时间复杂度
class BinaryIndexedTree(object):

    def __init__(self, N):
        self.B = [0] * N

    def low_bit(self, x):
        return x & (-x)

    # 第index个节点增加val, index从1开始算起
    def update(self, index, val):
        while index < len(self.B):
            self.B[index] += val
            index += self.low_bit(index)

    # 求数组A[0..index]的和, 包含index
    def get_sum(self, index):
        index = (len(self.B) + index) % len(self.B)
        ans = 0
        while index > 0:
            ans += self.B[index]
            index -= self.low_bit(index)
        return ans


class Solution:

    def reversePairs(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        arr = [x * 2 for x in arr]
        n1, n2 = len(arr), len(nums)
        btree = BinaryIndexedTree(n1 + 1)
        ans = 0
        for i, v in enumerate(reversed(nums)):
            index = bisect_left(arr, v)
            ans += btree.get_sum(index)
            index = bisect_left(arr, v * 2)
            btree.update(index + 1, 1)
        return ans

# @lc code=end
