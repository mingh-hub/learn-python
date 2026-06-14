# 数据容器：元组（tuple）

"""
1. 元组是数据容器中的一类，可以存储多个元素。
2. 定义
    t = (12, 13, 15, 99)
3. 特点
    3.1 可以存储不同类型的元素
    3.2 元素有序、可以重复、不可修改
    3.3 支持索引、切片、遍历、组包、解包等序列操作
4. 注意
    只有一个元素的元组，必须在元素后面加逗号，例如：("Python",)
5. 元组属于序列类型，列表、字符串、元组都属于序列。
"""

"""
2. 定义元组
"""
print("=================定义元组=================")
t = (12, 13, 15, 99, 198, "A", "Hello", "Python")
print(t)
print(type(t))

# 省略小括号也可以创建元组
t2 = 1, 2, 3
print(t2)
print(type(t2))

"""
3. 单元素元组
    单元素元组必须加逗号，否则小括号只表示普通分组。
"""
print("=================单元素元组=================")
t = ("Python")
print(t)
print(type(t)) # str

t = ("Python",)
print(t)
print(type(t)) # tuple

t = "Python",
print(t)
print(type(t)) # tuple

"""
4. 获取元素
    元组支持正向索引和反向索引。
"""
print("=================获取元素=================")
t = (12, 13, 15, 99, 198, "A", "Hello", "Python")
print(t[0])
print(t[-1])
print(t[-len(t)])

"""
5. 切片
    元组切片会返回一个新的元组。
"""
print("=================切片=================")
t = (12, 13, 15, 99, 198, "A", "Hello", "Python")
print(t[1:4])  # (13, 15, 99)
print(t[:3])   # (12, 13, 15)
print(t[3:])   # (99, 198, 'A', 'Hello', 'Python')
print(t[::-1]) # ('Python', 'Hello', 'A', 198, 99, 15, 13, 12)

"""
6. 不可变性
    元组本身不可修改，不能新增、删除或替换元素。
"""
print("=================不可变性=================")
t = (1, 2, 3)
# t[0] = 100   # 会报错 TypeError
print(t)

"""
7. 元组中可变元素的注意事项
    元组不可变，指的是元组中每个位置绑定的对象不能替换。
    如果元组里存放的是列表，列表本身仍然可以被修改。
"""
print("=================元组中可变元素的注意事项=================")
t = ([1, 2], "Python")
t[0].append(3)
print(t) # ([1, 2, 3], 'Python')

"""
8. 遍历元组
"""
print("=================遍历元组=================")
t = ("apple", "banana", "orange")
for item in t:
    print(item)

"""
9. 元组组包
    将多个值用逗号组合在一起，会自动形成一个元组，这个过程称为组包。
"""
print("=================元组组包=================")
person = "Alice", 25, "Shanghai"
print(person)
print(type(person)) # tuple

x = 10
y = 20
point = x, y
print(point)
print(type(point))

"""
10. 元组解包
    可以将元组中的元素一次性赋值给多个变量。
"""
print("=================元组解包=================")
# 基础解包
point = (10, 20)
x, y = point
print(x)
print(y)

person = "Alice", 25, "Shanghai"
name, age, city = person
print(name)
print(age)
print(city)

# 扩展解包 *
name, *other = person
print(name)
print(type(name).__name__) # str
print(other)
print(type(other).__name__) # list

"""
11. 组包与解包结合
    Python 中函数返回多个值时，返回值会被组包成元组；接收时可以直接解包。
"""
print("=================组包与解包结合=================")
def get_point():
    return 100, 200

point = get_point()
print(point)
print(type(point)) # tuple

x, y = get_point()
print(x)
print(y)

"""
12. 常用函数和方法
    len()：获取元素个数
    in：判断元素是否存在
    index()：获取元素第一次出现的索引
    count()：统计元素出现次数
"""
print("=================常用函数和方法=================")
t = (1, 2, 3, 2, 4)
print(len(t))       # 5
print(2 in t)       # True
print(t.index(2))   # 1
print(t.count(2))   # 2

"""
13. 与列表的区别
13.1 列表使用 []，元组使用 ()。
13.2 列表可变，元组不可变。
13.3 如果数据不需要修改，使用元组可以表达“固定不变”的语义。
"""
print("=================与列表的区别=================")
list_data = [1, 2, 3]
tuple_data = (1, 2, 3)
list_data[0] = 100
print(list_data)
print(tuple_data)

"""
14. 常见应用场景
14.1 表示固定结构的数据，例如坐标、日期、配置项。
14.2 函数返回多个值时，本质上通常是返回元组。
14.3 用作字典的键，但前提是元组中的元素也都可哈希。
"""
print("=================常见应用场景：表示固定结构的数据=================")
point = (100, 200)
print(f"x={point[0]}, y={point[1]}")

print("=================常见应用场景：函数返回多个值=================")
def get_user():
    return "Alice", 25

user_name, user_age = get_user()
print(user_name)
print(user_age)

print("=================常见应用场景：用作字典的键=================")
locations = {
    (0, 0): "origin",
    (1, 2): "target",
}
print(locations[(1, 2)])

"""
15. 注意事项汇总
- 单元素元组必须写成 ("Python",)，不能省略逗号。
- 元组不可变，不能直接修改、添加或删除元素。
- 元组中的可变对象本身仍然可以被修改。
- 元组是序列，支持索引、切片、遍历、组包、解包。
- 多个值用逗号组合时会自动组包成元组。
- 数据固定不变时，优先考虑使用元组表达语义。
"""
print("=================案例：变量交换=================")
# 现有 a=10, b=20 两个变量，将a,b两个变量的值交换
a=10
b=20
a, b = b, a
print(a, b)
