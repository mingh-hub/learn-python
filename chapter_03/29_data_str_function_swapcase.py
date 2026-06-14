# 字符串常用方法-swapcase

"""
1. 方法签名
    str.swapcase()
"""

"""
2. 基本用法
    将字符串中的大写字母转为小写，小写字母转为大写，返回新字符串。
"""
print("=================基本用法=================")
s = "Hello Python"
print(s.swapcase()) # hELLO pYTHON

"""
3. 非字母字符不受影响
"""
print("=================非字母字符不受影响=================")
s = "PyThOn 3.12!"
print(s.swapcase()) # pYtHoN 3.12!

"""
4. 与 lower() 和 upper() 的区别
"""
print("=================与 lower() 和 upper() 的区别=================")
s = "Hello"
print(s.lower())    # hello
print(s.upper())    # HELLO
print(s.swapcase()) # hELLO

"""
5. 常见应用场景
5.1 演示大小写转换规则
5.2 简单文本效果处理
"""
print("=================常见应用场景：简单文本效果处理=================")
text = "Python Is Fun"
print(text.swapcase())

"""
6. 注意事项汇总
- swapcase() 返回新字符串。
- 它会交换大小写，而不是统一转为某一种大小写。
- 数字、空格、标点符号不会受影响。
- 实际业务中更常用 lower()、upper() 做标准化。
"""
