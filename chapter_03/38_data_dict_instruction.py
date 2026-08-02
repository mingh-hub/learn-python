# 数据容器：字典（dict）

"""
1. 字典是使用“键值对”保存数据的数据容器。
2. 定义
    user = {"name": "Alice", "age": 25}
3. 特点
    3.1 键不能重复，重复赋值会覆盖原来的值；值可以重复
    3.2 键必须是可哈希对象，值可以是任意类型
    3.3 字典可以修改，不支持按位置进行索引和切片
    3.4 Python 3.7 及以后，字典会保留键值对的插入顺序
4. 注意
    空字典可以使用 {} 或 dict() 定义，{} 不是空集合。
5. 字典适合表示有明确字段名称的数据，以及建立数据之间的映射关系。
"""

"""
2. 定义字典
"""
print("=================2. 定义字典=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
print(user)
print(type(user))

empty_dict = {}
another_empty_dict = dict()
print(empty_dict)
print(another_empty_dict)
print(type(empty_dict))

# dict() 可以使用关键字参数或键值对序列创建字典
user = dict(name="Bob", age=30)
scores = dict([("Chinese", 90), ("Math", 95)])
print(user)
print(scores)

"""
3. 获取值
    dictionary[key]：键不存在时会报 KeyError
"""
print("=================3. 获取值=================")
user = {"name": "Alice", "age": 25}
print(user["name"])
print(user["age"])
# print(user["city"]) # KeyError: 'city'

"""
3.1 字典中的键和值能否重复
    键不能重复：相同的键只能保留一个，后面的值会覆盖前面的值。
    值可以重复：不同的键可以对应相同的值。
    键值对不能重复保存：因为键是唯一的，所以相同键值对也只会保留一份。
"""
print("=================3.1 键和值能否重复=================")

# 键重复时，后面的值覆盖前面的值
user = {"name": "Alice", "name": "Bob"}
print(user) # {'name': 'Bob'}
print(len(user)) # 1

# 不同的键可以保存相同的值
scores = {"Alice": 100, "Bob": 100}
print(scores)
print(len(scores)) # 2

# 再次写入相同的键值对，不会增加新的数据
user = {"name": "Alice"}
user["name"] = "Alice"
print(user)
print(len(user)) # 1

"""
4. 新增和修改键值对
    使用 dictionary[key] = value 赋值：
    键不存在时新增键值对，键已存在时修改对应的值。
"""
print("=================4. 新增和修改键值对=================")
user = {"name": "Alice", "age": 25}
user["city"] = "Shanghai"
print(user)

user["age"] = 26
print(user)

"""
5. 删除键值对
    del dictionary[key]：删除指定键，键不存在会报 KeyError
"""
print("=================5. 删除键值对=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
del user["city"]
print(user)
# del user["email"] # KeyError: 'email'

"""
6. 成员判断
    in 和 not in 默认判断键是否存在，不会判断值。
"""
print("=================6. 成员判断=================")
user = {"name": "Alice", "age": 25}
print("name" in user)
print("city" not in user)
print("Alice" in user) # False，只判断键

"""
7. 遍历字典
    直接遍历字典会依次得到每个键。
    通过键访问 dictionary[key] 可以在遍历时获取对应的值。
"""
print("=================7. 遍历字典=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}

for key in user:
    print(key)

for key in user:
    print(user[key])

for key in user:
    print(f"{key}={user[key]}")

"""
8. 常用内置函数
    len()：获取键值对数量
    min()、max()：获取最小键和最大键，要求键之间可以比较
    sorted()：对键排序并返回一个列表，不修改原字典
"""
print("=================8. 常用内置函数=================")
scores = {"Chinese": 90, "Math": 95, "English": 88}
print(len(scores))
print(min(scores))
print(max(scores))
print(sorted(scores))

"""
9. 键的要求
    字典的键必须唯一并且可哈希。
    数字、字符串、只包含可哈希元素的元组可以作为键。
    列表、字典、集合是可变对象，不能作为键。
"""
print("=================9. 键的要求=================")
locations = {
    1: "first",
    "name": "Alice",
    (31.23, 121.47): "Shanghai",
}
print(locations)

# {[1, 2]: "point"} # TypeError: unhashable type: 'list'

"""
10. 字典推导式
    语法：{key_expression: value_expression for item in iterable if condition}
"""
print("=================10. 字典推导式=================")
squares = {number: number ** 2 for number in range(1, 6)}
print(squares)

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}
print(even_squares)

"""
11. 合并字典
    Python 3.9 及以后可以使用 | 返回合并后的新字典。
    使用 |= 会直接修改左侧字典。
    键重复时，右侧字典的值会覆盖左侧字典的值。
"""
print("=================11. 合并字典=================")
defaults = {"theme": "light", "language": "zh-CN"}
custom = {"theme": "dark", "font_size": 16}

settings = defaults | custom
print(settings)
print(defaults) # | 不修改原字典

defaults |= custom
print(defaults)

"""
12. 嵌套字典
    字典的值可以是字典、列表、元组等任意类型。
"""
print("=================12. 嵌套字典=================")
student = {
    "name": "Alice",
    "scores": {
        "Chinese": 90,
        "Math": 95,
    },
    "skills": ["Python", "SQL"],
}
print(student["scores"]["Math"])
print(student["skills"][0])

student["scores"]["English"] = 88
print(student)

"""
13. 字典解包
    **dictionary 可以把字典的键值对展开。
    常用于创建新字典和向函数传递关键字参数。
"""
print("=================13. 字典解包=================")
base_user = {"name": "Alice", "age": 25}
complete_user = {**base_user, "city": "Shanghai", "age": 26}
print(complete_user)


def print_user(name, age):
    print(f"name={name}, age={age}")


print_user(**{"name": "Bob", "age": 30})

"""
14. 常见应用场景：单词计数
"""
print("=================14. 常见应用场景：单词计数=================")
words = ["python", "java", "python", "go", "python", "java"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)

"""
15. 遍历时修改字典的注意事项
    遍历字典期间不能改变字典的大小，否则会报 RuntimeError。
    可以遍历 list(dictionary) 创建的键列表，再修改原字典。
"""
print("=================15. 遍历时修改字典的注意事项=================")
scores = {"Alice": 90, "Bob": 55, "Tom": 80}

for name in list(scores):
    if scores[name] < 60:
        del scores[name]

print(scores)

"""
16. 注意事项汇总
- 字典使用键值对保存数据，键必须唯一且可哈希，值可以重复并且可以是任意类型。
- 重复写入同一个键会覆盖原值，不会新增一个键值对。
- 字典可以修改，但不能使用位置索引和切片。
- dictionary[key] 获取不存在的键会报 KeyError。
- in 和 not in 默认判断键，不判断值。
- 遍历字典时不能直接新增或删除键值对。
- Python 3.7 及以后字典保留插入顺序，但仍然通过键而不是位置访问值。

"""
