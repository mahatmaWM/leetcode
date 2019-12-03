# 给出一个整数数组 A 和一个查询数组 queries。
#
# 对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index] 上。然后，第 i 次查询的答案是 A 中偶数值的和。 
#
# （此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。） 
#
# 返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。 
#
# 
#
# 示例： 
#
# 输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# 输出：[8,6,2,4]
# 解释：
# 开始时，数组为 [1,2,3,4]。
# 将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
# 将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
# 将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
# 将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
# 
#
# 
#
# 提示： 
#
# 
# 1 <= A.length <= 10000 
# -10000 <= A[i] <= 10000 
# 1 <= queries.length <= 10000 
# -10000 <= queries[i][0] <= 10000 
# 0 <= queries[i][1] < A.length 
# 
# Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sumOfEven = sum(num for num in A if not num % 2)
        result = []

        for item in queries:
            value = item[0]
            index = item[1]
            newvalue = A[index] + value

            if not A[index] % 2 and not newvalue % 2:  # even and even
                sumOfEven += value
            elif not A[index] % 2 and newvalue % 2:  # even and odd
                sumOfEven -= A[index]
            elif A[index] % 2 and not newvalue % 2:  # odd and even
                sumOfEven += newvalue

            result.append(sumOfEven)
            A[index] = newvalue

        return result

# leetcode submit region end(Prohibit modification and deletion)
