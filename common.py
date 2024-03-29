
class people(object):
    # 员工类
    def __init__(self, name, daily_wage, join_date, leave_date):
        self.name = name #人员编号0, 1, 2...
        self.dw = daily_wage #日薪
        self.jd = join_date #入职日期
        self.ld = leave_date #请假日期列表
        self.sch = [] #日程表列表，元素为[项目编号，加入日期，结束日期]
        self.pj = '' #当前所在项目
        self.pj_bd = '' #进入当前项目的日期
        self.status = 0 #状态：0表示空闲，1表示项目中

class project(object):
    # 项目类
    def __init__(self, name, budget):
        self.name = name #项目编号0, 1, 2...
        self.bgt = budget #预算
        self.lebgt = budget #剩余预算
        self.de = 0 #日总支出
        self.peo = []  #项目人员编号列表，存people.name
        self.bd = '' #项目开始日期
        self.ed = '' #项目结束日期
        self.status = 0 #项目状态：0表示未完成，1表示已完成
