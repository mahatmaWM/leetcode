# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。 
#
# 示例: 
#
# 输入: nums = [1,2,3]
# 输出:
# [
#  [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# Related Topics 位运算 数组 回溯算法

# 递归：
# output = [[]]
# for i in range(len(nums)):
#     for j in range(len(output)):
#         output.append(output[j] + [nums[i]])
# return output

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []

        def backtrack(nums, choose, index):
            self.res.append(choose[:])
            for i in range(index, len(nums)):
                choose.append(nums[i])
                backtrack(nums, choose, i + 1)
                choose.pop()

        backtrack(nums, [], 0)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().subsets(nums = [1,2,3]))
