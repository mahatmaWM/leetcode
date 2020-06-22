# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
#
# 说明：解集不能包含重复的子集。 
#
# 示例: 
#
# 输入: [1,2,2]
# 输出:
# [
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
# ]
# Related Topics 数组 回溯算法

# 回溯算法，时间复杂度：O(n!)，解空间大小为n！
# 先排序是为了剪枝，j > i and nums[j] == nums[j - 1] 跳过，此步为了去除重复的子集。

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        self.res = []

        def back_track(start, tmp_res):
            self.res.append(tmp_res[:])
            if start == n:
                return
            for j in range(start, n):
                if j > start and nums[j] == nums[j - 1]:
                    continue
                tmp_res.append(nums[j])
                back_track(j + 1, tmp_res)
                tmp_res.pop()

        back_track(0, [])
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().subsetsWithDup(nums=[1, 2, 2]))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
