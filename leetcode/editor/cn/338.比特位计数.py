# 给定一个非负整数 num。
# 对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
#
# 示例 1:
#
# 输入: 2
# 输出: [0,1,1]
#
# 示例 2:
#
# 输入: 5
# 输出: [0,1,1,2,1,2]
#
# 进阶:
#
#
# 给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
# 要求算法的空间复杂度为O(n)。
# 你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
#
# Related Topics 位运算 动态规划

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    # 动态规划思路：
    # dp[i]为数字i的二进制表示中1的个数。
    # 奇数的二进制中1的个数=它上一位偶数的二进制中1的个数+1。
    # 偶数的二进制中1的个数=这个偶数除以2后的数二进制1的个数。
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            if i % 2 == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i // 2]
        return dp


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    print(Solution().countBits(num=5))
