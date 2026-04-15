from utils.logger import log

'''
    字典（dict）是一种无序的、可变的、键值对的数据结构。它更为常见的名字是哈希映射或关联数组
    字典中的每个元素都是一个键值对，键必须是唯一的，值可以是任意类型
    字典使用花括号 {} 定义，键值对之间使用冒号 : 分隔，多个键值对之间使用逗号 , 分隔
'''
'''
    创建字典
'''
# 使用花括号创建字典
my_dict01 = {}
log.info(f'创建的空字典: {my_dict01}') # {}

my_dict02 = {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling']}
log.info(f'创建的字典: {my_dict02}') # {'name': 'Alice', 'age': 30, 'city': 'New York', 'hobbies': ['reading', 'traveling']}

my_dict03 = {'name': 'Jayce', 7: [1, 2, 3, 4]}
log.info(f'创建的字典: {my_dict03}') # {'name': 'Jayce', 7: [1, 2, 3, 4]}

# 访问字典中的值
log.info(f"访问字典中的值: {my_dict03['name']}")
log.info(f"访问字典中的值: {my_dict03[7]}")

# 使用 dict() 函数创建字典
my_dict04 = dict(name='Bob', age=25, city='Los Angeles')
log.info(f'使用 dict() 函数创建的字典: {my_dict04}') # {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'}

'''
    确认字典中是否存在某个键
    使用 in 关键字可以检查字典中是否存在某个键，返回 True 或 False
'''
log.info(f"检查字典中是否存在键 'name': {'name' in my_dict02}") # True
log.info(f"检查字典中是否存在键 'country': {'country' in my_dict02}") # False

'''
    可以使用del或pop方法删除字典中的键值对
    del语句用于删除字典中的键值对，语法为 del dict[key]
    pop方法用于删除字典中的键值对，并返回被删除的值，语法为 dict.pop(key, default=None)，其中 key 是要删除的键，default 是当前键不存在时返回的默认值，默认为 None
'''
# 使用 del 删除键值对
my_dict05 = {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
log.info(f'原始字典: {my_dict05}') # {'name: 'Charlie', 'age': 35, 'city': 'Chicago'}
del my_dict05['age']
log.info(f'删除键值对后的字典: {my_dict05}') # {'name: 'Charlie', 'city': 'Chicago'} 
# 使用del方法删除不存在的键会引发 KeyError 异常
try:
    del my_dict05['age'] # KeyError: 'age'
except KeyError as e:
    log.error(f'删除不存在的键时发生错误: {e}')

# 使用 pop 删除键值对
my_dict06 = {'name': 'David', 'age': 40, 'city': 'Houston'}
log.info(f'原始字典: {my_dict06}') # {'name: 'David', 'age': 40, 'city': 'Houston'}
removed_value = my_dict06.pop('age')
log.info(f'删除键值对后的字典: {my_dict06}') # {'name: 'David', 'city': 'Houston'}
log.info(f'被删除的值: {removed_value}') # 40
# 使用pop方法删除不存在的键会引发 KeyError 异常，除非提供了默认值
try:
    removed_value = my_dict06.pop('age') # KeyError: 'age'
except KeyError as e:
    log.error(f'删除不存在的键时发生错误: {e}') 

log.info(f'使用默认值删除不存在的键: {my_dict06.pop("age", None)}') # 返回默认值，不引发异常

'''
    keys 和 values 是字典的键和值的迭代器方法。虽然键值对没有顺序，这两个方法可以用相同的顺序输出键和值
'''
my_dict07 = {'name': 'Eve', 'age': 28, 'city': 'Miami'}
log.info(f'字典的键: {list(my_dict07.keys())}') # ['name', 'age', 'city']
log.info(f'字典的值: {list(my_dict07.values())}') # ['Eve', 28, 'Miami']

'''
    使用update方法可以将一个字典的键值对更新到另一个字典中，如果有重复的键，后者的值会覆盖前者的值
'''
my_dict08 = {'name': 'Frank', 'age': 32, 'city': 'Seattle'}
my_dict09 = {'age': 33, 'country': 'USA'}
log.info(f'原始字典: {my_dict08}') # {'name': 'Frank', 'age': 32, 'city': 'Seattle'}
my_dict08.update(my_dict09)
log.info(f'更新后的字典: {my_dict08}') # {'name': 'Frank', 'age': 33, 'city': 'Seattle', 'country': 'USA'}

'''
    使用序列创建字典
'''
my_dict10 = {}
key_list = ['name', 'age', 'city']
value_list = ['Grace', 29, 'Boston']
for key, value in zip(key_list, value_list):
    my_dict10[key] = value
log.info(f'使用序列创建的字典: {my_dict10}')

# 其实也可以使用 dict() 函数和 zip() 函数结合来创建字典
my_dict11 = dict(zip(key_list, value_list))
log.info(f'使用 dict() 和 zip() 创建的字典: {my_dict11}')