#
# @lc app=leetcode.cn id=457 lang=python3
#
# [457] 环形数组循环
#
# https://leetcode-cn.com/problems/circular-array-loop/description/
#
# algorithms
# Medium (34.08%)
# Likes:    33
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 12.3K
# Testcase Example:  '[2,-1,1,2,2]'
#
# 给定一个含有正整数和负整数的环形数组 nums。 如果某个索引中的数 k 为正数，则向前移动 k 个索引。相反，如果是负数 (-k)，则向后移动 k
# 个索引。因为数组是环形的，所以可以假设最后一个元素的下一个元素是第一个元素，而第一个元素的前一个元素是最后一个元素。
#
# 确定 nums 中是否存在循环（或周期）。循环必须在相同的索引处开始和结束并且循环长度 >
# 1。此外，一个循环中的所有运动都必须沿着同一方向进行。换句话说，一个循环中不能同时包括向前的运动和向后的运动。
#
#
# 示例 1：
#
# 输入：[2,-1,1,2,2]
# 输出：true
# 解释：存在循环，按索引 0 -> 2 -> 3 -> 0 。循环长度为 3 。
#
#
# 示例 2：
#
# 输入：[-1,2]
# 输出：false
# 解释：按索引 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
#
#
# 示例 3:
#
# 输入：[-2,1,-1,-2,-2]
# 输出：false
# 解释：按索引 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为按索引 1 -> 2 的运动是向前的运动，而按索引 2 -> 1
# 的运动是向后的运动。一个循环中的所有运动都必须沿着同一方向进行。
#
#
#
# 提示：
#
#
# -1000 ≤ nums[i] ≤ 1000
# nums[i] ≠ 0
# 0 ≤ nums.length ≤ 5000
#
#
#
#
# 进阶：
#
# 你能写出时间时间复杂度为 O(n) 和额外空间复杂度为 O(1) 的算法吗？
#
#

# @lc code=start
class Solution:
    # 选取一个起点，采用两个快慢指针，慢指针一次走一步，快指针一次走两步，
    # 如果两者相遇，说明存在环（注意排除死循环的情况）
    # 然后遍历选每一个起点
    # 这里注意新一次尝试是不会进入之前尝试的点的，所以标记已访问的节点剪枝。
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def nextIndex(i):
            next_step = i + nums[i]
            if next_step >= 0:
                return next_step % len(nums)
            else:
                return (len(nums) + next_step) % len(nums)

        # 选择第i个点为起点，进行新一轮尝试
        for i in range(len(nums)):
            # 遇到之前轮访问过的节点就结束本轮尝试（一定会失败的）
            if nums[i] == 0: continue
            slow = i
            fast = nextIndex(i)

            # 保证快慢指针始终向同一个方向移动
            while nums[slow] * nums[fast] > 0 and nums[fast] * nums[nextIndex(fast)] > 0:
                if slow == fast:
                    # 进入一个局部圈死循环了
                    if slow == nextIndex(slow):
                        break
                    else:
                        return True
                slow = nextIndex(slow)
                fast = nextIndex(nextIndex(fast))

            # 把本轮访问过的节点都置位0
            val = nums[i]
            while val * nums[i] > 0:
                tmp = nextIndex(i)
                nums[i] = 0
                i = tmp

        return False


# @lc code=end
