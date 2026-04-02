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