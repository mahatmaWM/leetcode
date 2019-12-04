# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例: 
#
# 输入: [1,2,3]
# 输出:
# [
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
# ]
# Related Topics 回溯算法

# 递归解法，把问题拆解成规模更小的问题。
# e=[]
# if(len(nums)==1):
#     return [nums]
# for i in range(len(nums)):
#     q=self.permute(nums[:i]+nums[i+1:])
#     for c in q:
#         e.append([nums[i]]+c)
# return e

# 回溯解法：
# use_dict保留数字使用情况，choosed_nums


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
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

        # results = []
        # len_n = len(nums)
        #
        # def backtrack(choosed_nums, left_nums):
        #     if len(choosed_nums) == len_n:
        #         results.append(choosed_nums)
        #         return
        #     for i in range(len(left_nums)):
        #         x = choosed_nums.copy()
        #         x.append(left_nums[i])
        #         backtrack(x, left_nums[:i] + left_nums[i + 1:])
        #
        # backtrack([], nums)
        # return results

# leetcode submit region end(Prohibit modification and deletion)
