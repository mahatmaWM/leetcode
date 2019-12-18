# 给定一个整数数组 nums，求出数组从索引 i 到 j (i ≤ j) 范围内元素的总和，包含 i, j 两点。
#
# 示例： 
#
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
# 说明: 
#
# 
# 你可以假设数组不可变。 
# 会多次调用 sumRange 方法。 
# 
# Related Topics 动态规划

# 动态规划，使用curr_sum[i]保存从0到i的累积和。则 sumrange(i,j) = curr_sum[j]-curr_sum[i-1


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)

        self.curr_sum = [0] * self.n
        self.curr_sum[0] = nums[0]
        for i in range(1, self.n):
            self.curr_sum[i] = self.curr_sum[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.curr_sum[j]
        else:
            return self.curr_sum[j] - self.curr_sum[i - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# leetcode submit region end(Prohibit modification and deletion)
def main():
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)
    print(obj.sumRange(1,3))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
