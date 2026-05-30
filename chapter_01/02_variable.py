# 变量
# 定义：程序中用来存储单个数据的容器
num = 10
print(num)

# Python 是动态类型语言，在程序运行时才会进行类型检查，变量的类型可以在程序运行过程中改变（Java 是编译时），实际开发不建议这么做
num = "Hello Python"
print(num)

base = 10
incr = 20
print("第一个月的总播放量: ", base + incr)

base, incr = 10, 20
print("第一个月的总播放量: ", base + incr)
