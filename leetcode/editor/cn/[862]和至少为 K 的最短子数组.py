# 返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
#
# 如果没有和至少为 K 的非空子数组，返回 -1 。 
#
# 
#
# 
# 
#
# 示例 1： 
#
# 输入：A = [1], K = 1
# 输出：1
# 
#
# 示例 2： 
#
# 输入：A = [1,2], K = 4
# 输出：-1
# 
#
# 示例 3： 
#
# 输入：A = [2,-1,2], K = 3
# 输出：3
# 
#
# 
#
# 提示： 
#
# 
# 1 <= A.length <= 50000 
# -10 ^ 5 <= A[i] <= 10 ^ 5 
# 1 <= K <= 10 ^ 9 
# 
# Related Topics 队列 二分查找

# 思路：
# 本题涉及到求任意i j之间的元素和，需要用到的加速技巧是数组的前缀和。
# 另外有了前缀和，如果采用left right两个指针来模拟变长的滑动窗口，两个for循环复杂度是On2
# 一般是用队列来模拟滑动窗口，队尾模拟right指针的入队操作，队首模拟left指针的出队操作。
# 这里入队的时候是有优化空间的，见代码。

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        # 第一步，组织前缀和
        pre_sum = [0]
        for a in A:
            pre_sum.append(pre_sum[-1] + a)
        res = len(pre_sum) + 1

        import collections
        dq = collections.deque()
        # 第二步，利用dq来模拟滑动窗口
        for i in range(len(pre_sum)):
            # 这个while是模拟数组中有负数时，其实是可以优化加速的，
            # 但如果没有负数的场景，这里是没有用的
            while dq and pre_sum[i] <= pre_sum[dq[-1]]:
                dq.pop()
            # 这个while就是正常的队列头判断
            while dq and pre_sum[i] - pre_sum[dq[0]] >= K:
                res = min(res, i - dq[0])
                dq.popleft()
            dq.append(i)
        return res if res <= len(A) else -1


# leetcode submit region end(Prohibit modification and deletion)
def main():
    print(Solution().shortestSubarray(A=[1, 2], K=4))


if __name__ == "__main__":
    import time

    start = time.clock()
    main()
    print("%s sec" % (time.clock() - start))
