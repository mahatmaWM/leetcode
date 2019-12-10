# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
#
# 示例: 
#
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
#
# 说明: 
#
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。 
# 你算法的时间复杂度应该为 O(n2) 。 
# 
#
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗? 
# Related Topics 二分查找 动态规划

# 思路一：动态规划，复杂度为On2。
# 我们index位置的函数值，由index之前的max(f(j)) (j < index)决定，并且nums[index] > nums[j]。
# 为什么呢？因为一旦之前序列的最后一个值nums[j]大于现在即将变为整个序列最后一个元素的nums[index]，整个序列不再保持上升趋势。
# 转移方程为：f(i) = 1 + max(f(j) if nums[i] > nums[j]) 且(i > j)
# 这个方法设计i，j两次数组遍历。

# 思路二：二分查找 Onlogn。
# 我们建立一个临时数组tmp（用于存放一组最长上升子列），首先将nums[0]插入其中，然后遍历nums[1:]
#
# 如果遍历到的元素val <= tmp[0]，我们更新tmp[0]=val（也就是遍历到的元素比最长上升子序列中的最小元素小，我们通过贪心的策略，当然是越小越好，所以替换之前元素）
# 如果tmp[0] < val <= tmp[-1]，我们通过二分搜索法找到第一个>=val的元素位置，然后用val替换掉它（和上面的做法相同）
# 如果tmp[-1] < val，我们更新tmp.append(val)（也就是新加入的元素比最长上升子序列中的最后一个元素大，那么必然构成解）
#
# 题目中的例子为例，我们建立一个tmp=[10]。

# 然后发现10 < 9，所以 tmp:[9]
# 然后考虑9 < 2，所以 tmp:[2]
# 然后考虑2 < 5，所以 tmp:[2 5]
# 接着往后5 > 3 && 2 < 5，所以 tmp:[2 3]
# 而3 < 7，所以 tmp:[2 3 7]
# 接着7 < 101，所以 tmp:[2 3 7 101]
# 然后2 < 18 < 101，所以 tmp:[2 3 7 18]
# 对应lengthOfLIS1


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        len_nums = len(nums)
        mem = [1] * len_nums
        result = 1
        for i in range(1, len_nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    mem[i] = max(mem[i], 1 + mem[j])

            result = max(result, mem[i])

        return result

    def lengthOfLIS1(self, nums):
        import bisect
        mem = list()
        n = len(nums)
        for i in range(n):
            index = bisect.bisect_left(mem, nums[i])
            if len(mem) == index:
                mem.append(nums[i])
            else:
                mem[index] = nums[i]
        return len(mem)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().lengthOfLIS(nums=[10, 9, 2, 5, 3, 7, 101, 18]))
