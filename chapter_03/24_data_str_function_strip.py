# 字符串常用方法-strip

"""
1. 方法签名
    str.strip(chars)
        chars — 要去除的字符集合（可选，默认去除空白字符）
"""

"""
2. 基本用法
    去除字符串左右两侧的空白字符，返回新字符串。
"""
print("=================基本用法=================")
s = "  hello python  "
print(s.strip()) # hello python
print(s)         # 原字符串不变

"""
3. lstrip() 和 rstrip()
    lstrip() 只去除左侧。
    rstrip() 只去除右侧。
"""
print("=================lstrip() 和 rstrip()=================")
s = "  hello python  "
print(s.lstrip()) # hello python··
print(s.rstrip()) # ··hello python

"""
4. 去除指定字符
    chars 表示字符集合，不是完整子字符串。
"""
print("=================去除指定字符=================")
s = "---hello---"
print(s.strip("-")) # hello

s = "abcHelloabc"
print(s.strip("abc")) # Hello

"""
5. chars 不是前缀或后缀
    strip("ab") 会反复去除两侧属于 a 或 b 的字符。
"""
print("=================chars 不是前缀或后缀=================")
s = "ababaHelloabba"
print(s.strip("ab")) # Hello
s = "abcabaHelloabba"
print(s.strip("ab")) # cabaHello

"""
6. 常见应用场景
6.1 清理用户输入
6.2 清理文件读取后的换行符
6.3 清理简单包裹符号
"""
print("=================常见应用场景：清理用户输入=================")
name = "  Alice\n"
print(name.strip()) # Alice

"""
7. 注意事项汇总
- strip() 返回新字符串，不会修改原字符串。
- 默认去除空格、换行符、制表符等空白字符。
- chars 是字符集合，不是完整字符串。
- 只处理左侧用 lstrip()，只处理右侧用 rstrip()。
"""
