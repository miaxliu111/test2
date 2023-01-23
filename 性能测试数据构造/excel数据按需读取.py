# -*- codeing = utf-8 -*-
# @Time : 2023/1/11 6:21 下午
# @Author : xue
# @File : excel数据按需读取.py
# @Software: PyCharm


import os
import pandas as pd
from openpyxl import load_workbook


#获取excel表格数据并保存到其他文件中
path = r',,,,/xx'
nnewfile = path + '/' + 'huizong.xlsx'

# for name in filename:
#     with open (path + '/' + name , 'r' ,encoding='UTF-8') as file:
#         for data in file.readlines():
#             if data.split('[')[0] == 'DEBUG:CurrentTime=':
#                 curtime.append(data.split('[')[1].split(']')[0])
# writer = pd.ExcelWriter(newfile)
# df1 = pd.DataFrame({'msgid':msgid,'curtime':curtime})
# df1.to_excel(writer,sheet_name='dataforlog',index=0)
# writer.save()
# writer.close()

datafilename = os.listdir(path)
for datafilenamep in datafilename:
    database = pd.read_excel(path + '/' + datddatafilenamep ,converters={'msgid':str})
    database_msgid.extend(database['msgid'].values)

book = load_workbook(newfile)
writer = pd.ExcelWriter(newfile ,engine='openpyxl')
writer.book = book
df2 = pd.DataFrame({'DDD':XX , 'FFF':XXX})
df2.to_excel(writer,sheet_name='datdafor',index=0)
writer.save()
writer.close()