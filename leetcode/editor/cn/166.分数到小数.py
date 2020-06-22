# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
#
# 如果小数部分为循环小数，则将循环的部分括在括号内。 
#
# 示例 1: 
#
# 输入: numerator = 1, denominator = 2
# 输出: "0.5"
# 
#
# 示例 2: 
#
# 输入: numerator = 2, denominator = 1
# 输出: "2"
#
# 示例 3: 
#
# 输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
# 
# Related Topics 哈希表 数学

# 思路：输入分母和分子，然后把结果返回，如果结果有循环把循环部分用括号括起来。
# 1）思考存储两个列表，一个是余数列表numeratorlist ，一个是值的列表valuelist
# 2）当每次除完，把余数*10再当做除数除以分母（如果出现相同的除数，则代表要开始进行循环了，记录此时的index）
# 3）每次除完的值放在值的列表里面，根据index插入括号
# 4）使用sign来记录符号，全部化成正数进行除法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1 if numerator * denominator >= 0 else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        numeratorlist = []
        valuelist = []
        indexValue = -1

        # 第一次除，如果能整除，则返回结果
        div, mod = divmod(numerator, denominator)
        if mod == 0:
            return str(div * sign)

        # 如果不能整除，则开始余数*10的模拟过程，并记录余数是否之前出现过（循环的情况）
        valuelist.append(div)
        valuelist.append(".")
        mod = mod * 10
        while True:
            numeratorlist.append(mod)
            div, mod = divmod(mod, denominator)
            valuelist.append(div)
            mod = mod * 10
            if mod in numeratorlist:
                indexValue = numeratorlist.index(mod) + 2
                break
            if mod == 0:
                break

        if indexValue != -1:
            valuelist.append(")")
            valuelist.insert(indexValue, "(")

        if sign < 0:
            valuelist.insert(0, "-")
        resultStr = ''.join(map(str, valuelist))
        return resultStr

# leetcode submit region end(Prohibit modification and deletion)
