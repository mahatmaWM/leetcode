#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (44.54%)
# Likes:    465
# Dislikes: 0
# Total Accepted:    55.1K
# Total Submissions: 123.7K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#
#
# 说明 :
#
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
#
#
#

# @lc code=start
class Solution:
    # 思路：借助哈希表保存累加和curr_sum及出现的次数。
    # 若累加和curr_sum - k在哈希表中存在，则说明存在一段连续序列使得和为k。
    # 则之前的累加和中，curr_sum−k 出现的次数即为有多少种子序列使得累加和为sum-k。
    def subarraySum(self, nums: List[int], k: int) -> int:
        import collections
        hash = collections.defaultdict(int)
        # 为了第一次累加到k时的连续子数组有预设值1
        hash[0] = 1
        curr_sum = 0
        count = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            hash[curr_sum] += 1
            if (curr_sum - k) in hash: count += hash[curr_sum - k]
        return count
# @lc code=end

