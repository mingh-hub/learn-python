# for 循环
"""
for 循环和 while 循环区别：
1. while 循环是通过条件表达式来控制是否要进行下一次循环，而 for 循环的本质是一种轮询遍历机制，对集合内容进行逐条处理
2. 都可以用 break 强制中断循环
"""

## 语法结构
"""
for element in collection
    loop code
else: # 可选结构，可有可无，是在 for 循环结束后执行的语句
    loop end code
"""

msg = "Hello Python"
for char in msg:
    print(char)
    break

## range 语句
"""
作用：生成指定队则的数字序列
用法：
1. range(end)：获取一个从 0 开始到 end 结束的数字序列（不含 end）
2. range(start, end)：获取一个从 start 开始到 end 结束的数字序列（不含 end）
3. range(start, end, step)：获取一个从 start 开始到 end 结束，step 步长的数字序列（不含 end）
"""

## 案例1：计算 100-500 之间所有 3 的倍数的数字和
coll = range(100, 501)
add = 0
for i in coll:
    if i % 3 == 0:
        add += i
else:
    print(f"100-500 之间所有 3 的倍数的数字和为：{add}")
