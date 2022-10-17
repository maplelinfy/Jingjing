
'''
注：字符串日期格式统一为'YYYY-MM-DD'
'''

from tools import if_workday, find_next_workday, date_int2str, date_str2int
from tools import month_day
from read_file import load_project_list, load_people_list


def cal_begin_date(people_list):
    '''
    根据所有人的最早入职时间确定开始日期
    '''
    begin_date = '9999-99-99'
    for peo in people_list:
        if peo.jd < begin_date:
            begin_date = peo.jd
    return begin_date

def assign_project(people_list, project_list, date):
    '''
    每天开始前，遍历所有员工，如果该员工当前闲置并且已经入职，则循环所有项目，并计算该员工加入后“项目剩余预算%单日总支出”，将该员工放入该值最小的项目中
    '''
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
    '''
    每天结束后，遍历所有项目，首先计算该项目的剩余预算，并且根据剩余预算预估今日是否为项目最后一天。
    '''
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

def project_status_analysis(pj, people_list, date):
    '''
    判断今天是否为项目最后一天，1表示是，0表示否
    '''
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
    '''
    每天结束后检查所有项目是否均已结束，1表示均已结束，0表示还没都结束
    '''
    for pro in project_list:
        if pro.status == 0:
            return 0
    return 1

def workflow(people_list, project_list, date):
    """
    每日工作流，分为每天开始前assign_project以及每天结束后daily_update
    """
    assign_project(people_list, project_list, date)
    daily_update(people_list, project_list, date)
    return if_close(project_list)

def work(people_list, project_list):
    '''
    根据计算的开始日期，循环遍历所有日期来执行工作流
    :param people_list: 员工列表，元素为people实例
    :param project_list: 项目列表，元素为project实例
    :return:
    '''
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
    people_list = load_people_list()
    project_list = load_project_list()
    work(people_list, project_list)