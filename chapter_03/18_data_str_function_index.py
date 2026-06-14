# 字符串常用方法-index

"""
1. 方法签名
    str.index(sub, start, end)
        sub — 要查找的子字符串（必传）
        start — 开始查找的起始索引（可选，默认为 0）
        end — 结束查找的结束索引（可选，默认为字符串长度），不包含该位置
"""

"""
2. 基本用法
    返回子字符串第一次出现的索引。如果找不到，会抛出 ValueError。
"""
print("=================基本用法=================")
s = "hello world"
print(s.index("o"))      # 4
print(s.index("world"))  # 6

"""
3. 使用 start 和 end 限制查找区间
    index 只在 [start, end) 这个左闭右开区间内查找。
"""
print("=================使用 start 和 end 限制查找区间=================")
s = "hello world, hello python"
print(s.index("hello"))        # 0
print(s.index("hello", 6))     # 13
print(s.index("hello", 6, 20)) # 13

"""
4. 与 find() 的区别
    find() 找不到返回 -1。
    index() 找不到会抛出 ValueError。
"""
print("=================与 find() 的区别=================")
s = "banana"
print(s.find("x"))   # -1
try:
    print(s.index("x"))
except ValueError as e:
    print(type(e).__name__) # ValueError

"""
5. 常见应用场景
5.1 确定子字符串必须存在的位置
5.2 配合切片提取内容
"""
print("=================常见应用场景：配合切片提取内容=================")
email = "alice@example.com"
at_pos = email.index("@")
print(email[:at_pos])      # alice
print(email[at_pos + 1:])  # example.com

"""
6. 注意事项汇总
- 如果子字符串可能不存在，优先使用 find() 或先用 in 判断。
- index() 更适合“找不到就是异常”的场景。
- start 和 end 可以为负数，规则与切片一致。
- index() 区分大小写。
"""
