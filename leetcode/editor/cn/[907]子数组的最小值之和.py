# 给定一个整数数组 A，找到 min(B) 的总和，其中 B 的范围为 A 的每个（连续）子数组。
#
# 由于答案可能很大，因此返回答案模 10^9 + 7。 
#
# 
#
# 示例： 
#
# 输入：[3,1,2,4]
# 输出：17
# 解释：
# 子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。
# 最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
#
# 
#
# 提示： 
#
# 
# 1 <= A <= 30000 
# 1 <= A[i] <= 30000 
# 
#
# 
# Related Topics 栈 数组

# https://blog.csdn.net/qq_17550379/article/details/86548585

# 思路：
# 针对 [3,1,2,4] 元素，比如包含元素1的子数组，其最小值一定是1，一共有2*3个子数组。1前面1个元素，1后面2个元素，(1+1)*(2+1)
# 那么现在的问题就是怎么计算左边的最大长度和右边的最大长度？可以通过单调栈。使用什么样的单调栈呢？
# 不难想到我们需要求左边第一个小于当前元素的位置和右边第一个小于当前元素的位置，这两个位置就是我们能找到的最大值，这就需要维护一个严格单调递增的栈。
# 注意一头一尾添加一个为0的元素

# 这个问题还有一个陷阱就是当包含重复元素的时候我们怎么计算？例如[71,55,82,55]，此时有两种策略
# nextList包含重复元素，preList不包含
# nextList不包含重复元素，preList包含
# 使用的是第二种策略

# 这里使用递增栈（栈低到栈顶依次递增）

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        A = [0] + A + [0]
        stack = list()
        next_smaller = [-1] * len(A)
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                pre_index = stack.pop()
                next_smaller[pre_index] = i - pre_index
            stack.append(i)

        stack.clear()
        pre_smaller = [-1] * len(A)
        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                stack.pop()
            if stack:
                pre_smaller[i] = i - stack[-1]
            stack.append(i)

        return sum(
            i * j * k for i, j, k in zip(A, next_smaller, pre_smaller)) % (
                           10 ** 9 + 7)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().sumSubarrayMins(A=[3, 1, 2, 4]))
