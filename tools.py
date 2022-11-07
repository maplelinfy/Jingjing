
import datetime

from read_file import load_black_white_list


black_list, white_list = load_black_white_list()

def if_workday(date):
    """
    根据日期判断是否为工作日（需定期根据法定节假日更新black_list和white_list文件）
    :param date: 日期
    :return: 1：工作日；0：休息日
    """
    if date in black_list:
        return 0
    if date in white_list:
        return 1
    y, m, d = date_str2int(date)
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
        if if_workday(tomorrow):
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
