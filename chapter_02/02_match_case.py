# 结构模式匹配 match...case

## 3.10 版本新语法

day = input("Enter a day: ").strip()

match int(day):
    case 1:
        print("星期一")
    case 2:
            print("星期二")
    case 3:
        print("星期三")
    case 4:
        print("星期四")
    case 5:
        print("星期五")
    case 6 | 7 if False: # if 条件成立才进行匹配
        print("周末休息！！！")
    case _: # 匹配其它所有情况
        print("输入错误！！！")

## match...case 与 if 的区别

# match...case：基于某个变量的多个固定值进行分支判断，可以用结构匹配模式

# if：条件判断涉及复杂的逻辑判定、范围比较及组合条件时
