
问题描述：

![image](https://github.com/maplelinfy/Jingjing/blob/master/%E9%97%AE%E9%A2%98%E6%8F%8F%E8%BF%B0.jpg)

解决步骤

1、以所有人最早的开始日期为起始日期对每一个工作日进行循环

2、每天开始时，查看哪些人目前处于闲置状态，对所有闲置状态的人进行循环，对每个闲置状态的人，判断分别放入到所有项目中，计算“项目剩余预算%单日总支出”取最小的放入

3、每天结束时，计算每个项目的剩余预算，并预估剩余预算能否支撑次日，如不能，则该项目于本日结束，将所有人的状态改为闲置

4、每天结束后，判断是否所有项目均已完结，如完结，则退出
