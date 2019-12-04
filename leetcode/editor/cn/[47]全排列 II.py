#给定一个可包含重复数字的序列，返回所有不重复的全排列。 
#
# 示例: 
#
# 输入: [1,1,2]
#输出:
#[
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
#] 
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


#leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        nums.sort()
        use_dict = dict.fromkeys(nums, False)  # 初始化一个字典，保存数字是否使用过

        def backtrack(results, choosed_nums, use_dict):
            import copy
            if len(choosed_nums) == len(nums):
                # use deepcopy here!!!
                results.append(copy.deepcopy(choosed_nums))
                return

            for x in nums:
                if not use_dict[x]:
                    use_dict[x] = True
                    choosed_nums.append(x)
                    backtrack(results, choosed_nums, use_dict)
                    choosed_nums.pop(x)
                    use_dict[x] = False

        backtrack(results, [], use_dict)
        return results

        
#leetcode submit region end(Prohibit modification and deletion)
