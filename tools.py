
import datetime
from read_file import load_black_list, load_white_list

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #每个月有多少天，如遇闰年，2月需单独考虑

class people(object):
    def __init__(self, name, daily_wage, join_date, leave_date):
        self.name = name #人员编号0, 1, 2...
        self.dw = daily_wage #日薪
        self.jd = join_date #入职日期
        self.ld = leave_date #请假日期
        self.sch = [] #日程表
        self.pro = '' #当前所在项目
        self.pro_bd = '' #进入当前项目的日期
        self.status = 0 #状态：0表示空闲，1表示项目中

class project(object):
    def __init__(self, name, budget):
        self.name = name #项目编号0, 1, 2...
        self.bgt = budget #预算
        self.lebgt = budget #剩余预算
        self.de = 0 #日总支出
        self.peo = []  # 项目人员
        self.bd = '' #项目开始日期
        self.ed = '' #项目结束日期
        self.status = 0 #项目状态：0表示未完成，1表示已完成

def if_workday(y, m, d):
    """
    根据日期判断是否为工作日（暂时仅适用于中国大陆2022年，如需之前年份或次年后年份，需更新black_list和white_list）
    :param y: 年
    :param m: 月
    :param d: 日
    :return: 1：工作日；0：休息日
    """
    # black_list = ['2022-9-12', '2022-10-3', '2022-10-4', '2022-10-5', '2022-10-6', '2022-10-7'] #周一到周五但是是休息日
    # white_list = ['2022-10-8', '2022-10-9'] #周六日但是是工作日
    black_list = load_black_list()
    white_list = load_white_list()
    today = '-'.join([str(y), str(m), str(d)])
    if today in black_list:
        return 0
    if today in white_list:
        return 1
    wk = datetime.date(y, m, d).weekday() #计算星期几，0-4表示工作日，5和6表示周六日
    if wk < 5:
        return 1
    else:
        return 0

def find_next_workday(date):
    """
    计算下一个工作日
    """
    while(1):
        today = datetime.datetime.strptime(date, '%Y-%m-%d')
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        y, m, d = date_str2int(tomorrow)
        if if_workday(y, m, d):
            return tomorrow
        else:
            date = tomorrow

def date_int2str(y, m, d):
    '''
    将int类日期转换为str型，例如date_int2str(2022, 1, 2)返回为'2022-01-02'
    '''
    sy = str(y)
    sm = str(m)
    if m < 10:
        sm = '0' + sm
    sd = str(d)
    if d < 10:
        sd = '0' + sd
    return '-'.join([sy, sm, sd])

def date_str2int(date):
    '''
    将str类日期转换为int，例如date_str2int('2022-01-02')返回为2022, 1, 2
    '''
    y, m, d = date.split('-')
    return int(y), int(m), int(d)