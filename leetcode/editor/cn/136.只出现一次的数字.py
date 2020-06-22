# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明： 
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
#
# 示例 1: 
#
# 输入: [2,2,1]
# 输出: 1
# 
#
# 示例 2: 
#
# 输入: [4,1,2,1,2]
# 输出: 4
# Related Topics 位运算 哈希表

# 利用位运算的异或，相同为0，则所有出现两次的最后被异或为0，剩下只出现一次的数字。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for item in nums:
            res = res ^ item
        return res

# leetcode submit region end(Prohibit modification and deletion)
