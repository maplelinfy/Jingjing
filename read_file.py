
import xlrd
import xlwt

from data_check import black_white_list_check, people_file_check, project_file_check, duplicate_people_name_check, duplicate_project_name_check
from common import people, project
from constant import *

people_name = [] #员工姓名
project_name = [] #项目名称

def load_list(list_file):
    '''
    读单列文件为列表
    '''
    res = []
    with open(list_file) as f:
        for line in f:
            date = line.strip()
            black_white_list_check(date)
            if date != '':
                res.append(date)
    return res

def load_black_white_list():
    '''
    读取黑白名单列表
    '''
    return load_list(black_list_file), load_list(white_list_file)

def read_xlsx(xlsx_file):
    '''
    读取excel文件存为列表
    '''
    res = []
    wb = xlrd.open_workbook(xlsx_file)
    sh = wb.sheet_by_name('Sheet1')
    for i in range(0, sh.nrows):
        ll = sh.row_values(i)
        res.append(ll)
    return res

def load_people_list():
    '''
    根据员工信息文件初始化员工实例列表
    '''
    people_info = read_xlsx(people_file)
    people_list = []
    for i in range(len(people_info)):
        daily_wage = str(people_info[i][1]).strip()
        join_date = str(people_info[i][2]).strip()
        leave_date = []
        leave_date_str = str(people_info[i][3]).strip()
        if leave_date_str != '':
            leave_date = leave_date_str.split(',')
        people_file_check(daily_wage, join_date, leave_date)
        peo = people(i, float(daily_wage), join_date, leave_date)
        people_list.append(peo)
        name = str(people_info[i][0]).strip()
        people_name.append(name)
    duplicate_people_name_check(people_name)
    print('员工合计' + str(len(people_list)) + '人')
    return people_list

def load_project_list():
    '''
    根据项目信息文件初始化项目实例列表
    '''
    project_info = read_xlsx(project_file)
    project_list = []
    for i in range(len(project_info)):
        budget = str(project_info[i][1]).strip()
        project_file_check(budget)
        pro = project(i, float(budget))
        project_list.append(pro)
        name = str(project_info[i][0]).strip()
        project_name.append(name)
    duplicate_project_name_check(project_name)
    print('项目合计' + str(len(project_list)) + '个')
    return project_list

def load_data():
    '''
    数据初始化
    '''
    return load_people_list(), load_project_list()

def save_people_result(people_list):
    '''
    输出员工信息文件
    '''
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')
    worksheet.write(0, 0, '姓名')
    worksheet.write(0, 1, '项目名称')
    worksheet.write(0, 2, '开始时间')
    worksheet.write(0, 3, '结束时间')
    row = 1
    for peo in people_list:
        peo_name = people_name[peo.name]
        for pj in peo.sch:
            pj_name = project_name[pj[0]]
            worksheet.write(row, 0, peo_name)
            worksheet.write(row, 1, pj_name)
            worksheet.write(row, 2, pj[1])
            worksheet.write(row, 3, pj[2])
            row += 1
    workbook.save(people_out_file)

def save_project_result(project_list):
    '''
    输出项目信息文件
    '''
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Sheet1')
    worksheet.write(0, 0, '项目名称')
    worksheet.write(0, 1, '项目开始时间')
    worksheet.write(0, 2, '项目结束时间')
    worksheet.write(0, 3, '项目剩余预算')
    row = 1
    for pj in project_list:
        pj_name = project_name[pj.name]
        worksheet.write(row, 0, pj_name)
        worksheet.write(row, 1, pj.bd)
        worksheet.write(row, 2, pj.ed)
        worksheet.write(row, 3, pj.lebgt)
        row += 1
    workbook.save(project_out_file)

def save_results(people_list, project_list):
    """
    保存数据
    """
    save_people_result(people_list)
    save_project_result(project_list)
