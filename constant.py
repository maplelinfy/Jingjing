
import os

input_folder = './inputFiles'
black_list_file = os.path.join(input_folder, 'blackList.txt')
white_list_file = os.path.join(input_folder, 'whiteList.txt')
project_file = os.path.join(input_folder, 'project.xlsx')
people_file = os.path.join(input_folder, 'people.xlsx')

output_folder = './outputFiles'
project_out_file = os.path.join(output_folder, 'project_out.xlsx')
people_out_file = os.path.join(output_folder, 'people_out.xlsx')

MAX_DAYS = 3650 # 循环的最大天数，可根据实际情况调整
