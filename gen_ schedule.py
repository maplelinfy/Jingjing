
import datetime

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #每个月有多少天，如遇闰年，2月需单独考虑

class people(object):
    def __init__(self, name, daily_wage, join_date, leave_date):
        self.name = name #人员编号0, 1, 2...
        self.dw = daily_wage #日薪
        self.jd = join_date #入职日期
        self.ld = leave_date #请假日期
        self.sch = [] #日程表
        self.pro = ''
        self.pro_bd = ''
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
    black_list = ['2022-9-12', '2022-10-3', '2022-10-4', '2022-10-5', '2022-10-6', '2022-10-7'] #周一到周五但是是休息日
    white_list = ['2022-10-8', '2022-10-9'] #周六日但是是工作日
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

def cal_begin_date(people_list):
    begin_date = '9999-99-99'
    for peo in people_list:
        if peo.jd < begin_date:
            begin_date = peo.jd
    return begin_date

def assign_project(people_list, project_list, date):
    for peo in people_list:
        if peo.status == 0 and peo.jd <= date:
            min_remainder = 1e10
            min_pj = -1
            for pj in project_list:
                if pj.status == 0 and pj.lebgt >= pj.de + peo.dw:
                    rd = pj.lebgt / (pj.de + peo.dw)
                    if rd < min_remainder:
                        min_pj = pj.name
                        min_remainder = rd
            if min_pj != -1:
                peo.pro = min_pj
                peo.pro_bd = date
                peo.status = 1
                pj = project_list[min_pj]
                pj.de += peo.dw
                pj.peo.append(peo.name)
                if len(pj.peo) == 1:
                    pj.bd = date

def daily_update(people_list, project_list, date):
    for pj in project_list:
        if pj.status == 1: continue
        pj_peo = pj.peo
        de = pj.de
        for p in pj_peo:
            peo = people_list[p]
            if date in peo.ld:
                de -= peo.dw
        pj.lebgt = pj.lebgt - de
        if project_status_analysis(pj, people_list, date):
            pj.status = 1
            pj.ed = date
            for p in pj_peo:
                peo = people_list[p]
                peo.status = 0
                peo.sch.append([pj.name, peo.pro_bd, date])

def find_next_workday(date):
    while(1):
        today = datetime.datetime.strptime(date, '%Y-%m-%d')
        tomorrow = today + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        y, m, d = date_str2int(tomorrow)
        if if_workday(y, m, d):
            return tomorrow
        else:
            date = tomorrow

def project_status_analysis(pj, people_list, date):
    next_date = find_next_workday(date)
    pj_peo = pj.peo
    de = pj.de
    for p in pj_peo:
        peo = people_list[p]
        if next_date in peo.ld:
            de -= peo.dw
    if de > pj.lebgt:
        return 1
    else:
        return 0

def if_close(project_list):
    for pro in project_list:
        if pro.status == 0:
            return 0
    return 1

def workflow(people_list, project_list, date):
    assign_project(people_list, project_list, date)
    daily_update(people_list, project_list, date)
    return if_close(project_list)

def date_int2str(y, m, d):
    sy = str(y)
    sm = str(m)
    if m < 10:
        sm = '0' + sm
    sd = str(d)
    if d < 10:
        sd = '0' + sd
    return '-'.join([sy, sm, sd])

def date_str2int(date):
    y, m, d = date.split('-')
    return int(y), int(m), int(d)

def work(people_list, project_list):
    begin_date = cal_begin_date(people_list)
    by, bm, bd = date_str2int(begin_date)
    for d in range(bd, month_day[bm - 1] + 1):  # 本年度本月剩余日的
        if if_workday(by, bm, d):
            date = date_int2str(by, bm, d)
            label = workflow(people_list, project_list, date)
            if label:
                return
    for m in range(bm + 1, 13):  # 本年度下个月以后的
        for d in range(1, month_day[m - 1] + 1):
            if if_workday(by, m, d):
                date = date_int2str(by, m, d)
                label = workflow(people_list, project_list, date)
                if label:
                    return
    for y in range(by + 1, 2024):  # 下一年以后的
        for m in range(1, 13):
            for d in range(1, month_day[m - 1] + 1):
                if if_workday(y, m, d):
                    date = date_int2str(y, m, d)
                    label = workflow(people_list, project_list, date)
                    if label:
                        return


def begin():
    people_list = []
    project_list = []
    peo0 = people(0, 200, '2022-03-01', [])
    peo1 = people(1, 300, '2022-03-01', [])
    peo2 = people(2, 500, '2022-03-01', [])
    proj0 = project(0, 3400)
    proj1 = project(1, 4700)
    proj2 = project(2, 2000)
    people_list = [peo0, peo1, peo2]
    project_list = [proj0, proj1, proj2]
    work(people_list, project_list)
    print(peo0.sch)
    print(peo1.sch)
    print(peo2.sch)
    print(proj0.lebgt, proj0.de)
    print(proj1.lebgt, proj1.de)
    print(proj2.lebgt, proj2.de)

begin()
