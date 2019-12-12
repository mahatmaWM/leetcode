# 验证给定的字符串是否可以解释为十进制数字。
#
# 例如: 
#
# "0" => true 
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# " -90e3 " => true
# " 1e" => false
# "e3" => false
# " 6e-1" => true
# " 99e2.5 " => false
# "53.5e93" => true
# " --6 " => false
# "-+3" => false
# "95a54e53" => false
#
# 说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表： 
#
# 
# 数字 0-9 
# 指数 - "e" 
# 正/负号 - "+"/"-" 
# 小数点 - "." 
# 
#
# 当然，在输入中，这些字符的上下文也很重要。 
#
# 更新于 2015-02-10: 
# C++函数的形式已经更新了。如果你仍然看见你的函数接收 const char * 类型的参数，请点击重载按钮重置你的代码。
# Related Topics 数学 字符串


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        state = [
            {},
            # 状态1,空格(后面可以接空格、符号、数字、小数点)
            {"blank": 1, "sign": 2, "digit": 3, ".": 4},
            # 状态2,发现符号位(后面跟数字、小数点)
            {"digit": 3, ".": 4},
            # 状态3,数字(一直循环到非数字)
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            # 状态4,小数点(后面只有紧接数字)
            {"digit": 5},
            # 状态5,小数点之后(后面只能为数字,e,或者以空格结束)
            {"digit": 5, "e": 6, "blank": 9},
            # 状态6,发现e(后面只能符号位, 和数字)
            {"sign": 7, "digit": 8},
            # 状态7,e之后(只能为数字)
            {"digit": 8},
            # 状态8,e之后的数字后面(只能为数字或者以空格结束)
            {"digit": 8, "blank": 9},
            # 状态9,终止状态 (如果发现非空,就失败)
            {"blank": 9}
        ]
        cur_state = 1
        for c in s:
            if c.isdigit():
                c = "digit"
            elif c in " ":
                c = "blank"
            elif c in "+-":
                c = "sign"

            if c not in state[cur_state]:
                return False
            cur_state = state[cur_state][c]
        if cur_state not in [3, 5, 8, 9]:
            return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
