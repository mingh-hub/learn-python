# 字符串常用方法-split

"""
1. 方法签名
    str.split(sep, maxsplit)
        sep — 分隔符（可选，默认按任意空白字符分割）
        maxsplit — 最大分割次数（可选，默认 -1 表示不限制）
"""

"""
2. 基本用法
    按分隔符切分字符串，返回列表。
"""
print("=================基本用法=================")
s = "apple,banana,orange"
print(s.split(",")) # ['apple', 'banana', 'orange']

"""
3. 默认按空白字符分割
    不传 sep 时，会自动处理连续空格、制表符、换行符。
"""
print("=================默认按空白字符分割=================")
s = "  hello   python\tworld\n"
print(s.split()) # ['hello', 'python', 'world']

"""
4. 使用 maxsplit 限制分割次数
"""
print("=================使用 maxsplit 限制分割次数=================")
s = "name=Alice=Tom"
print(s.split("=", 1)) # ['name', 'Alice=Tom']
print(s.split("=", 2)) # ['name', 'Alice', 'Tom']

"""
5. rsplit() — 从右向左分割
    rsplit() 用法与 split() 类似，但限制分割次数时从右侧开始。
"""
print("=================rsplit() — 从右向左分割=================")
s = "www.example.com"
print(s.split(".", 1))  # ['www', 'example.com']
print(s.rsplit(".", 1)) # ['www.example', 'com']

"""
6. 空字段行为
    指定 sep 时，连续分隔符会产生空字符串。
"""
print("=================空字段行为=================")
s = "a,,b,"
print(s.split(",")) # ['a', '', 'b', '']

"""
7. 常见应用场景
7.1 拆分 CSV 风格文本
7.2 拆分路径或域名
7.3 解析简单键值对
"""
print("=================常见应用场景：解析简单键值对=================")
line = "name=Alice"
key, value = line.split("=", 1)
print(key)
print(value)

"""
8. 注意事项汇总
- split() 返回列表。
- sep 不传时按任意空白字符分割，并自动忽略首尾空白。
- sep 指定为空字符串 "" 会报 ValueError。
- 需要从右侧限制分割次数时使用 rsplit()。
"""
