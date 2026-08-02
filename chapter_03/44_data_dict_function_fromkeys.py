# 字典类方法-fromkeys()

"""
1. 方法签名
    dict.fromkeys(iterable, value=None)

    使用 iterable 中的元素作为键，为每个键设置相同的 value。
    value 默认为 None，方法会返回一个新字典。
"""

"""
2. fromkeys() 基本用法
"""
print("=================2. fromkeys() 基本用法=================")
fields = ["name", "age", "city"]
user = dict.fromkeys(fields)
print(user)

"""
3. 指定默认值
"""
print("=================3. 指定默认值=================")
subjects = ["Chinese", "Math", "English"]
scores = dict.fromkeys(subjects, 0)
print(scores)

"""
4. iterable 可以是不同的可迭代对象
"""
print("=================4. 不同的可迭代对象=================")
print(dict.fromkeys(("name", "age"), "unknown"))
print(dict.fromkeys({"read", "write"}, False))
print(dict.fromkeys("ABC", 0))

"""
5. iterable 中的重复元素
    字典的键不能重复，因此重复元素只会产生一个键。
"""
print("=================5. iterable 中的重复元素=================")
keys = ["name", "age", "name", "city"]
user = dict.fromkeys(keys, "unknown")
print(user)
print(len(user))

"""
6. 使用不可变默认值
    数字、字符串、布尔值、None 等不可变对象可以安全地作为共同默认值。
"""
print("=================6. 使用不可变默认值=================")
permissions = dict.fromkeys(["read", "write", "delete"], False)
permissions["read"] = True
print(permissions)

"""
7. 可变默认值会被共享
    fromkeys() 不会为每个键分别创建 value。
    value 是列表、字典或集合时，所有键会引用同一个对象。
"""
print("=================7. 可变默认值会被共享=================")
groups = dict.fromkeys(["A", "B"], [])
groups["A"].append("Alice")
print(groups)
print(groups["A"] is groups["B"])

"""
8. 使用字典推导式创建独立的可变值
    每次执行表达式 [] 都会创建一个新列表。
"""
print("=================8. 创建独立的可变值=================")
groups = {key: [] for key in ["A", "B"]}
groups["A"].append("Alice")
print(groups)
print(groups["A"] is groups["B"])

"""
9. fromkeys() 与字典推导式的区别
    fromkeys() 适合所有键使用同一个不可变默认值的情况。
    字典推导式可以为不同的键计算不同的值，也可以创建独立的可变对象。
"""
print("=================9. fromkeys() 与字典推导式的区别=================")
keys = ["A", "B", "C"]
same_values = dict.fromkeys(keys, 0)
calculated_values = {key: index for index, key in enumerate(keys, start=1)}
print(same_values)
print(calculated_values)

"""
10. 常见使用场景：初始化字段
"""
print("=================10. 常见使用场景：初始化字段=================")
required_fields = ["username", "email", "phone"]
form_data = dict.fromkeys(required_fields, "")
form_data["username"] = "alice"
print(form_data)

"""
11. 注意事项汇总
- fromkeys() 是 dict 的类方法，会返回一个新字典。
- iterable 中的元素会成为字典的键，重复元素会被去除。
- 不提供 value 时，每个键对应的值都是 None。
- 所有键共享同一个 value 对象，可变默认值可能产生修改联动。
- 需要独立的可变值或按键计算值时，使用字典推导式。
"""
