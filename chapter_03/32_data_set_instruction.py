# 数据容器：集合（set）

"""
1. 集合是数据容器中的一类，可以存储多个元素。
2. 定义
    s = {12, 13, 15, 99}
3. 特点
    3.1 可以存储不同类型的元素
    3.2 元素无序、不可重复、可以修改
    3.3 不支持索引和切片
4. 注意
    空集合必须使用 set() 定义，{} 定义的是空字典。
5. 集合常用于去重、成员判断、交集、并集、差集等场景。
"""

"""
2. 定义集合
"""
print("=================2. 定义集合=================")
s = {12, 13, 15, 99, 198, "A", "Hello", "Python"}
print(s)
print(type(s))

# 空集合必须使用 set()
empty_set = set()
print(empty_set)
print(type(empty_set))

empty_dict = {}
print(empty_dict)
print(type(empty_dict)) # dict

"""
3. 元素不可重复
    集合会自动去除重复元素。
"""
print("=================3. 元素不可重复=================")
s = {1, 2, 3, 2, 1, 4}
print(s)
print(len(s)) # 4

names = ["Alice", "Bob", "Alice", "Tom", "Bob"]
unique_names = set(names)
print(unique_names)

"""
4. 元素无序
    集合中的元素没有固定顺序，不能通过索引获取元素。
"""
print("=================4. 元素无序=================")
s = {"apple", "banana", "orange"}
print(s)
# print(s[0]) # TypeError: 'set' object is not subscriptable

"""
5. 添加元素
    add()：添加一个元素
    update()：添加多个元素，可以接收列表、元组、集合、字符串等可迭代对象
"""
print("=================5. 添加元素=================")
s = {"apple", "banana"}
s.add("orange")
print(s)

s.add("apple")
print(s) # 重复元素不会被添加

s.update(["pear", "grape"])
print(s)

s.update(("watermelon", "peach"))
print(s)

"""
6. 删除元素
    remove()：删除指定元素，元素不存在会报 KeyError
    discard()：删除指定元素，元素不存在不会报错
    pop()：随机删除并返回一个元素
    clear()：清空集合
"""
print("=================6. 删除元素=================")
s = {"apple", "banana", "orange", "pear"}
s.remove("banana")
print(s)

# s.remove("banana") # KeyError: 'banana'
s.discard("banana")
print(s)

value = s.pop()
print(value)
print(s)

s.clear()
print(s)

"""
7. 成员判断
    使用 in 和 not in 判断元素是否存在。
"""
print("=================7. 成员判断=================")
s = {"apple", "banana", "orange"}
print("apple" in s)
print("pear" in s)
print("pear" not in s)

"""
8. 遍历集合
    集合可以使用 for 循环遍历，但遍历顺序不固定。
"""
print("=================8. 遍历集合=================")
s = {"apple", "banana", "orange"}
for item in s:
    print(item)

"""
9. 集合运算：交集
    intersection() 或 &：获取两个集合中共同存在的元素。
"""
print("=================9. 集合运算：交集=================")
python_students = {"Alice", "Bob", "Tom"}
java_students = {"Bob", "Jack", "Tom"}
print(python_students.intersection(java_students))
print(python_students & java_students)

"""
10. 集合运算：并集
    union() 或 |：合并两个集合中的所有元素，并自动去重。
"""
print("=================10. 集合运算：并集=================")
python_students = {"Alice", "Bob", "Tom"}
java_students = {"Bob", "Jack", "Tom"}
print(python_students.union(java_students))
print(python_students | java_students)

"""
11. 集合运算：差集
    difference() 或 -：获取只存在于左侧集合、不存在于右侧集合的元素。
"""
print("=================11. 集合运算：差集=================")
python_students = {"Alice", "Bob", "Tom"}
java_students = {"Bob", "Jack", "Tom"}
print(python_students.difference(java_students))
print(python_students - java_students)
print(java_students - python_students)

"""
12. 集合运算：对称差集
    symmetric_difference() 或 ^：获取只存在于其中一个集合、不同时存在于两个集合的元素。
"""
print("=================12. 集合运算：对称差集=================")
python_students = {"Alice", "Bob", "Tom"}
java_students = {"Bob", "Jack", "Tom"}
print(python_students.symmetric_difference(java_students))
print(python_students ^ java_students)

"""
13. 集合关系判断
    issubset()：判断一个集合是否是另一个集合的子集
    issuperset()：判断一个集合是否是另一个集合的超集
    isdisjoint()：判断两个集合是否没有交集
"""
print("=================13. 集合关系判断=================")
a = {1, 2}
b = {1, 2, 3, 4}
c = {5, 6}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(c))

"""
14. 集合推导式
    集合推导式可以快速生成集合，并自动去重。
"""
print("=================14. 集合推导式=================")
numbers = [1, 2, 3, 4, 5, 2, 3]
even_numbers = {item for item in numbers if item % 2 == 0}
print(even_numbers)

square_numbers = {item ** 2 for item in numbers}
print(square_numbers)

"""
15. 集合元素的限制
    集合中的元素必须是不可变类型，例如数字、字符串、元组。
    列表、字典、集合本身是可变类型，不能作为集合元素。
"""
print("=================15. 集合元素的限制=================")
s = {1, "Python", (10, 20)}
print(s)

# s = {[1, 2], 3} # TypeError: unhashable type: 'list'
# s = {{1, 2}, 3} # TypeError: unhashable type: 'set'

"""
16. 常见应用场景：列表去重
    set() 可以快速去重，但会丢失原来的顺序。
"""
print("=================16. 常见应用场景：列表去重=================")
numbers = [1, 2, 3, 2, 1, 4, 5, 4]
unique_numbers = set(numbers)
print(unique_numbers)

"""
17. 常见应用场景：共同好友
"""
print("=================17. 常见应用场景：共同好友=================")
user_a_friends = {"Alice", "Bob", "Tom", "Jack"}
user_b_friends = {"Bob", "Tom", "Lucy"}
common_friends = user_a_friends & user_b_friends
print(common_friends)

"""
18. 常见应用场景：权限合并
"""
print("=================18. 常见应用场景：权限合并=================")
default_permissions = {"read", "comment"}
admin_permissions = {"read", "comment", "delete", "update"}
all_permissions = default_permissions | admin_permissions
print(all_permissions)

"""
19. 与列表、元组的区别
19.1 列表使用 []，元组使用 ()，集合使用 {}。
19.2 列表和元组有序，集合无序。
19.3 列表可以重复，元组可以重复，集合不可重复。
19.4 列表和集合可以修改，元组不可修改。
19.5 列表和元组支持索引、切片，集合不支持索引、切片。
"""
print("=================19. 与列表、元组的区别=================")
list_data = [1, 2, 2, 3]
tuple_data = (1, 2, 2, 3)
set_data = {1, 2, 2, 3}
print(list_data)
print(tuple_data)
print(set_data)

"""
20. 注意事项汇总
- 空集合必须写成 set()，{} 是空字典。
- 集合无序，不能使用索引和切片。
- 集合元素不可重复，重复元素会被自动去除。
- 集合本身可以修改，可以添加、删除、清空元素。
- 集合中的元素必须是不可变类型。
- 集合适合做去重、成员判断、交集、并集、差集等操作。
"""
