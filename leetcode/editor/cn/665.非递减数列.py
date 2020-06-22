# 给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。 
#
# 示例 1: 
#
# 
# 输入: [4,2,3]
# 输出: True
# 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
# 
#
# 示例 2: 
#
# 
# 输入: [4,2,1]
# 输出: False
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
# 
#
# 说明: n 的范围为 [1, 10,000]。 
# Related Topics 数组

# 思路：
# 找到i比i-1严格小的个数count，并记录i的位置。
#
# 如果个数为0，返回true；如果个数大于1，返回false；
# 如果个数等于1，则再次判断，这时需要判断位置i位置什么位置：
#   如果位于头尾，则只需要改位置i本身即可，返回true。
#   如果位于中间，则比较是否i+1大于等于i-1
#
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return True

        count = 0
        result = []

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                count += 1
                result.append(i)
        if count == 0:
            return True
        elif count > 1:
            return False
        else:
            i = result[0]
            if i == 1 or i == len(nums) - 1 or nums[i + 1] >= nums[i - 1] or \
                    nums[i - 2] <= nums[i]:
                return True
            else:
                return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().checkPossibility(nums=[1, 2, 3]))
