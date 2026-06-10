# 列表常用方法-extend
from pathlib import Path

"""
1. 方法签名与基本用法
    list.extend(iterable)
1.1 参数：iterable —— 一个可迭代对象（如列表、元组、字符串、集合、字典、生成器等）。将可迭代对象的每个元素分别添加到末尾
1.2 返回值：None。该方法直接修改原列表，将 iterable 中的每个元素依次追加到末尾。
"""
print("=================方法签名与基本用法=================")
fruits = ['apple', 'banana']
fruits.extend(['cherry', 'date'])
print(fruits)   # ['apple', 'banana', 'cherry', 'date']

"""
2. 参数详解
2.1 任何可迭代对象
2.2 生成器/迭代器
2.3 不可迭代对象会引发 TypeError
"""
print("=================参数详解：任何可迭代对象=================")
a = [1, 2]
a.extend((3, 4))          # 元组
a.extend({5, 6})          # 集合
# 特别注意字符串：它会被视为字符的可迭代对象，每个字符单独成为列表元素，而不是整个字符串作为一个元素（这一点与 append 不同）。如果想将字符串整体加入，用 append。
a.extend('78')            # 字符串 → '7', '8'
a.extend({'x': 9, 'y': 10})  # 字典 → 只扩展键 'x', 'y'
print(a)   # [1, 2, 3, 4, 5, 6, '7', '8', 'x', 'y']

print("=================参数详解：生成器/迭代器=================")
def count_up_to(n):
    i = 1
    while i <= n:
        yield i # 把 i 的值返回给调用者；函数的状态（局部变量、执行位置等）被冻结保存，下次再取值时，会从 yield 的下一行继续执行 --> 生成器
        i += 1

nums = [0]
nums.extend(count_up_to(3))   # [0, 1, 2, 3]
print(nums)

print("=================参数详解：不可迭代对象会引发 TypeError=================")
# [1].extend(5)   # TypeError: 'int' object is not iterable

"""
3. 时间复杂度
    list.extend(iterable) 的时间复杂度为 O(k)，其中 k 是 iterable 中的元素数量。
3.1 底层会先计算可迭代对象的长度（如果是已知长度的序列，如列表、元组），一次性预留足够空间，然后将元素逐一复制到新位置，避免了多次动态扩容。这比循环调用 append() 更高效。
3.2 如果可迭代对象是生成器或长度未知，则会动态调整容量，但均摊时间复杂度仍是 O(k)。

空间复杂度：需要 O(k) 的额外空间用于存放新元素（在扩容时可能临时需要更多内存）。
"""
"""
4. 常见使用场景
4.1 合并多个列表
4.2 从文件读取行收集
4.3 扁平化一层嵌套
4.4 使用生成器动态添加
"""
print("=================常见使用场景：合并多个列表=================")
all_data = []
batches = ["1", "2", "3", "4", "5", "6", "7"]
for batch in batches:
    all_data.extend(batch)
print(all_data)

print("=================常见使用场景：从文件读取行收集=================")
list_date = []
sample_file = Path(__file__).resolve().parents[1] / "chapter_01" / "01_literal.py"
with sample_file.open("r") as file:
    for line in file:
        list_date.extend(line.strip().split(','))   # 将每行分割的单词展平加入
print(list_date)

print("=================常见使用场景：扁平化一层嵌套=================")
nested = [[1, 2], [3, 4], [5]]
flat = []
for sublist in nested:
    flat.extend(sublist)
print(flat)
flat = [item for sublist in nested for item in sublist] # --> 这个更常用
print(flat)

print("=================常见使用场景：使用生成器动态添加=================")
result = [0]
result.extend(x*2 for x in range(1, 4))   # 生成器表达式 # [0, 2, 4, 6]
print(result)

"""
5. 注意事项与易错点
5.1 字符串被拆成字符
5.2 修改原列表，别意外影响其他引用
5.3 扩展自身？小心无限循环
"""
print("=================注意事项与易错点：字符串被拆成字符=================")
a = ['hello']
a.extend(' world')   # 期望得到 ['hello', ' world'] 或 ['hello world']？
print(a)             # ['hello', ' ', 'w', 'o', 'r', 'l', 'd']

print("=================注意事项与易错点：修改原列表，别意外影响其他引用=================")
a = [1, 2]
b = a
a.extend([3])
print(b)   # [1, 2, 3]

print("=================注意事项与易错点：扩展自身？小心无限循环=================")
a = [1, 2]
a.extend(a)   # [1, 2, 1, 2]  → 先把自身元素读一遍再加入，操作完成时 a 变成长度 4
# 但如果 extend 的迭代器是动态依赖于列表本身的，比如：
"""
这里生成器表达式在迭代 a，同时 a 又被扩展
这种操作会产生什么结果？
生成器表达式会在 extend 内部不断从 a 获取下一个值，而 a 又被不断扩展，
可能导致迭代到新添加的元素，产生无限循环或 MemoryError。

永远不要在 extend 迭代同一个列表时，使用依赖于该列表的可迭代对象（除非你确切知道你在做什么）。
一个安全的操作是 a.extend(a)，它先获取 a 的完整视图（快照），然后一次性添加，所以不会死循环。
但使用生成器表达式时要格外小心。
"""
a = [1, 2]
# a.extend(x*2 for x in a)

"""
6. 与 += 的细微差别
6.1 list1 += list2 等价于 list1.extend(list2)，但 += 左侧必须是列表，右侧可以是任何可迭代对象。
6.2 对于不可变序列（如元组），+= 会创建新对象并重新绑定变量，而 extend 只能用于列表。
"""

"""
7. 性能：多次 append vs 一次 extend
    在循环中多次 append 不如用 extend 一次性加入一个生成器或列表。如果必须逐个判断，用列表推导式收集后再 extend。
"""

"""
8. 内部原理简述
    list.extend() 在 CPython 中的实现大致如下：
8.1 尝试获取可迭代对象的长度（如果支持 len，如列表、元组），调用 PyObject_LengthHint 得到一个估计长度。
8.2 确保列表有足够容量容纳新增元素，必要时调用 list_resize 一次扩容到位。
8.3 如果可迭代对象是列表或元组，使用快速路径：直接通过 memcpy 将内部数组的元素指针批量复制到列表末尾，并增加引用计数。
8.4 如果不是内置类型，遍历可迭代对象，对每个元素执行 PyList_Append（类似循环 append），但容量已预留，避免反复扩容。
8.5 更新列表长度。

因为有快速路径，extend(list) 极快，接近 O(k) 且常数极小。
"""
