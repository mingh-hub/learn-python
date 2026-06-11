# 列表方法-count

"""
1. 方法签名与基本用法
    list.count(value)
1.1 参数：value —— 要计数的对象。
1.2 返回值：整数，表示 value 在列表中出现的次数。如果元素不存在，返回 0。
"""
print("=================方法签名与基本用法 ===================")

fruits = ['apple', 'banana', 'apple', 'cherry']
print(fruits.count('apple'))   # 2
print(fruits.count('banana'))  # 1
print(fruits.count('orange'))  # 0

"""
2. 相等性判断：依赖 ==
    count() 使用 == 运算符来判断元素是否与 value 相等，不是 is。
"""
print("=================相等性判断：依赖 [==]=================")

class User:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

users = [User('Alice'), User('Bob'), User('Alice')]
print(users.count(User('Alice')))   # 2

"""
3. 与 collections.Counter 对比
"""
print("=================与 collections.Counter 对比=================")
from collections import Counter

data = ['a', 'b', 'a', 'c', 'b', 'a']

# 单次查询
print(data.count('a'))       # 3

# 所有元素频率
counter = Counter(data)
print(counter['a'])          # 3
print(counter.most_common(2))  # [('a', 3), ('b', 2)] 一个包含 (element, count) 元组的列表，按 count 降序排列。

"""
4. 内部原理简述
    CPython 中 list.count() 的 C 实现大致如下：
-> 获取列表长度 n。
-> 初始化计数器 count = 0。
-> 遍历 i 从 0 到 n-1：
        对 list[i] 和 value 执行 PyObject_RichCompareBool(item, value, Py_EQ)。
        如果返回 1，则 count += 1。
-> 返回 count。
"""