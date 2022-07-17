#
# @lc app=leetcode.cn id=491 lang=python3
#
# [491] 递增子序列
#

# @lc code=start
class Solution:
    # 思路：相当于是一个回溯递归搜索路径的问题，不停的尝试往结果里面添加可能的元素
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        import copy

        # 从nums中挑选，当前的挑选结果为tmp_path
        # 当前在nums中准备挑选位置为start，上一次挑选的数字为pre_num
        def dfs(nums, tmp_path, start, pre_num):
            nonlocal res
            if len(tmp_path) > 1: res.append(copy.deepcopy(tmp_path))
            memo = set()
            for i in range(start, len(nums)):
                # 将要添加的num[i]更小 或者 将要第二次添加num[i] (会与第一次挑选的形成一样的结果)
                if nums[i] < pre_num or nums[i] in memo: continue
                memo.add(nums[i])
                tmp_path.append(nums[i])
                dfs(nums, tmp_path, i + 1, nums[i])
                tmp_path.pop()

        dfs(nums, [], 0, float('-inf'))
        return res
# @lc code=end
