# 字典常用方法-keys()、values() 和 items()

"""
1. 方法签名
    dictionary.keys()
        返回由所有键组成的动态视图。

    dictionary.values()
        返回由所有值组成的动态视图。

    dictionary.items()
        返回由所有 (key, value) 键值对组成的动态视图。
"""

"""
2. keys() 获取所有键
"""
print("=================2. keys() 获取所有键=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
keys = user.keys()
print(keys)
print(type(keys))

for key in keys:
    print(key)

"""
3. values() 获取所有值
"""
print("=================3. values() 获取所有值=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
values = user.values()
print(values)
print(type(values))

for value in values:
    print(value)

"""
4. items() 获取所有键值对
    每个键值对以二元元组的形式出现，遍历时可以直接解包。
"""
print("=================4. items() 获取所有键值对=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
items = user.items()
print(items)
print(type(items))

for key, value in items:
    print(f"{key}={value}")

"""
5. 字典视图是动态的
    视图不会复制数据，原字典变化后，已经获得的视图也会反映变化。
"""
print("=================5. 字典视图是动态的=================")
user = {"name": "Alice"}
keys = user.keys()
values = user.values()
items = user.items()

user["age"] = 25
print(keys)
print(values)
print(items)

"""
6. 字典视图不支持位置索引
    需要按位置访问时，可以先转换为列表或元组。
"""
print("=================6. 字典视图不支持位置索引=================")
user = {"name": "Alice", "age": 25}
keys = user.keys()
# print(keys[0]) # TypeError: 'dict_keys' object is not subscriptable
print(list(keys)[0])
print(list(user.values()))
print(list(user.items()))

"""
7. 视图与列表快照的区别
    视图会跟随字典变化，转换出的列表是转换时的数据快照。
"""
print("=================7. 视图与列表快照的区别=================")
user = {"name": "Alice"}
keys_view = user.keys()
keys_snapshot = list(user.keys())

user["age"] = 25
print(keys_view)
print(keys_snapshot)

"""
8. 成员判断
"""
print("=================8. 成员判断=================")
user = {"name": "Alice", "age": 25}
print("name" in user.keys())
print("Alice" in user.values())
print(("age", 25) in user.items())

"""
9. keys() 和 items() 的集合运算
    keys() 视图支持交集、并集和差集等集合运算。
    items() 中的值可哈希时，也可以执行集合运算。
"""
print("=================9. keys() 和 items() 的集合运算=================")
user_a = {"name": "Alice", "age": 25}
user_b = {"name": "Bob", "city": "Shanghai"}
print(user_a.keys() & user_b.keys())
print(user_a.keys() | user_b.keys())
print(user_a.keys() - user_b.keys())

"""
10. 注意事项汇总
- keys()、values() 和 items() 返回视图对象，不是列表。
- 视图会动态反映原字典的变化。
- 视图不支持位置索引，需要时可以使用 list() 转换。
- items() 中的每个元素都是 (key, value) 元组，可以直接解包。
- keys() 适合判断和比较键集合，values() 适合遍历值，items() 适合同时遍历键和值。
"""
