# 字符串常用方法-startswith

"""
1. 方法签名
    str.startswith(prefix, start, end)
        prefix — 要判断的前缀，可以是字符串或字符串元组
        start — 开始判断的起始索引（可选，默认为 0）
        end — 结束判断的结束索引（可选，默认为字符串长度），不包含该位置
"""

"""
2. 基本用法
    判断字符串是否以指定内容开头，返回 True 或 False。
"""
print("=================基本用法=================")
s = "hello world"
print(s.startswith("hello")) # True
print(s.startswith("world")) # False

"""
3. 使用 start 和 end 限制判断区间
"""
print("=================使用 start 和 end 限制判断区间=================")
s = "hello world"
print(s.startswith("world", 6))     # True
print(s.startswith("world", 6, 11)) # True

"""
4. 使用元组判断多个前缀
"""
print("=================使用元组判断多个前缀=================")
filename = "main.py"
print(filename.startswith(("main", "test"))) # True

"""
5. endswith() — 判断结尾
    endswith() 用法与 startswith() 类似，用于判断字符串是否以指定内容结尾。
"""
print("=================endswith() — 判断结尾=================")
filename = "report.pdf"
print(filename.endswith(".pdf"))          # True
print(filename.endswith((".jpg", ".png"))) # False

"""
6. 常见应用场景
6.1 判断 URL 协议
6.2 判断文件扩展名
6.3 判断日志级别
"""
print("=================常见应用场景：判断 URL 协议=================")
url = "https://example.com"
if url.startswith(("http://", "https://")):
    print("合法 URL")

"""
7. 注意事项汇总
- startswith() 和 endswith() 返回布尔值。
- prefix/suffix 可以是字符串，也可以是字符串元组。
- 它们区分大小写。
- 判断开头或结尾时，比 find()、切片写法更直接。
"""
