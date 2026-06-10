# 列表常用方法-index

"""
1. 方法签名与基本用法
    list.index(value, start=0, stop=len(list))
1.1 参数
    value：要查找的元素，必选。---> 如果 value 在列表内找不到，会报：ValueError: list.index(x): x not in list
    start：开始查找的起始索引（包含），可选，默认 0。
    stop：结束查找的索引（不包含），可选，默认 len(list)，即搜索到列表末尾。
1.2 返回值：value 在列表中的第一个匹配项的索引（整数）。
1.2 原列表不会被修改，纯粹是查询方法。
"""
print("=================方法签名与基本用法=================")
colors = ['red', 'green', 'blue', 'green']
print(colors.index('green', 2, 10))  # 3
print(colors.index('blue'))    # 2

"""
2. 参数详解
2.1 value 参数
    要查找的元素，通过 == 运算符进行比较。可以是任何对象。
    由于比较依赖 ==，自定义类可以重写 __eq__ 来控制查找行为。
2.2 start 和 stop 参数
    指定搜索的切片范围 [start, stop)，行为与切片完全一致：包含 start，不包含 stop。
    如果 start 省略，默认为 0。
    如果 stop 省略，默认为 len(list)。
    start 和 stop 可以超出列表实际长度，Python 会将其截断到有效范围内，但不建议过分依赖这种隐式截断。
    支持负数索引，与切片规则相同
"""
print("=================参数详解：value 参数=================")
print([1, 2, 3].index(2))  # 整数
print(['a', 'b'].index('a'))  # 字符串
print([[1, 2], [3, 4]].index([1, 2]))  # 列表（比较值）

print("=================参数详解：start 和 stop 参数=================")
numbers = [10, 20, 30, 20, 40]

# 从索引 2 开始找 20
print(numbers.index(20, 2))   # 3
# print(numbers.index(20, len(numbers)))   # ValueError: list.index(x): x not in list

# 在索引 1~3 (不包括3) 的范围找 30
print(numbers.index(30, 1, 3)) # 2

# 搜索索引为 -3, -2 的元素，即 [10, 15]，找到 10 在索引 1
a = [5, 10, 15, 10]
print(a.index(10, -3, -1))

"""
3. 异常处理：ValueError
3.1 如果要查找的值在指定范围内不存在，会抛出 ValueError，这是与 find()（字符串方法，返回 -1）不同的设计。
3.2 因此，在不明确值是否存在时，有几种安全的处理方式：
    使用 in 检查
    try/except（推荐，EAFP 风格）
    利用条件表达式包装，但依然可能两次遍历
"""
print("=================异常处理：ValueError=================")
lst = [1, 2, 3]
# lst.index(4)   # ValueError: 4 is not in list

# 使用 in 检查，但是会有一个问题，in 和 index 会遍历两次列表
value = 100
if value in lst:
    idx = lst.index(value)
    print(idx)

# try/except（推荐，EAFP 风格）
try:
    idx = lst.index(value)
    print(idx)
except ValueError:
    idx =-1
print(idx)

"""
4. 时间复杂度
    list.index() 执行的是线性搜索，时间复杂度为 O(n)，n 为搜索范围内的元素个数。
4.1 最好情况：元素在 start 位置，O(1)。
4.2 最坏情况：元素在 stop-1 位置或不存在，需要遍历整个搜索区间，O(n)。
4.3 空间复杂度：O(1)，不需要额外空间。

这意味着对于大型列表，频繁调用 index() 可能成为性能瓶颈。如果需要多次按值查找，可以考虑：
1. 构建一个值到索引的字典 {value: index}，提供 O(1) 的查找（但内存开销较大，且只能记录一个索引）。
2. 如果顺序不重要，使用 set 或 dict 等哈希结构。
"""

"""
5. 与 in 操作符的比较
x in lst  -> 判断是否存在 -> 布尔值 -> 无异常
lst.index(x) -> 返回索引 -> 整数 -> ValueError
"""

"""
6. 查找多个匹配项的方法
    index() 只能找到第一个匹配。要找到所有匹配项的索引，可以使用
6.1 列表推导式 + enumerate
6.2 循环逐步查找，使用 start 参数
"""
print("=================查找多个匹配项的方法：列表推导式 + enumerate=================")
lst = [10, 20, 10, 30, 10]
# enumerate(lst) 遍历列表的同时，返回每个元素的 索引 和 值，形如 (索引, 值) 的配对。
# (i, v) --> (索引, 值)
indices = [i for i, v in enumerate(lst) if v == 10]
print(indices)

print("=================查找多个匹配项的方法：循环逐步查找，使用 start 参数=================")

def find_all(lst, value):
    indices = []
    start = 0
    while True:
        try:
            idx = lst.index(value, start)
            indices.append(idx)
            start = idx + 1
        except ValueError:
            break
    return indices

print(find_all(lst, 30))
print(find_all(lst, 40))

"""
7. 常见使用场景
7.1 获取元素位置
7.2 判断是否存在并获取索引（try/except）
7.3 在切片范围内搜索
7.4 自定义对象查找
"""
print("=================常见使用场景：在切片范围内搜索=================")
log = ['INFO', 'WARN', 'ERROR', 'WARN', 'INFO']
first_warn_after_index_1 = log.index('WARN', 2)   # 返回 3
print(first_warn_after_index_1)

print("=================常见使用场景：自定义对象查找=================")
class Task:
    def __init__(self, name):
        self.name = name
    def __eq__(self, other):
        return self.name == other.name

tasks = [Task('A'), Task('B'), Task('C')]
pos = tasks.index(Task('B'))   # 1，依赖 __eq__
print(pos)

"""
8. 注意事项与易错点
8.1 元素不存在抛出异常
8.2 start/stop 索引范围与切片相同
8.3 不要与 find() 混淆
    list 没有 find() 方法，字符串才有。字符串的 find() 找不到时返回 -1，而列表的 index() 抛出异常。这是 Python 中不一致的设计，也是新手常犯错误。
8.4 在循环中修改列表再查找
    如果列表在查找期间被修改（例如多线程或错误逻辑），结果可能不符合预期。index() 并不会快照列表，而是在当前状态下搜索。
8.5 浮点数比较问题
    由于浮点精度，index() 可能找不到理论上相等的值，尤其是经过计算后的浮点数。推荐使用 math.isclose 配合循环比较，或使用 decimal.Decimal。
8.6  性能敏感性
    在大型列表或循环内反复调用 index() 会拖慢程序，考虑改用字典映射值到索引。
"""

"""
9. 内部原理简述
CPython 实现中，list.index() 主要过程为：
-> 标准化 start 和 stop 索引（处理负数，限制在有效范围内）。
-> 从 start 索引开始循环，一直到 stop-1
-> 对每个元素调用 PyObject_RichCompareBool(item, value, Py_EQ)（即 == 比较）。
-> 如果返回 1（真），立即返回当前索引。
-> 如果循环结束仍未找到，引发 ValueError，消息包含 " x not in list"。

由于比较操作可能触发 Python 代码（如自定义 __eq__），这使得最坏情况耗时不仅与列表长度有关，还受比较开销影响。
"""
