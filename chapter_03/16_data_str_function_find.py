# 字符串常用方法-find

"""
1. 方法签名
    str.find(sub, start, end)
        sub — 要查找的子字符串（必传）
        start — 开始查找的起始索引（可选，默认为 0）
        end — 结束查找的结束索引（可选，默认为字符串长度），不包含该位置
"""

"""
2. 基本用法
    返回子串首次出现的最小索引（从 0 开始），如果没找到则返回 -1。
    索引位置是字符串中字符的位置，空格也占一个位置。
"""
s = "hello world"

s.find("o")      # 4
s.find("world")  # 6
s.find("python") # -1

"""
3. 使用 start 和 end 限制搜索区间
    find 只在 [start, end) 这个左闭右开区间内查找。
"""
s = "hello world, hello python"

# 从索引 6 开始查找 'hello'
s.find("hello", 6)       # 13

# 在 [6, 15) 区间内查找 'hello'，找不到
s.find("hello", 6, 15)   # -1

"""
4. 返回值详解与 index() 的区别
    都是返回索引，主要差异点是 find() 找不到返回 -1，index() 找不到会抛异常：ValueError
"""

"""
5. rfind() — 从右向左查找
    rfind() 用法与 find() 完全相同，但它返回最后一次出现的位置（仍然是从左数的索引）。
"""
print("=================rfind() — 从右向左查找=================")
s = "hello world, hello"
print(s.rfind("hello"))   # 13
print(s.rfind("o"))       # 17  (最后一个'o'的索引)
print(s.rfind("x"))       # -1

"""
6. 查找空字符串的行为
    查找空字符串 '' 会返回 start 的值（如果未指定则为 0），因为空字符串被认为存在于任何位置。
"""
print("=================查找空字符串的行为=================")
s = "abc"
print(s.find(""))       # 0
print(s.find("", 2))    # 2
print(s.find("",3))     # 3 start 最大值为字符串本身长度：len(s)
print(s.find("", 4))    # -1  (因为 start=4 超出了字符串长度)

"""
7. 查找所有匹配项
    find 每次只返回第一个匹配，要找出所有位置，可以循环查找并移动 start
"""
s = "ababa"
sub = "ab"
pos = s.find(sub)
while pos != -1:
    print(pos)          # 0, 2
    # 注意这里使用 pos + 1 而非 pos + len(sub)，是为了支持重叠匹配（例如在 "aaa" 中找 "aa"，位置 0 和 1 都算匹配）。如果不需要重叠，可以用 pos + len(sub)。
    pos = s.find(sub, pos + 1)   # 从当前找到位置的下一个索引继续找

"""
8. 性能与实现
8.1 时间复杂度：O(n*m) 最坏情况（暴力匹配），其中 n 为字符串长度，m 为子串长度。CPython 实际实现使用了 Fast Search 算法（Boyer-Moore 的变体），
    平均情况下非常快，尤其对于较长的字符串和子串。
8.2 它是大小写敏感的："Hello".find("h") 返回 -1，因为 h 和 H 不同。
8.3 可以查找任意字符串，不仅仅是单个字符。
"""

"""
9. 常见应用场景
9.1 判断是否包含某子串
9.2 提取子串
9.3 简单解析
9.4 循环取出所有分割字段
"""
print("=================常见应用场景：判断是否包含某子串=================")
if s.find("error") != -1:
    print("包含")

# 不过更 Pythonic 的方式是直接用 in:
if "error" in s:
    print("包含")

print("=================常见应用场景：提取子串=================")
url = "https://example.com/path"
pos = url.find("://")
if pos != -1:
    protocol = url[:pos]   # "https"
    print(protocol)

print("=================常见应用场景：简单解析=================")
line = "name=Alice;age=25"
start = line.find("=") + 1
end = line.find(";")
value = line[start:end]
print(value) # "Alice"

"""
10. 注意事项汇总
- find 只返回第一个匹配，使用循环可找全部。
- 区分大小写，需要忽略大小时先 s.lower().find(...)。
- 不要混淆索引：find 返回的是字符串中的位置，适合直接用于切片。
- 空子串返回 start，设计如此，避免踩坑。
- start 和 end 可以为负数，表示从字符串末尾开始计算的位置，规则与切片一致。
"""