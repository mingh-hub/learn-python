# 列表常用方法-clear

"""
1. 方法签名与基本用法
    list.clear()
1.1 参数：无。
1.2 返回值：None。该方法直接修改原列表，不返回新列表。
"""
print("=================方法签名与基本用法=================")
items = [1, 2, 3]
items.clear()
print(items)   # []
print(len(items))   # 0

"""
2. 返回值 —— 返回 None
"""
print("=================返回 None=================")
a = [1, 2, 3]
b = a.clear()   # b 是 None
print(a)        # []
print(b)        # None

"""
3. 时间复杂度
    list.clear() 的时间复杂度为 O(n)，其中 n 是原列表的长度。
3.1 它需要遍历底层数组，将每个元素指针设为 NULL，并减少这些元素的引用计数（以便垃圾回收）。
3.2 尽管从用户角度看“一次性清空”，但释放每个元素引用仍需要与元素数量成正比的时间。
3.3 空间上，列表内部保留原有的已分配容量（allocated 可能不变），以便后续 append 直接重用。
"""

"""
4. 常见使用场景
4.1 重置复用同一个列表对象
4.2 清空共享列表
4.3 结合 try/finally 的安全清理
"""
print("=================常见使用场景：重置复用同一个列表对象=================")
def process(items):
    items.append("123")

pages = ['first page', 'second page', 'third page']
buffer = []
for page in pages:
    buffer.append(page)
    process(buffer)
    buffer.clear()   # 重置，避免重新分配新列表
print(buffer)

print("=================常见使用场景：清空共享列表=================")
class Tracker:
    def __init__(self):
        self.data = []
    def reset(self):
        self.data.clear() # 无论外部是否有对 data 的引用，清空后所有引用都会看到空列表。
print(Tracker())
print(Tracker().reset()) # None

print("=================常见使用场景：结合 try/finally 的安全清理=================")
results = []
try:
    for item in reversed(pages):
        results.append(item + 'A')
    print(results)
finally:
    results.clear()  # 确保敏感数据被清除

"""
5. 注意事项与易错点
5.1 不要与重新赋值混淆
    a.clear() 修改原对象，a = [] 只是让变量绑定新对象
5.2 clear() 后已分配容量仍在
    清空列表不释放底层数组内存，列表的容量 (allocated) 通常保留，以支持后续高效添加。如果你需要同时释放内存，可以重新赋值为 []
5.3 对空列表调用是安全的
    [].clear()   # 不会报错，列表保持为 []
"""
print("=================注意事项与易错点：不要与重新赋值混淆=================")
def reset(lst):
    lst = []          # 只改变了局部变量 lst，不影响外部传入的列表

def reset_correct(lst):
    lst.clear()       # 真正清空外部列表

data = [1, 2, 3]
reset(data)
print(data)           # [1, 2, 3]  → 没变化
reset_correct(data)
print(data)           # []         → 被清空了

"""
6. 内部原理简述
    在 CPython 中，list.clear() 的 C 实现大致如下：
-> 获取列表长度 n。
-> 遍历底层 ob_item 数组，对每个槽位执行：
    -> 取出元素指针 item = ob_item[i]。
    -> 将 ob_item[i] 置为 NULL。
    -> 调用 Py_DECREF(item) 减少该对象的引用计数。
-> 将列表的长度字段 ob_size 设置为 0。
-> 注意，列表的 allocated 容量保持不变，底层内存没有释放。
"""