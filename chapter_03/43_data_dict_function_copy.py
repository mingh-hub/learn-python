# 字典常用方法-copy()

"""
1. 方法签名
    dictionary.copy()

    返回字典的浅拷贝。
    原字典和新字典是两个不同对象，但嵌套的可变对象仍然会被共享。
"""

"""
2. copy() 基本用法
"""
print("=================2. copy() 基本用法=================")
user = {"name": "Alice", "age": 25}
copied_user = user.copy()
print(user)
print(copied_user)
print(user is copied_user)

"""
3. copy() 的返回值
    copy() 返回一个新的 dict 对象，不修改原字典。
"""
print("=================3. copy() 的返回值=================")
settings = {"theme": "dark", "font_size": 16}
result = settings.copy()
print(result)
print(type(result))

"""
4. 修改浅拷贝的第一层数据
    两个字典本身相互独立，修改第一层数据不会相互影响。
"""
print("=================4. 修改浅拷贝的第一层数据=================")
original = {"name": "Alice", "age": 25}
copied = original.copy()

copied["name"] = "Bob"
copied["city"] = "Shanghai"
print(original)
print(copied)

"""
5. copy() 是浅拷贝
    嵌套的列表、字典等可变对象仍被两个字典共同引用。
"""
print("=================5. copy() 是浅拷贝=================")
original = {
    "name": "Alice",
    "skills": ["Python"],
    "address": {"city": "Shanghai"},
}
copied = original.copy()

copied["skills"].append("SQL")
copied["address"]["city"] = "Beijing"
print(original)
print(copied)
print(original["skills"] is copied["skills"])

"""
6. copy() 与直接赋值的区别
    直接赋值不会创建新字典，只是让两个变量指向同一个字典。
"""
print("=================6. copy() 与直接赋值的区别=================")
original = {"name": "Alice"}
same_dict = original
copied = original.copy()

same_dict["name"] = "Bob"
copied["name"] = "Tom"
print(original)
print(same_dict)
print(copied)
print(original is same_dict)
print(original is copied)

"""
7. 深拷贝
    需要连同嵌套对象一起复制时，可以使用 copy 模块的 deepcopy()。
"""
print("=================7. 深拷贝=================")
from copy import deepcopy

original = {"name": "Alice", "skills": ["Python"]}
deep_copied = deepcopy(original)
deep_copied["skills"].append("SQL")
print(original)
print(deep_copied)
print(original["skills"] is deep_copied["skills"])

"""
8. 常见使用场景：保留修改前的第一层数据
"""
print("=================8. 常见使用场景：保留修改前的数据=================")
config = {"theme": "light", "font_size": 14}
old_config = config.copy()

config.update({"theme": "dark", "font_size": 16})
print(old_config)
print(config)

"""
9. 注意事项汇总
- copy() 创建一个新的字典对象，不修改原字典。
- 直接赋值只复制引用，不会创建新字典。
- copy() 是浅拷贝，只复制字典本身，不复制嵌套的可变对象。
- 只修改第一层键值对时，浅拷贝通常已经足够。
- 需要让嵌套可变对象也相互独立时，使用 copy.deepcopy()。
"""
