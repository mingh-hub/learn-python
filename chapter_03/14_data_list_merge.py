# 列表：合并

num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 12, 23, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

## 1. 常规合并
for num in num_list2:
    num_list1.append(num)
print(f"正常合并后的列表：{num_list1}")

### 去重
new_list = []
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print(f"正常合并去重后的列表：{new_list}")

## 2. 解包合并
### 解包：将列表这一类容器解开成一个一个独立的元素
### 组包：将多个值合并到一个容器
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 12, 23, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
num_list = [*num_list1, *num_list2] # 解包
print(f"解包合并后的列表：{num_list}")
### 去重
new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print(f"解包合并去重后的列表：{new_list}")

## 3. 使用 +
num_list = num_list1 + num_list2
print(f"使用 + 合并后的列表：{num_list}")
### 去重
new_list = []
for num in num_list:
    if num not in new_list:
        new_list.append(num)
print(f"使用 + 合并去重后的列表：{new_list}")

## 4. 使用列表推导式
seen = set()
print(seen)
new_list = [x for x in num_list if x not in seen and not seen.add(x)] # seen.add(x) 如果 seen 已存在，返回 None，not seen.add(x) 表示向集合 seen 中添加元素成功
print(seen)
seen.clear()
print(seen)
print(f"使用列表推导式去重后的列表：{new_list}")
