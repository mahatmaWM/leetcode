#
# @lc app=leetcode.cn id=853 lang=python3
#
# [853] 车队
#
# https://leetcode-cn.com/problems/car-fleet/description/
#
# algorithms
# Medium (35.80%)
# Likes:    64
# Dislikes: 0
# Total Accepted:    4.8K
# Total Submissions: 13.4K
# Testcase Example:  '12\n[10,8,0,5,3]\n[2,4,1,1,3]'
#
# N  辆车沿着一条车道驶向位于 target 英里之外的共同目的地。
#
# 每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。
#
# 一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。
#
# 此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
#
# 车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
#
# 即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
#
#
#
# 会有多少车队到达目的地?
#
#
#
# 示例：
#
# 输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# 输出：3
# 解释：
# 从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
# 从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
# 从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
# 请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。
#
#
#
# 提示：
#
#
# 0 <= N <= 10 ^ 4
# 0 < target <= 10 ^ 6
# 0 < speed[i] <= 10 ^ 6
# 0 <= position[i] < target
# 所有车的初始位置各不相同。
#
#
#

# @lc code=start
class Solution:
    # 按照汽车所在位置逆序排序，然后计算每辆车到target位置的时间。
    # 这种遍历连续区间，且要比较连续元素大小的场景，都可以使用一个栈来保存最终结果。
    # 如果当前time比栈顶的时间小，说明当前车辆是可以追上前面那辆栈顶的车，可以合并为一个车队，否则当前车辆单独作为一个车队。
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(pos, spe) for pos, spe in zip(position, speed)]
        sorted_cars = sorted(cars, reverse=True)
        times = [(target - pos) / spe for pos, spe in sorted_cars]
        stack = []
        for time in times:
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]: stack.append(time)
        return len(stack)

# @lc code=end

