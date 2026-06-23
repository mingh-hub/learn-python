# 集合常用方法-copy()

"""
1. 方法签名
    set.copy()

    返回一个集合的浅拷贝。
    原集合和新集合是两个不同对象。
"""

"""
2. copy() 基本用法
"""
print("=================2. copy() 基本用法=================")
numbers = {1, 2, 3}
new_numbers = numbers.copy()
print(numbers)
print(new_numbers)
print(numbers is new_numbers) # False

"""
3. copy() 的返回值
    copy() 返回一个新的 set 对象。
"""
print("=================3. copy() 的返回值=================")
fruits = {"apple", "banana"}
result = fruits.copy()
print(result)
print(type(result))

"""
4. 修改拷贝后的集合
    拷贝后，对新集合做添加或删除，不会影响原集合。
"""
print("=================4. 修改拷贝后的集合=================")
origin = {"read", "write"}
backup = origin.copy()

backup.add("delete")
backup.discard("read")

print(origin)
print(backup)

"""
5. copy() 是浅拷贝
    集合中的元素必须可哈希，通常是不可变对象。
    如果元素是元组，元组本身可以被共享，但元组不可变，所以一般不会产生修改联动问题。
"""
print("=================5. copy() 是浅拷贝=================")
points = {(0, 0), (1, 2)}
copied_points = points.copy()
print(points)
print(copied_points)
print(points is copied_points)

"""
6. copy() 与直接赋值的区别
    直接赋值不会创建新集合，只是让两个变量指向同一个集合。
"""
print("=================6. copy() 与直接赋值的区别=================")
s1 = {1, 2, 3}
s2 = s1
s3 = s1.copy()

s2.add(4)
s3.add(5)

print(s1)
print(s2)
print(s3)
print(s1 is s2) # True
print(s1 is s3) # False

"""
7. 常见使用场景：保留修改前的数据
"""
print("=================7. 常见使用场景：保留修改前的数据=================")
permissions = {"read", "comment"}
old_permissions = permissions.copy()

permissions.add("delete")
permissions.add("update")

print(old_permissions)
print(permissions)

"""
8. 注意事项汇总
- copy() 会创建一个新的集合对象。
- copy() 不会修改原集合。
- 直接赋值不会复制集合，只是复制变量引用。
- 需要保留原集合状态时，可以先使用 copy()。
"""
