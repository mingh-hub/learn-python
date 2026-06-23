# 集合常用方法-add() 和 update()

"""
1. 方法签名
    set.add(element)
        element：要添加到集合中的单个元素

    set.update(iterable)
        iterable：可迭代对象，例如列表、元组、字符串、集合、字典等
"""

"""
2. add() 基本用法
    add() 用来向集合中添加一个元素。
    如果元素已经存在，集合不会发生变化。
"""
print("=================2. add() 基本用法=================")
fruits = {"apple", "banana"}
fruits.add("orange")
print(fruits)

fruits.add("apple")
print(fruits) # 重复元素不会被添加

"""
3. add() 的返回值
    add() 会直接修改原集合，返回值是 None。
"""
print("=================3. add() 的返回值=================")
numbers = {1, 2, 3}
result = numbers.add(4)
print(numbers)
print(result) # None

"""
4. add() 添加不可变元素
    集合中的元素必须是不可变类型。
    数字、字符串、元组可以添加到集合中。
"""
print("=================4. add() 添加不可变元素=================")
s = set()
s.add(100)
s.add("Python")
s.add((1, 2))
print(s)

# s.add([1, 2]) # TypeError: unhashable type: 'list'
# s.add({1, 2}) # TypeError: unhashable type: 'set'

"""
5. update() 基本用法
    update() 用来一次性添加多个元素。
    update() 会把可迭代对象中的元素逐个加入集合。
"""
print("=================5. update() 基本用法=================")
fruits = {"apple", "banana"}
fruits.update(["orange", "pear"])
print(fruits)

fruits.update(("grape", "peach"))
print(fruits)

"""
6. update() 添加集合
    update() 可以接收另一个集合，相当于把两个集合合并到原集合中。
"""
print("=================6. update() 添加集合=================")
python_students = {"Alice", "Bob"}
new_students = {"Tom", "Jack", "Alice"}
python_students.update(new_students)
print(python_students)

"""
7. update() 添加字符串
    字符串也是可迭代对象，update("abc") 会把每个字符逐个加入集合。
"""
print("=================7. update() 添加字符串=================")
letters = set()
letters.update("hello")
print(letters) # {'h', 'e', 'l', 'o'}，重复的 l 只保留一个

"""
8. update() 添加字典
    字典也是可迭代对象，直接 update(dict) 时添加的是字典的键。
"""
print("=================8. update() 添加字典=================")
keys = set()
user = {"name": "Alice", "age": 25}
keys.update(user)
print(keys)

"""
9. add() 和 update() 的区别
9.1 add() 添加一个整体元素。
9.2 update() 添加可迭代对象中的每一个元素。
"""
print("=================9. add() 和 update() 的区别=================")
s1 = {"Python"}
s1.add("abc")
print(s1)

s2 = {"Python"}
s2.update("abc")
print(s2)

"""
10. 常见使用场景：收集去重数据
"""
print("=================10. 常见使用场景：收集去重数据=================")
visited_pages = set()
visited_pages.add("/home")
visited_pages.add("/detail")
visited_pages.add("/home")
print(visited_pages)

batch_pages = ["/search", "/detail", "/cart"]
visited_pages.update(batch_pages)
print(visited_pages)

"""
11. 注意事项汇总
- add() 接收一个元素，update() 接收一个可迭代对象。
- add() 和 update() 都会修改原集合，返回值都是 None。
- 添加重复元素时，集合不会新增重复数据。
- 集合中的元素必须是不可变类型。
- update("abc") 会添加 "a"、"b"、"c"，不是添加整个字符串 "abc"。
"""
