#给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。 
#
# 示例: 
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
#输出: 6
#解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
#
# 进阶: 
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
# Related Topics 数组 分治算法 动态规划

# 一次遍历数组，对数组进行累加的操作。
# 需要维护两个变量，分别为局部最优curr_sum，和全局最优max_sum。
# 遍历数组时，从第一个元素开始累加，并赋值给局部最优curr_sum，当局部最优为负数时，可放弃对应子串，重置局部最优为0。
# 每一次计算出新的局部最优时，与当前全局最优比较，将较大的值付给全局最优。


#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = 0
        max_sum = -2147483647

        for i in range(0, len(nums)):
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = curr_sum + nums[i]
            max_sum = max(curr_sum, max_sum)

        return max_sum
        
#leetcode submit region end(Prohibit modification and deletion)
