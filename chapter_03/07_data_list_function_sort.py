# 列表常用方法-sort

"""
1. 方法签名与基本用法
    list.sort(*, key=None, reverse=False)
1.1 * 并不是一个参数，而是一个语法分隔符，表示它后面的所有参数都必须是仅限关键字参数（keyword-only arguments）。
1.2 key：一个函数（或 None），用于在比较前对每个元素进行预处理，排序将基于该函数的返回值进行。默认为 None，表示直接比较元素本身。
1.3 reverse：布尔值，False 表示升序（默认），True 表示降序。
1.4 返回值：None，该方法直接修改原列表，不返回新列表。
"""
numbers = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers)   # [1, 1, 3, 4, 5, 9]

numbers.sort(reverse=True)
print(numbers)   # [9, 5, 4, 3, 1, 1]

words = ['banana', 'apple', 'Cherry']
words.sort(key=str.lower)
print(words)  # ['apple', 'banana', 'Cherry']

"""
2. key 参数详解
    key 是排序中最强大的功能。它接受一个单参数函数，该函数会被作用于列表中的每一个元素，排序依据的是函数的返回值，而原始元素不变。
    拿 key=len 来举例，len(str) 是一个单参数函数，返回长度，reverse=False 表示按列表中元素长度升序排列
2.1 按字符串长度排序
2.2 使用 lambda 表达式
2.3 使用 operator.itemgetter 或 attrgetter
    对列表中的字典或对象按特定字段排序，可以用标准库的便捷函数。
    对于自定义对象，用 attrgetter。
2.4 多级排序
    由于 sort() 是稳定的，你可以通过多次调用来实现多级排序（优先级从低到高）。
2.5 不区分大小写的字符串排序
"""
print("=================key 参数详解：按字符串长度排序=================")
words = ['apple', 'banana', 'kiwi', 'fig']
words.sort(key=len)
print(words)   # ['fig', 'kiwi', 'apple', 'banana']

print("=================key 参数详解：使用 lambda 表达式=================")
students = [('Alice', 22), ('Bob', 18), ('Charlie', 20)]
students.sort(key=lambda student: student[1])   # 按年龄排序，1 是下标，第二个参数为年龄
print(students)  # [('Bob', 18), ('Charlie', 20), ('Alice', 22)]

print("=================key 参数详解：使用 operator.itemgetter 或 attrgetter=================")
# 对列表中的字典或对象按特定字段排序，可以用标准库的便捷函数。
from operator import itemgetter

records = [
    {'name': 'Bob', 'score': 85},
    {'name': 'Alice', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]
records.sort(key=itemgetter('score'))
print(records) # 按 score 升序：Charlie(78), Bob(85), Alice(92)

# 对于自定义对象，用 attrgetter。
from operator import attrgetter

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __repr__(self):
        return f'{self.name}({self.grade})'

s = [Student('Bob', 85), Student('Alice', 92)]
s.sort(key=attrgetter('grade'))
print(s)   # [Bob(85), Alice(92)]

print("=================key 参数详解：多级排序=================")
# 由于 sort() 是稳定的，你可以通过多次调用来实现多级排序（优先级从低到高）。
data = [('Bob', 'B'), ('Alice', 'A'), ('Bob', 'A'), ('Alice', 'B')]
# 先按次要关键字排序（优先级低）
data.sort(key=lambda x: x[1])   # 按字母
# 再按主要关键字排序（优先级高）
data.sort(key=lambda x: x[0])   # 按姓名
print(data)  # [('Alice', 'A'), ('Alice', 'B'), ('Bob', 'A'), ('Bob', 'B')]

# 也可以一次性用元组作为 key 返回值实现多级排序
data.sort(key=lambda x: (x[0], x[1]))
print(data)

print("=================key 参数详解：不区分大小写的字符串排序=================")
names = ['alice', 'Bob', 'CHARLIE']
names.sort(key=str.lower)
print(names)   # ['alice', 'Bob', 'CHARLIE']

"""
3. reverse 参数
    reverse=False（默认）：从小到大，升序。
    reverse=True：从大到小，降序。
reverse 只是简单地反转比较结果，不会影响排序的稳定性。
"""

"""
4. 返回值 — 最常见的陷阱
    sort() 返回 None
    绝对不要写 a = a.sort()，否则 a 会变成 None，列表丢失。
"""

"""
5. 排序稳定性
    Python 的 list.sort() 是稳定的，即当两个元素的排序键相等时，它们在列表中的原始相对顺序会被保留。
"""
print("=================排序稳定性=================")
pairs = [(1, 'b'), (1, 'a'), (2, 'c'), (2, 'd')]
pairs.sort(key=lambda x: x[0])   # 按数字排序，数字相等时保持原顺序 # 结果: [(1, 'b'), (1, 'a'), (2, 'c'), (2, 'd')]
print(pairs)

"""
6. 时间复杂度与算法
    list.sort() 使用 Timsort 算法，是一种自适应、稳定、混合型排序算法，结合了归并排序和插入排序。
6.1 最坏时间复杂度：O(n log n)
6.2 最好情况：O(n)（列表已基本有序时）
6.3 空间复杂度：O(n)（归并时需要临时空间）
6.4 稳定性：稳定
"""

"""
7. 排序的元素必须可比较
7.1 不同类型元素不能排序
    Python 3 中，如果列表包含不能直接比较的类型（如字符串和整数），调用 sort() 会引发 TypeError。
7.2 自定义对象排序
    对于自定义类的实例，如果需要排序，必须实现 __lt__（小于）方法，或者通过 key 提取出可比较的值。
"""
print("=================排序的元素必须可比较：不同类型元素不能排序=================")
a = [3, '1']
# a.sort()   # TypeError: '<' not supported between instances of 'str' and 'int'
a.sort(key=lambda x: str(x))   # 按字符串比较，结果 ['1', 3]
print(a)

print("=================排序的元素必须可比较：自定义对象排序=================")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __lt__(self, other):
        return self.age < other.age
    def __repr__(self):
        return f'{self.name}({self.age})'

people = [Person('Bob', 25), Person('Alice', 20)]
people.sort()   # 按年龄排序
print(people)   # [Alice(20), Bob(25)]

"""
8. 与 sorted() 的对比
8.1 作用对象：只能用于列表 --> 任意可迭代对象（列表、元组、字符串、字典、集合等）
8.2 返回值：None，原地修改 --> 返回一个新的排序后的列表
8.3 是否修改原序列：是 --> 否
8.4 参数：key, reverse --> iterable, key, reverse
8.5 使用场景：无需保留原列表，追求效率 --> 需要保留原序列，或对非列表排序
"""
print("=================与 sorted() 的对比=================")
# sorted 返回新列表
tup = (3, 1, 2)
sorted_tup = sorted(tup)   # [1, 2, 3]，原元组不变
print(sorted_tup)

# 对字典排序
d = {'c': 1, 'a': 2, 'b': 3}
sorted_keys = sorted(d)    # 按键排序
print(sorted_keys)
sorted_items = sorted(d.items(), key=lambda x: x[1])  # 按值排序
print(sorted_items)

"""
9. 常见使用场景
"""
print("=================常见使用场景=================")
# 9.1 简单数字或字符串排序
names = ['Zoe', 'alice', 'Bob']
names.sort()   # 按 Unicode 码点排序，大写字母在小写前面 # ['Bob', 'Zoe', 'alice']
print(names)

# 9.2 不区分大小写排序
names.sort(key=str.lower) # ['alice', 'Bob', 'Zoe']
print(names)

# 9.3 按对象属性排序
products = [{'name': 'B', 'price': 20}, {'name': 'A', 'price': 30}]
products.sort(key=lambda p: p['price'])
print(products)

# 9.4 多条件排序（先价格后名称）
products.sort(key=lambda p: (p['price'], p['name']))
print(products)

# 9.5 降序排列并取前 N 个
scores = [88, 92, 75, 92, 85]
scores.sort(reverse=True)
top3 = scores[:3]
print(top3) # [92, 92, 88]

"""
10. 注意事项与易错点
10.1 sort() 返回 None：不能赋值给变量期望得到排序后的列表。
10.2 不同类型元素混合排序：会引发 TypeError，需统一类型或使用 key 转换。
10.3 reverse 参数是关键字参数：必须写 reverse=True，不能写成 True 作为位置参数（如 sort(True) 会报错，因为现在方法定义中的 * 禁止了位置参数，在 Python 3 中会提示 TypeError，早期 Python 2 可能允许但行为古怪）。
10.4 不可变序列（如元组）没有 sort 方法：必须用 sorted() 生成新列表。
10.5 对列表本身排序时，如果列表元素是可变对象，排序后原列表会调整顺序，但不会影响元素内部状态。
10.6 key 函数会被多次调用：确保 key 函数是快速的，没有副作用；Python 内部会对每个元素调用一次 key 并缓存计算结果，但依赖具体实现（Timsort 中会使用“装饰-排序-去装饰”技术，即先计算所有 key，然后排序，因此 key 函数只执行一次）。
10.7 稳定性可用于复杂排序，但注意多次排序时顺序：若希望先按 A 降序再按 B 升序（A 优先级高于 B），可通过一次排序用复合 key 实现：key=lambda x: (-x.A, x.B) 或分步排序（先排 B 再排 A，并确保 A 排序稳定）。
"""

"""
11. 内部原理简述

Python 的 list.sort() 底层采用 Timsort，核心思想：
1. 扫描列表，识别并收集已有序的连续段（称为 run）。
2. 如果 run 长度小于一个最小值（通常 32），就使用二分插入排序扩展它。
3. 反复将相邻的 run 合并（merge），合并过程是稳定的。
4. 在合并时利用临时数组，当合并区域近似有序时做优化。

这种策略使得近乎有序的数据排序极快（O(n)），且在最坏情况下保持 O(n log n)，空间复杂度为 O(n)。

对于 key 参数，Python 会执行“装饰-排序-去装饰”的优化：先遍历列表，对每个元素调用 key 函数生成一个装饰元组 (key_value, original_value)；
然后对装饰后的列表排序；最后去除装饰恢复原始元素。这样每个 key 函数只被调用一次，且排序过程中直接比较 key_value。
"""

"""
12. 性能优化建议

1. 尽量使用 list.sort() 而不是 sorted() 如果不需要保留原列表，因为 sort() 避免了一次列表复制。
2. key 函数应选择开销小的操作，避免复杂计算或 I/O。operator 模块的 itemgetter、attrgetter 通常比 lambda 更快。
3. 如果需要多次按不同 key 排序，可考虑一次复合 key，而不是多次调用 sort()，后者虽然稳定但会有额外遍历开销。
4. 对于极大列表，注意内存占用；Timsort 需要 O(n) 额外空间，通常不成问题。
5. 如果只关心前 K 个最大/最小元素，使用 heapq.nlargest / nsmallest 比完整排序更高效。
"""
