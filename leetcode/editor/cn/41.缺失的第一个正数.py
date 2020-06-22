# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1: 
#
# 输入: [1,2,0]
# 输出: 3
# 
#
# 示例 2: 
#
# 输入: [3,4,-1,1]
# 输出: 2
# 
#
# 示例 3: 
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 
#
# 说明: 
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。 
# Related Topics 数组

# 思路1：
# 数组长度为n，说明里面没有出现的最小正整数一定是小于n的，那么定义一个长度为n的hash记录一遍数组，在递增遍历整数n以内的数字，遇到及返回结果
# 这种方法的空间为O（n）

# 思路2：
# 常数空间的还没有想到



# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        n = len(nums)
        hashed = [0] * n
        for i in range(n):
            if 0 < nums[i] <= n:
                hashed[nums[i] - 1] += 1

        for i in range(n):
            if hashed[i] == 0:
                return i + 1
        return n + 1

    def firstMissingPositive2(self, nums):
        if not nums:
            return 1

        n = len(nums)
        hashed = [0] * n
        for i in range(n):
            if 0 < nums[i] <= n:
                hashed[nums[i] - 1] += 1

        for i in range(n):
            if hashed[i] == 0:
                return i + 1
        return n + 1

# leetcode submit region end(Prohibit modification and deletion)
