# 字符串常用方法-title

"""
1. 方法签名
    str.title()
"""

"""
2. 基本用法
    将每个单词的首字母转为大写，其余字母转为小写，返回新字符串。
"""
print("=================基本用法=================")
s = "hello python world"
print(s.title()) # Hello Python World

"""
3. 其余字母会被转为小写
"""
print("=================其余字母会被转为小写=================")
s = "hELLO pYTHON"
print(s.title()) # Hello Python

"""
4. 与 capitalize() 的区别
    capitalize() 只处理整个字符串的第一个字符。
    title() 会处理每个单词。
"""
print("=================与 capitalize() 的区别=================")
s = "hello python"
print(s.capitalize()) # Hello python
print(s.title())      # Hello Python

"""
5. 单词边界行为
    title() 会根据非字母字符判断单词边界。
"""
print("=================单词边界行为=================")
s = "hello-python's world"
print(s.title()) # Hello-Python'S World

"""
6. 常见应用场景
6.1 简单格式化标题
6.2 格式化英文姓名
"""
print("=================常见应用场景：简单格式化标题=================")
title = "learn python string methods"
print(title.title())

"""
7. 注意事项汇总
- title() 返回新字符串。
- title() 会把每个单词的首字母大写，其余字母小写。
- 对带撇号的英文单词，title() 的结果可能不符合自然语言习惯。
- 只处理第一个字符时使用 capitalize()。
"""
