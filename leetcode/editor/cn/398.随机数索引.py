#
# @lc app=leetcode.cn id=398 lang=python3
#
# [398] 随机数索引
#
# https://leetcode-cn.com/problems/random-pick-index/description/
#
# algorithms
# Medium (61.36%)
# Likes:    56
# Dislikes: 0
# Total Accepted:    5.3K
# Total Submissions: 8.6K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# 给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。
#
# 注意：
# 数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。
#
# 示例:
#
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
# solution.pick(3);
#
# // pick(1) 应该返回 0。因为只有nums[0]等于1。
# solution.pick(1);
#
# 思路：
# （1）计数器count记录target值个数
# （2）以1/count的概率抽样
#

# @lc code=start
class Solution:
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, count) < 1:  # 以某一概率(1/count)抽样
                    res = i
                count += 1
        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end

