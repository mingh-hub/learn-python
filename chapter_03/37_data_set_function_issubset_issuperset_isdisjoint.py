# 集合常用方法-issubset()、issuperset() 和 isdisjoint()

"""
1. 方法签名
    set.issubset(other)
        判断当前集合是否是 other 的子集，等价于 <=

    set.issuperset(other)
        判断当前集合是否是 other 的超集，等价于 >=

    set.isdisjoint(other)
        判断当前集合和 other 是否没有交集
"""

"""
2. issubset() 基本用法
    如果当前集合中的所有元素都在另一个集合中，返回 True。
"""
print("=================2. issubset() 基本用法=================")
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))
print(a <= b)

"""
3. issubset() 判断失败
"""
print("=================3. issubset() 判断失败=================")
a = {1, 5}
b = {1, 2, 3, 4}
print(a.issubset(b))

"""
4. issuperset() 基本用法
    如果当前集合包含另一个集合中的所有元素，返回 True。
"""
print("=================4. issuperset() 基本用法=================")
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))
print(a >= b)

"""
5. issubset() 和 issuperset() 的关系
    a 是 b 的子集，等价于 b 是 a 的超集。
"""
print("=================5. issubset() 和 issuperset() 的关系=================")
a = {"read", "comment"}
b = {"read", "comment", "delete", "update"}
print(a.issubset(b))
print(b.issuperset(a))

"""
6. 真子集和真超集
    < 判断真子集：左侧必须是右侧的子集，并且两个集合不能相等。
    > 判断真超集：左侧必须是右侧的超集，并且两个集合不能相等。
"""
print("=================6. 真子集和真超集=================")
a = {1, 2}
b = {1, 2, 3}
c = {1, 2}
print(a < b)
print(a < c)
print(b > a)
print(c > a)

"""
7. isdisjoint() 基本用法
    如果两个集合没有任何共同元素，返回 True。
"""
print("=================7. isdisjoint() 基本用法=================")
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))

"""
8. isdisjoint() 判断失败
    如果两个集合至少有一个共同元素，返回 False。
"""
print("=================8. isdisjoint() 判断失败=================")
a = {1, 2, 3}
b = {3, 4, 5}
print(a.isdisjoint(b))

"""
9. 使用交集理解 isdisjoint()
    a.isdisjoint(b) 等价于 len(a & b) == 0。
"""
print("=================9. 使用交集理解 isdisjoint()=================")
a = {"apple", "banana"}
b = {"orange", "pear"}
print(a & b)
print(len(a & b) == 0)
print(a.isdisjoint(b))

"""
10. 常见使用场景：权限检查
"""
print("=================10. 常见使用场景：权限检查=================")
required_permissions = {"read", "comment"}
user_permissions = {"read", "comment", "delete"}
danger_permissions = {"delete", "update"}

print(required_permissions.issubset(user_permissions))
print(user_permissions.issuperset(required_permissions))
print(required_permissions.isdisjoint(danger_permissions))

"""
11. 常见使用场景：判断两个用户是否没有共同好友
"""
print("=================11. 常见使用场景：判断两个用户是否没有共同好友=================")
user_a_friends = {"Alice", "Bob"}
user_b_friends = {"Tom", "Jack"}
user_c_friends = {"Bob", "Lucy"}

print(user_a_friends.isdisjoint(user_b_friends))
print(user_a_friends.isdisjoint(user_c_friends))

"""
12. 注意事项汇总
- issubset() 判断是否是子集，可以使用 <=。
- issuperset() 判断是否是超集，可以使用 >=。
- < 判断真子集，> 判断真超集。
- isdisjoint() 判断两个集合是否没有交集。
- 这些方法都返回布尔值 True 或 False，不会修改原集合。
"""
