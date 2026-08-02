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
    dictionary.get(key, default)：键不存在时返回 default，默认返回 None
"""
print("=================3. 获取值=================")
user = {"name": "Alice", "age": 25}
print(user["name"])
print(user.get("age"))
print(user.get("city"))
print(user.get("city", "未知"))
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
5. update() 批量更新
    update() 可以使用另一个字典、键值对序列或关键字参数批量更新数据。
    已存在的键会被覆盖，不存在的键会被添加。
"""
print("=================5. update() 批量更新=================")
user = {"name": "Alice", "age": 25}
result = user.update({"age": 26, "city": "Shanghai"})
print(user)
print(result) # None，update() 会直接修改原字典

user.update([("email", "alice@example.com")], active=True)
print(user)

"""
6. setdefault() 获取或添加默认值
    键存在时，返回已有值，不修改字典。
    键不存在时，添加 key: default 并返回 default；default 默认为 None。
"""
print("=================6. setdefault() 获取或添加默认值=================")
user = {"name": "Alice"}
print(user.setdefault("name", "Unknown"))
print(user)

print(user.setdefault("city", "Shanghai"))
print(user)

"""
7. 删除键值对
    del dictionary[key]：删除指定键，键不存在会报 KeyError
    pop(key, default)：删除指定键并返回值；提供 default 后，键不存在时返回 default
    popitem()：删除并返回最后插入的键值对
    clear()：清空字典
"""
print("=================7. 删除键值对=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
del user["city"]
print(user)

age = user.pop("age")
print(age)
print(user)

print(user.pop("email", "未设置邮箱"))

key_value = user.popitem()
print(key_value)
print(user)

user = {"name": "Alice", "age": 25}
result = user.clear()
print(user)
print(result) # None

"""
8. 成员判断
    in 和 not in 默认判断键是否存在，不会判断值。
"""
print("=================8. 成员判断=================")
user = {"name": "Alice", "age": 25}
print("name" in user)
print("city" not in user)
print("Alice" in user)          # False，只判断键
print("Alice" in user.values()) # True，判断值

"""
9. 获取键、值和键值对
    keys()：返回所有键的动态视图
    values()：返回所有值的动态视图
    items()：返回所有 (key, value) 键值对的动态视图
"""
print("=================9. 获取键、值和键值对=================")
user = {"name": "Alice", "age": 25}
keys = user.keys()
values = user.values()
items = user.items()
print(keys)
print(values)
print(items)

# 字典视图会跟随原字典的变化
user["city"] = "Shanghai"
print(keys)
print(items)

"""
10. 遍历字典
    直接遍历字典等价于遍历 dictionary.keys()。
"""
print("=================10. 遍历字典=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}

for key in user:
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f"{key}={value}")

"""
11. 常用内置函数
    len()：获取键值对数量
    min()、max()：获取最小键和最大键，要求键之间可以比较
    sorted()：对键排序并返回一个列表，不修改原字典
"""
print("=================11. 常用内置函数=================")
scores = {"Chinese": 90, "Math": 95, "English": 88}
print(len(scores))
print(min(scores))
print(max(scores))
print(sorted(scores))

"""
12. 键的要求
    字典的键必须唯一并且可哈希。
    数字、字符串、只包含可哈希元素的元组可以作为键。
    列表、字典、集合是可变对象，不能作为键。
"""
print("=================12. 键的要求=================")
locations = {
    1: "first",
    "name": "Alice",
    (31.23, 121.47): "Shanghai",
}
print(locations)

# {[1, 2]: "point"} # TypeError: unhashable type: 'list'

"""
13. fromkeys() 创建具有相同默认值的字典
    dict.fromkeys(iterable, value) 使用可迭代对象中的元素作为键。
    value 是每个键共同使用的默认值，默认为 None。
"""
print("=================13. fromkeys()=================")
fields = ["name", "age", "city"]
user = dict.fromkeys(fields)
scores = dict.fromkeys(["Chinese", "Math", "English"], 0)
print(user)
print(scores)

"""
14. fromkeys() 与可变默认值
    fromkeys() 不会为每个键分别创建可变对象，所有键会引用同一个默认对象。
    需要独立的列表、字典或集合时，应使用字典推导式。
"""
print("=================14. fromkeys() 与可变默认值=================")
groups = dict.fromkeys(["A", "B"], [])
groups["A"].append("Alice")
print(groups) # A 和 B 对应的列表都发生了变化

groups = {key: [] for key in ["A", "B"]}
groups["A"].append("Alice")
print(groups) # 每个键拥有独立的列表

"""
15. 字典推导式
    语法：{key_expression: value_expression for item in iterable if condition}
"""
print("=================15. 字典推导式=================")
squares = {number: number ** 2 for number in range(1, 6)}
print(squares)

even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}
print(even_squares)

"""
16. 合并字典
    Python 3.9 及以后可以使用 | 返回合并后的新字典。
    使用 |= 会直接修改左侧字典。
    键重复时，右侧字典的值会覆盖左侧字典的值。
"""
print("=================16. 合并字典=================")
defaults = {"theme": "light", "language": "zh-CN"}
custom = {"theme": "dark", "font_size": 16}

settings = defaults | custom
print(settings)
print(defaults) # | 不修改原字典

defaults |= custom
print(defaults)

"""
17. copy() 浅拷贝与直接赋值
    直接赋值只会复制引用，两个变量指向同一个字典。
    copy() 创建一个新字典，但嵌套的可变对象仍会被共享。
"""
print("=================17. copy() 浅拷贝与直接赋值=================")
original = {"name": "Alice", "skills": ["Python"]}
same_dict = original
copied = original.copy()

same_dict["name"] = "Bob"
print(original["name"]) # Bob
print(original is same_dict)
print(original is copied)

copied["skills"].append("SQL")
print(original["skills"]) # 浅拷贝仍然共享内部列表

"""
18. 嵌套字典
    字典的值可以是字典、列表、元组等任意类型。
"""
print("=================18. 嵌套字典=================")
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
19. 字典解包
    **dictionary 可以把字典的键值对展开。
    常用于创建新字典和向函数传递关键字参数。
"""
print("=================19. 字典解包=================")
base_user = {"name": "Alice", "age": 25}
complete_user = {**base_user, "city": "Shanghai", "age": 26}
print(complete_user)


def print_user(name, age):
    print(f"name={name}, age={age}")


print_user(**{"name": "Bob", "age": 30})

"""
20. 常见应用场景：单词计数
"""
print("=================20. 常见应用场景：单词计数=================")
words = ["python", "java", "python", "go", "python", "java"]
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

"""
21. 遍历时修改字典的注意事项
    遍历字典期间不能改变字典的大小，否则会报 RuntimeError。
    可以遍历 list(dictionary) 创建的键列表，再修改原字典。
"""
print("=================21. 遍历时修改字典的注意事项=================")
scores = {"Alice": 90, "Bob": 55, "Tom": 80}

for name in list(scores):
    if scores[name] < 60:
        del scores[name]

print(scores)

"""
22. 注意事项汇总
- 字典使用键值对保存数据，键必须唯一且可哈希，值可以重复并且可以是任意类型。
- 重复写入同一个键会覆盖原值，不会新增一个键值对。
- 字典可以修改，但不能使用位置索引和切片。
- dictionary[key] 获取不存在的键会报 KeyError，get() 可以提供默认值。
- in 和 not in 默认判断键，不判断值。
- keys()、values()、items() 返回的是动态视图。
- update()、setdefault()、clear() 和 |= 会直接修改原字典。
- copy() 是浅拷贝，嵌套的可变对象仍可能被共享。
- 遍历字典时不能直接新增或删除键值对。
- Python 3.7 及以后字典保留插入顺序，但仍然通过键而不是位置访问值。

23. 常用方法专题文件
- 39_data_dict_function_get_setdefault.py：get()、setdefault()
- 40_data_dict_function_update.py：update()
- 41_data_dict_function_delete.py：del、pop()、popitem()、clear()
- 42_data_dict_function_keys_values_items.py：keys()、values()、items()
- 43_data_dict_function_copy.py：copy()、浅拷贝与深拷贝
- 44_data_dict_function_fromkeys.py：fromkeys()
"""
