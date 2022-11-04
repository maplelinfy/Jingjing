
'''
所有有返回值的函数统一返回0表示格式正确，1表示格式有误
'''

import re

def date_check(date):
    '''
    日期检测，格式需为 YYYY-MM-DD
    '''
    res = re.findall('^20[0-2][0-9]-[0-1][0-9]-[0-3][0-9]$', date)
    if len(res) > 0:
        y, m, d = date.split('-')
        m = int(m)
        d = int(d)
        if m == 0 or m > 12 or d == 0 or d > 31:
            return 1
        else:
            return 0
    else:
        return 1

def money_check(n):
    '''
    金额检测，即判断n是否为float类型数字
    '''
    try:
        float(n)
        return 0
    except ValueError:
        return 1

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
        return 0, []
    else:
        return 1, duplicate_list

def duplicate_name_check_easy(name_list):
    '''
    重名检测，只判断是否有重名
    '''
    if len(name_list) == len(set(name_list)):
        return 0
    else:
        return 1

def black_white_list_check(date):
    '''
    黑白名单错误日期检测
    '''
    if date_check(date):
        print('警告！黑白名单中日期格式有误，错误日期：' + date)

def people_file_check(daily_wage, join_date, leave_date):
    '''
    员工列表文件数据检测
    '''
    if daily_wage == '':
        print('警告！员工列表文件中日薪存在缺失，请补充')
    else:
        if money_check(daily_wage):
            print('警告！员工列表文件中日薪格式有误，错误日薪：' + daily_wage)
    if join_date == '':
        print('警告！员工列表文件中入职日期存在缺失，请补充')
    else:
        if date_check(join_date):
            print('警告！员工列表文件中入职日期格式有误，错误日期：' + join_date)
    for ld in leave_date:
        if date_check(ld):
            print('警告！员工列表文件中休假日期格式有误，错误日期：' + ld)

def project_file_check(budget):
    '''
    项目列表文件数据检测
    '''
    if budget == '':
        print('警告！项目列表文件中预算存在缺失，请补充')
    else:
        if money_check(budget):
            print('警告！项目列表文件中预算格式有误，错误预算：' + budget)

def duplicate_people_name_check(people_name):
    '''
    员工重名检测
    '''
    for name in people_name:
        if name == '':
            print('警告！员工列表文件中有姓名为空')
            break
    res, name = duplicate_name_check(people_name)
    if res:
        print('警告！员工列表文件中有重名，重名为：')
        print(name)

def duplicate_project_name_check(project_name):
    '''
    项目重名检测
    '''
    for name in project_name:
        if name == '':
            print('警告！项目列表文件中有名称为空')
            break
    res, name = duplicate_name_check(project_name)
    if res:
        print('警告！项目列表文件中有重名，重名为：')
        print(name)
