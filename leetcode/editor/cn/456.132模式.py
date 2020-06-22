# 给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。
# 设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。
#
# 注意：n 的值小于15000。 
#
# 示例1: 
#
# 
# 输入: [1, 2, 3, 4]
#
# 输出: False
#
# 解释: 序列中不存在132模式的子序列。
# 
#
# 示例 2: 
#
# 
# 输入: [3, 1, 4, 2]
#
# 输出: True
#
# 解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
# 
#
# 示例 3: 
#
# 
# 输入: [-1, 3, 2, 0]
#
# 输出: True
#
# 解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
# 
# Related Topics 栈


# 利用来栈来做，思路是我们维护一个栈和一个变量third，其中third就是第三个数字，也是pattern
#   132中的2，栈里面按顺序放所有大于third的数字，也是pattern
#   132中的3，那么我们在遍历的时候，如果当前数字小于third，即pattern
#   132中的1找到了，我们直接返回true即可，因为已经找到了，注意我们应该从后往前遍历数组。
# 如果当前数字大于栈顶元素，那么我们按顺序将栈顶数字取出，赋值给third，然后将该数字压入栈，这样保证了栈里的元素仍然都是大于third的，我们想要的顺序依旧存在，进一步来说，栈里存放的都是可以维持second > third的second值，其中的任何一个值都是大于当前的third值，如果有更大的值进来，那就等于形成了一个更优的second > third的这样一个组合，并且这时弹出的third值比以前的third值更大，为什么要保证third值更大，因为这样才可以更容易的满足当前的值first比third值小这个条件。


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 2:
            return False
        third = float('-inf')
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    third = stack.pop()
            stack.append(nums[i])
        return False

# leetcode submit region end(Prohibit modification and deletion)
