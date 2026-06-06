# while 循环

## while 语法结构
"""
while 条件表达式:
    循环语句1
    循环语句2

while 条件表达式:
    循环语句1
    循环语句2
else:
    条件为 False，循环正常结束
"""
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("循环正常结束")

## 案例：计算 1-100 之间所有偶数累加和

i = 1
j = 0
while i <= 100:
    if i % 2 == 0:
        j += i
    i += 1
else:
    print("计算结束，1-100 之间所有偶数累加和为: %s" % j)
