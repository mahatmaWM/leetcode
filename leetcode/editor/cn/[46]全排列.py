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
        self.results = []
        memo = dict.fromkeys(nums, False)  # 保存数字是否使用过

        def backtrack(tmp_res, memo):
            if len(tmp_res) == len(nums):
                self.results.append(tmp_res[:])
                return

            for x in nums:
                if not memo[x]:
                    memo[x] = True
                    tmp_res.append(x)
                    backtrack(tmp_res, memo)
                    tmp_res.pop()
                    memo[x] = False

        backtrack([], memo)
        return self.results


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().permute(nums=[1, 2, 3]))
