# 条件判断

if True:
    print("True") # Python 中是通过缩进来描述代码归属的，如这行归属于 if 代码块的语句，需要在前缩进 4 个空格
else:
    print("False")

# 案例：判断是否润年
## 非整百年份且能被 4 整除；或者整百年份且能被400整除

year = input("请输入需要判定的年份：")

if not year.isdigit():
    print("请输入正确的年份！")
else:
    # 判断是否为润年
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f"{year} 是润年")
    else:
        print(f"{year} 不是润年")
