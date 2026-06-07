# 列表常用方法-remove

"""
1. 方法签名与基本用法
    list.remove(element)
    1.1 参数：element —— 要删除的元素值。可以是任意 Python 对象。
    1.2 返回值：None。该方法直接修改原列表，不返回被删除的元素。
    1.3 行为：从左到右扫描列表，删除第一个与 element 相等的元素。如果列表中没有该值，则引发 ValueError。
"""
fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
# fruits.remove('banana1') # ValueError: list.remove(x): x not in list
print(fruits)   # ['apple', 'cherry', 'banana']   (只删除了第一个 'banana')

"""
2. 参数说明与相等性判断
    remove 使用 == 运算符来判断元素是否相等，而不是 is（身份比较）。因此，对于自定义对象，其 __eq__ 方法决定了删除行为。
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

people = [Person('Alice', 12), Person('Bob', 22), Person('Alice', 28)]
people.remove(Person('Alice', 12))
print([(p.name, p.age) for p in people])

"""
3. 返回值与副作用
    remove 返回 None，这是一个常见的坑；所以一定不要 a = a.remove(2)，a 会变为 None
"""

print("=================返回值与副作用=================")
a = [1, 2, 3]
b = a.remove(2)   # b 是 None
print(a)          # [1, 3]
print(b)          # None

"""
4. 时间复杂度
    list.remove() 的时间复杂度为 O(n)：
    4.1 需要遍历列表以找到第一个匹配元素，最坏情况要扫描整个列表（元素在末尾或不存在） —— O(n)。
    4.2 找到后，将该位置之后的所有元素向前移动一位以填补空缺，移动操作也是 O(n)。
    4.3 总开销：O(n) 的搜索 + O(n) 的移动，但常数意义上仍然是 O(n)。
    4.4 如果需要根据索引精确删除，且已知索引，pop(index) 或 del list[index] 直接移动元素，但省去了搜索开销，不过删除非末尾元素时移动还是 O(n)。
"""

"""
5. 异常处理：ValueError
5.1 当要删除的元素在列表中不存在时，会立即抛出 ValueError。
5.2 因此，在不明确元素是否存在时，应先用 in 检查，或使用 try/except 捕获异常。
"""
nums = [1, 2, 3]
# nums.remove(4)   # ValueError: list.remove(x): x not in list

if 4 in nums:
    nums.remove(4)
# 或
try:
    nums.remove(4)
except ValueError:
    pass

"""
6. 常见使用场景
6.1 删除某个不需要的特定值
6.2 实现“如果存在则删除”
6.3 自定义对象按值删除
    利用 __eq__ 使得对象可删除，常用于管理任务列表、节点等。
"""

"""
7. 注意事项与易错点
7.1 在遍历列表时删除元素（经典陷阱）
    7.1.1. 直接 for item in list: 时删除会导致跳过元素或索引错乱。
        原因：删除后列表变短，循环的迭代器内部索引不会同步调整，从而漏掉紧接着的元素。
    7.1.2. 解决方法：
        a 使用列表推导式创建新列表（推荐）
        b 遍历副本，for/while 循环处理
        c 倒序遍历索引
7.2 试图删除所有匹配项
    remove 一次只删一个。若要删全部，可使用循环但注意上述陷阱，或直接用列表推导式。
7.3 可变对象相等性
    如果列表里是可变对象（如列表、字典），remove 比较的是值，但删除的是第一个匹配的对象实例，而非所有相等对象。同时注意对象在列表期间被修改可能导致不预期匹配。
"""
print("=================注意事项与易错点：在遍历列表时删除元素=================")
numbers = [1, 2, 2, 3, 4]
for num in numbers:
    if num == 2:
        numbers.remove(2) # 期望结果是 [1, 3, 4] ，但实际结果是 [1, 2, 3, 4] —— 跳过了第二个 2
print(numbers)

print("=================注意事项与易错点：使用列表推导式创建新列表=================")
numbers = [num for num in numbers if num != 2]
print(numbers) # [1, 3, 4]

print("=================注意事项与易错点：遍历副本=================")
numbers = [1, 2, 2, 3, 4]
for num in numbers[:]:
    if num == 2:
        numbers.remove(2)
print(numbers) # [1, 3, 4]

print("=================注意事项与易错点：倒序遍历索引=================")
numbers = [1, 2, 2, 3, 4]
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] == 2:
        del numbers[i]   # 或 numbers.pop(i)
print(numbers) # [1, 3, 4]

print("=================注意事项与易错点：试图删除所有匹配项=================")
# 删除所有的 2
numbers = [1, 2, 2, 3, 4]
while 2 in numbers:
    numbers.remove(2)   # 正确但效率低 O(n²)
# 更好的方式：
numbers = [x for x in numbers if x != 2]
print(numbers) # [1, 3, 4]

"""
8. 内部原理简述
list.remove() 的 C 实现大致步骤：
8.1 遍历底层数组，对每个元素调用 PyObject_RichCompareBool(item, value, Py_EQ)，直到找到第一个相等的。
8.2 若未找到，引发 ValueError。
8.3 若找到，计算该元素之后的元素个数，通过 memmove 将后续元素整体前移一位。
8.4 更新列表长度，并将原本最后一个位置设为 NULL 以帮助 GC。
因此，搜索和移动是主要的性能开销。
"""

"""
9. 替代方案与最佳实践
9.1 删除所有等于某值的元素：列表推导式 [x for x in lst if x != value] 或 filter()，时间复杂度 O(n)，且不会出现迭代时修改的问题。
9.2 按索引删除且需要被删值：使用 pop(index)。
9.3 按条件删除：同样用列表推导式或 filter，例如删除所有偶数 [x for x in lst if x % 2 != 0]。
9.4 频繁按值删除且数据量大：考虑改用 set 或 dict（如果需要保留顺序可用 collections.OrderedDict 或 Python 3.7+ 普通 dict），它们根据值直接定位删除，接近 O(1)。但注意元素需可哈希。
9.5 清空列表：list.clear() 或 del lst[:]，比逐个 remove 高效得多。
"""
