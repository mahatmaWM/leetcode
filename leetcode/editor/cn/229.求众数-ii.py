#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#
# https://leetcode-cn.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (43.27%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 40.9K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。
#
# 说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: [3]
#
# 示例 2:
#
# 输入: [1,1,1,3,3,2,2,2]
# 输出: [1,2]
#
#


# @lc code=start
class Solution:
    # 思路：与169题一样，都属于摩尔投票法的使用。
    # 本题的结果可能有0个、1个、2个。
    def majorityElement(self, nums: List[int]) -> List[int]:
        mor1, mor2, mor1_cnt, mor2_cnt = None, None, 0, 0
        for num in nums:
            if mor1_cnt == 0 and num != mor2:
                mor1 = num
                mor1_cnt += 1
            elif mor2_cnt == 0 and num != mor1:
                mor2 = num
                mor2_cnt += 1
            else:
                if mor1 == num: mor1_cnt += 1
                elif mor2 == num: mor2_cnt += 1
                else:
                    mor1_cnt -= 1
                    mor2_cnt -= 1

        # 确认这两个数字
        mor1_cnt, mor2_cnt = 0, 0
        for num in nums:
            if num == mor1: mor1_cnt += 1
            elif num == mor2: mor2_cnt += 1
        return [i for i, c in zip((mor1, mor2), (mor1_cnt, mor2_cnt)) if c > len(nums) // 3]


# @lc code=end
