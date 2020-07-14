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
class Solution1:
    # 暴力枚举O(N*k)，K太大时会超时
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0: return False
        for i in range(len(nums)):
            j = i + 1
            while j < len(nums) and j < i + k + 1:
                if abs(nums[j] - nums[i]) <= t: return True
                j += 1
        return False


from sortedcontainers import SortedSet


class Solution:
    # 与219题的区别，nums[i] 和 nums[j]不再是相等，而是差值小于等于t
    # 所以219题用hash O(1)时间判断元素的思路不能用，上面在窗口内判断元素是线性时间，所以会超时
    # 想办法加速元素判断，如果能O(logK)判断元素，平衡树结构合适。
    #
    # java的treeSet数据结构，其floor()方法和ceiling()方法可以在logK时间内找到最靠近的元素
    # python中没有类似的treeSet数据结构，使用SortedSet替换，用其二分查找最靠近的元素
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0: return False
        sort_set = SortedSet([])
        sort_set.add(nums[0])
        for i in range(1, len(nums)):
            insert_index = sort_set.bisect_left(nums[i])
            # 插入位置分别为最左端、最右端、中间三种情况(但是最右端时涉及到len，也是线性时间)
            if insert_index == 0:
                if abs(nums[i] - sort_set[insert_index]) <= t: return True
            elif insert_index == len(sort_set):
                if abs(nums[i] - sort_set[insert_index - 1]) <= t: return True
            else:
                if abs(nums[i] - sort_set[insert_index - 1]) <= t or abs(nums[i] - sort_set[insert_index]) <= t:
                    return True
            sort_set.add(nums[i])
            if i >= k: sort_set.remove(nums[i - k])
        return False


# @lc code=end
