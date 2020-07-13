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
# Total pre_sumepted:    55.1K
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
    # 参考前缀和计算的思路，借助哈希表保存curr_sum以及其出现的次数
    # 如果curr_sum-k也在哈希表中，则说明存在一段连续序列使得和为k，将其个数累加。
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {}
        pre_sum = 0
        res = 0
        for num in nums:
            pre_sum += num
            if pre_sum == k: res += 1
            if pre_sum - k in hash: res += hash[pre_sum - k]
            hash[pre_sum] = hash.get(pre_sum, 0) + 1
        return res


class Solution1:
    # 使用前缀和，然后再暴力枚举，O(N2)会超时
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt, n = 0, len(nums)
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + nums[i - 1]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                if pre[j] - pre[i - 1] == k: cnt += 1
        return cnt


# @lc code=end
