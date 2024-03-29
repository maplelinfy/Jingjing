
# _Just For You_

### 状态

* 开发已完成，流程已跑通，结果准确性测试验证中

* 2022-11-03新增输入文件数据格式检测

### 问题描述

![问题描述](https://github.com/maplelinfy/Jingjing/blob/master/doc/%E9%97%AE%E9%A2%98%E6%8F%8F%E8%BF%B0.jpg)

### 解决步骤

1、以所有员工最早的入职日期为起始日期对后续每一个工作日进行遍历

2、对每个工作日，分为每天开始时和每天结束时：

（1）每天开始时，查看哪些已入职的员工目前处于闲置状态，对每个闲置的员工，分别在所有未完成项目中，计算“项目剩余预算%单日总支出”，取余数最小的项目加入

（2）每天结束时，计算每个未完成项目的剩余预算，并预估剩余预算能否支撑到下个工作日，如不能，则该项目于本日结束，将所有参与该项目的员工状态改为闲置。最后，判断是否所有项目均已完结，如完结，则结束

### 文件说明

* _run.ipynb_ ：juypter执行文件

* _run.py_ ：执行文件

* _schedule.py_ ：工作流函数

* _tools.py_ ：时间工具函数

* _read_file.py_ ：读写文件函数

* _common.py_ ：员工/项目类定义

* _constant.py_ ：参数文件，可自行配置文件输入输出名

* _data_check.py_ ：输入文件数据格式检测函数

* _requirements.txt_ ：所需python包

* _inputFiles_ ：输入文件放置文件夹，需按指定格式自行配置，详见输入文件说明

* _outputFiles_ ：输出文件文件夹，存放所有输出文件，详见输出文件说明

* _doc_ ：文档目录，包括问题描述、离线操作手册

### 操作流程

#### 输入文件说明：

* _blackList.txt_ : 周一到周五但是是休息日的日期列表，需根据国家法定节假日定期更新，单列，详见示例文件 _./inputFiles/blackList.txt_

* _whiteList.txt_ : 周六周日但是是工作日的日期列表，需根据国家法定节假日定期更新，单列，详见示例文件 _./inputFiles/whiteList.txt_

* _people.xlsx_ : 员工列表，分为4列：{姓名,日薪,入职日期,休假日期}，详见示例文件 _./inputFiles/people_eg.xlsx_

* _project.xlsx_ : 项目列表，分为2列：{项目名称,项目总预算}，详见示例文件 _./inputFiles/project_eg.xlsx_

说明：

1、通常情况我们可以通过周几来判断是否是工作日，但当遇到某些国家法定节假日时可能会做出某些调整，导致某些周一至周五变为休息日，亦或某些周六周日变为工作日，因而需要将这些特例做单独处理

2、所有文件均无表头，第一行即为真实数据！

3、_people.xlsx_ 和 _project.xlsx_ 信息请放在“Sheet1”页！

4、_people.xlsx_ 和 _project.xlsx_ 两个文件中，除休假日期，其余均不可为空！

5、字符串日期格式统一为 _YYYY-MM-DD_，例如 _2022-10-08_

6、休假日期用英文逗号做分割，例如2022-01-03,2022-03-04，没有可置空

7、所有文件统一放入文件夹 _inputFiles_

8、如需修改相关文件名，可在 _constant.py_ 中进行修改

9、程序已加入对输入文件中数据的验证提示功能，包括员工重名检测、项目名称重名检测、日薪格式检测、项目预算格式检测、入职日期格式检测、休假日期格式检测。仅做提示，不会做修正或中断程序。可能导致错误如下：

（1）员工姓名和项目名称请确保没有重名，否则结果会出现混淆

（2）金额类数据格式错误会导致程序报错中断

（3）日期类格式错误（2000年以前、2030年以后的日期均会提示）可能会导致结果错误，也可能导致程序报错中断

10、当前仅测试xlsx文件可用，xls和csv格式暂未测试

#### 输出文件说明：

* _people_out.xlsx_ ：员工排期输出：分为4列：{姓名，所在项目名称，进入项目时间，退出项目时间}，详见示例文件 _./outputFiles/people_out_eg.xlsx_

* _project_out.xlsx_ ：项目信息输出，分为4列：{项目名称，项目开始时间，项目结束时间，项目剩余预算}，详见示例文件 _./outputFiles/project_out_eg.xlsx_

说明：

1、所有输出文件统一放入文件夹 _outputFiles_

2、如需修改相关文件名，可在 _constant.py_ 中进行修改

#### 运行步骤：

以下两种方式任选其一即可，推荐python版本为3.6/3.7/3.8

1、python

安装python和git

        win+R输入cmd，弹出命令行窗口（mac打开“终端”即可）

        进入到一个保存代码的目录

        git clone https://github.com/maplelinfy/Jingjing.git

        cd Jingjing

        pip install -r requirements.txt（可先pip list查看需要的包是否存在，请保证版本一致，xlrd2.0版本不可用。如下载速度过慢，可在命令后加参数-i https://pypi.tuna.tsinghua.edu.cn/simple）

        python run.py

2、jupyter notebook

安装anaconda和git

        win+R输入cmd，弹出命令行窗口（mac打开“终端”即可）

        进入到一个保存代码的目录（最好放C盘，其他盘需先切换目录）

        git clone https://github.com/maplelinfy/Jingjing.git

        下载完成后，输入 jupyter notebook，回车，会自动弹出网页窗口显示目录

        点击进入到刚才下载下来的Jingjing文件夹

        点击进入 run.ipynb

        点击代码块至可编辑状态，ctrl+enter执行代码

#### 离线版如何使用：

详见离线操作手册

![离线操作手册](https://github.com/maplelinfy/Jingjing/blob/master/doc/%E7%A6%BB%E7%BA%BF%E6%93%8D%E4%BD%9C%E6%89%8B%E5%86%8C.docx)

### TODO

1、细化输出文件展示内容
