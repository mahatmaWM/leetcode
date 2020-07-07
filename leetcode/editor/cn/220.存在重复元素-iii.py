#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#
# https://leetcode-cn.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (26.22%)
# Likes:    182
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 71.4K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# 在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j
# 的差的绝对值也小于等于 ķ 。
#
# 如果存在则返回 true，不存在返回 false。
#
#
#
# 示例 1:
#
# 输入: nums = [1,2,3,1], k = 3, t = 0
# 输出: true
#
# 示例 2:
#
# 输入: nums = [1,0,1,1], k = 1, t = 2
# 输出: true
#
# 示例 3:
#
# 输入: nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出: false
#
#


# @lc code=start
class Solution:
    # 给定一个数组，判断数组中是否存在两个不同位置i,j的元素，j-i<=k, |nums[j]-nums[i]|<=t.
    # 本题需要推导技巧：
    # |nums[j]−nums[i]|<=t 推导出 |nums[j]/t−nums[i]/t|<=1 推导出 |floor(nums[j]/t)−floor(nums[i]/t)|<=1
    # 所以 floor(nums[j]/t) 一定属于 {floor(nums[i]/t−1,floor(nums[i]/t),floor(nums[i]/t)+1}
    #
    # 如果 floor(nums[j]/t) 不属于 {floor(nums[i]/t−1,floor(nums[i]/t),floor(nums[i]/t)+1}
    # 则 |nums[j]−nums[i]|<=t 不成立。

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0: return False

        import collections
        dicts = collections.OrderedDict()
        import math
        for i in range(len(nums)):
            key = math.floor(nums[i] / max(1, t))
            for m in (key - 1, key, key + 1):
                if m in dicts and abs(nums[i] - dicts[m]) <= t: return True
            dicts[key] = nums[i]
            if i >= k: dicts.popitem(last=False)
        return False


# @lc code=end
