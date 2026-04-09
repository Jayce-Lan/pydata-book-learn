from utils.logger import log

'''
    序列函数
'''

'''
    enumerate函数，用于将一个可迭代对象转换为一个包含索引和值的迭代器
    语法：enumerate(iterable, start=0)
    iterable: 可迭代对象，如列表、元组、字符串等
    start: 索引的起始值，默认为0
    当索引数据时，使用 enumerate 的一个好方法是计算序列（唯一的） dict 映射到位置的值
'''
some_list = ['a', 'b', 'c']
mapping = {}
for index, value in enumerate(some_list):
    log.info(f'索引: {index}, 值: {value}')
    mapping[value] = index
log.info(f'mapping: {mapping}') # {'a': 0, 'b': 1, 'c': 2}

'''
    sorted函数，用于对可迭代对象进行排序，返回一个新的列表
    语法：sorted(iterable, key=None, reverse=False)
    iterable: 可迭代对象，如列表、元组、字符串等
    key: 用于排序的函数，默认为None，表示直接比较元素
    reverse: 是否反向排序，默认为False
'''
# 列表排序
some_list = [3, 1, 2, 5, 4, 0, 2]
sorted_list = sorted(some_list)
log.info(f'排序后的列表: {sorted_list}') # [0, 1, 2, 2, 3, 4, 5]
# 字符串排序
some_string = 'hello world'
sorted_string = sorted(some_string)
log.info(f'排序后的字符串: {sorted_string}') # [' ', 'd', 'e', 'h', 'l', 'l', 'o', 'o', 'r', 'w']

'''
    zip函数，可以将多个列表、元组或其它序列成对组合成一个元组列表
    语法：zip(*iterables)
    iterables: 可迭代对象，如列表、元组、字符串等
    zip函数会返回一个迭代器，生成由输入的可迭代对象中对应位置的元素组成的元组
    当输入的可迭代对象长度不同时，zip函数会以最短的可迭代对象为准，生成的元组数量等于最短可迭代对象的长度
'''
seq1 = ['a', 'b', 'c']
seq2 = [0, 1, 2]
zipped = zip(seq1, seq2)
log.info(f'zip结果: {list(zipped)}') # [('a', 0), ('b', 1), ('c', 2)]

seq3 = [True, False]
zipped = zip(seq1, seq2, seq3)
log.info(f'zip结果: {list(zipped)}') # [('a', 0, True), ('b', 1, False)]

# 迭代多个序列时与enumerate结合使用
for index, (a, b) in enumerate(zip(seq1, seq2)):
    log.info(f'索引: {index}, a: {a}, b: {b}')

'''
    reversed函数，可以从后向前迭代一个序列
    语法：reversed(seq)
    seq: 可迭代对象，如列表、元组、字符串等
    reversed函数返回一个迭代器，生成输入序列中元素的反向序列
'''
reversed_list = list(reversed(range(5)))
log.info(f'reversed结果: {reversed_list}') # [4, 3, 2, 1, 0]
reversed_string = ''.join(reversed('hello'))
log.info(f'reversed结果: {reversed_string}') # 'olleh' 