# 给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
#
# 找到所有在 [1, n] 范围之间没有出现在数组中的数字。 
#
# 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。 
#
# 示例: 
#
# 
# 输入:
# [4,3,2,7,8,2,3,1]
#
# 输出:
# [5,6]
# 
# Related Topics 数组

# 思路一
# 原地变负来标记。比如对于[4, 3, 2, 7, 8, 2, 3, 1]，把这些元素作为list的索引，指向的元素变换成负数，
# 那么没有变换成负数的位置就是没有人指向它，故这个位置对应的下标没有出现。
#
# 思路二
# 使用set去重后判断。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

# leetcode submit region end(Prohibit modification and deletion)
