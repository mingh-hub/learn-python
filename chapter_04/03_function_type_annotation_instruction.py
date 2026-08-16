# Python 3.14 类型注解

import annotationlib
from functools import wraps
from typing import (
    Annotated,
    Any,
    Callable,
    ClassVar,
    Final,
    Literal,
    Mapping,
    NewType,
    Never,
    NotRequired,
    Protocol,
    ReadOnly,
    Sequence,
    Self,
    TypedDict,
    TypeIs,
    assert_never,
    cast,
    get_args,
    get_origin,
    get_type_hints,
    overload,
    runtime_checkable,
)


"""
1. 类型注解用于说明变量、函数参数和返回值预期使用的数据类型。
2. 类型注解可以提高代码可读性，并帮助编辑器、mypy、Pyright 等工具发现类型问题。
3. Python 是动态类型语言，默认不会在运行时强制执行类型注解。
4. 本文件以 Python 3.14 为目标版本，示例使用当前推荐的类型注解语法。
"""

"""
1. 类型注解基础
    变量注解的基本语法：variable_name: type = value
    冒号后面是变量预期使用的类型，等号后面才是实际赋值。
    只写 variable_name: type 会创建注解，但不会给变量赋值。
"""
print("=================1. 类型注解基础=================")

user_name: str = "Alice"
user_age: int = 20
height: float = 1.68
is_active: bool = True

print(user_name)
print(user_age)
print(height)
print(is_active)

# 只有注解，没有赋值。
future_score: float

# print(future_score)
# NameError：future_score 只有类型注解，目前还没有绑定实际值

"""
1.1 注解不会改变对象的类型
    注解是提供给开发者和类型检查工具的信息，不会转换数据，也不会限制变量重新赋值。
    下面把字符串赋给 int 注解的变量，Python 仍然可以运行，但静态类型检查工具会报告问题。
"""
print("=================1.1 注解不会改变对象的类型=================")

quantity: int = 10
print(quantity, type(quantity))

quantity = "十个"  # type: ignore[assignment]
print(quantity, type(quantity))

"""
1.2 查看变量注解
    模块、类和函数通常通过 __annotations__ 保存注解信息。
    Python 3.14 开始，模块级注解采用延迟求值，应使用 annotationlib.get_annotations() 读取。
    局部变量的注解主要供静态分析使用，不一定能通过运行时对象直接读取。
"""
print("=================1.2 查看变量注解=================")


class ExampleSettings:
    language: str = "中文"
    retry_count: int = 3


print(ExampleSettings.__annotations__)

"""
2. 函数参数与返回值注解
    在参数名后使用 : type 标注参数类型。
    在函数参数列表后使用 -> type 标注返回值类型。
    没有返回结果的函数通常标注为 -> None。
"""
print("=================2. 函数参数与返回值注解=================")


def calculate_rectangle_area(length: float, width: float) -> float:
    return length * width


def build_greeting(name: str, times: int = 1) -> str:
    return " ".join([f"你好，{name}！"] * times)


def print_message(message: str) -> None:
    print(message)


print(calculate_rectangle_area(5.0, 3.0))
print(build_greeting("Alice", 2))
print_message("类型注解让函数接口更加清晰。")
print(calculate_rectangle_area.__annotations__)

"""
2.1 默认参数与可空类型的区别
    设置默认值表示调用函数时可以省略该实参。
    str | None 表示值可以是 str 或 None，但不代表调用时可以省略参数。
    参数能否省略由是否存在默认值决定，与可空类型本身无关。
"""
print("=================2.1 默认参数与可空类型的区别=================")


def find_user(user_id: int, nickname: str | None = None) -> str:
    if nickname is None:
        return f"用户 {user_id} 暂无昵称"
    return f"用户 {user_id} 的昵称是 {nickname}"


def require_optional_value(value: str | None) -> str:
    if value is None:
        return "没有内容"
    return value


print(find_user(1001))
print(find_user(1002, "Bob"))
print(require_optional_value(None))

# require_optional_value()
# TypeError：虽然 value 可以是 None，但它没有默认值，因此调用时不能省略

"""
2.2 不定长参数的注解
    *args 的注解描述每一个位置实参的类型，不是描述 args 元组本身。
    **kwargs 的注解描述每一个关键字实参值的类型，不是描述 kwargs 字典本身。
    函数内部的 args 是元组，kwargs 是字典。
"""
print("=================2.2 不定长参数的注解=================")


def calculate_total(*prices: float) -> float:
    return sum(prices)


def create_labels(**labels: str) -> dict[str, str]:
    return labels


print(f"{calculate_total(19.9, 29.9, 9.9):.2f}")
print(create_labels(language="Python", level="进阶"))

"""
3. 容器类型注解
    Python 3.14 可以直接使用 list、tuple、dict 和 set 配合方括号描述元素类型。
    list[str] 表示元素都是字符串的列表。
    dict[str, float] 表示键是字符串、值是浮点数的字典。
"""
print("=================3. 容器类型注解=================")

student_names: list[str] = ["Alice", "Bob", "Cindy"]
coordinates: tuple[float, float] = (31.23, 121.47)
rgb_color: tuple[int, int, int] = (255, 128, 0)
scores: dict[str, float] = {"Alice": 88.5, "Bob": 95.0}
tags: set[str] = {"Python", "类型注解"}

print(student_names)
print(coordinates)
print(rgb_color)
print(scores)
print(tags)

"""
3.1 固定长度与不定长度元组
    tuple[str, int] 表示固定包含两个元素，且两个位置的类型分别是 str 和 int。
    tuple[int, ...] 使用省略号表示元组可以包含任意数量的 int 元素。
"""
print("=================3.1 元组类型注解=================")

student_record: tuple[str, int] = ("Alice", 20)
number_tuple: tuple[int, ...] = (1, 2, 3, 4, 5)
empty_number_tuple: tuple[int, ...] = ()

print(student_record)
print(number_tuple)
print(empty_number_tuple)

"""
3.2 嵌套容器类型
    容器类型可以嵌套，用于描述更复杂的数据结构。
    注解层级过深时会降低可读性，可以使用类型别名简化，后面会详细介绍。
"""
print("=================3.2 嵌套容器类型=================")

class_scores: dict[str, list[float]] = {
    "第一组": [88.0, 92.5, 79.0],
    "第二组": [95.0, 86.5, 90.0],
}
print(class_scores)

"""
3.3 使用抽象容器类型
    参数只需要读取序列时，可以使用 Sequence[T]，而不是限制为 list[T]。
    参数只需要读取键值数据时，可以使用 Mapping[K, V]，而不是限制为 dict[K, V]。
    参数类型尽量宽松、返回类型尽量明确，可以让函数适用于更多数据结构。
"""
print("=================3.3 使用抽象容器类型=================")


def average_score(values: Sequence[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)


def print_prices(prices: Mapping[str, float]) -> None:
    for product_name, price in prices.items():
        print(f"{product_name}：{price:.2f}元")


print(average_score([80.0, 90.0, 100.0]))
print(average_score((75.0, 85.0, 95.0)))
print_prices({"键盘": 299.0, "鼠标": 99.0})

"""
4. 联合类型与 Literal
    A | B 表示值可以是 A 或 B。
    T | None 表示值可以是 T 或 None。
    Literal[value1, value2] 把允许的值限制为指定的字面量。
"""
print("=================4. 联合类型与 Literal=================")

type Identifier = int | str
type SortOrder = Literal["asc", "desc"]


def normalize_identifier(identifier: Identifier) -> str:
    return str(identifier).strip()


def sort_numbers(numbers: Sequence[int], order: SortOrder = "asc") -> list[int]:
    return sorted(numbers, reverse=order == "desc")


print(normalize_identifier(1001))
print(normalize_identifier(" user-1002 "))
print(sort_numbers([5, 2, 8, 1], "asc"))
print(sort_numbers([5, 2, 8, 1], "desc"))

# sort_numbers([5, 2, 8, 1], "random")
# Python 可以运行，但静态类型检查工具会指出 "random" 不属于允许的 Literal 值

"""
4.1 Any 与 object
    Any 表示跳过静态类型检查，几乎可以对值进行任何操作。
    object 表示任意 Python 对象，但使用具体操作前需要通过 isinstance 等方式缩小类型范围。
    不确定类型时优先考虑 object，只在确实需要关闭类型检查时使用 Any。
"""
print("=================4.1 Any 与 object=================")


def return_any_value(value: Any) -> Any:
    return value


def describe_object(value: object) -> str:
    if isinstance(value, str):
        return f"字符串长度：{len(value)}"
    if isinstance(value, int):
        return f"整数的两倍：{value * 2}"
    return f"其他对象：{value!r}"


print(return_any_value({"name": "Alice"}))
print(describe_object("Python"))
print(describe_object(10))

"""
5. Callable：可调用对象的注解
    Callable[[parameter_types], return_type] 用于描述函数、方法等可调用对象。
    Callable[[float, float], float] 表示接收两个 float 并返回 float 的函数。
    Callable[..., T] 表示参数形式不限，但返回值是 T。
"""
print("=================5. Callable：可调用对象的注解=================")

type BinaryOperation = Callable[[float, float], float]


def add_numbers(number1: float, number2: float) -> float:
    return number1 + number2


def apply_operation(
    number1: float,
    number2: float,
    operation: BinaryOperation,
) -> float:
    return operation(number1, number2)


print(apply_operation(10.0, 5.0, add_numbers))
print(apply_operation(10.0, 5.0, lambda left, right: left * right))

"""
5.1 返回函数的注解
    高阶函数返回另一个函数时，也可以使用 Callable 描述返回函数的参数和返回值。
"""
print("=================5.1 返回函数的注解=================")

type PriceRule = Callable[[float], float]


def create_discount(discount_rate: float) -> PriceRule:
    def apply_discount(price: float) -> float:
        return price * discount_rate

    return apply_discount


vip_discount: PriceRule = create_discount(0.8)
print(vip_discount(100.0))

"""
5.2 装饰器的基础注解
    Python 3.14 可以在函数名后直接声明类型参数。
    **Parameters 表示参数规格，ResultT 表示返回值类型。
    Callable[Parameters, ResultT] 可以完整保留原函数的参数签名和返回类型。
"""
print("=================5.2 装饰器的基础注解=================")


def log_result[**Parameters, ResultT](
    function: Callable[Parameters, ResultT],
) -> Callable[Parameters, ResultT]:
    @wraps(function)
    def wrapper(*args: Parameters.args, **kwargs: Parameters.kwargs) -> ResultT:
        result = function(*args, **kwargs)
        print(f"{function.__name__} 返回：{result}")
        return result

    return wrapper


@log_result
def multiply_numbers(number1: int, number2: int) -> int:
    return number1 * number2


print(multiply_numbers(4, 5))

"""
6. 类型别名与 NewType
    类型别名为复杂类型提供更容易理解的名称，不会创建新的运行时类型。
    NewType 用于表达语义不同但底层类型相同的数据，帮助静态检查工具区分它们。
"""
print("=================6. 类型别名与 NewType=================")

type UserId = int
type ScoreHistory = dict[str, list[float]]

user_id: UserId = 1001
score_history: ScoreHistory = {
    "Alice": [88.0, 90.0],
    "Bob": [92.5, 95.0],
}

print(user_id)
print(score_history)

OrderId = NewType("OrderId", int)
ProductId = NewType("ProductId", int)

order_id = OrderId(10001)
product_id = ProductId(20001)

print(order_id, type(order_id))
print(product_id, type(product_id))

"""
6.1 类型别名与 NewType 的区别
    type UserId = int 声明了类型别名，UserId 和 int 对静态检查工具来说基本相同。
    OrderId 和 ProductId 是不同的静态类型，可以避免把商品编号误传给订单编号参数。
    NewType 在运行时几乎没有额外成本，OrderId(10001) 得到的对象仍然是 int。
"""
print("=================6.1 类型别名与 NewType 的区别=================")


def find_order(target_order_id: OrderId) -> str:
    return f"查询订单：{target_order_id}"


print(find_order(order_id))

# find_order(product_id)
# Python 可以运行，但静态类型检查工具会指出 ProductId 不能替代 OrderId

"""
7. 自定义类、延迟注解与 Self
    自定义类的名称可以直接作为参数和返回值类型。
    Python 3.14 默认延迟求值注解，因此类定义内部可以直接使用正在定义的类名。
    Self 表示当前类或其子类，适合标注返回 self 的链式调用方法。
"""
print("=================7. 自定义类、延迟注解与 Self=================")


class TreeNode:
    def __init__(
        self,
        value: str,
        children: list[TreeNode] | None = None,
    ) -> None:
        self.value = value
        self.children: list[TreeNode] = [] if children is None else children

    def add_child(self, child: TreeNode) -> Self:
        self.children.append(child)
        return self

    def display(self, level: int = 0) -> None:
        print(f"{'  ' * level}{self.value}")
        for child in self.children:
            child.display(level + 1)


root = TreeNode("编程语言")
root.add_child(TreeNode("Python")).add_child(TreeNode("Java"))
root.display()

"""
7.1 type、ClassVar 与 Final
    type[ClassName] 表示接收类对象本身，而不是该类的实例。
    ClassVar[T] 表示属性属于类，不是实例字段。
    Final[T] 表示变量不应重新赋值，但 Python 运行时不会强制阻止修改。
"""
print("=================7.1 type、ClassVar 与 Final=================")

MAX_LOGIN_ATTEMPTS: Final[int] = 3


class User:
    category: ClassVar[str] = "普通用户"

    def __init__(self, name: str) -> None:
        self.name = name

    def introduce(self) -> str:
        return f"我是{self.name}，类型是{self.category}。"


def create_instance(class_type: type[User], name: str) -> User:
    return class_type(name)


new_user = create_instance(User, "Alice")
print(new_user.introduce())
print(MAX_LOGIN_ATTEMPTS)

"""
8. TypedDict：描述字典结构
    普通 dict[str, object] 只能说明键和值的大致类型，不能说明每个键的名称和对应类型。
    TypedDict 可以为固定结构的字典分别标注每个字段。
    NotRequired[T] 表示字段可以省略，ReadOnly[T] 表示字段创建后不应被修改。
    TypedDict 主要用于静态类型检查，运行时创建的对象仍然是普通字典。
"""
print("=================8. TypedDict：描述字典结构=================")


class ProductData(TypedDict):
    product_id: ReadOnly[ProductId]
    name: str
    price: float
    stock: int
    category: NotRequired[str]
    description: NotRequired[str]


def print_product(product: ProductData) -> None:
    print(
        f"商品：{product['name']}，"
        f"价格：{product['price']:.2f}，"
        f"库存：{product['stock']}"
    )


keyboard: ProductData = {
    "product_id": ProductId(20001),
    "name": "机械键盘",
    "price": 299.0,
    "stock": 20,
    "category": "数码产品",
}

print_product(keyboard)
print(type(keyboard))

"""
9. 泛型：类型参数语法
    泛型用于表达多个位置之间相互关联的类型，而不是简单地表示任意类型。
    Python 3.14 可以在函数名或类名后的方括号中直接声明类型参数。
    同一次调用中的相同类型参数代表相同的具体类型。
"""
print("=================9. 泛型：类型参数语法=================")


def first_item[ItemT](items: Sequence[ItemT]) -> ItemT | None:
    if not items:
        return None
    return items[0]


class Box[ItemT]:
    def __init__(self, value: ItemT) -> None:
        self._value = value

    def get(self) -> ItemT:
        return self._value

    def set(self, value: ItemT) -> None:
        self._value = value


first_name = first_item(["Alice", "Bob"])
first_number = first_item([10, 20, 30])
print(first_name)
print(first_number)

text_box: Box[str] = Box("Python")
number_box: Box[int] = Box(100)
print(text_box.get())
print(number_box.get())
print(first_item.__type_params__)
print(Box.__type_params__)

"""
9.1 受约束的类型参数
    类型参数可以通过冒号添加约束或上界。
    TextT: (str, bytes) 表示 TextT 只能是 str 或 bytes，并保持输入与返回类型一致。
"""
print("=================9.1 受约束的类型参数=================")


def duplicate_text[TextT: (str, bytes)](value: TextT) -> TextT:
    return value + value


print(duplicate_text("Python"))
print(duplicate_text(b"Python"))

"""
10. Protocol：结构化类型
    Protocol 描述对象需要提供哪些属性或方法，而不要求对象继承指定基类。
    只要对象具有协议要求的结构，静态类型检查工具就可以接受它。
    这种方式也称为结构化子类型，与 Python 的鸭子类型思想相符。
"""
print("=================10. Protocol：结构化类型=================")


@runtime_checkable
class SupportsSummary(Protocol):
    def summary(self) -> str:
        ...


class Book:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def summary(self) -> str:
        return f"《{self.title}》，{self.price:.2f}元"


class Course:
    def __init__(self, name: str, lessons: int) -> None:
        self.name = name
        self.lessons = lessons

    def summary(self) -> str:
        return f"课程：{self.name}，共{self.lessons}课时"


def print_summary(item: SupportsSummary) -> None:
    print(item.summary())


book = Book("Python 类型注解", 69.0)
course = Course("Python 进阶", 24)
print_summary(book)
print_summary(course)
print(isinstance(book, SupportsSummary))

"""
10.1 runtime_checkable 的限制
    使用 @runtime_checkable 后，可以通过 isinstance 检查对象是否具有协议声明的成员。
    运行时检查通常只确认成员是否存在，不会完整检查方法参数和返回值是否匹配。
    完整的协议兼容性仍然应交给静态类型检查工具判断。
"""

"""
11. overload、cast、Never、Annotated 与 TypeIs
    typing 还提供了一些用于表达特殊类型关系的工具。
"""
print("=================11. 其他常用类型工具=================")

"""
11.1 overload 函数重载
    @overload 可以描述同一个函数在不同参数下对应的不同返回类型。
    overload 声明只提供给类型检查工具，最后仍然需要一个真正执行的函数实现。
"""
print("=================11.1 overload 函数重载=================")


@overload
def parse_value(value: str, as_number: Literal[True]) -> int:
    ...


@overload
def parse_value(value: str, as_number: Literal[False] = False) -> str:
    ...


def parse_value(
    value: str,
    as_number: bool = False,
) -> int | str:
    if as_number:
        return int(value)
    return value.strip()


parsed_number = parse_value("100", True)
parsed_text = parse_value(" Python ")
print(parsed_number, type(parsed_number))
print(parsed_text, type(parsed_text))

"""
11.2 cast 类型断言
    cast(TargetType, value) 告诉静态类型检查工具把 value 当作 TargetType。
    cast 不会进行类型检查或类型转换，运行时会原样返回 value。
"""
print("=================11.2 cast 类型断言=================")

raw_value: object = "Python"
text_value = cast(str, raw_value)
print(text_value.upper())
print(text_value is raw_value)

"""
11.3 Never 与穷尽性检查
    Never 表示不可能产生值的类型。
    始终抛出异常的函数可以返回 Never。
    assert_never() 可以帮助类型检查工具确认分支是否覆盖了联合类型的所有可能值。
"""
print("=================11.3 Never 与穷尽性检查=================")


def raise_config_error(message: str) -> Never:
    raise ValueError(f"配置错误：{message}")


type TaskStatus = Literal["pending", "completed"]


def describe_status(status: TaskStatus) -> str:
    match status:
        case "pending":
            return "任务待处理"
        case "completed":
            return "任务已完成"
    assert_never(status)


print(raise_config_error.__annotations__)
print(describe_status("completed"))

"""
11.4 Annotated 附加元数据
    Annotated[T, metadata] 可以在基础类型 T 上附加额外元数据。
    元数据可以供框架、验证库或文档工具使用，Python 本身不会自动执行其中的规则。
"""
print("=================11.4 Annotated 附加元数据=================")

type PositiveInt = Annotated[int, "必须大于 0"]


def set_quantity(value: PositiveInt) -> int:
    if value <= 0:
        raise ValueError("数量必须大于 0")
    return value


print(set_quantity(5))
print(PositiveInt.__value__)
print(get_origin(PositiveInt.__value__))
print(get_args(PositiveInt.__value__))

"""
11.5 TypeIs 类型缩小
    TypeIs[NarrowedType] 表示函数返回 True 时，传入值可以缩小为 NarrowedType。
    TypeIs 适合把重复的 isinstance 检查封装成可以被静态类型工具理解的判断函数。
    缩小后的类型必须是原参数类型的子类型。
"""
print("=================11.5 TypeIs 类型缩小=================")


def is_string_sequence(
    values: Sequence[object],
) -> TypeIs[Sequence[str]]:
    return all(isinstance(value, str) for value in values)


def join_strings(values: Sequence[object]) -> str:
    if is_string_sequence(values):
        return ", ".join(values)
    return "序列中包含非字符串元素"


print(join_strings(["Python", "类型注解", "TypeIs"]))
print(join_strings(["Python", 3.14]))

"""
12. 运行时读取类型注解
    Python 3.14 默认延迟求值注解，需要读取时才计算注解表达式。
    annotationlib.get_annotations() 是 Python 3.14 提供的底层读取接口。
    typing.get_type_hints() 会解析类型别名等信息，并返回更适合类型处理的注解字典。
    get_origin() 和 get_args() 可以拆解 list[str]、联合类型等组合类型。
"""
print("=================12. 运行时读取类型注解=================")

print(TreeNode.add_child.__annotations__)
print(annotationlib.get_annotations(TreeNode.add_child))
print(
    annotationlib.get_annotations(
        TreeNode.add_child,
        format=annotationlib.Format.STRING,
    )
)
print(get_type_hints(TreeNode.add_child))

list_annotation = list[str]
union_annotation = int | str

print(get_origin(list_annotation))
print(get_args(list_annotation))
print(get_origin(union_annotation))
print(get_args(union_annotation))

"""
12.1 类型注解不等于运行时验证
    Python 默认不会根据注解检查传入的数据。
    程序处理外部输入时，仍然需要 isinstance、条件判断或专门的验证库。
"""
print("=================12.1 类型注解不等于运行时验证=================")


def add_integers(number1: int, number2: int) -> int:
    return number1 + number2


print(add_integers(10, 20))
print(add_integers("10", "20"))  # type: ignore[arg-type]


def register_age(age: int) -> int:
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("age 必须是整数")
    if age < 0:
        raise ValueError("age 不能小于 0")
    return age


print(register_age(20))

# register_age("20")
# TypeError：运行时检查发现 age 不是整数

"""
12.2 静态类型检查工具
    类型注解需要配合编辑器或静态类型检查工具才能提前发现问题。
    常见工具包括 mypy、Pyright 和基于 Pyright 的 Pylance。
    静态检查不会执行程序，适合在运行或提交代码前发现潜在类型错误。

    常见命令示例：
        mypy chapter_04/03_function_type_annotation_instruction.py
        pyright chapter_04/03_function_type_annotation_instruction.py

    不同工具和配置的严格程度可能不同，应在项目中统一 Python 版本和检查规则。
"""
print("=================12.2 静态类型检查工具=================")

"""
13. Python 3.14 推荐写法
    本文件以 Python 3.14 为目标版本，统一使用以下现代语法：
    （1）使用 list[str]，不再使用 typing.List[str]。
    （2）使用 int | str，不再使用 Union[int, str]。
    （3）使用 str | None，通常不再使用 Optional[str]。
    （4）使用 type Alias = ... 声明类型别名。
    （5）使用 def function[T] 和 class ClassName[T] 声明泛型。
    （6）使用 Self、Never、TypeIs、ReadOnly 和 NotRequired 表达更精确的类型关系。
    （7）使用 annotationlib 读取 Python 3.14 延迟求值的注解。

    旧式 Union、Optional、TypeVar 和 Generic 写法仍可用于维护旧项目，
    但新建的 Python 3.14 项目可以优先采用本文件中的现代写法。
"""
print("=================13. Python 3.14 推荐写法=================")

"""
14. 综合案例：带类型注解的订单计算
    本案例综合使用以下知识点：
    （1）NewType 区分订单编号和商品编号。
    （2）TypedDict 描述订单项和计算结果的字典结构。
    （3）Literal 限制货币单位。
    （4）Callable 描述可替换的折扣规则。
    （5）Sequence 允许调用者传入列表或元组。
    （6）DiscountRule | None 表示折扣规则可以是 None。
    （7）ReadOnly 和 NotRequired 描述只读字段与可选字段。
"""
print("=================14. 综合案例：带类型注解的订单计算=================")

type Currency = Literal["CNY", "USD"]
type DiscountRule = Callable[[float], float]


class OrderItem(TypedDict):
    product_id: ReadOnly[ProductId]
    name: str
    unit_price: float
    quantity: int
    remark: NotRequired[str]


class OrderResult(TypedDict):
    order_id: ReadOnly[OrderId]
    subtotal: float
    discount_amount: float
    total: float
    currency: Currency


def percentage_discount(rate: float) -> DiscountRule:
    if not 0 <= rate <= 1:
        raise ValueError("折扣率必须在 0 到 1 之间")

    def apply_discount(amount: float) -> float:
        return amount * rate

    return apply_discount


def calculate_order(
    target_order_id: OrderId,
    items: Sequence[OrderItem],
    discount_rule: DiscountRule | None = None,
    *,
    currency: Currency = "CNY",
) -> OrderResult:
    subtotal = 0.0

    for item in items:
        if item["quantity"] <= 0:
            raise ValueError("商品数量必须大于 0")
        if item["unit_price"] < 0:
            raise ValueError("商品单价不能小于 0")
        subtotal += item["unit_price"] * item["quantity"]

    subtotal = round(subtotal, 2)
    total = subtotal if discount_rule is None else discount_rule(subtotal)
    total = round(total, 2)
    return {
        "order_id": target_order_id,
        "subtotal": subtotal,
        "discount_amount": round(subtotal - total, 2),
        "total": total,
        "currency": currency,
    }


order_items: list[OrderItem] = [
    {
        "product_id": ProductId(20001),
        "name": "Python 进阶书",
        "unit_price": 79.8,
        "quantity": 2,
    },
    {
        "product_id": ProductId(20002),
        "name": "Python 练习册",
        "unit_price": 39.9,
        "quantity": 1,
    },
]

order_result = calculate_order(
    OrderId(10001),
    order_items,
    percentage_discount(0.9),
    currency="CNY",
)

print("订单计算结果：")
for result_key, result_value in order_result.items():
    print(f"{result_key}：{result_value}")

"""
15. 常见错误
    下面部分示例在运行时可能不会报错，但会被静态类型检查工具发现。
"""
print("=================15. 常见错误=================")

# count: int
# print(count)
# NameError：类型注解不等于赋值

# age: int = "20"
# 静态类型错误：字符串不能赋给声明为 int 的变量

# def invalid_default(retry_count: int = "3") -> None:
#     pass
# 静态类型错误：默认值类型与参数注解不一致

# def nullable_but_required(value: str | None) -> None:
#     print(value)
#
# nullable_but_required()
# TypeError：可空类型允许传入 None，但不会让参数自动获得默认值

# wrong_scores: list[int] = [90, "优秀", 88]
# 静态类型错误：list[int] 中不应包含 str

# converted_number = cast(int, "100")
# print(converted_number + 1)
# TypeError：cast 不会把字符串转换成整数

# MAX_LOGIN_ATTEMPTS = 5
# 静态类型错误：Final 变量不应重新赋值，但 Python 运行时不会阻止

# invalid_product: ProductData = {"name": "鼠标", "price": 99.0}
# 静态类型错误：ProductData 缺少必填的 stock 字段

# find_order(ProductId(20001))
# 静态类型错误：ProductId 不能替代 OrderId

"""
16. 注意事项
    16.1 类型注解用于描述预期类型，不会自动完成类型转换或运行时验证。
    16.2 函数参数应尽量使用 Sequence、Mapping 等满足需求的抽象类型。
    16.3 函数返回值应尽量写出明确类型，让调用者知道会得到什么数据。
    16.4 T | None 表示值可以为空，参数是否可以省略取决于是否设置默认值。
    16.5 谨慎使用 Any，过多的 Any 会使静态类型检查失去作用。
    16.6 类型别名用于简化表达，NewType 用于区分语义不同的相同底层类型。
    16.7 TypedDict 适合描述固定字典结构，复杂业务对象也可以使用类或数据类。
    16.8 泛型类型参数用于表达类型之间的关系，不应把所有不确定类型都改成泛型。
    16.9 cast 只是静态类型断言，不会进行运行时检查或类型转换。
    16.10 编写公共函数和模块时，应配合 mypy 或 Pyright 等工具持续检查。
    16.11 团队项目应统一最低 Python 版本，避免使用运行环境不支持的新注解语法。
"""
