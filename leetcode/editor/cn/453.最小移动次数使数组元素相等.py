# 给定一个长度为 n 的非空整数数组，找到让数组所有元素相等的最小移动次数。每次移动可以使 n - 1 个元素增加 1。
#
# 示例: 
#
# 
# 输入:
# [1,2,3]
#
# 输出:
# 3
#
# 解释:
# 只需要3次移动（注意每次移动会增加两个元素的值）：
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# Related Topics 数学

# 假设最终数组中全为某一个数f,一共加了n次，数组的长度为l，数组中最小的数字为m,数组和为s
# f*l=s+(l-1)*n，f最小的情况是什么 一定是数组中的最小值加了n 即f=n+m
# 代入得
# nl+ml=s+ln-n
# n=s-ml

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums) * min(nums)

# leetcode submit region end(Prohibit modification and deletion)
