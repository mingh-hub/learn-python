# 字符串

## 字符串定义

### 1. 双引号定义（推荐）
str1 = "Hello Python"
print(str1)

### 2. 单引号定义
str2 = 'Hello Python'
print(str2)

### 3. 三引号定义（可换行）
str3 = """
起来！不愿做奴隶的人们
！！！！
"""
print(str3)

## 字符串拼接

### + 号拼接（无法拼接字符串与非字符串，比如 int 类型）
str_connect1 = "你好：" + "Java"
print(str_connect1)

name = "小明"
age = 18
profession = "软件开发"

print(name + str(age) + profession)

### 多个字符串字面量可以直接写
str_connect2 = "你好：" "Python"
print(str_connect2)

### 字符串拼接问题
# 1. 拼接繁琐
# 2. 破坏字符串完整性
# 3. 类型转换
# 4. 如何处理？ -> 字符串格式化（05_str_format.py）
