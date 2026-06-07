# 列表常用方法-insert

"""
1. 方法签名与基本用法：list.insert(index, object)
    参数
        index：整数，表示插入位置的索引。新元素会被放置在该索引所指元素的前面。
        object：要插入的对象，可以是任意 Python 类型，如数字，字符串，列表，字典，None等
    返回值：None
    作用：列表长度增加 1，插入位置及之后的所有元素都会向后移动一位。
"""

list = [1, 3, 5, 7, 9]
print(list)

res = list.insert(1, 2)
print(res) # None
print(list)

"""
2. 索引的详细规则
    index 参数支持负数以及超出列表长度的值，Python 会自动进行边界处理。
    支持反向索引插入
"""
list.insert(10, 10) # 超大正索引，Python 会自动进行边界处理
print(list)

list.insert(0, 0) # 插入开头
print(list)

list.insert(len(list), 99) # 插入末尾，等价于 list.apend()
print(list)

list.insert(-1, 98) # 反向索引插入
print(list)

"""
3. 时间复杂度：O(n)
    3.1 list.insert() 的时间复杂度是 O(n)，其中 n 是列表当前的长度。
        原因：列表底层是连续内存的数组。在任意位置插入元素，需要将该位置之后的所有元素依次向后移动一位，以便腾出空间。插入位置越靠前，需要移动的元素越多。
    3.2 最坏情况：在索引 0 插入，需要移动全部 n 个元素，耗时 O(n)。
        最好情况：在末尾插入（index >= len），移动 0 个元素，此时相当于 append，但 append 本身就是为末尾添加设计的，效率更高（均摊 O(1)）。
    3.3 因此，如果需要频繁在列表头部或中间插入元素，list 并不是最佳数据结构，应优先考虑 collections.deque（双端队列，头尾插入 O(1)）或链表等。
"""

"""
4. 常见使用场景
    4.1 在列表指定位置插入元素
    4.2 维持有序列表（如插入排序）
        对大数据量建议使用 bisect 模块的 insort，底层也是 O(n)，但查找位置是 O(log n)
    4.3 构建嵌套结构
"""
print("=================常见使用场景：在列表指定位置插入元素=================")
queue = ['task1', 'task3']
queue.insert(1, 'task2')   # ['task1', 'task2', 'task3']
print(queue)

print("=================常见使用场景：维持有序列表=================")
sorted_list = [1, 5, 8, 10]
new_val = 6
for i, v in enumerate(sorted_list):
    if v > new_val:
        sorted_list.insert(i, new_val)
        break
else:
    sorted_list.append(new_val)
print(sorted_list)   # [1, 5, 6, 8, 10]

print("=================常见使用场景：构建嵌套结构=================")
matrix = []
matrix.insert(0, [3, 4])
matrix.insert(0, [1, 2])
print(matrix) # [[3, 4], [1, 2]]

"""
5. 注意事项与易错点
    5.1 返回值是 None，不要误用赋值
    5.2 可变对象引用问题
        如果多次插入同一个可变对象，它们会指向同一块内存，修改一个会影响所有。
    5.3 遍历列表时使用 insert
        在 for 循环中遍历列表的同时向列表插入元素，会导致索引混乱甚至无限循环。
    5.4 性能陷阱：循环内头部插入
        如果需要“后进先出”的顺序，可以用 append 然后 reverse，或者使用 collections.deque 的 appendleft。
"""

print("=================注意事项与易错点：返回值是 None，不要误用赋值=================")
a = [1, 2]
b = a.insert(0, 0)   # b 是 None
print(a)             # [0, 1, 2]
print(b)             # None

print("=================注意事项与易错点：可变对象引用问题=================")
obj = {'count': 0}
lst = []
for i in range(3):
    obj['count'] = i
    lst.insert(0, obj)
print(lst)   # [{'count': 2}, {'count': 2}, {'count': 2}]

print("=================注意事项与易错点：遍历列表时使用 insert=================")
# a = [2, 4, 6]
# for item in a:
#     if item % 2 == 0:
#         a.insert(0, item * 10)   # 无限循环，a 不断增长
#         print(a)

print("=================注意事项与易错点：性能陷阱=================")
result = []
for i in range(100):
    result.insert(0, i)    # 每次 O(n)，总复杂度 O(n²)

"""
6. 内部原理简述
    6.1 Python 列表底层是一个 C 的数组（PyObject **ob_item），记录了元素指针。执行 insert(index, item) 时，C 函数大致做：
        -> 检查索引并标准化（负数转换、越界修正）。
        -> 确保列表容量足够（若容量不足，先扩容，类似 append 的机制）。
        -> 将 index 位置及之后的所有元素通过 memmove 向后移动一个位置。
        -> 将新元素指针放入 index 位置。
        -> 更新列表长度。
    6.2 这种数组移动操作是 insert 性能开销的主要来源。
"""
