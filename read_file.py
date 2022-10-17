
'''
输入文件说明：
blackList.txt: 周一到周五但是是休息日的日期列表
whiteList.txt: 周六日但是是工作日的日期列表
project.xlsx: 项目列表，分为2列：项目名称,项目总预算
people.xlsx: 员工列表，分为4列：姓名,日薪,入职日期,休假日期(用英文逗号做分割，例如2022-01-03,2022-03-04)
所有文件统一放入文件夹inputFiles，project.xlsx和people.xlsx信息请放在Sheet1页
'''

import xlrd
import os

from tools import people, project

input_folder = './inputFiles'
black_list_file = os.path.join(input_folder, 'blackList.txt')
white_list_file = os.path.join(input_folder, 'whiteList.txt')
project_file = os.path.join(input_folder, 'project.xlsx')
people_file = os.path.join(input_folder, 'people.xlsx')

def load_list(list_file):
    res = []
    with open(list_file) as f:
        for line in f:
            res.append(line.strip())
    return res

def load_black_list():
    return load_list(black_list_file)

def load_white_list():
    return load_list(white_list_file)

def read_xlsx(xlsx_file):
    res = []
    wb = xlrd.open_workbook(xlsx_file)
    sh = wb.sheet_by_name('Sheet1')
    for i in range(0, sh.nrows):
        ll = sh.row_values(i)
        res.append(ll)
    return res

def load_project_list():
    project_info = read_xlsx(project_file)
    project_list = []
    for i in range(len(project_info)):
        pro = project(i, project_info[i][1])
        project_list.append(pro)
    return project_list

def load_people_list():
    people_info = read_xlsx(people_file)
    people_list = []
    for i in range(len(people_info)):
        leave_date = people_info[i][3].split(',')
        peo = people(i, people_info[i][1], people_info[i][2], leave_date)
        people_list.append(peo)
    return people_list
