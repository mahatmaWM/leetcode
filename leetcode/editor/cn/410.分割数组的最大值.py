#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#
# https://leetcode-cn.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (43.21%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    6.9K
# Total Submissions: 16K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# 给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
#
# 注意:
# 数组长度 n 满足以下条件:
#
#
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
#
#
# 示例:
#
#
# 输入:
# nums = [7,2,5,10,8]
# m = 2
#
# 输出:
# 18
#
# 解释:
# 一共有四种方法将nums分割为2个子数组。
# 其中最好的方式是将其分为[7,2,5] 和 [10,8]，
# 因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
#
# 解法：
# 最小和必然落在 [max(nums), sum(nums)] 之间
# 我们可以使用二分来进行查找
#


# @lc code=start
class Solution:
    # 由于题目的返回要求：返回最小和的值
    # 最小和必然落在 [max(nums), sum(nums)] 之间
    # 我们可以使用二分来进行查找
    def splitArray(self, nums: List[int], m: int) -> int:

        def splitArrayCnt(sum_flag):
            count = 0
            sub_sum = 0
            for i in range(len(nums)):
                sub_sum += nums[i]
                if sub_sum > sum_flag:
                    count += 1
                    sub_sum = nums[i]
            # 末尾还有一个子数组我们没有统计
            count += 1
            return count

        # 淘汰算法
        # 我们由前向后对nums进行划分，使其子数组和 <= mid，然后统计满足条件的数组数量
        # 若我们选的sum值过小，则满足条件的数量 > m，目标值应落在 [mid+1, high)
        # 若我们选的sum值过大，则满足条件的数量 < m，目标值应落在 [low, mid)
        low, high = max(nums), sum(nums) + 1
        while low < high:
            mid = low + (high - low) // 2
            count = splitArrayCnt(mid)
            if count > m:
                low = mid + 1
            else:
                high = mid
        return low


# @lc code=end
