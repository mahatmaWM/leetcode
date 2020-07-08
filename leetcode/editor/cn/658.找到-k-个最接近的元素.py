#
# @lc app=leetcode.cn id=658 lang=python3
#
# [658] 找到 K 个最接近的元素
#
# https://leetcode-cn.com/problems/find-k-closest-elements/description/
#
# algorithms
# Medium (43.74%)
# Likes:    107
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 24.8K
# Testcase Example:  '[1,2,3,4,5]\n4\n3'
#
# 给定一个排序好的数组，两个整数 k 和 x，从数组中找到最靠近 x（两数之差最小）的 k 个数。返回的结果必须要是按升序排好的。如果有两个数与 x
# 的差值一样，优先选择数值较小的那个数。
#
# 示例 1:
#
#
# 输入: [1,2,3,4,5], k=4, x=3
# 输出: [1,2,3,4]
#
#
#
#
# 示例 2:
#
#
# 输入: [1,2,3,4,5], k=4, x=-1
# 输出: [1,2,3,4]
#
#
#
#
# 说明:
#
#
# k 的值为正数，且总是小于给定排序数组的长度。
# 数组不为空，且长度不超过 10^4
# 数组里的每个元素与 x 的绝对值不超过 10^4
#
#
#
#
# 更新(2017/9/19):
# 这个参数 arr 已经被改变为一个整数数组（而不是整数列表）。 请重新加载代码定义以获取最新更改。
#
#


# @lc code=start
class Solution:
    # 二分查找+双指针法，二分查找到数组中第一个不小于x的数的位置，然后从这个地方开始向两个方向扩展区间
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        # 二分查找：第一个不小于target的数的位置
        def searchInsert(nums, target):
            n = len(nums)
            if target > nums[n - 1]: return n
            left, right = 0, n - 1
            while left <= right:
                mid = (right + left) >> 1
                if nums[mid] == target: return mid
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        i = searchInsert(arr, x)
        # print('i={}'.format(i))

        # 处理在一头一尾的特殊情况
        if i == 0: return arr[:k]
        if i == len(arr): return arr[-k:]

        # 对于区间[left, l, right)，判断left从哪个位置开始计算
        if arr[i] == x:
            left, right = i, i + 1
        else:
            if x - arr[i - 1] <= arr[i] - x:
                left, right = i - 1, i
            else:
                left, right = i, i + 1
        # print('1left={},right={}'.format(left, right))
        # 向两边扩展
        while right - left < k:
            if left == 0:
                right += 1
                continue
            if right == len(arr):
                left -= 1
                continue
            if x - arr[left - 1] <= arr[right] - x:
                left -= 1
            else:
                right += 1
        # print('2left={},right={}'.format(left, right))
        return arr[left:right]


# @lc code=end
