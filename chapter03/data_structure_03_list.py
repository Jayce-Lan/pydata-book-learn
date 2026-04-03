from utils.logger import log

'''
    list列表
    列表语义与元组接近，且都是序列类型，在许多函数中，列表和元组可以互换使用，但列表是可变的，而元组是不可变的。
'''
# 与元组相比，列表是可变的，可以修改列表中的元素
list1 = [2, 3, 4, None]
log.info(f'list1: {list1}')  # list1: [2, 3, 4, None]

# 除了使用[]创建列表，还可以使用list()函数创建列表
tuple1 = ('foo', 'boo', 'bar')
list2 = list(tuple1)  # 从元组创建列表
log.info(f'list2: {list2}')  # list2: ['foo', 'boo', 'bar']

# 修改列表中的元素
list2[1] = 'hello'
log.info(f'list2: {list2}')  # list2: ['foo', 'hello', 'bar']

# list函数通常在数据处理中用于实体化迭代器或生成器
gen = range(10)
log.info(f'gen: {gen}')  # gen: range(0, 10)
list3 = list(gen)  # 从生成器创建列表
log.info(f'list3: {list3}')  # list3: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 添加和删除元素
