#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (63.54%)
# Likes:    629
# Dislikes: 0
# Total Accepted:    176.3K
# Total Submissions: 277.4K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
#
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#
#
#


# @lc code=left
class Solution1:
    # 直接统计出现次数
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for k, v in counter.items():
            if v > len(nums) // 2: return k


class Solution2:
    # 排序后，中位数既是结果，O(NlogN)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


class Solution3:
    # 堆，不知为啥超级慢
    def majorityElement(self, nums: List[int]) -> int:
        return heapq.nlargest(len(nums) // 2 + 1, nums)[-1]


class Solution:
    # 分治法，左右分别求众数，最后判断正确的众数，O(NlogN)
    def majorityElement(self, nums: List[int]) -> int:

        def findNum(nums):
            if len(nums) == 1: return nums[0]
            mid = len(nums) // 2
            left_num = findNum(nums[0:mid])
            right_num = findNum(nums[mid:])
            if left_num == right_num: return left_num
            return left_num if nums.count(left_num) >= nums.count(right_num) else right_num

        return findNum(nums)


class Solution5:
    # 摩尔投票法
    def majorityElement(self, nums: List[int]) -> int:
        mor, mor_cnt = None, 0
        for num in nums:
            # 发现一个新摩尔
            if mor_cnt == 0:
                mor, mor_cnt = num, 1
            # 遇到相同的数就+1，不同的数就-1
            elif num == mor:
                mor_cnt += 1
            else:
                mor_cnt -= 1

        # 确认mor
        mor_cnt = 0
        for num in nums:
            if num == mor: mor_cnt += 1
        return mor if mor_cnt > len(nums) // 2 else 0


# @lc code=right
