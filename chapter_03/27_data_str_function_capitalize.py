# 字符串常用方法-capitalize

"""
1. 方法签名
    str.capitalize()
"""

"""
2. 基本用法
    将字符串第一个字符转为大写，其余字符转为小写，返回新字符串。
"""
print("=================基本用法=================")
s = "hello python"
print(s.capitalize()) # Hello python

"""
3. 其余字符会被转为小写
"""
print("=================其余字符会被转为小写=================")
s = "hELLO PYTHON"
print(s.capitalize()) # Hello python

"""
4. 字符串以空格开头
    capitalize() 处理的是字符串第一个字符。如果第一个字符是空格，后面的字母不会变成首字母。
"""
print("=================字符串以空格开头=================")
s = " hello python"
print(s.capitalize()) #  hello python
print(s.strip().capitalize()) # Hello python

"""
5. 常见应用场景
5.1 简单格式化一句话
5.2 处理用户输入的句子
"""
print("=================常见应用场景：简单格式化一句话=================")
sentence = "python is easy"
print(sentence.capitalize())

"""
6. 注意事项汇总
- capitalize() 只关注字符串第一个字符。
- 其余字符会被转换为小写。
- 如果需要每个单词首字母大写，使用 title()。
- capitalize() 返回新字符串，不会修改原字符串。
"""
