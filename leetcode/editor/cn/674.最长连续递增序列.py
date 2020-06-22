# 给定一个未经排序的整数数组，找到最长且连续的的递增序列。
#
# 示例 1: 
#
# 
# 输入: [1,3,5,4,7]
# 输出: 3
# 解释: 最长连续递增序列是 [1,3,5], 长度为3。
# 尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。
# 
#
# 示例 2: 
#
# 
# 输入: [2,2,2,2,2]
# 输出: 1
# 解释: 最长连续递增序列是 [2], 长度为1。
# 
#
# 注意：数组长度不会超过10000。 
# Related Topics 数组

# 遍历数组，查看所有的连续递增子序列，并及时记录连续递增子序列的最大值，这里需要注意遍历的范围和变量的初始化。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        res, cur_len = 1, 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                cur_len += 1
                res = max(cur_len, res)
            else:
                cur_len = 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
