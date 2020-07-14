#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (60.13%)
# Likes:    242
# Dislikes: 0
# Total Accepted:    35.7K
# Total Submissions: 59.4K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。
#
# 示例:
#
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#



# @lc code=start
class Solution:
    # 回溯算法，时间复杂度：O(n!)，解空间大小为n！
    # 先排序是为了剪枝，j > i and nums[j] == nums[j - 1] 跳过，此步为了去除重复的子集。
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def back_track(start, tmp_res):
            nonlocal res
            res.append(copy.deepcopy(tmp_res))
            if start == len(nums): return
            for j in range(start, len(nums)):
                if j > start and nums[j] == nums[j - 1]: continue
                tmp_res.append(nums[j])
                back_track(j + 1, tmp_res)
                tmp_res.pop()

        back_track(0, [])
        return res


# @lc code=end
