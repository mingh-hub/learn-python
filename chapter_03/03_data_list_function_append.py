# 列表常用方法-append

str = ["a", "b", "c", "d", "e"]

## append()：在列表的尾部追加元素
"""
list.append(item)
1. 方法签名与基本用法
    参数：接收一个参数 item，可以是任意 Python 对象（字符串，整数，列表，字典，自定义对象等）
    返回 None，该方法直接修改原列表，不返回新列表
    作用：原列表长度加 1，新元素被放在原列表最后位置
2. 时间复杂度
    append 的均摊时间复杂度为 O(1)。
    Python 列表底层使用动态数组实现，会预留额外空间。当容量不足时，会重新分配一块更大的内存并拷贝元素，这个扩容操作偶尔发生，但均摊到每次 append 上仍然是常数时间。
"""
str.append("f")
print(str)

str1 = ["g", "h", "i"]
str.append(str1) # 这个操作会在 str 中的 'f' 元素后增加一个列表元素对象
print(str)

"""
3. 常见使用场景与模式
    3.1 逐个构建列表
    3.2 收集满足条件的元素
    3.3 与循环、函数式编程结合
"""
print("=================常见使用场景与模式：逐个构建列表=================")
squares = []
for i in range(10):
    squares.append(i ** 2)
print(squares)

print("=================常见使用场景与模式：收集满足条件的元素=================")
even = []
for x in range(20):
    if x % 2 == 0:
        even.append(x)
print(even)

"""
4. 注意点
    4.1 返回值是 None
    4.2 可变对象的引用问题：如果多次 append 同一个可变对象（如列表、字典），它们指向的是同一块内存，修改其中一个会影响所有。
    4.3 在遍历列表时修改列表
"""
print("=================注意点：可变对象的引用问题=================")
container = []
obj = {'key': 0}
for i in range(3):
    obj['key'] = i
    container.append(obj)
print(container)   # [{'key': 2}, {'key': 2}, {'key': 2}]

print("=================注意点：在遍历列表时修改列表=================")
# a = [1, 2, 3]
# for item in a:
#     a.append(item * 2)   # 无限循环，列表不断增长
#     print(a)



