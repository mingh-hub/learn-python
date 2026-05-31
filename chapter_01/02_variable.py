# 变量
# 定义：程序中用来存储单个数据的容器
from operator import and_

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

# 变量命名规则
# 1. 只能包含字母（a-z，A-Z）、数字（0-9）、下划线（_）
# 2. 不能以数字开头
# 3. 不能使用关键字：True、False、None、and、or、if、else、else、for、while
# 4. 严格区分大小写：age、Age、AGE 是三个变量

# 变量命名规范（PEP8：https://peps.python.org/pep-0008）
#1. 见名知意
# 2. 多个部分使用下划线连接（蛇形命名法，区别于Java的驼峰命名法）
# 3. 英文字母全小写
