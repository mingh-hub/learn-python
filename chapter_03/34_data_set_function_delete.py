# 集合常用方法-remove()、discard()、pop() 和 clear()

"""
1. 方法签名
    set.remove(element)
        删除指定元素，元素不存在会报 KeyError

    set.discard(element)
        删除指定元素，元素不存在不会报错

    set.pop()
        随机删除并返回集合中的一个元素，集合为空会报 KeyError

    set.clear()
        清空集合中的所有元素，返回 None
"""

"""
2. remove() 基本用法
    remove() 删除集合中的指定元素。
"""
print("=================2. remove() 基本用法=================")
fruits = {"apple", "banana", "orange"}
fruits.remove("banana")
print(fruits)

"""
3. remove() 删除不存在的元素
    如果元素不存在，remove() 会报 KeyError。
"""
print("=================3. remove() 删除不存在的元素=================")
fruits = {"apple", "orange"}
# fruits.remove("banana") # KeyError: 'banana'
print(fruits)

"""
4. discard() 基本用法
    discard() 也可以删除指定元素。
"""
print("=================4. discard() 基本用法=================")
fruits = {"apple", "banana", "orange"}
fruits.discard("banana")
print(fruits)

"""
5. discard() 删除不存在的元素
    如果元素不存在，discard() 不会报错。
"""
print("=================5. discard() 删除不存在的元素=================")
fruits = {"apple", "orange"}
fruits.discard("banana")
print(fruits)

"""
6. remove() 和 discard() 的区别
6.1 remove() 更严格，元素不存在时会报错。
6.2 discard() 更安全，元素不存在时什么都不做。
"""
print("=================6. remove() 和 discard() 的区别=================")
permissions = {"read", "write", "delete"}

if "delete" in permissions:
    permissions.remove("delete")
print(permissions)

permissions.discard("admin")
print(permissions)

"""
7. pop() 基本用法
    pop() 会从集合中随机删除并返回一个元素。
    因为集合无序，所以不能认为 pop() 一定删除某个固定元素。
"""
print("=================7. pop() 基本用法=================")
tasks = {"task1", "task2", "task3"}
task = tasks.pop()
print(task)
print(tasks)

"""
8. pop() 处理空集合
    空集合调用 pop() 会报 KeyError。
"""
print("=================8. pop() 处理空集合=================")
empty_set = set()
# empty_set.pop() # KeyError: 'pop from an empty set'
print(empty_set)

"""
9. 使用 pop() 消耗集合
    可以用 while 循环逐个取出并处理集合中的元素。
"""
print("=================9. 使用 pop() 消耗集合=================")
tasks = {"download", "parse", "save"}
while tasks:
    current_task = tasks.pop()
    print(current_task)
print(tasks)

"""
10. clear() 基本用法
    clear() 会清空集合中的所有元素。
"""
print("=================10. clear() 基本用法=================")
numbers = {1, 2, 3, 4}
result = numbers.clear()
print(numbers)
print(result) # None

"""
11. 常见使用场景：安全删除用户标签
"""
print("=================11. 常见使用场景：安全删除用户标签=================")
tags = {"python", "beginner", "note"}
tags.discard("beginner")
tags.discard("unknown")
print(tags)

"""
12. 注意事项汇总
- remove() 删除不存在的元素会报 KeyError。
- discard() 删除不存在的元素不会报错，更适合做安全删除。
- pop() 会随机删除并返回一个元素，不能指定删除目标。
- 空集合调用 pop() 会报 KeyError。
- clear() 会清空原集合，返回 None。
"""
