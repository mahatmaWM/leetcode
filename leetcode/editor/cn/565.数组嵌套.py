#
# @lc app=leetcode.cn id=565 lang=python3
#
# [565] 数组嵌套
#
# https://leetcode-cn.com/problems/array-nesting/description/
#
# algorithms
# Medium (58.65%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 10.4K
# Testcase Example:  '[5,4,0,3,1,6,2]'
#
# 索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，其中 S[i] = {A[i], A[A[i]],
# A[A[A[i]]], ... }且遵守以下的规则。
#
# 假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]...
# 以此类推，不断添加直到S出现重复的元素。
#
#
#
# 示例 1:
#
# 输入: A = [5,4,0,3,1,6,2]
# 输出: 4
# 解释:
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
#
# 其中一种最长的 S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
#
#
#
#
# 提示：
#
#
# N是[1, 20,000]之间的整数。
# A中不含有重复的元素。
# A中的元素大小在[0, N-1]之间。
#
#
#


# @lc code=start
class Solution:
    # 本质是在数组中找到一个访问环，最大的访问环。
    # 注意，已访问过的节点是不会出现在其他访问环里面的
    def arrayNesting(self, nums: List[int]) -> int:
        next_step_dict = {}
        for i in range(len(nums)):
            next_step_dict[i] = nums[i]
        ans = 0
        start = 0
        flag = 'visited'
        # 尝试每个节点作为开始点
        while start < len(nums):
            curr = start
            temp_ans = 0
            # 找到以当前节点tmp为开始点的最大环
            while next_step_dict[curr] != flag:
                temp_ans += 1
                next_step = next_step_dict[curr]
                next_step_dict[curr] = flag
                curr = next_step
            ans = max(ans, temp_ans)
            start += 1
        return ans


# @lc code=end
