#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        # 记录当前位置i可构成的集合最大长度，以及路径
        memo_len, memo_path = [0] * n, [0] * n
        for i in range(n):
            length, pre = 1, i
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if memo_len[j] + 1 > length:
                        length = memo_len[j] + 1
                        pre = j
            memo_len[i] = length
            memo_path[i] = pre

        # 找到最长路径以及起点
        max_len, max_pre = -1, -1
        for i in range(n):
            if memo_len[i] > max_len:
                max_len = memo_len[i]
                max_pre = i

        # 根据起点找出具体路径
        res = list()
        while max_len > 0:
            max_len = max_len -1
            res.append(nums[max_pre])
            max_pre = memo_path[max_pre]
        res.sort()
        return res
# @lc code=end

