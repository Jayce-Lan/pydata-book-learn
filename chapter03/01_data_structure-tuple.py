import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

'''
    tuple元组
'''
# 简单元组
tup = 4, 5, 6 # 也可以写为 tup = (4, 5, 6)
log.info(tup)  # (4, 5, 6)

# 元组的元素可以是不同类型的对象
tup2 = 4, 'hello', [1, 2, 3]
log.info(tup2)  # (4, 'hello', [1, 2, 3])

tup3 = (1, 2, 3), (4, 5)
log.info(tup3)  # ((1, 2, 3), (4, 5))

# 使用tuple()函数创建元组，可以将任何可迭代对象转换为元组
tup4 = tuple([1, 2, 3])  # 从列表创建
log.info(tup4)  # (1, 2, 3)

tup5 = tuple('hello')  # 从字符串创建
log.info(tup5)  # ('h', 'e', 'l', 'l', 'o')

log.info(tup5[2])  # 'l'
# 元组是不可变的，不能修改元组中的元素
try:
    tup5[2] = 'x'  # 会引发TypeError
except TypeError as e:
    log.error(f"Error: {e}")  # Error: 'tuple' object does not support item assignment

# 如果元组中的某个元素是可变对象（如列表），则可以修改该可变对象
tup6 = (1, 2, [3, 4])
log.info(tup6)  # (1, 2, [3, 4])
tup6[2][0] = 'x'  # 修改列表中的元素
log.info(tup6)  # (1, 2, ['x', 4])

tup7 = (1, 'foo', ['a', 'b'], 3)
log.info(tup7)  # (1, 'foo', ['a', 'b'], 3)
tup7[2].append('c')  # 修改列表中的元素
log.info(tup7)  # (1, 'foo', ['a', 'b', 'c'], 3)

# 运用+运算符连接元组
tup8 = (1, 2) + (3, 4)
log.info(tup8)  # (1, 2, 3, 4)

# 运用*运算符重复元组
tup9 = ('foo', 'bar')
log.info(f"tup9: {tup9 * 4}")  # ('foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'bar')

# 拆分元组，如果想把元组的元素赋值给变量，Python会试图拆分元组
tup10 = (1, 2, 3)
a, b, c = tup10
log.info(f"a: {a}, b: {b}, c: {c}")  # a: 1, b: 2, c: 3
# 值得注意的是，如果变量的数量与元组中的元素数量不匹配，就会引发ValueError异常
try:
    d, e = tup10
    log.info(f"d: {d}, e: {e}")  # ValueError: too many values to unpack (expected 2)
except ValueError as e:
    log.error(f"Error: {e}") # Error: too many values to unpack (expected 2, got 3)

# 含有元组的元素也会被拆分
tup11 = (1, (2, 3), 4)
a, (b, c), d = tup11
log.info(f"a: {a}, b: {b}, c: {c}, d: {d}")  # a: 1, b: 2, c: 3, d: 4
# 也可以不拆分元组中的元素
a, b, c = tup11
log.info(f"a: {a}, b: {b}, c: {c}") # a: 1, b: (2, 3), c: 4

# 使用变量拆分遍历带有元组的列表
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    log.info(f"a: {a}, b: {b}, c: {c}")
    # a: 1, b: 2, c: 3
    # a: 4, b: 5, c: 6
    # a: 7, b: 8, c: 9

# 如果只希望截取元组的前几个值，而且不希望报错，可以使用*运算符来捕获剩余的元素
# 这样可以避免too many values to unpack的错误
tup12 = (1, 2, 3, 4, 5)
a, b, *rest = tup12
log.info(f"a: {a}, b: {b}, rest: {rest}")  # a: 1, b: 2, rest: [3, 4, 5]
# 一般情况下，*rest会捕获剩余的元素，并将它们放在一个列表中。如果不需要捕获剩余的元素，可以使用_来表示
a, b, *_ = tup12
log.info(f"a: {a}, b: {b}")  # a: 1, b: 2
# 也可以截取后几个值
*rest, c, d = tup12
log.info(f"rest: {rest}, c: {c}, d: {d}")  # rest: [1, 2, 3], c: 4, d: 5

# 元组的一些方法
# count()方法可以统计元组中某个元素出现的次数
tup13 = (1, 2, 3, 2, 4, 2)
log.info(tup13.count(2))  # 3

# index()方法可以返回元组中某个元素第一次出现的索引位置
log.info(tup13.index(2))  # 1
# 如果元素不存在于元组中，index()方法会引发ValueError异常
try:
    log.info(tup13.index(5))  # ValueError: tuple.index(x): x not found
except ValueError as e:
    log.error(f"Error: {e}")  # Error: tuple.index(x): x not found
