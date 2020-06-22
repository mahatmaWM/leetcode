# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。 
#
# 示例 1: 
#
# 输入: [3,2,3]
# 输出: [3]
#
# 示例 2: 
#
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]
# Related Topics 数组

# 思路：
# 与169题一样，都是属于摩尔投票法的使用。
# 本题的结果可能有0个、1个、2个。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 摩尔投票法
        m = n = None
        mcount = ncount = 0
        for num in nums:
            if num == m:
                mcount += 1
            elif num == n:
                ncount += 1
            elif not mcount:
                m, mcount = num, 1
            elif not ncount:
                n, ncount = num, 1
            else:
                mcount -= 1
                ncount -= 1
        # 再次找这两个数字
        mcount = ncount = 0
        for num in nums:
            if num == m:
                mcount += 1
            elif num == n:
                ncount += 1
        N = len(nums)
        return [i for i, c in zip((m, n), (mcount, ncount)) if c > N // 3]

# leetcode submit region end(Prohibit modification and deletion)
