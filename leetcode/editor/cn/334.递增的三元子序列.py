# 给定一个未排序的数组，判断这个数组中是否存在长度为 3 的递增子序列。
#
# 数学表达式如下:
#
# 如果存在这样的 i, j, k, 且满足 0 ≤ i < j < k ≤ n-1，
# 使得 arr[i] < arr[j] < arr[k] ，返回 true ; 否则返回 false 。
#
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1) 。
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: true
#
#
# 示例 2:
#
# 输入: [5,4,3,2,1]
# 输出: false
#

# 子串要求连续的，子序列不需要连续
# 思路：感觉这题使用 递增栈 可以找到当前元素左边第一个更小的元素位置。
# 然后遍历一遍这个数组即可。

# 但是这题目只需要找到3个，那么更巧的办法是遍历的过程中先找最小值，再找次小值，如果这时又找到第3个，就退出。

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_num, sec_num = float('inf'), float('inf')  # 初始化最小值，次小值

        for i in nums:
            # 先维护最小值
            min_num = min(i, min_num)
            # 再维护次小值
            if i > min_num: sec_num = min(i, sec_num)
            # 发现第三大数
            if i > sec_num: return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
