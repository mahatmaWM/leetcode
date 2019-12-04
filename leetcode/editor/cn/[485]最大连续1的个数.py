# 给定一个二进制数组， 计算其中最大连续1的个数。
#
# 示例 1: 
#
# 
# 输入: [1,1,0,1,1,1]
# 输出: 3
# 解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
# 
#
# 注意： 
#
# 
# 输入的数组只包含 0 和1。 
# 输入数组的长度是正整数，且不超过 10,000。 
# 
# Related Topics 数组

# 遍历一次数组，记录临时的连续1个数和最终结果max对比即可。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp_res = 0
        res = 0
        for i in nums:
            if i == 1:
                temp_res += 1
                res = max(res, temp_res)
            else:
                temp_res = 0
        return res

# leetcode submit region end(Prohibit modification and deletion)
