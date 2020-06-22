# 给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
#
# 如果数组元素个数小于 2，则返回 0。 
#
# 示例 1: 
#
# 输入: [3,6,9,1]
# 输出: 3
# 解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
#
# 示例 2: 
#
# 输入: [10]
# 输出: 0
# 解释: 数组元素个数小于 2，因此返回 0。
#
# 说明: 
#
# 
# 你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。 
# 请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。 
# 
# Related Topics 排序

# 思路是采用桶排序的方法。
# 首先，求随机数组中的最大元素，最小元素，为线性时间复杂度；
# 然后，在最大元素和最小元素之间，分配（N-1）个间隔，即为size=N个桶（bucket）。
# 每个桶为一个有序实数对（None,None），将每个数依次往目标桶里塞。
# 其中，桶的上下界若已有元素（存在一个桶对应多个元素），则只需计算新元素与下界的较小值，同时计算其与上界的较大值，并将该最值作为新下界/上界即可；
# 最后，计算每个桶的下界与下一个桶的上界的差值。差值最大值即为最大间隔。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        a, b = min(nums), max(nums)
        size = (b - a) // (len(nums) - 1) or 1
        bucket = [[None, None] for _ in range((b - a) // size + 1)]
        for n in nums:
            b = bucket[(n - a) // size]
            b[0] = n if b[0] is None else min(b[0], n)
            b[1] = n if b[1] is None else max(b[1], n)
        bucket = [b for b in bucket if b[0] is not None]
        return max(
            bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    a = Solution()
    print(a.maximumGap(nums=[3]))
