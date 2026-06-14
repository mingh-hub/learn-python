# 字符串常用方法-lower

"""
1. 方法签名
    str.lower()
"""

"""
2. 基本用法
    将字符串中的大写字母转换为小写，返回新字符串。
"""
print("=================基本用法=================")
s = "Hello Python"
print(s.lower()) # hello python
print(s)         # 原字符串不变

"""
3. upper() — 转大写
    upper() 与 lower() 相反，会将字符串中的小写字母转换为大写。
"""
print("=================upper() — 转大写=================")
s = "Hello Python"
print(s.upper()) # HELLO PYTHON

"""
4. 大小写不敏感比较
    比较前先统一大小写，可以避免大小写差异造成判断失败。
"""
print("=================大小写不敏感比较=================")
user_input = "YES"
print(user_input.lower() == "yes") # True

"""
5. 常见应用场景
5.1 用户输入标准化
5.2 搜索时忽略大小写
5.3 判断文件扩展名
"""
print("=================常见应用场景：搜索时忽略大小写=================")
text = "Python is powerful"
keyword = "python"
print(keyword.lower() in text.lower()) # True

print("=================常见应用场景：判断文件扩展名=================")
filename = "REPORT.PDF"
print(filename.lower().endswith(".pdf")) # True

"""
6. 注意事项汇总
- lower() 和 upper() 都返回新字符串。
- 它们主要影响有大小写概念的字符。
- 需要更严格的大小写无关比较时，可以了解 casefold()。
"""
