
'''
输入文件说明：
blackList.txt: 周一到周五但是是休息日的日期列表
whiteList.txt: 周六日但是是工作日的日期列表
project.xlsx: 项目列表，分为2列：项目名称,项目总预算
people.xlsx: 员工列表，分为4列：姓名,日薪,入职日期,休假日期(用英文逗号做分割，例如2022-01-03,2022-03-04)
（可参考实例文件project_eg.xlsx和people_eg.xlsx）
注意：
1、所有文件均无表头！！！第一行即为真实数据
2、所有文件统一放入文件夹inputFiles
3、project.xlsx和people.xlsx信息请放在Sheet1页！！！

输出文件说明：
project_out.xlsx：项目信息输出，分为4列：项目名称，项目开始时间，项目结束时间，项目剩余预算
people_out.xlsx：员工排期输出：分为4列：姓名，所在项目，进入时间，退出时间
（可参考实例文件project_out_eg.xlsx和people_out_eg.xlsx）
所有输出文件统一放入文件夹outputFiles
'''

import xlrd
import xlwt
import os

from common import people, project

input_folder = './inputFiles'
black_list_file = os.path.join(input_folder, 'blackList.txt')
white_list_file = os.path.join(input_folder, 'whiteList.txt')
project_file = os.path.join(input_folder, 'project.xlsx')
people_file = os.path.join(input_folder, 'people.xlsx')

output_folder = './outputFiles'
project_out_file = os.path.join(output_folder, 'project_out.xlsx')
people_out_file = os.path.join(output_folder, 'people_out.xlsx')

people_name = [] #存员工姓名
project_name = [] #存项目名称

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
