# 冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
#
# 现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。 
#
# 所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。 
#
# 说明: 
#
# 
# 给出的房屋和供暖器的数目是非负数且不会超过 25000。 
# 给出的房屋和供暖器的位置均是非负数且不会超过10^9。 
# 只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。 
# 所有供暖器都遵循你的半径标准，加热的半径也一样。 
# 
#
# 示例 1: 
#
# 
# 输入: [1,2,3],[2]
# 输出: 1
# 解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。
# 
#
# 示例 2: 
#
# 
# 输入: [1,2,3,4],[1,4]
# 输出: 1
# 解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
# 
# Related Topics 二分查找
#
# 1、对houses, heaters分别进行排序
# 2、对于每一个房屋，找到距离这个房屋最近的暖器，注意这里用i,i+1两个heater的中值与house对比，并算出距离dist；
# 3、对于所有房屋计算出的dist，取其中的最大值

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        heater_index = r = 0
        for house_pos in sorted(houses):
            # find a heater cloest to house_pos
            while house_pos >= sum(heaters[heater_index:heater_index + 2]) / 2.:
                heater_index += 1
            r = max(r, abs(heaters[heater_index] - house_pos))
        return r

# leetcode submit region end(Prohibit modification and deletion)
