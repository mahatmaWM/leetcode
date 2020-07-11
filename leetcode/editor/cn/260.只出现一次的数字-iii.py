#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#
# https://leetcode-cn.com/problems/single-number-iii/description/
#
# algorithms
# Medium (72.50%)
# Likes:    235
# Dislikes: 0
# Total Accepted:    23K
# Total Submissions: 31.7K
# Testcase Example:  '[1,2,1,3,2,5]'
#
# 给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。
#
# 示例 :
#
# 输入: [1,2,1,3,2,5]
# 输出: [3,5]
#
# 注意：
#
#
# 结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
# 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
#
#
#

# @lc code=start
class Solution1:
    def singleNumber(self, nums: List[int]) -> List[int]:
        import collections
        count = collections.Counter(nums)
        res = []
        for num, c in count.items():
            if c == 1: res.append(num)
        return res

class Solution:
    # 位运算思路：想到这个系列的第一个题（只有一个数字出现一次，其余数字出现两次）。做法是异或操作。
    # 这个题也是用异或。把所有的数字进行一次异或，得到的是只出现了一次的两个数字的异或。
    #
    # 这两个数字不等，因此他们的二进制必定至少1位不同，即异或结果中为1的那位（一个数字的该位为1，另个数字的该位为0）。
    # 找出从右向左的第一个不同的位置（异或值为1的位置），给mask在该位置设置成1，mask的其余位置是0. mask存在的意义在于我们能通过该位置来分辨出两个只出现了一次的数字。
    #
    # 然后技巧性的来了：再进行一次异或操作。每个数字都跟mask相与。通过与的结果为0和为1，即可区分出两个数字。
    #
    # 我刚开始有点不明白的是，为什么把所有的元素都重新异或了？其实，因为除了这两个元素以外，其他的元素都出现了两次，这两次相同的数字的和mask的与操作的结果是相同的，所以会被异或两次抵消掉。
    #
    # 汇总一下思路，
    # 1、先通过异或找出两个元素的异或结果
    # 2、再根据异或结果的出现为1的位置作为mask，mask的二进制只有1位是1，也就是只看两个元素的该位置，其他出现两次的元素异或后都变成0了。
    # 3、最后，通过与操作判断该位置是0还是1区分两个元素。
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        # 从xor中找到第一个为1的bit位，其一定是两个不同的数字做异或得到的
        mask = 1
        while xor & mask == 0:
            mask = mask << 1

        num1, num2 = 0, 0
        for num in nums:
            if num & mask == 0:
                num1 ^= num
            else:
                num2 ^= num
        return [num1, num2]
# @lc code=end

