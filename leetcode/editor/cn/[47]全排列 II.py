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
# 1、首先将数组排序，这一步很关键，是后面剪枝的基础；
#
# 2、只处理第 1 次遇到的那个数。
# 也就是说下面这种情况 i > 0 and nums[i] == nums[i - 1] and 之前那个数还没有使用，即 marked[i-1] == false 时，
# 第二个数字不取，说明当前的i也不能用，continue

# https://www.jianshu.com/p/e987b8cc1fd7
# 注意参数：
# nums为输入数组
# pre为已经选取的元素列表
# used[i]为第i个元素是否被使用
# res保存最终结果
#
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
        used = [False] * len(nums)
        res = []
        self.backtrack(nums, [], used, res)
        return res

    def backtrack(self, nums, pre, used, res):
        if len(pre) == len(nums):
            # must deep copy
            import copy
            res.append(copy.deepcopy(pre))
            return
        for i in range(len(nums)):
            if not used[i]:
                if i != 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                pre.append(nums[i])
                self.backtrack(nums, pre, used, res)
                used[i] = False
                pre.pop()


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().permuteUnique(nums=[1, 1, 2]))
