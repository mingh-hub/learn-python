# Python 函数基础

"""
1. 函数是组织好的、可以重复使用的一段代码。
2. 使用函数可以减少重复代码，并让程序结构更加清晰。
3. 定义函数的基本语法：

    def function_name(parameter1, parameter2):
        '''函数的说明文档'''
        function_body
        return result

4. def 用于定义函数，函数名的命名规则与变量名相同，通常使用小写字母和下划线。
5. 定义函数时，函数体不会立即执行；只有调用函数时，函数体才会执行。
6. parameter 表示参数，可以让函数根据不同的数据完成相应的任务。
7. return 用于返回结果并结束函数；没有编写 return 的函数默认返回 None。
"""

"""
1. 定义和调用函数
    定义函数：使用 def 关键字创建函数。
    调用函数：在函数名后添加小括号。
"""
print("=================1. 定义和调用函数=================")


def say_hello():
    print("Hello, Python!")


say_hello()
say_hello()

"""
1.1 使用 pass 定义空函数
    pass 是一个空语句，不会执行任何操作。
    函数暂时没有具体功能时，可以使用 pass 保留函数结构，避免语法错误。
    只包含 pass 的函数没有编写 return，因此默认返回 None。
"""
print("=================1.1 使用 pass 定义空函数=================")


def future_feature():
    pass


print(future_feature())

"""
2. 参数与实参
    参数是函数定义中用来接收数据的变量，也称为形式参数，简称形参。
    实参是调用函数时传入的实际数据。
    形参只在函数内部使用，每次调用函数都可以传入不同的实参。
"""
print("=================2. 参数与实参=================")


def greet(name):
    print(f"你好，{name}！")


greet("Alice")
greet("Bob")


def introduce(name, age):
    print(f"我叫{name}，今年{age}岁。")


introduce("Alice", 20)

"""
2.1 位置参数和关键字参数
    位置参数：实参按照位置依次传给对应的形参。
    关键字参数：调用时使用 parameter=value，可以不按照形参顺序传递。
    一次调用中，位置参数必须写在关键字参数前面。
"""
print("=================2.1 位置参数和关键字参数=================")


def print_student(name, age, city):
    print(f"姓名：{name}，年龄：{age}，城市：{city}")


print_student("Alice", 20, "Shanghai")
print_student(city="Beijing", name="Bob", age=22)

"""
2.2 默认参数
    定义函数时可以为参数设置默认值。
    调用函数时如果没有传入对应实参，就会使用默认值。
    有默认值的参数必须放在没有默认值的参数后面。
"""
print("=================2.2 默认参数=================")


def greet_with_language(name, language="中文"):
    if language == "中文":
        print(f"你好，{name}！")
    else:
        print(f"Hello, {name}!")


greet_with_language("Alice")
greet_with_language("Alice", None)
greet_with_language("Bob", "English")

"""
2.3 可变对象作为参数
    调用函数时，形参会引用实参所对应的对象。
    在函数内部给形参重新赋值，不会改变函数外部变量的指向。
    如果传入列表、字典等可变对象，并在函数内部修改对象，外部也能看到修改结果。
"""
print("=================2.3 可变对象作为参数=================")


def change_number(number):
    number = 100
    print(f"函数内部的数字：{number}")


original_number = 10
change_number(original_number)
print(f"函数外部的数字：{original_number}")


def add_skill(skills, skill):
    skills.append(skill)


user_skills = ["Python"]
add_skill(user_skills, "SQL")
print(user_skills)

"""
2.4 可变对象作为默认参数的注意事项
    默认参数的值只会在定义函数时创建一次。
    使用列表、字典或集合作为默认值，会导致多次调用共享同一个对象。
    推荐使用 None 作为默认值，再在函数内部创建新的可变对象。
"""
print("=================2.4 可变默认参数=================")


def collect_item(item, items=[]):
    items.append(item)
    return items


print(collect_item("Python"))
print(collect_item("SQL"))


def collect_item_safely(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(collect_item_safely("Python"))
print(collect_item_safely("SQL"))

"""
2.5 类型注解
    可以在参数名后使用 : type 标注参数类型，在小括号后使用 -> type 标注返回值类型。
    类型注解可以提高代码可读性，并帮助编辑器和检查工具发现问题。
    Python 在运行时不会根据类型注解强制检查数据类型。
"""
print("=================2.5 类型注解=================")


def multiply(number1: int, number2: int) -> int:
    return number1 * number2


print(multiply(4, 5))
print(multiply.__annotations__)

"""
3. 函数的返回值
    return 可以把函数内部的计算结果返回给调用者。
    调用者可以使用变量接收返回值，也可以直接使用返回值。
    return 执行后，函数会立即结束，后面的代码不会再执行。
"""
print("=================3. 函数的返回值=================")


def add(number1, number2):
    result = number1 + number2
    return result


total = add(10, 20)
print(total)
print(add(5, 8))


def get_absolute_value(number):
    if number < 0:
        return -number
    return number


print(get_absolute_value(-10))
print(get_absolute_value(6))

"""
3.1 没有 return 和返回多个值
    函数没有编写 return，或者只写 return，返回值都是 None。
    return value1, value2 可以一次返回多个值，实际返回的是一个元组。
"""
print("=================3.1 没有 return 和返回多个值=================")


def show_message(message):
    print(message)


return_value = show_message("这段文字在函数内部输出。")
print(return_value)


def calculate(number1, number2):
    total = number1 + number2
    difference = number1 - number2
    return total, difference


calculate_result = calculate(10, 3)
print(calculate_result)

total, difference = calculate(10, 3)
print(total)
print(difference)

"""
4. 函数的说明文档
    文档字符串（docstring）用于说明函数的功能、参数和返回值。
    文档字符串应写在函数体的第一行，并使用三引号包裹。
    Sphinx 风格使用 :param parameter: 说明参数，使用 :return: 说明返回值。
    可以通过 function_name.__doc__ 查看，也可以使用 help(function_name) 查看帮助信息。
"""
print("=================4. 函数的说明文档=================")


def calculate_rectangle_area(length: float, width: float) -> float:
    """
    计算长方形的面积。

    :param length: 长方形的长
    :param width: 长方形的宽
    :return: 长方形的面积
    """
    return length * width


print(calculate_rectangle_area(5, 3))
print(calculate_rectangle_area.__doc__)
# help(calculate_rectangle_area)

"""
5. 函数的嵌套调用
    一个函数可以调用另一个函数，这种方式称为函数的嵌套调用。
    执行到函数调用时，会先进入被调用的函数；被调用函数结束后，再继续执行原函数。
"""
print("=================5. 函数的嵌套调用=================")


def sum_numbers(number1, number2, number3):
    return number1 + number2 + number3


def average_numbers(number1, number2, number3):
    total = sum_numbers(number1, number2, number3)
    return total / 3


average = average_numbers(80, 90, 100)
print(f"平均分：{average}")

"""
5.1 在实参中嵌套调用函数
    函数的返回值可以直接作为另一个函数的实参。
    嵌套调用按照从内到外的顺序执行。
"""
print("=================5.1 在实参中嵌套调用函数=================")


def double(number):
    return number * 2


def square(number):
    return number ** 2


print(square(double(3)))

"""
6. 变量作用域
    在函数内部定义的变量是局部变量，通常只能在当前函数中使用。
    在函数外部定义的变量是全局变量，可以在函数内部读取。
    局部变量与全局变量同名时，函数内部优先使用局部变量，不会修改全局变量。
"""
print("=================6. 变量作用域=================")

scope_message = "全局变量"


def show_scope():
    scope_message = "局部变量"
    print(f"函数内部：{scope_message}")


show_scope()
print(f"函数外部：{scope_message}")

"""
6.1 使用 global 修改全局变量
    在函数内部给全局变量赋值时，需要先使用 global 声明。
    全局变量会增加代码之间的依赖，应谨慎使用，通常优先通过参数和返回值传递数据。
"""
print("=================6.1 使用 global 修改全局变量=================")

visit_count = 0


def add_visit_count():
    global visit_count
    visit_count += 1
    return visit_count


print(add_visit_count())
print(add_visit_count())
print(visit_count)

"""
7. 综合案例：计算商品总价
    calculate_total 负责计算价格，print_order 负责组织并输出订单信息。
"""
print("=================7. 综合案例：计算商品总价=================")


def calculate_total(price, quantity, discount=1):
    """根据单价、数量和折扣计算商品总价。"""
    return price * quantity * discount


def print_order(product_name, price, quantity, discount=1):
    """计算并输出订单信息。"""
    total = calculate_total(price, quantity, discount)
    print(f"商品：{product_name}")
    print(f"数量：{quantity}")
    print(f"总价：{total:.2f}元")


print_order("Python 入门书", 59.8, 2, 0.9)

"""
8. 常见调用错误
    参数数量不匹配、关键字参数名错误、调用尚未定义的函数都会导致程序报错。
    下面的错误示例保持注释状态，取消注释后可以观察对应的错误信息。
"""
print("=================8. 常见调用错误=================")

# introduce("Alice")
# TypeError：缺少 age 参数

# introduce("Alice", 20, "Shanghai")
# TypeError：传入的实参数量过多

# introduce(username="Alice", age=20)
# TypeError：函数没有名为 username 的参数

# call_before_definition()
# NameError：执行到这里时，函数还没有定义
# def call_before_definition():
#     print("函数定义完成")

"""
9. 注意事项
    9.1 必须先定义函数，再调用函数。
    9.2 函数名应清晰表达功能，通常使用动词或动词短语。
    9.3 调用函数时，实参的数量和使用方式要与形参匹配。
    9.4 print() 用于输出信息，return 用于把结果返回给调用者，两者作用不同。
    9.5 每个函数尽量只完成一个明确的任务，方便阅读和重复使用。
    9.6 避免使用可变对象作为默认参数，推荐使用 None 代替。
    9.7 向函数传入可变对象时，要注意函数是否会修改原对象。
    9.8 类型注解用于说明预期类型，不会替代必要的数据检查。
"""
