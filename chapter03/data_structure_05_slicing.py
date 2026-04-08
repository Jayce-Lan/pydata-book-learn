from utils.logger import log
'''
    切片
    1. list[start:stop:step]
        start: 起始位置，默认为0
        stop: 结束位置，默认为len(list)
        step: 步长，默认为1
    2. list[start:stop]
        等价于list[start:stop:1]
    3. list[:stop]
        等价于list[0:stop:1]
    4. list[start:]
        等价于list[start:len(list):1]
    5. list[:]
        等价于list[0:len(list):1]，即复制整个列表
'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
    list[start:stop]返回list中从start到stop-1位置的元素组成的新列表
    如果start或stop超出list的范围，Python会自动调整为list的边界
'''
sublist = list[2:5]
log.info(f'list[2:5]: {sublist}') # [3, 4, 5]

'''
    使用切片赋值，可以在指定位置插入、删除或替换元素
'''
list_test = [1, 2, 3, 4, 5]
list_test[2:3] = [10, 20] # 将list_test中索引2位置的元素替换为10和20，原来的3被删除了
log.info(f'切片赋值后的list_test: {list_test}') # [1, 2, 10, 20, 5]

'''
    切片的起始位置和结束位置都可以省略，默认为列表的边界
'''
log.info(f'list[:5]: {list[:5]}') # [1, 2, 3, 4, 5]
log.info(f'list[5:]: {list[5:]}') # [6, 7, 8, 9]
log.info(f'list[:]: {list[:]}') # [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''
    切片的步长可以为负数，表示从右向左切片
    例如：
    H  E  L  L  O
    0  1  2  3  4
    -4 -3 -2 -1 
'''
log.info(f'list[-4:]: {list[-4:]}') # [6, 7, 8, 9]
log.info(f'list[-5:]: {list[-5:]}') # [5, 6, 7, 8, 9]
log.info(f'list[:-5]: {list[:-5]}') # [1, 2, 3, 4]
log.info(f'list[-5:-2]: {list[-5:-2]}') # [5, 6, 7]


'''
    在第二个:后使用可以以指定步长，默认为1
'''
log.info(f'list[::2]: {list[::2]}') # [1, 3, 5, 7, 9]
log.info(f'list[::3]: {list[::3]}') # [1, 4, 7]
# 当步长设置为-1时，可以实现列表的反转
log.info(f'list[::-1]: {list[::-1]}') # [9, 8, 7, 6, 5, 4, 3, 2, 1]