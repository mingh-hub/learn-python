# 字符串常用方法-count

"""
1. 方法签名
    str.count(sub, start, end)
        sub — 要统计的子字符串（必传）
        start — 开始统计的起始索引（可选，默认为 0）
        end — 结束统计的结束索引（可选，默认为字符串长度），不包含该位置
"""

"""
2. 基本用法
    返回子字符串在字符串中出现的次数。如果没有找到，则返回 0。
    count() 区分大小写，空格、标点符号也会参与匹配。
"""
print("=================基本用法=================")
s = "hello world"
print(s.count("o"))       # 2
print(s.count("world"))   # 1
print(s.count("python"))  # 0

"""
3. 使用 start 和 end 限制统计区间
    count 只在 [start, end) 这个左闭右开区间内统计。
"""
print("=================使用 start 和 end 限制统计区间=================")
s = "hello world, hello python"
print(s.count("hello"))        # 2
print(s.count("hello", 6))     # 1
print(s.count("hello", 6, 15)) # 0

"""
4. 不统计重叠匹配
    count() 统计的是非重叠匹配次数。
"""
print("=================不统计重叠匹配=================")
s = "aaaa"
print(s.count("aa"))   # 2，匹配位置为 0 和 2

# 如果需要统计重叠匹配，可以用 find() 循环移动一个字符
sub = "aa"
pos = s.find(sub)
total = 0
while pos != -1:
    total += 1
    pos = s.find(sub, pos + 1)
print(total)           # 3，匹配位置为 0、1、2

"""
5. 查找空字符串的行为
    统计空字符串 '' 时，结果为区间长度 + 1。
    因为空字符串被认为存在于每个字符之间，以及字符串开头和结尾。
"""
print("=================查找空字符串的行为=================")
s = "abc"
print(s.count(""))       # 4
print(s.count("", 1))    # 3
print(s.count("", 1, 2)) # 2
print(s.count("", 4))    # 0

"""
6. 与 find() 的区别
    find() 返回第一次出现的索引，找不到返回 -1。
    count() 返回出现次数，找不到返回 0。
"""
print("=================与 find() 的区别=================")
s = "banana"
print(s.find("na"))   # 2
print(s.count("na"))  # 2
print(s.find("x"))    # -1
print(s.count("x"))   # 0

"""
7. 性能与实现
7.1 时间复杂度：通常与字符串长度和子串长度相关。
7.2 count() 会从左到右扫描字符串，找到一次非重叠匹配后继续向后统计。
7.3 它是大小写敏感的："Hello".count("h") 返回 0，因为 h 和 H 不同。
"""

"""
8. 常见应用场景
8.1 统计某个字符出现次数
8.2 判断某个关键词出现频率
8.3 简单校验文本格式
"""
print("=================常见应用场景：统计某个字符出现次数=================")
text = "apple,banana,orange"
print(text.count(","))   # 2

print("=================常见应用场景：判断某个关键词出现频率=================")
log = "error: timeout; info: retry; error: failed"
error_count = log.count("error")
if error_count > 0:
    print(error_count)   # 2

print("=================常见应用场景：简单校验文本格式=================")
email = "alice@example.com"
if email.count("@") == 1:
    print("邮箱格式初步正确")

"""
9. 注意事项汇总
- count 统计的是非重叠匹配，不适合直接统计重叠子串。
- 区分大小写，需要忽略大小写时先 s.lower().count(...)。
- start 和 end 可以为负数，表示从字符串末尾开始计算的位置，规则与切片一致。
- 空子串的统计结果比较特殊：一般为区间长度 + 1。
- count 适合统计次数；如果只判断是否包含，推荐使用 in。
"""
