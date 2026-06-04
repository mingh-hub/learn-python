# 赋值运算符

## 赋值运算符是编程语言中用于将值或表达式的结果保存到变量中的运算符

num = int(input("input num: "))

a = num # 赋值运算符
print(f"num is {a}")

b = num
b += 2 # 加法赋值运算符
print(f"num += 2 is {b}")

c = num
c -= 2 # 减法赋值运算符
print(f"num -= 2 is {c}")

d = num
d *= 2 # 乘法赋值运算符
print(f"num *= 2 is {d}")

e = num
e /= 2 # 除法赋值运算符
print(f"num /= 2 is {e}")

f = num
f %= 2 # 取模赋值运算符
print(f"num %= 2 is {f}")

g = num
g //= 2 # 取整除赋值运算符
print(f"num //= 2 is {g}")

h = num
h **= 2 # 幂赋值运算符
print(f"num **= 2 is {h}")
