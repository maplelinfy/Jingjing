
from read_file import load_data, save_results
from tools import find_next_workday
from constant import MAX_DAYS


def cal_begin_date(people_list):
    '''
    根据所有人的最早入职时间确定开始日期
    '''
    begin_date = '9999-99-99'
    for peo in people_list:
        if peo.jd < begin_date:
            begin_date = peo.jd
    return begin_date

def cal_daily_expense(de, pj_peo, people_list, date):
    '''
    计算项目在某天的日支出，需要扣除当年休假员工的日薪
    '''
    for p in pj_peo:
        peo = people_list[p]
        if date in peo.ld:
            de -= peo.dw
    return de

def if_project_final_day(pj, people_list, date):
    '''
    判断今天是否为项目最后一天，1表示是，0表示否。通过估计明天总花销与剩余总预算做对比进行判断。
    '''
    next_date = find_next_workday(date)
    pj_peo = pj.peo
    de = pj.de
    de = cal_daily_expense(de, pj_peo, people_list, next_date)
    if de > pj.lebgt:
        return 1
    else:
        return 0

def assign_project(people_list, project_list, date):
    '''
    每天开始前，遍历所有员工，如果该员工当前已经入职并且闲置，则循环所有未完成的项目，并计算该员工加入后“项目剩余预算%单日总支出”，将该员工放入到该值最小的项目中
    '''
    for peo in people_list:
        if peo.status == 0 and peo.jd <= date:
            min_remainder = 1e10
            min_pj = -1
            for pj in project_list:
                if pj.status == 0 and pj.lebgt >= pj.de + peo.dw:
                    rd = pj.lebgt % (pj.de + peo.dw)
                    if rd < min_remainder:
                        min_pj = pj.name
                        min_remainder = rd
            if min_pj != -1: #等于-1表示所有项目均不需要新人
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
    每天结束后，遍历所有项目，首先计算该项目的剩余预算，并且根据剩余预算预估今日是否为项目最后一天，如是最后一天，则做关闭该项目，并释放所有员工
    '''
    for pj in project_list:
        if pj.status == 1: continue
        pj_peo = pj.peo
        de = pj.de #今日总花销初始值
        de = cal_daily_expense(de, pj_peo, people_list, date)
        pj.lebgt = pj.lebgt - de
        if if_project_final_day(pj, people_list, date):
            pj.status = 1
            pj.ed = date
            for p in pj_peo:
                peo = people_list[p]
                peo.status = 0
                peo.sch.append([pj.name, peo.pro_bd, date])

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
    date = begin_date
    for _ in range(MAX_DAYS):
        label = workflow(people_list, project_list, date)
        if label:
            return
        else:
            date = find_next_workday(date)

def begin():
    '''
    读数据、处理、写结果。
    '''
    people_list, project_list = load_data()
    work(people_list, project_list)
    save_results(people_list, project_list)
