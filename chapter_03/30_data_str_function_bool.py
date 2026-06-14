# 字符串常用方法-类型判断

"""
1. 方法概览
    字符串提供了一组以 is 开头的方法，用于判断字符串内容是否符合某种类型或格式。
    这些方法都会返回布尔值：True 或 False。
"""

"""
2. isalpha() — 是否全部由字母组成
    只要字符串中包含数字、空格、标点符号，结果就是 False。
"""
print("=================isalpha() — 是否全部由字母组成=================")
print("hello".isalpha())      # True
print("hello你好".isalpha())  # True
print("hello123".isalpha())   # False
print("hello world".isalpha()) # False

"""
3. isdigit() — 是否全部由数字字符组成
    常用于判断字符串是否可以作为非负整数处理。
"""
print("=================isdigit() — 是否全部由数字字符组成=================")
print("123".isdigit())   # True
print("001".isdigit())   # True
print("12.3".isdigit())  # False
print("-123".isdigit())  # False

"""
4. isdecimal() — 是否全部由十进制数字组成
    isdecimal() 比 isdigit() 更严格，更适合判断普通十进制数字。
"""
print("=================isdecimal() — 是否全部由十进制数字组成=================")
print("123".isdecimal()) # True
print("-123".isdecimal()) # False
print("123.2".isdecimal()) # False
print("①".isdigit())     # True
print("①".isdecimal())   # False
print("一二三".isdigit())   # False
print("一二三".isdecimal())   # False

"""
5. isnumeric() — 是否全部由数字字符组成
    isnumeric() 比 isdigit() 范围更广，一些中文数字、罗马数字也可能返回 True。
"""
print("=================isnumeric() — 是否全部由数字字符组成=================")
print("123".isnumeric()) # True
print("一二三".isnumeric()) # True
print("Ⅻ".isnumeric())   # True

"""
6. isalnum() — 是否全部由字母或数字组成
    字符串中不能包含空格、标点符号等其他字符。
"""
print("=================isalnum() — 是否全部由字母或数字组成=================")
print("abc123".isalnum()) # True
print("abc".isalnum())    # True
print("123".isalnum())    # True
print("123一二三".isalnum())    # True
print("123一二三Ⅻ".isalnum())    # True
print("abc_123".isalnum()) # False

"""
7. isspace() — 是否全部由空白字符组成
    空格、换行符、制表符都属于空白字符。
"""
print("=================isspace() — 是否全部由空白字符组成=================")
print("   ".isspace())    # True
print("\n\t".isspace())   # True
print(" a ".isspace())    # False

"""
8. islower() 和 isupper() — 判断大小写
    islower() 判断是否至少包含一个有大小写的字符，并且所有有大小写的字符都是小写。
    isupper() 判断是否至少包含一个有大小写的字符，并且所有有大小写的字符都是大写。
"""
print("=================islower() 和 isupper() — 判断大小写=================")
print("hello".islower())  # True
print("Hello".islower())  # False
print("HELLO".isupper())  # True
print("Hello".isupper())  # False
print("123".islower())    # False

"""
9. istitle() — 是否符合标题格式
    每个单词首字母大写，其余字母小写时返回 True。
"""
print("=================istitle() — 是否符合标题格式=================")
print("Hello Python".istitle()) # True
print("Hello python".istitle()) # False
print("HELLO PYTHON".istitle()) # False

"""
10. isidentifier() — 是否是合法标识符
    可以用于判断字符串是否能作为 Python 变量名、函数名等标识符。
"""
print("=================isidentifier() — 是否是合法标识符=================")
print("user_name".isidentifier()) # True
print("user1".isidentifier())     # True
print("1user".isidentifier())     # False
print("user-name".isidentifier()) # False

"""
11. isprintable() — 是否都是可打印字符
    换行符、制表符等控制字符通常不是可打印字符。
"""
print("=================isprintable() — 是否都是可打印字符=================")
print("hello".isprintable())  # True
print("hello\n".isprintable()) # False
print("hello\t".isprintable()) # False

"""
12. 空字符串的判断结果
    多数类型判断方法对空字符串返回 False。
"""
print("=================空字符串的判断结果=================")
s = ""
print(s.isalpha())  # False
print(s.isdigit())  # False
print(s.isalnum())  # False
print(s.isspace())  # False

"""
13. 常见应用场景
13.1 校验用户输入是否为数字
13.2 判断用户名是否只包含字母和数字
13.3 判断变量名是否合法
13.4 判断文本是否需要大小写转换
"""
print("=================常见应用场景：校验用户输入是否为数字=================")
age = "25"
if age.isdecimal():
    print(int(age))

print("=================常见应用场景：判断用户名是否只包含字母和数字=================")
username = "Alice123"
if username.isalnum():
    print("用户名格式正确")

print("=================常见应用场景：判断变量名是否合法=================")
name = "user_age"
if name.isidentifier():
    print("可以作为变量名")

"""
14. 注意事项汇总
- 这些方法都返回 True 或 False。
- 空字符串通常返回 False。
- isdigit()、isdecimal()、isnumeric() 范围不同，普通整数校验优先考虑 isdecimal()。
- isalpha() 不只判断英文字母，中文等字母字符也可能返回 True。
- 判断 Python 关键字不能只靠 isidentifier()，还需要配合 keyword.iskeyword()。
"""
