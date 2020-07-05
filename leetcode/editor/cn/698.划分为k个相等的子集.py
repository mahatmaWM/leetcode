#
# @lc app=leetcode.cn id=698 lang=python3
#
# [698] 划分为k个相等的子集
#
# https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (41.88%)
# Likes:    175
# Dislikes: 0
# Total Accepted:    11.4K
# Total Submissions: 27.1K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# 给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
#
# 示例 1：
#
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
#
#
#
# 提示：
#
#
# 1 <= k <= len(nums) <= 16
# 0 < nums[i] < 10000
#
#
#


# @lc code=start
class Solution:

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 不能被整除一定不行
        target, rem = divmod(sum(nums), k)
        if rem: return False

        # 排序数组，处理特殊情况
        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        # 递归
        def search(groups):
            if not nums: return True
            v = nums.pop()
            # 尝试将v放入groups的每一个集合中
            for group_i, group_v in enumerate(groups):
                if group_v + v <= target:
                    groups[group_i] += v
                    if search(groups): return True
                    groups[group_i] -= v
            nums.append(v)
            return False

        return search([0] * k)


# @lc code=end
