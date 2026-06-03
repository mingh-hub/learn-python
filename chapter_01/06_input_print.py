# 输入与输出

# input：次函数的功能就是获取键盘输入的数据，具体语法：s = input(键盘输入信息)
# print：次函数的功能就是将数据输出到控制台，语法：print(输出的信息)
name = input("请输入您的姓名：")
print(f"欢迎您：{name}")

# 案例：模拟银行卡取款业务
total = 10000

password = input("input your password: ")
print(f"your password is correct: {password}")

amount = int(input("input your amount: "))

print(f"your balance is: {total - amount}")
