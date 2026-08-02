# 字典删除操作-del、pop()、popitem() 和 clear()

"""
1. 操作与方法签名
    del dictionary[key]
        删除指定键值对，键不存在会报 KeyError。

    dictionary.pop(key[, default])
        删除指定键值对并返回对应的值。
        键不存在且没有提供 default 时会报 KeyError。

    dictionary.popitem()
        删除并返回最后插入的 (key, value) 键值对。
        字典为空时会报 KeyError。

    dictionary.clear()
        清空字典，返回 None。
"""

"""
2. del 删除指定键值对
"""
print("=================2. del 删除指定键值对=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
del user["city"]
print(user)

# del user["email"] # KeyError: 'email'

"""
3. pop() 删除并返回值
"""
print("=================3. pop() 删除并返回值=================")
user = {"name": "Alice", "age": 25}
age = user.pop("age")
print(age)
print(user)

"""
4. pop() 删除不存在的键
    提供 default 后，键不存在时返回 default，不会报错。
"""
print("=================4. pop() 删除不存在的键=================")
user = {"name": "Alice"}
# user.pop("age") # KeyError: 'age'
print(user.pop("age", 0))
print(user)

"""
5. popitem() 删除最后插入的键值对
    Python 3.7 及以后，popitem() 按后进先出顺序删除。
"""
print("=================5. popitem() 删除最后插入的键值对=================")
user = {"name": "Alice", "age": 25, "city": "Shanghai"}
item = user.popitem()
print(item)
print(user)

"""
6. popitem() 处理空字典
"""
print("=================6. popitem() 处理空字典=================")
empty_dict = {}
# empty_dict.popitem() # KeyError: 'popitem(): dictionary is empty'
print(empty_dict)

"""
7. 使用 popitem() 逐个处理数据
"""
print("=================7. 使用 popitem() 逐个处理数据=================")
tasks = {
    "download": "下载数据",
    "parse": "解析数据",
    "save": "保存数据",
}

while tasks:
    task_name, description = tasks.popitem()
    print(task_name, description)

print(tasks)

"""
8. clear() 清空字典
"""
print("=================8. clear() 清空字典=================")
user = {"name": "Alice", "age": 25}
result = user.clear()
print(user)
print(result)

"""
9. clear() 与重新赋值的区别
    clear() 清空原对象，所有引用都会看到变化。
    重新赋值只让当前变量指向一个新字典，不影响原对象的其他引用。
"""
print("=================9. clear() 与重新赋值的区别=================")
data = {"name": "Alice"}
same_data = data
data.clear()
print(data)
print(same_data)

data = {"name": "Bob"}
same_data = data
data = {}
print(data)
print(same_data)

"""
10. 注意事项汇总
- del 删除指定键，键不存在会报 KeyError。
- pop() 删除指定键并返回值，可以提供键不存在时的默认值。
- popitem() 删除并返回最后插入的键值对，返回值是元组。
- 空字典调用 popitem() 会报 KeyError。
- clear() 清空原字典并返回 None，其他引用也会看到字典被清空。
"""
