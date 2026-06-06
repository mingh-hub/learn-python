# 条件判断 if...else / if...elif...else
import sys

if True:
    print("True") # Python 中是通过缩进来描述代码归属的，如这行归属于 if 代码块的语句，需要在前缩进 4 个空格
else:
    print("False")

def is_int_str(s):
    s = s.strip()
    if s.startswith(('-', '+')):
        return s[1:].isdigit()
    return s.isdigit()

# 案例：判断是否润年
## 非整百年份且能被 4 整除；或者整百年份且能被400整除

# year = input("请输入需要判定的年份：")
#
# if not year.isdigit():
#     print("请输入正确的年份！")
# else:
#     # 判断是否为润年
#     year = int(year)
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         print(f"{year} 是润年")
#     else:
#         print(f"{year} 不是润年")

# 判断输入的数字是正数，负数还是0
year = input("请输入需要判定的数字：")

if not is_int_str(year):
    print("请输入正确的数字！")
    sys.exit(f"{year} <---不是正确的数字")

year = int(year)

if year > 0:
    print(f"{year} 是正数")
elif year < 0:
    print(f"{year} 是负数")
else:
    print(f"{year} 为 0")
