# Python 函数进阶

from functools import partial, wraps
from time import perf_counter


"""
1. 本篇在函数基础之上，继续学习参数规则、高阶函数、闭包、递归和装饰器。
2. Python 中的函数也是对象，可以赋值给变量、作为参数传递，也可以作为返回值。
3. 进阶语法可以增强函数的灵活性，但函数签名和执行过程仍应保持清晰易懂。
4. 建议先掌握 01_function_base_instruction.py 中的参数、返回值、调用栈和作用域。
"""

"""
1. 函数参数详解
    形参是定义函数时声明的变量，实参是调用函数时传入的数据。
    调用函数时，Python 会按照函数签名把实参与形参进行绑定。
    参数可以按照位置或名称传递，还可以设置默认值、接收不定长数据和限制传递方式。
"""
print("=================1. 函数参数详解=================")

"""
1.1 参数绑定与对象引用
    Python 调用函数时，会让形参引用实参所对应的对象。
    给形参重新赋值，只会改变局部变量的引用，不会改变函数外部变量的引用。
    如果形参引用列表、字典等可变对象，修改对象内容后，函数外部也能看到变化。
"""
print("=================1.1 参数绑定与对象引用=================")


def reassign_number(number):
    number = 100
    print(f"函数内部重新赋值：{number}")


original_number = 10
reassign_number(original_number)
print(f"函数外部保持不变：{original_number}")


def add_course(courses, course):
    courses.append(course)


course_list = ["Python"]
add_course(course_list, "SQL")
print(f"函数外部看到列表变化：{course_list}")

"""
1.2 位置传参、关键字传参与混合传参
    位置传参按照实参的位置依次绑定形参。
    关键字传参通过 parameter=value 指定形参，不必遵循形参的排列顺序。
    两种方式可以混合使用，但位置实参必须写在关键字实参前面。
"""
print("=================1.2 传参方式=================")


def create_user(name, age, city="上海"):
    return {"name": name, "age": age, "city": city}


print(create_user("Alice", 20, "北京"))
print(create_user(age=22, name="Bob", city="深圳"))
print(create_user("Cindy", city="杭州", age=19))

"""
1.3 默认参数
    默认参数允许调用者省略一部分实参，调用时传值可以覆盖默认值。
    普通参数中，没有默认值的参数必须放在有默认值的参数前面。
    默认值在执行 def 语句时计算一次，而不是每次调用函数时重新计算。
    不应直接使用列表、字典或集合作为默认值，推荐使用 None 后在函数内部创建对象。
"""
print("=================1.3 默认参数=================")


def calculate_price(price, discount=1, shipping_fee=0):
    return price * discount + shipping_fee


print(calculate_price(100))
print(calculate_price(100, 0.9))
print(calculate_price(100, shipping_fee=10, discount=0.8))


def create_default_config():
    print("创建默认配置，这段代码只在定义函数时执行一次。")
    return {"language": "中文"}


def show_config(config=create_default_config()):
    print(config)


show_config()
show_config()


def remember_item(item, history=[]):
    """错误示范：多次调用会共享同一个默认列表。"""
    history.append(item)
    return history


print(remember_item("Python"))
print(remember_item("SQL"))


def remember_item_safely(item, history=None):
    """推荐写法：每次省略 history 时创建一个新列表。"""
    if history is None:
        history = []
    history.append(item)
    return history


print(remember_item_safely("Python"))
print(remember_item_safely("SQL"))

"""
1.4 不定长参数
    *args 用于接收多余的位置实参，函数内部得到一个元组。
    **kwargs 用于接收多余的关键字实参，函数内部得到一个字典。
    args 和 kwargs 只是约定俗成的名称，真正具有语法作用的是 * 和 **。
"""
print("=================1.4 不定长参数=================")


def calculate_average(*scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)


print(calculate_average(80, 90, 100))
print(calculate_average(75, 88, 92, 96))


def print_user_profile(name, **details):
    print(f"姓名：{name}")
    for key, value in details.items():
        print(f"{key}：{value}")


print_user_profile("Alice", age=20, city="上海", occupation="程序员")


def record_event(event_name, *values, level="INFO", **metadata):
    print(f"事件：{event_name}")
    print(f"附加值：{values}")
    print(f"级别：{level}")
    print(f"元数据：{metadata}")


record_event(
    "user_login",
    "web",
    "mobile",
    level="WARNING",
    user_id=1001,
    ip="127.0.0.1",
)

"""
1.5 参数解包
    调用函数时，* 可以把列表、元组等可迭代对象解包为多个位置实参。
    ** 可以把字典解包为多个关键字实参，字典的键必须与形参名称对应。
    定义函数时的 *args 和 **kwargs 用于收集实参；调用函数时的 * 和 ** 用于展开数据。
"""
print("=================1.5 参数解包=================")


def calculate_volume(length, width, height):
    return length * width * height


dimensions = [5, 4, 3]
print(calculate_volume(*dimensions))


def display_product(name, price, category):
    print(f"商品：{name}，价格：{price}，分类：{category}")


product = {"name": "Python 进阶书", "price": 79.8, "category": "图书"}
display_product(**product)

default_options = {"language": "中文", "page_size": 20}
custom_options = {"page_size": 50, "show_image": True}
merged_options = {**default_options, **custom_options}


def show_options(**options):
    print(options)


show_options(**merged_options)

"""
1.6 仅限位置参数
    在函数签名中，/ 前面的形参是仅限位置参数，只能按照位置传递。
    仅限位置参数允许函数内部修改形参名称，而不影响已有调用代码。
    一些 Python 内置函数也使用仅限位置参数。
"""
print("=================1.6 仅限位置参数=================")


def calculate_power(base, exponent, /):
    return base**exponent


print(calculate_power(2, 3))

# calculate_power(base=2, exponent=3)
# TypeError：base 和 exponent 是仅限位置参数，不能使用关键字传递

"""
1.7 仅限关键字参数
    单独的 * 后面的形参是仅限关键字参数，调用时必须写出参数名称。
    *args 后面的普通形参也自动成为仅限关键字参数。
    对含义不够直观的布尔值或配置项使用关键字传参，可以提高代码可读性。
"""
print("=================1.7 仅限关键字参数=================")


def export_report(data, *, file_type="csv", include_header=True):
    print(f"数据：{data}")
    print(f"文件类型：{file_type}，包含表头：{include_header}")


export_report(["Alice", "Bob"], file_type="xlsx", include_header=False)

# export_report(["Alice", "Bob"], "xlsx", False)
# TypeError：file_type 和 include_header 必须使用关键字传递

"""
1.8 参数的完整排列顺序
    函数可以按照以下顺序组合不同类型的参数：
    （1）仅限位置参数。
    （2）普通参数和默认参数。
    （3）不定长位置参数 *args。
    （4）仅限关键字参数。
    （5）不定长关键字参数 **kwargs。
"""
print("=================1.8 参数的完整排列顺序=================")


def process_data(
    source,
    /,
    operation,
    limit=10,
    *filters,
    reverse=False,
    **options,
):
    print(f"数据源：{source}")
    print(f"操作：{operation}，数量限制：{limit}")
    print(f"过滤条件：{filters}")
    print(f"是否反转：{reverse}")
    print(f"其他选项：{options}")


process_data(
    "students.csv",
    "sort",
    20,
    "active",
    "verified",
    reverse=True,
    encoding="utf-8",
)

"""
2. 函数是一等对象
    Python 中的函数也是对象，可以像数字、字符串等数据一样使用。
    函数可以赋值给变量、保存到容器、作为实参传递，还可以作为另一个函数的返回值。
    接收函数作为参数或返回函数的函数称为高阶函数。
"""
print("=================2. 函数是一等对象=================")


def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


selected_operation = add
print(selected_operation(10, 3))

operations = {
    "add": add,
    "subtract": subtract,
}
print(operations["subtract"](10, 3))

"""
2.1 函数作为参数
    把函数作为参数传入，可以让调用者决定具体的处理规则。
    作为参数传递时只写函数名；写成 function() 会先调用函数并传入它的返回值。
"""
print("=================2.1 函数作为参数=================")


def apply_operation(number1, number2, operation):
    return operation(number1, number2)


print(apply_operation(8, 5, add))
print(apply_operation(8, 5, subtract))

"""
2.2 函数作为返回值
    函数可以根据条件选择并返回另一个函数。
    返回函数时同样只写函数名，调用者拿到函数后可以在需要时执行。
"""
print("=================2.2 函数作为返回值=================")


def get_operation(operation_name):
    if operation_name == "add":
        return add
    if operation_name == "subtract":
        return subtract
    raise ValueError(f"不支持的操作：{operation_name}")


operation = get_operation("add")
print(operation(20, 6))

"""
3. 匿名函数 lambda
    lambda 用于创建只包含一个表达式的匿名函数，表达式的结果会自动返回。
    基本语法：lambda parameter1, parameter2: expression
    lambda 适合编写短小、只使用一次的回调；复杂逻辑应使用 def 定义普通函数。
"""
print("=================3. 匿名函数 lambda=================")

multiply = lambda number1, number2: number1 * number2
print(multiply(4, 5))

students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 95},
    {"name": "Cindy", "score": 82},
]

students_by_score = sorted(students, key=lambda student: student["score"])
print(students_by_score)

"""
4. LEGB 作用域规则
    Python 按照 LEGB 顺序查找变量：
    Local：当前函数内部的局部作用域。
    Enclosing：外层函数的作用域。
    Global：当前模块的全局作用域。
    Built-in：Python 提供的内置作用域。
    找到同名变量后就会停止继续向外查找，因此局部变量可能遮蔽外层变量。
"""
print("=================4. LEGB 作用域规则=================")

scope_name = "Global"


def show_legb():
    scope_name = "Enclosing"

    def inner():
        local_name = "Local"
        print(f"局部作用域：{local_name}")
        print(f"外层函数作用域：{scope_name}")
        print(f"内置作用域中的 len：{len([1, 2, 3])}")

    inner()


show_legb()
print(f"全局作用域：{scope_name}")

"""
5. 嵌套函数、nonlocal 与闭包
    在一个函数内部定义的函数称为嵌套函数或内层函数。
    内层函数可以读取外层函数的变量；需要修改外层变量时，必须使用 nonlocal 声明。
    闭包是能够记住并访问定义环境中变量的函数，即使外层函数已经执行结束。
"""
print("=================5. 嵌套函数、nonlocal 与闭包=================")


def create_counter(start=0):
    count = start

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


counter1 = create_counter()
print(counter1())
print(counter1())

counter2 = create_counter(100)
print(counter2())
print(counter1())

"""
5.1 使用闭包创建函数工厂
    函数工厂根据配置创建具有不同行为的函数。
    返回的内层函数会保存各自定义环境中的配置，彼此之间互不影响。
"""
print("=================5.1 使用闭包创建函数工厂=================")


def create_multiplier(factor):
    def multiply_by_factor(number):
        return number * factor

    return multiply_by_factor


double = create_multiplier(2)
triple = create_multiplier(3)
print(double(10))
print(triple(10))

"""
5.2 闭包的延迟绑定
    闭包保存的是变量本身，而不是创建函数那一刻变量的值。
    循环结束后，循环中创建的函数会读取变量最后一次绑定的值。
    可以使用默认参数在创建函数时保存当前值，避免延迟绑定问题。
"""
print("=================5.2 闭包的延迟绑定=================")

late_binding_functions = [
    lambda number: number * factor for factor in range(1, 4)
]
print([function(10) for function in late_binding_functions])

bound_functions = [
    lambda number, factor=factor: number * factor for factor in range(1, 4)
]
print([function(10) for function in bound_functions])

"""
6. 递归函数
    函数直接或间接调用自身，称为递归。
    递归函数必须包含终止条件，并在每次调用时逐步接近终止条件。
    每次递归调用都会创建新的栈帧，递归层数过深会触发 RecursionError。
"""
print("=================6. 递归函数=================")


def factorial(number):
    if number < 0:
        raise ValueError("阶乘只接受非负整数")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


print(factorial(5))

"""
6.1 使用递归处理嵌套数据
    数据的嵌套层数不确定时，递归通常比多层循环更自然。
    每次调用负责处理当前层，遇到子列表时继续递归处理。
"""
print("=================6.1 使用递归处理嵌套数据=================")


def sum_nested_numbers(data):
    total = 0
    for item in data:
        if isinstance(item, list):
            total += sum_nested_numbers(item)
        else:
            total += item
    return total


nested_numbers = [1, [2, 3], [4, [5, 6]]]
print(sum_nested_numbers(nested_numbers))

"""
6.2 递归与循环的选择
    Python 不会自动进行尾递归优化，因此递归并不适合所有重复计算。
    树形结构、嵌套结构等问题适合递归；简单计数和大量重复运算通常优先使用循环。
"""
print("=================6.2 递归与循环的选择=================")


def factorial_with_loop(number):
    if number < 0:
        raise ValueError("阶乘只接受非负整数")
    result = 1
    for current_number in range(2, number + 1):
        result *= current_number
    return result


print(factorial_with_loop(5))

"""
7. 装饰器基础
    装饰器用于在不修改原函数代码的情况下，为函数增加额外功能。
    装饰器接收原函数，创建包装函数，并返回包装函数。
    @decorator 语法等价于 function = decorator(function)。
"""
print("=================7. 装饰器基础=================")


def announce(function):
    def wrapper():
        print(f"准备调用 {function.__name__}")
        result = function()
        print(f"{function.__name__} 调用结束")
        return result

    return wrapper


def prepare_report():
    print("正在生成报告。")
    return "报告生成完成"


wrapped_prepare_report = announce(prepare_report)
print(wrapped_prepare_report())


@announce
def send_message():
    print("正在发送消息。")
    return "消息发送成功"


print(send_message())

"""
8. 装饰器进阶
    通用装饰器使用 *args 和 **kwargs 接收被装饰函数的所有实参，并返回原函数的结果。
    functools.wraps 会保留原函数的名称、文档字符串等元数据。
"""
print("=================8. 装饰器进阶=================")


def log_call(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(f"调用函数：{function.__name__}")
        print(f"位置实参：{args}")
        print(f"关键字实参：{kwargs}")
        result = function(*args, **kwargs)
        print(f"返回结果：{result}")
        return result

    return wrapper


@log_call
def divide(number1, number2=1):
    """计算两个数字相除的结果。"""
    return number1 / number2


print(divide(10, number2=2))
print(divide.__name__)
print(divide.__doc__)

"""
8.1 带参数的装饰器
    带参数的装饰器需要三层函数：
    最外层接收装饰器配置，中间层接收被装饰函数，最内层包装函数负责增加功能。
    @repeat(times=3) 会先执行 repeat(times=3)，得到真正的装饰器。
"""
print("=================8.1 带参数的装饰器=================")


def repeat(times):
    if times < 1:
        raise ValueError("重复次数必须大于 0")

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = function(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(times=3)
def greet(name):
    print(f"你好，{name}！")


greet("Alice")

"""
8.2 统计函数执行时间
    装饰器适合处理日志记录、权限检查、缓存和性能统计等横切功能。
    perf_counter() 提供适合测量短时间间隔的高精度计时器。
"""
print("=================8.2 统计函数执行时间=================")


def measure_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = function(*args, **kwargs)
        duration = perf_counter() - start_time
        print(f"{function.__name__} 执行时间：{duration:.6f}秒")
        return result

    return wrapper


@measure_time
def sum_range(end):
    return sum(range(end))


print(sum_range(100_000))

"""
8.3 多个装饰器的执行顺序
    多个装饰器从下到上完成装饰，离函数最近的装饰器最先应用。
    调用函数时从上到下进入包装函数，再按照相反顺序退出。
    @decorator_a @decorator_b 等价于 decorator_a(decorator_b(function))。
"""
print("=================8.3 多个装饰器的执行顺序=================")


def decorator_a(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("进入装饰器 A")
        result = function(*args, **kwargs)
        print("离开装饰器 A")
        return result

    return wrapper


def decorator_b(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print("进入装饰器 B")
        result = function(*args, **kwargs)
        print("离开装饰器 B")
        return result

    return wrapper


@decorator_a
@decorator_b
def run_task():
    print("执行任务")


run_task()

"""
9. 常用函数式工具
    sorted、map 和 filter 都可以接收函数，用于指定排序、转换或筛选规则。
    functools.partial 可以固定函数的部分参数，创建一个新的可调用对象。
"""
print("=================9. 常用函数式工具=================")

products = [
    {"name": "键盘", "price": 299},
    {"name": "鼠标", "price": 99},
    {"name": "显示器", "price": 1299},
]

products_by_price = sorted(products, key=lambda product: product["price"])
print(products_by_price)

numbers = [1, 2, 3, 4, 5, 6]
squares = list(map(lambda number: number**2, numbers))
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(squares)
print(even_numbers)

# 简单转换和筛选使用推导式通常更直观。
squares_with_comprehension = [number**2 for number in numbers]
even_numbers_with_comprehension = [number for number in numbers if number % 2 == 0]
print(squares_with_comprehension)
print(even_numbers_with_comprehension)


def calculate_tax(price, rate):
    return price * rate


calculate_vat = partial(calculate_tax, rate=0.13)
print(calculate_vat(100))

"""
10. 综合案例：订单处理流程
    本案例综合使用参数限制、参数解包、高阶函数、闭包和装饰器：
    （1）商品名称、单价和数量使用仅限位置参数。
    （2）折扣规则以函数形式传入。
    （3）*extra_services 和 **options 接收可选配置。
    （4）闭包保存订单处理次数。
    （5）装饰器记录调用信息和执行时间。
"""
print("=================10. 综合案例：订单处理流程=================")


def create_discount(discount_rate):
    if not 0 <= discount_rate <= 1:
        raise ValueError("折扣率必须在 0 到 1 之间")

    def apply_discount(amount):
        return amount * discount_rate

    return apply_discount


order_counter = create_counter()


@log_call
@measure_time
def process_order(
    product_name,
    unit_price,
    quantity,
    /,
    discount_rule,
    *extra_services,
    customer_level="普通会员",
    **options,
):
    order_number = order_counter()
    subtotal = unit_price * quantity
    total = discount_rule(subtotal)
    return {
        "order_number": order_number,
        "product_name": product_name,
        "subtotal": subtotal,
        "total": total,
        "extra_services": extra_services,
        "customer_level": customer_level,
        "options": options,
    }


order_arguments = ["Python 进阶书", 79.8, 2, create_discount(0.9)]
extra_services = ["礼品包装", "优先发货"]
order_options = {
    "customer_level": "黄金会员",
    "invoice": True,
    "remark": "工作日送达",
}

order_result = process_order(
    *order_arguments,
    *extra_services,
    **order_options,
)

print("订单处理结果：")
for result_key, result_value in order_result.items():
    print(f"{result_key}：{result_value}")

"""
11. 常见错误
    下面的错误示例保持注释状态，取消注释后可以观察对应的错误信息。
"""
print("=================11. 常见错误=================")

# create_user(name="Alice", 20)
# SyntaxError：位置实参不能写在关键字实参后面

# create_user("Alice", name="Bob", age=20)
# TypeError：name 同时接收了位置实参和关键字实参

# def invalid_default(name="Alice", age):
#     pass
# SyntaxError：普通参数中，没有默认值的参数不能放在默认参数后面

# calculate_volume(*[2, 3])
# TypeError：解包后只有两个实参，缺少 height

# display_product(**{"name": "键盘", "amount": 299, "category": "数码"})
# TypeError：amount 不是函数可以接收的关键字参数，并且缺少 price

# def create_broken_counter():
#     count = 0
#
#     def counter():
#         count += 1
#         return count
#
#     return counter
#
# create_broken_counter()()
# UnboundLocalError：修改外层函数变量前没有使用 nonlocal

# def recurse_forever():
#     return recurse_forever()
#
# recurse_forever()
# RecursionError：递归函数没有终止条件

# def broken_decorator(function):
#     def wrapper(*args, **kwargs):
#         return function(*args, **kwargs)
#
#     # 忘记 return wrapper
#
# @broken_decorator
# def broken_function():
#     print("无法正常调用")
#
# broken_function()
# TypeError：装饰后 broken_function 的值是 None

"""
12. 注意事项
    12.1 优先设计清晰、明确的函数签名，不要为了灵活而滥用 *args 和 **kwargs。
    12.2 参数较多或布尔参数含义不直观时，优先使用关键字参数。
    12.3 不要使用列表、字典或集合作为默认参数，推荐使用 None。
    12.4 调用函数时的 * 和 ** 用于解包，定义函数时用于收集不定长参数。
    12.5 简单且只使用一次的回调可以使用 lambda，复杂逻辑应使用 def。
    12.6 闭包适合保存少量状态，复杂状态通常更适合使用类管理。
    12.7 递归必须有终止条件，并注意 Python 的最大递归深度。
    12.8 编写装饰器时，应返回原函数结果，并使用 functools.wraps 保留函数信息。
    12.9 每个函数尽量只完成一个明确任务，使代码更容易测试、复用和维护。
"""
