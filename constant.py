
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

import os

input_folder = './inputFiles'
black_list_file = os.path.join(input_folder, 'blackList.txt')
white_list_file = os.path.join(input_folder, 'whiteList.txt')
project_file = os.path.join(input_folder, 'project.xlsx')
people_file = os.path.join(input_folder, 'people.xlsx')

output_folder = './outputFiles'
project_out_file = os.path.join(output_folder, 'project_out.xlsx')
people_out_file = os.path.join(output_folder, 'people_out.xlsx')

MAX_DAYS = 2000 # 循环的最大天数，建议保持不变
