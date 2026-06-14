# 字符串常用方法-partition

"""
1. 方法签名
    str.partition(sep)
        sep — 分隔符（必传）
"""

"""
2. 基本用法
    从左到右查找第一个 sep，将字符串拆成三部分：(分隔符前, 分隔符本身, 分隔符后)。
"""
print("=================基本用法=================")
s = "name=Alice"
print(s.partition("=")) # ('name', '=', 'Alice')

"""
3. 分隔符不存在
    如果 sep 不存在，返回：(原字符串, '', '')。
"""
print("=================分隔符不存在=================")
s = "name Alice"
print(s.partition("=")) # ('name Alice', '', '')

"""
4. rpartition() — 从右向左分割
    rpartition() 从右侧查找最后一个 sep。
"""
print("=================rpartition() — 从右向左分割=================")
s = "archive.tar.gz"
print(s.partition("."))  # ('archive', '.', 'tar.gz')
print(s.rpartition(".")) # ('archive.tar', '.', 'gz')

"""
5. 与 split() 的区别
    partition() 固定返回 3 个元素，适合只按第一个分隔符拆一次。
"""
print("=================与 split() 的区别=================")
s = "key=value=extra"
print(s.partition("="))  # ('key', '=', 'value=extra')
print(s.split("=", 1))   # ['key', 'value=extra']

"""
6. 常见应用场景
6.1 解析简单键值对
6.2 拆分协议头
6.3 获取文件扩展名
"""
print("=================常见应用场景：解析简单键值对=================")
line = "age=25"
key, sep, value = line.partition("=")
if sep:
    print(key)
    print(value)

"""
7. 注意事项汇总
- partition() 固定返回三元组。
- sep 不能为空字符串，否则会报 ValueError。
- 只需要拆一次时，partition() 通常比 split() 更直接。
- 需要从右侧拆一次时使用 rpartition()。
"""
