# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
# ]
# Related Topics 回溯算法

# 递归解法：
# 对于一个数组，先排序，这是为了有相同的数字的时候可以跳过
# 全排列的思路就是在当前数组中任选一个数作为第一个数，剩下的数字组成一个新的数组，再在该数组中选一个数作为第一个数，依次循环
# 遇到两个或多个相同的数字，直接跳过，不然会有重复
# nums.sort()
# res = []
# def dfs(nums, path):
#     if not nums:
#         res.append(path)
#         return
#     for i in range(len(nums)):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         dfs(nums[:i] + nums[i + 1:], path + [nums[i]])
# dfs(nums, [])
# return res

# 回溯解法：
# 求解关键：找到重复的原因，对树进行剪枝。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        memo = [False] * len(nums)
        self.res = []

        # 路径：记录在 tmp_res 中
        # 选择列表：nums 中不存在于 memo 的那些元素
        # 结束条件：nums 中的元素全都在 tmp_res 中出现
        def backtrack(tmp_res, memo):
            if len(tmp_res) == len(nums):
                self.res.append(tmp_res[:])
                return
            for i in range(len(nums)):
                if not memo[i]:
                    # 有重复元素时的剪枝条件：元素相等时，前一个已被用则当前的就不用
                    if i > 0 and nums[i] == nums[i - 1] and memo[i - 1]:
                        continue

                    memo[i] = True
                    tmp_res.append(nums[i])
                    backtrack(tmp_res, memo)
                    memo[i] = False
                    tmp_res.pop()

        backtrack([], memo)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().permuteUnique(nums=[1, 1, 2]))
