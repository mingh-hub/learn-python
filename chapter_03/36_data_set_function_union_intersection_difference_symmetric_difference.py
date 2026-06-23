# 集合常用方法-union()、intersection()、difference() 和 symmetric_difference()

"""
1. 方法签名
    set.union(*others)
        返回并集，等价于 |

    set.intersection(*others)
        返回交集，等价于 &

    set.difference(*others)
        返回差集，等价于 -

    set.symmetric_difference(other)
        返回对称差集，等价于 ^
"""

"""
2. union() 并集
    union() 返回所有集合中的全部元素，并自动去重。
"""
print("=================2. union() 并集=================")
python_students = {"Alice", "Bob", "Tom"}
java_students = {"Bob", "Jack", "Tom"}
result = python_students.union(java_students)
print(result)
print(python_students | java_students)

"""
3. union() 不修改原集合
"""
print("=================3. union() 不修改原集合=================")
a = {1, 2}
b = {2, 3}
c = a.union(b)
print(a)
print(b)
print(c)

"""
4. union() 合并多个集合
"""
print("=================4. union() 合并多个集合=================")
a = {1, 2}
b = {2, 3}
c = {3, 4}
print(a.union(b, c))

"""
5. intersection() 交集
    intersection() 返回多个集合中共同存在的元素。
"""
print("=================5. intersection() 交集=================")
python_students = {"Alice", "Bob", "Tom"}
java_students = {"Bob", "Jack", "Tom"}
result = python_students.intersection(java_students)
print(result)
print(python_students & java_students)

"""
6. intersection() 合并多个条件
"""
print("=================6. intersection() 合并多个条件=================")
python_students = {"Alice", "Bob", "Tom", "Lucy"}
java_students = {"Bob", "Tom", "Jack"}
go_students = {"Tom", "Jack", "Lucy"}
print(python_students.intersection(java_students, go_students))

"""
7. difference() 差集
    difference() 返回只存在于左侧集合、不存在于其他集合的元素。
"""
print("=================7. difference() 差集=================")
python_students = {"Alice", "Bob", "Tom"}
java_students = {"Bob", "Jack", "Tom"}
result = python_students.difference(java_students)
print(result)
print(python_students - java_students)
print(java_students - python_students)

"""
8. difference() 合并多个排除条件
"""
print("=================8. difference() 合并多个排除条件=================")
all_users = {"Alice", "Bob", "Tom", "Jack", "Lucy"}
blocked_users = {"Tom"}
inactive_users = {"Jack", "Lucy"}
active_users = all_users.difference(blocked_users, inactive_users)
print(active_users)

"""
9. symmetric_difference() 对称差集
    symmetric_difference() 返回只存在于其中一个集合、不同时存在于两个集合的元素。
"""
print("=================9. symmetric_difference() 对称差集=================")
a = {1, 2, 3}
b = {3, 4, 5}
result = a.symmetric_difference(b)
print(result)
print(a ^ b)

"""
10. 对称差集与差集的区别
    a - b：只要 a 中独有的元素。
    a ^ b：要 a 和 b 中各自独有的元素。
"""
print("=================10. 对称差集与差集的区别=================")
a = {"read", "write", "delete"}
b = {"read", "comment"}
print(a - b)
print(b - a)
print(a ^ b)

"""
11. 与 update 类方法的区别
    union()、intersection()、difference()、symmetric_difference() 会返回新集合，不修改原集合。
    update 类方法会直接修改原集合。
"""
print("=================11. 与 update 类方法的区别=================")
a = {1, 2, 3}
b = {3, 4}
result = a.union(b)
print(a)
print(result)

a.update(b)
print(a)

"""
12. 常见使用场景：权限计算
"""
print("=================12. 常见使用场景：权限计算=================")
default_permissions = {"read", "comment"}
admin_permissions = {"read", "comment", "delete", "update"}
disabled_permissions = {"delete"}

all_permissions = default_permissions.union(admin_permissions)
available_permissions = all_permissions.difference(disabled_permissions)
common_permissions = default_permissions.intersection(admin_permissions)

print(all_permissions)
print(available_permissions)
print(common_permissions)

"""
13. 注意事项汇总
- union() 求并集，可以使用 |。
- intersection() 求交集，可以使用 &。
- difference() 求差集，可以使用 -，左右顺序会影响结果。
- symmetric_difference() 求对称差集，可以使用 ^。
- 这些方法都会返回新集合，不会修改原集合。
"""
