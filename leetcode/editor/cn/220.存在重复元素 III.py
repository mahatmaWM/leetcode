# 给定一个整数数组，判断数组中是否有两个不同的索引 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值最大为 t，并且 i 和 j 之间的差的绝对值最大为 ķ。
#
# 示例 1: 
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
# Related Topics 排序 Ordered Map

# 给定一个数组，判断数组中是否存在两个不同位置i,j的元素，j - i <= k,
# |nums[j] - nums[i]| <= t.

# |nums[j]−nums[i]|<=t⇒
# |nums[j]/t−nums[i]/t|<=1⇒
# |floor(nums[j]/t)−floor(nums[i]/t)|<=1⇒
# floor(nums[j]/t)∈{floor(nums[i]/t−1,floor(nums[i]/t),floor(nums[i]/t)+1}
#
# 如果
# floor(nums[j]/t)∉{floor(nums[i]/t−1,floor(nums[i]/t),floor(nums[i]/t)+1}
# , 则|nums[j]−nums[i]|<=t|nums[j]−nums[i]|<=t 不成立。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        import collections
        dicts = collections.OrderedDict()

        for i in range(len(nums)):
            key = nums[i] / max(1, t)
            for m in (key - 1, key, key + 1):
                if m in dicts and abs(nums[i] - dicts[m]) <= t:
                    return True
            dicts[key] = nums[i]
            if i >= k:
                dicts.popitem(last=False)
        return False

# leetcode submit region end(Prohibit modification and deletion)
