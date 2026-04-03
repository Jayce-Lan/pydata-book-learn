from utils.logger import log

'''
    list列表
    列表语义与元组接近，且都是序列类型，在许多函数中，列表和元组可以互换使用，但列表是可变的，而元组是不可变的。
'''
'''
    list的基础操作
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

'''
    如果不考虑性能，remove和append可以当做完美的多重集数据结构
'''
# 添加和删除元素
list4 = [1, 2, 'foo']
log.info(f'list4: {list4}')  # list4: [1, 2, 'foo']
# 将元素添加到末尾
list4.append('bar')
log.info(f'list4: {list4}')  # list4: [1, 2, 'foo', 'bar']
# 将元素添加到指定位置
list4.insert(2, 'hello') # 在索引2的位置插入'hello'，后续元素依次后移
log.info(f'list4: {list4}')  # list4: [1, 'hello', 2, 'foo', 'bar']

# 与insert相反的是pop方法，pop方法会删除指定位置的元素，并返回该元素
popped = list4.pop(2)  # 删除索引2的元素，并返回
log.info(f'popped: {popped}')  # popped: 'hello'
log.info(f'list4: {list4}')  # list4: [1, 2, 'foo', 'bar']

# 使用remove方法删除列表中的元素，remove方法会删除列表中第一个匹配的元素
list5 = [1, 2, 3, 2, 4, 2, 5, 2, 6]
log.info(f'list5: {list5}')  # list5: [1, 2, 3, 2, 4, 2, 5, 2, 6]
log.info(f'list5.count(2): {list5.count(2)}')  # list5.count(2): 4

log.info(f'remove: {list5.remove(2)}')  # 删除列表中第一个匹配的元素2，返回值为None
log.info(f'list5: {list5}')  # list5: [1, 3, 2, 4, 2, 5, 2, 6]
log.info(f'list5.count(2): {list5.count(2)}')


'''
    值的检查
'''
list6 = ['foo', 'bar', 'baz', 'qux']
log.info(f'boss in list6: {"boss" in list6}')  # boss in list6: False
log.info(f'foo in list6: {"foo" in list6}')  # foo in list6: True

'''
    串联列表
    性能优先级：extend > +运算符
'''
list7 = [1, 2, 3]
list8 = [4, 5, 6]
# 与元组一样，列表也可以使用+运算符进行串联
list9 = list7 + list8
log.info(f'list9: {list9}')  # list9: [1, 2, 3, 4, 5, 6]

# 已定义的列表可以使用extend方法进行串联，extend方法会将另一个列表中的元素添加到当前列表的末尾，可以追加多个元素
# 性能上来说，extend方法比使用+运算符更高效，因为+运算符会创建一个新的列表，而extend方法会直接修改原有的列表
list10 = [1, 2, 3]
list10.extend([4, 5, 6, (7, 8)])
log.info(f'list10: {list10}')  # list10: [1, 2, 3, 4, 5, 6, (7, 8)]

'''
    list的排序
'''
list11 = [7, 2, 5, 1, 3]
# 使用sort方法对列表进行排序，sort方法会直接修改原有的列表
list11.sort()
log.info(f'list11: {list11}')  # list11: [1, 2, 3, 5, 7]

# sort内置了一些参数，可以自定义排序规则
# key参数可以指定一个函数，用于从每个元素中提取一个用于排序的键
list12 = ['foo', 'card', 'bar', 'aaaa']
list12.sort(key=len, reverse=True)  # 根据字符串长度进行排序
log.info(f'list12: {list12}')  # list12: ['card', 'aaaa', 'foo', 'bar']

# reverse参数可以指定排序的顺序，默认为False，表示升序排序，如果设置为True，则表示降序排序
list13 = [7, 2, 5, 1, 3]
list13.sort(reverse=True)  # 降序排序
log.info(f'list13: {list13}')  # list13: [7, 5, 3, 2, 1]