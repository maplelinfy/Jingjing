
'''
所有函数统一返回1表示格式正确，0表示格式有误
'''

import re

def date_check(date):
    '''
    日期检测，格式需为 YYYY-MM-DD
    '''
    res = re.findall('^20[0-2][0-9]-[0-1][0-9]-[0-3][0-9]$', date)
    if len(res) > 0:
        return 1
    else:
        return 0

def money_check(n):
    '''
    金额检测，即判断n是否为float类型数字
    '''
    try:
        float(n)
        return 1
    except ValueError:
        return 0

def duplicate_name_check(name_list):
    '''
    重名检测，输出重名列表
    '''
    name_dict = {}
    duplicate_list = []
    for name in name_list:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    for name in name_dict:
        if name_dict[name] > 1:
            duplicate_list.append(name)
    if len(duplicate_list) == 0:
        return 1, []
    else:
        return 0, duplicate_list

def duplicate_name_check_easy(name_list):
    '''
    重名检测，只判断是否有重名
    '''
    if len(name_list) == len(set(name_list)):
        return 1
    else:
        return 0
