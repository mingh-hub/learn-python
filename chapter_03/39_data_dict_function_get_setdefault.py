# 字典常用方法-get() 和 setdefault()

"""
1. 方法签名
    dictionary.get(key, default=None)
        获取 key 对应的值。
        key 不存在时返回 default，不会修改原字典。

    dictionary.setdefault(key, default=None)
        key 存在时返回对应的值。
        key 不存在时添加 key: default，并返回 default。
"""

"""
2. get() 获取存在的键
"""
print("=================2. get() 获取存在的键=================")
user = {"name": "Alice", "age": 25}
print(user.get("name"))
print(user.get("age", 0))
print(user)

"""
3. get() 获取不存在的键
    不提供 default 时返回 None，提供 default 时返回指定的默认值。
    get() 不会因为键不存在而报 KeyError。
"""
print("=================3. get() 获取不存在的键=================")
user = {"name": "Alice"}
print(user.get("age"))
print(user.get("age", 0))
print(user.get("city", "未知"))
print(user) # get() 不会添加键值对

"""
4. 区分“键不存在”和“值为 None”
    get() 默认都返回 None，无法单独区分这两种情况。
    需要区分时，可以先使用 in 判断键是否存在。
"""
print("=================4. 区分键不存在和值为 None=================")
user = {"name": "Alice", "email": None}
print(user.get("email"))
print(user.get("phone"))
print("email" in user)
print("phone" in user)

"""
5. get() 常见场景：计数
"""
print("=================5. get() 常见场景：计数=================")
words = ["python", "java", "python", "go", "python", "java"]
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)

"""
6. setdefault() 获取存在的键
    key 已存在时返回原来的值，不会使用 default 覆盖原值。
"""
print("=================6. setdefault() 获取存在的键=================")
user = {"name": "Alice", "city": "Beijing"}
result = user.setdefault("city", "Shanghai")
print(result)
print(user)

"""
7. setdefault() 添加不存在的键
    key 不存在时，把 default 保存到字典并返回该值。
"""
print("=================7. setdefault() 添加不存在的键=================")
user = {"name": "Alice"}
result = user.setdefault("city", "Shanghai")
print(result)
print(user)

email = user.setdefault("email")
print(email)
print(user)

"""
8. setdefault() 常见场景：数据分组
    setdefault(key, []) 可以在键第一次出现时创建列表。
"""
print("=================8. setdefault() 常见场景：数据分组=================")
students = [
    ("A", "Alice"),
    ("B", "Bob"),
    ("A", "Tom"),
    ("B", "Lucy"),
]
groups = {}

for group_name, student_name in students:
    groups.setdefault(group_name, []).append(student_name)

print(groups)

"""
9. get() 和 setdefault() 的区别
9.1 get() 只读取数据，不会修改字典。
9.2 setdefault() 在键不存在时会添加键值对。
9.3 两个方法在键不存在时都不会报 KeyError。
"""
print("=================9. get() 和 setdefault() 的区别=================")
data = {}
print(data.get("count", 0))
print(data)

print(data.setdefault("count", 0))
print(data)

"""
10. 注意事项汇总
- get() 适合安全读取，键不存在时返回默认值，不修改字典。
- setdefault() 适合“读取已有值，没有则创建”的场景。
- setdefault() 不会覆盖已经存在的值。
- get() 返回 None 时，不能直接确定是键不存在还是对应的值为 None。
- 只需要读取数据时优先使用 get()，需要初始化数据时使用 setdefault()。
"""
