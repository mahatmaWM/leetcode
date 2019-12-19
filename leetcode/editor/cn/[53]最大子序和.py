# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例: 
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 
#
# 进阶: 
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。 
# Related Topics 数组 分治算法 动态规划

# 思路：动态规划，空间复杂度为O(n)
# 考虑状态转移方程，当前位置i的最大子序列和 dp[i] = max(dp[i - 1] + nums[i], nums[i])


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        res = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            res = max(dp[i], res)
        return res

    # 动态规划，空间复杂度为O1，不需要保存整个dp数组，只需要pre_max, cur_max就可以了
    def maxSubArray2(self, nums):
        n = len(nums)
        pre_max = nums[0]
        res = nums[0]
        for i in range(1, n):
            cur_max = max(pre_max + nums[i], nums[i])
            res = max(cur_max, res)
            pre_max = cur_max
        return res

    # 分治法
    def maxSubArray1(self, nums):
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)

        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)

        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().maxSubArray1(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
