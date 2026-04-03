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
