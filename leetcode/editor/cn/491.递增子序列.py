# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。
#
# 示例:
#
#
# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
#
# 说明:
#
#
# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
#
# Related Topics 深度优先搜索

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(nums, tmp_path, loc, length, pre_num):
            nonlocal res
            if length > 1: res.append(tmp_path[:])
            memo = set()
            for i in range(loc, len(nums)):
                # 将要添加的num[i]更小 或者 将要第二次添加num[i]
                if nums[i] < pre_num or nums[i] in memo: continue
                memo.add(nums[i])
                tmp_path.append(nums[i])
                dfs(nums, tmp_path, i + 1, length + 1, nums[i])
                tmp_path.pop()

        dfs(nums, [], 0, 0, float('-inf'))
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    print(Solution().findSubsequences(nums=[4, 6, 7, 7]))
