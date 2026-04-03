from utils.logger import log
import bisect

'''
    二分检索
    1. bisect.bisect_left(arr, x)
        返回 x 应该插入的最左位置
        如果 x 已存在，返回第一个 x 左边的索引
        用于找重复元素的第一个位置（大于等于x）
    2. bisect.bisect_right(arr, x)
        返回 x 应该插入的最右位置
        如果 x 已存在，返回最后一个 x 右边的索引
        用于找重复元素的最后一个位置（大于x）
    3. bisect.bisect(arr, x)
        和 bisect_right 完全一样
    4. bisect.insort_left(arr, x)
        在 bisect_left 位置插入 x，保持列表有序
    5. bisect.insort_right(arr, x)
        在 bisect_right 位置插入 x，保持列表有序
    6. bisect.insort(arr, x)
        和 insort_right 一样
'''
# 首先，使用bisect必须保证list有序，否则不生效
list = [1, 3, 3, 3, 5, 6, 7, 8]

'''
    bisect_left(list, x)返回list中从左到右第一个[大于等于]x的位置
    如果list中没有x，返回第一个大于x的位置,如果list中所有元素都小于x，返回len(list)
'''
# 查询从左到右第一个大于或等于3的位置，如果元素
index_left = bisect.bisect_left(list, 3)
log.info(f'第一个大于等于3的位置: {index_left}')
log.info(f'list: {list}')

list_error = [1, 3, 2, 4, 2, 5, 6]
index_error = bisect.bisect_left(list_error, 2)
log.info(f'错误的list: {list_error}')
log.info(f'错误的list中第一个2的位置: {index_error}') # 1, 因为list_error没有排序，所以bisect_left返回了错误的结果

'''
    bisect_right(list, x)返回list中第一个[大于]x的位置
    如果list中没有x，返回第一个大于x的位置,如果list中所有元素都小于或等于x，返回len(list)
'''
index_right = bisect.bisect_right(list, 1)
log.info(f'从右到左第一个1的位置: {index_right}')
index_right = bisect.bisect_right(list, 9)
log.info(f'从右到左第一个9的位置: {index_right}')

'''
    bisect(list, x)和bisect_right完全一样
'''
index_bisect = bisect.bisect(list, 3)
log.info(f'从右到左第一个3的位置: {index_bisect}')
index_bisect = bisect.bisect(list, 9)
log.info(f'从右到左第一个9的位置: {index_bisect}')

'''
    insort_left(list, x)在bisect_left(list, x)位置插入x，保持list有序
'''
log.info(f'数据插入前list: {list}')
bisect.insort_left(list, 2)
log.info(f'list: {list}')

'''
    insort_right(list, x)在bisect_right(list, x)位置插入x，保持list有序
'''
bisect.insort_right(list, 2)
log.info(f'list: {list}')

'''
    insort(list, x)和insort_right完全一样
'''
bisect.insort(list, 2)
log.info(f'list: {list}')
