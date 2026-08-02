# 字典常用方法-update()

"""
1. 方法签名
    dictionary.update([other], **kwargs)

    使用 other 或关键字参数中的键值对更新字典。
    键不存在时添加键值对，键已存在时覆盖原值。
    update() 直接修改原字典，返回 None。
"""

"""
2. 使用字典更新
"""
print("=================2. 使用字典更新=================")
user = {"name": "Alice", "age": 25}
user.update({"age": 26, "city": "Shanghai"})
print(user)

"""
3. 使用键值对序列更新
    other 可以是由二元序列组成的可迭代对象。
"""
print("=================3. 使用键值对序列更新=================")
user = {"name": "Alice"}
user.update([("age", 25), ("city", "Shanghai")])
print(user)

user.update((("email", "alice@example.com"), ("active", True)))
print(user)

"""
4. 使用关键字参数更新
    关键字参数的名称会作为字符串键。
"""
print("=================4. 使用关键字参数更新=================")
user = {"name": "Alice"}
user.update(age=25, city="Shanghai")
print(user)

"""
5. 同时使用 other 和关键字参数
    同一个键出现多次时，后处理的关键字参数会覆盖前面的值。
"""
print("=================5. 同时使用 other 和关键字参数=================")
settings = {"theme": "light"}
settings.update({"theme": "dark", "language": "zh-CN"}, theme="system")
print(settings)

"""
6. update() 的返回值
    update() 会直接修改原字典，返回值始终是 None。
"""
print("=================6. update() 的返回值=================")
user = {"name": "Alice"}
result = user.update({"age": 25})
print(user)
print(result)

"""
7. update() 与 | 的区别
    update() 修改原字典。
    | 返回一个合并后的新字典，不修改左右两侧的字典。
"""
print("=================7. update() 与 | 的区别=================")
defaults = {"theme": "light", "language": "zh-CN"}
custom = {"theme": "dark", "font_size": 16}

merged = defaults | custom
print(defaults)
print(merged)

defaults.update(custom)
print(defaults)

"""
8. update() 与 |= 的关系
    update() 和 |= 都会修改左侧字典。
    键冲突时都使用右侧的值。
"""
print("=================8. update() 与 |= 的关系=================")
data1 = {"a": 1, "b": 2}
data2 = {"b": 20, "c": 3}
data1 |= data2
print(data1)

"""
9. 常见场景：使用用户配置覆盖默认配置
"""
print("=================9. 常见场景：合并配置=================")
config = {
    "host": "127.0.0.1",
    "port": 8000,
    "debug": False,
}
user_config = {
    "port": 9000,
    "debug": True,
}
config.update(user_config)
print(config)

"""
10. 注意事项汇总
- update() 可以接收字典、键值对可迭代对象和关键字参数。
- 键不存在时新增，键存在时覆盖原值。
- update() 直接修改原字典，返回 None。
- 关键字参数产生的键一定是字符串。
- Python 3.9 及以后，| 返回新字典，|= 修改原字典。
"""
