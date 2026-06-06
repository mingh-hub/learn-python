# 嵌套循环

## 案例：根据输入的长宽打印方形图案

# length = int(input("input length: "))
# width = int(input("input width: "))
#
# for w in range(width):
#     for l in range(length):
#         print("*", end="  ")
#     print()

## 案例2：输出九九乘法表

i = 1 # 行
j = 1 # 列

for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {i * j}", end="\t")
    print()
