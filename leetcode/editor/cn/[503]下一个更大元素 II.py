# 给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），输出每个元素的下一个更大元素。
# 数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
# 如果不存在，则输出 -1。
#
# 示例 1: 
#
# 
# 输入: [1,2,1]
# 输出: [2,-1,2]
# 解释: 第一个 1 的下一个更大的数是 2；
# 数字 2 找不到下一个更大的数；
# 第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
# 
#
# 注意: 输入数组的长度不会超过 10000。 
# Related Topics 栈


# 与496类似，这里出现循环寻找的情况，所以数组我们可能遍历两次。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [-1] * len(nums)
        stack = []
        for i in range(len(nums)) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res

# leetcode submit region end(Prohibit modification and deletion)
