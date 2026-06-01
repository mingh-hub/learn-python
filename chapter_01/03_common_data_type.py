import types

# 常见数据类型

# 常见基础数据类型
# int 整数
# float 浮点数
# str 字符串
# bool 布尔
# NoneType 空值

# type() 函数可以查看字面量和变量类型（变量本身没有类型，查的其实是容器内数据的类型）
print(type(100))
print(type("Hello"))
a = True
print(type(a))
a = None
print(type(a))

# 可以通过 isinstance() 函数检查是否属于指定类型
print(isinstance("Hello Python", str))
print(isinstance(None, float))
# NoneType 不是直接可用的内置名称，有如下三种写法
print(isinstance(None, type(None)))
print(isinstance(None, None.__class__))
print(isinstance(None, types.NoneType)) # 这个要导包 import types

