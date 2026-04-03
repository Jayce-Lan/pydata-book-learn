import logging
import logging.config
import os

current_filename = os.path.splitext(os.path.basename(__file__))[0]
logging.config.fileConfig('logging.conf')
log = logging.getLogger(current_filename)

'''
    Python中的元素替换
    与Java中的元素替换不同，Python中的元素替换不需要通过中间值来暂存某个元素的值，而是直接通过赋值语句来完成元素的替换。
'''
a, b = 1, 2
log.info(f"Before swap: a = {a}, b = {b}")  # Before swap: a = 1, b = 2
b, a = a, b  # 直接通过赋值语句来完成元素的替换
log.info(f"After swap: a = {a}, b = {b}")  # After swap: a = 2, b = 1
