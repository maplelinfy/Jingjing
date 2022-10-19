
import xlrd
import xlwt

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
            res.append(line.strip())
    return res

def load_black_list():
    '''
    读取黑名单列表
    '''
    return load_list(black_list_file)

def load_white_list():
    '''
    读取白名单列表
    '''
    return load_list(white_list_file)

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

def load_project_list():
    '''
    根据项目信息文件初始化项目实例列表
    '''
    project_info = read_xlsx(project_file)
    project_list = []
    for i in range(len(project_info)):
        pro = project(i, float(project_info[i][1]))
        project_list.append(pro)
        project_name.append(project_info[i][0])
    print('项目合计' + str(len(project_list)) + '个')
    return project_list

def load_people_list():
    '''
    根据员工信息文件初始化员工实例列表
    '''
    people_info = read_xlsx(people_file)
    people_list = []
    for i in range(len(people_info)):
        leave_date = people_info[i][3].split(',')
        peo = people(i, float(people_info[i][1]), people_info[i][2], leave_date)
        people_list.append(peo)
        people_name.append(people_info[i][0])
    print('员工合计' + str(len(people_list)) + '人')
    return people_list

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
