# 字符串常用方法-replace

"""
1. 方法签名
    str.replace(old, new, count)
        old — 要被替换的旧字符串
        new — 替换后的新字符串
        count — 最多替换次数（可选，默认替换全部）
"""

"""
2. 基本用法
    返回替换后的新字符串。字符串不可变，原字符串不会被修改。
"""
print("=================基本用法=================")
s = "hello world"
new_s = s.replace("world", "python")
print(s)      # hello world
print(new_s)  # hello python

"""
3. 替换全部匹配项
"""
print("=================替换全部匹配项=================")
s = "one fish, two fish, red fish"
print(s.replace("fish", "cat"))

"""
4. 使用 count 限制替换次数
"""
print("=================使用 count 限制替换次数=================")
s = "aaaa"
print(s.replace("a", "A", 2))  # AAaa
print(s.replace("aa", "X", 1)) # Xaa

"""
5. 删除字符串中的内容
    将 old 替换为空字符串 ""，可以实现删除效果。
"""
print("=================删除字符串中的内容=================")
s = "2026-06-14"
print(s.replace("-", "")) # 20260614

"""
6. 常见应用场景
6.1 清理文本
6.2 统一格式
6.3 简单脱敏
"""
print("=================常见应用场景：统一格式=================")
phone = "138 0000 8888"
print(phone.replace(" ", "")) # 13800008888

print("=================常见应用场景：简单脱敏=================")
name = "Alice"
print(name.replace("lic", "***")) # A***e

"""
7. 注意事项汇总
- replace() 返回新字符串，不会修改原字符串。
- 默认替换全部匹配项，可以用 count 限制次数。
- replace() 区分大小写。
- 如果 old 不存在，会返回与原字符串内容相同的新结果。
"""
