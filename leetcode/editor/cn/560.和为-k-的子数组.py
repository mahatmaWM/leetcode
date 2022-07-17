#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
class Solution:
    # 参考前缀和计算的思路，借助哈希表保存pre_sum以及其出现的次数
    # 如果pre_sum-k也在哈希表中，则说明存在一段连续序列使得和为k，将其个数累加。
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {}
        pre_sum = 0
        res = 0
        for num in nums:
            pre_sum += num
            if pre_sum == k:
                res += 1
            if pre_sum - k in hash:
                res += hash[pre_sum - k]
            hash[pre_sum] = hash.get(pre_sum, 0) + 1
        return res
# @lc code=end

