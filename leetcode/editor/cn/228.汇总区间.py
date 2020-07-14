#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
# https://leetcode-cn.com/problems/summary-ranges/description/
#
# algorithms
# Medium (52.60%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 20.7K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# 给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
#
# 示例 1:
#
# 输入: [0,1,2,4,5,7]
# 输出: ["0->2","4->5","7"]
# 解释: 0,1,2 可组成一个连续的区间; 4,5 可组成一个连续的区间。
#
# 示例 2:
#
# 输入: [0,2,3,4,6,8,9]
# 输出: ["0","2->4","6","8->9"]
# 解释: 2,3,4 可组成一个连续的区间; 8,9 可组成一个连续的区间。
#
#

# @lc code=start
class Solution:
    # 双指针遍历数组
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        left, right = 0, 0
        res = []
        while right < len(nums):
            while right < len(nums) - 1 and nums[right] + 1 == nums[right + 1]:
                right += 1
            # 相等说明只有一个数
            if left == right:
                res.append(str(nums[right]))
            else:
                res.append("{}->{}".format(nums[left], nums[right]))

            right = right + 1
            left = right
        return res
# @lc code=end

