# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
#
# 说明： 
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？ 
#
# 示例 1: 
#
# 输入: [2,2,3,2]
# 输出: 3
# 
#
# 示例 2: 
#
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
# Related Topics 位运算

# 如果不计空间使用，则使用字典遍历一遍即可。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0
        three = 0
        for i in range(0, len(nums)):
            two |= one & nums[
                i]  # 当新来的为0时，two = two | 0，two不变，当新来的为1时，（当one此时为0，则two = two|0，two不变；当one此时为1时，则two = two | 1，two变为1
            one ^= nums[i]  # 新来的为0，one不变，新来为1时，one是0、1交替改变
            three = one & two  # 当one和two为1是，three为1（此时代表要把one和two清零了）
            one &= ~three  # 把one清0
            two &= ~three  # 把two清0
        return one

    # leetcode submit region end(Prohibit modification and deletion)
