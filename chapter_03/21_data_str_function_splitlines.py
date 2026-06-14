# 字符串常用方法-splitlines

"""
1. 方法签名
    str.splitlines(keepends)
        keepends — 是否保留换行符（可选，默认为 False）
"""

"""
2. 基本用法
    按行切分字符串，返回列表。
"""
print("=================基本用法=================")
text = "first line\nsecond line\nthird line"
print(text.splitlines())

"""
3. 保留换行符
    keepends=True 时，每一行会保留原来的换行符。
"""
print("=================保留换行符=================")
text = "first line\nsecond line\n"
print(text.splitlines(True))

"""
4. 与 split("\\n") 的区别
    splitlines() 能识别多种换行符，并且末尾换行不会额外产生空字符串。
"""
print("=================与 split('\\\\n') 的区别=================")
text = "a\nb\n"
print(text.split("\n"))   # ['a', 'b', '']
print(text.splitlines())  # ['a', 'b']

"""
5. 支持多种行边界
    splitlines() 可以处理 \n、\r\n、\r 等行分隔符。
"""
print("=================支持多种行边界=================")
text = "a\r\nb\rc\n"
print(text.splitlines()) # ['a', 'b', 'c']

"""
6. 常见应用场景
6.1 逐行读取多行文本
6.2 处理日志文本
6.3 保留或去掉换行符
"""
print("=================常见应用场景：处理日志文本=================")
log = "INFO start\nERROR failed\nINFO end"
for line in log.splitlines():
    if line.startswith("ERROR"):
        print(line)

"""
7. 注意事项汇总
- splitlines() 专门用于按行拆分文本。
- keepends=True 可以保留换行符。
- 如果文本末尾有换行符，splitlines() 不会像 split("\\n") 那样额外产生空字符串。
"""
