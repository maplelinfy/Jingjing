
### 问题描述

![问题描述](https://github.com/maplelinfy/Jingjing/blob/master/%E9%97%AE%E9%A2%98%E6%8F%8F%E8%BF%B0.jpg)

### 解决步骤

1、以所有人最早的开始日期为起始日期对后续每一个工作日进行循环

2、对每个工作日，分为每天开始时和每天结束时：

1> 每天开始时，查看哪些已入职的员工目前处于闲置状态，对每个满足条件的员工，分别放入到所有项目中，计算“项目剩余预算%单日总支出”，取余数最小的项目加入

2> 每天结束时，计算每个未完成项目的剩余预算，并预估剩余预算能否支撑到下个工作日，如不能，则该项目于本日结束，将所有参与该项目的员工状态改为闲置

3> 每天结束后，判断是否所有项目均已完结，如完结，则退出

### 文件说明

_gen_schedule.py_ ：主流程

_tools.py_ ：工具类

_read_file.py_ ：读写文件函数，可修改文件名称

_inputFiles_ ：输入文件放置文件夹，需按指定格式自行配置

_outputFiles_ ：输出文件文件夹，存放所有输出文件

-requirements.txt_ ：所需python包

### 操作流程

#### 输入文件说明：

blackList.txt: 周一到周五但是是休息日的日期列表

whiteList.txt: 周六日但是是工作日的日期列表

project.xlsx: 项目列表，分为2列：项目名称,项目总预算

people.xlsx: 员工列表，分为4列：姓名,日薪,入职日期,休假日期(用英文逗号做分割，例如2022-01-03,2022-03-04)

所有文件统一放入文件夹inputFiles，project.xlsx和people.xlsx信息请放在Sheet1页

#### 运行步骤：

以下两种方式任选其一即可

1、python

        git clone https://github.com/maplelinfy/Jingjing.git

        cd Jingjing

        pip install -r requirements.txt

        python gen_schedule.py

2、jupyter notebook
