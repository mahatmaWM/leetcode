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

# @lc code=start
class Solution:
    # 摩尔投票法
    def majorityElement(self, nums: List[int]) -> int:
        m = None
        mor_cnt = 0
        # 遇到相同的数就+1，不同的数就-1
        for num in nums:
            if not mor_cnt:
                m, mor_cnt = num, 1
            elif num == m:
                mor_cnt += 1
            else:
                mor_cnt -= 1
        # 再次找这个数字
        mor_cnt = 0
        for num in nums:
            if num == m: mor_cnt += 1
        N = len(nums)
        return m if mor_cnt > N // 2 else 0
# @lc code=end

