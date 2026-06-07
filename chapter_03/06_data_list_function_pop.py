# 列表常用方法-pop

"""
1. 方法签名与基本用法
    list.pop([index])
    参数：index 为可选参数，表示要删除元素的索引，默认值为 -1（即最后一个元素）。
    返回值：被删除的元素，类型取决于列表存储的对象。
    副作用：原列表长度减少 1，指定位置的元素被移除，后续元素（如果有）向前移动一位。
"""
colors = ['red', 'green', 'blue']
last = colors.pop()        # 不传参，默认删除最后一个
print(last)    # 'blue'
print(colors)  # ['red', 'green']

second = colors.pop(0)    # 删除索引 0 的元素
print(second)  # 'red'
print(colors)  # ['green']

"""
2. 参数详解
2.1 默认索引 -1
    不传任何参数时，pop() 等价于 pop(-1)，始终移除最右侧元素。
2.2 正整数索引
    传入 0 到 len(list)-1 之间的整数，移除该位置的元素。
2.3 负数索引
    负数从末尾倒计数，-1 是最后一个，-2 是倒数第二个，依此类推。必须满足 -len(list) <= index <= -1。
2.4 索引越界
    如果索引超出上述范围，会立即引发 IndexError。
"""
lst = [1, 2]
# lst.pop(2)    # IndexError: pop index out of range
# lst.pop(-3)   # IndexError: pop index out of range

"""
3. 时间复杂度
    list.pop() 的时间复杂度取决于索引位置
3.1 pop() 或 pop(-1)（移除末尾）：O(1)
    因为不需要移动其他元素，只需调整列表的长度计数
3.2 pop(i) 其中 i 不是最后一个有效索引：O(n)，n 为列表长度
    删除位置之后的所有元素都需要向前移动一位，最坏情况是 pop(0)，移动所有剩余 n-1 个元素
"""

"""
4. 常见使用场景
4.1 实现栈（LIFO 后进先出）
    pop() 默认删除末尾，与 append() 配对，完美模拟栈。
4.2 逐项处理并消耗列表
4.3 安全地删除并获取元素
4.4 在循环中删除特定条件的元素（倒序索引）
"""

print("=================常见使用场景：实现栈=================")
stack = []
stack.append('page1')
stack.append('page2')
stack.append('page3')

while stack:
    current = stack.pop()
    print(f"处理 {current}")   # 先 page3，再 page2，最后 page1

print("=================常见使用场景：逐项处理并消耗列表=================")
tasks = ['A', 'B', 'C']
while tasks:
    task = tasks.pop()   # 从后往前处理
    print(task)

print("=================常见使用场景：安全地删除并获取元素=================")
inventory = ['sword', 'shield', 'potion']
item = inventory.pop(1)  # 卸下盾牌并获取它
print(item)
print(inventory)

print("=================常见使用场景：在循环中删除特定条件的元素（倒序索引）=================")
nums = [1, 2, 3, 2, 4]
for i in range(len(nums)-1, -1, -1):
    if nums[i] == 2:
        nums.pop(i)
print(nums) # 结果: [1, 3, 4]

"""
5. 内部原理简述
list.pop() 的 C 实现大致过程如下：
5.1 解析参数，确定索引 i（默认为列表长度 -1）。
5.2 如果列表为空或索引越界，抛出 IndexError。
5.3 获取索引 i 处元素的引用，作为返回值。
5.4 计算需要向前移动的元素数量（len - 1 - i）。如果 i 不是最后一个元素，则调用 memmove 将 i 之后的所有元素整体向前移动一个位置。
5.5 将原数组最后一个位置（现为多余位置）置为 NULL，帮助垃圾回收。
5.6 列表长度减 1，可能触发缩容（如果内存占用远大于实际长度，解释器可能会缩小分配空间，但这是可选的优化）。
5.7 返回被移除的元素。
"""
