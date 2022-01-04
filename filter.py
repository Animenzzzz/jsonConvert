#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf-8 -*-
import json
import csv
from os import write

# 数据源 /Users/mac/Desktop/yyyy.json
# 输出的数据 /Users/mac/Desktop/res.csv


with open("/Users/mac/Desktop/yyyy.json",mode='r',encoding='utf-8') as input_file:
    input_dict = json.load(input_file)


pageStats = input_dict['data']['pageStats']
monthStats = input_dict['data']['monthStats']

rr = {'pageExpenses':[]}

for item in pageStats:
    for item2 in item['pageExpenses']:
        for item3 in item2['expenses']:
            d = item3['cts']
            t = item3['cost']
            c = item3['categoryName']
            if 'remark' in item3:
                r = item3['remark']
            else:
                r = ''
            tile = {
                        '时间':d,
                        '金额':t,
                        '分类':c,
                        '备注':r,
                        '类型':'支出'
                    }
            rr['pageExpenses'].append(tile)

output_json = json.dumps(rr, ensure_ascii=False)

data_file = open('/Users/mac/Desktop/res.csv', 'w')
csv_writer = csv.writer(data_file)

count = 0
 
for emp in rr['pageExpenses']:
    if count == 0:
        header = emp.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(emp.values())
 
data_file.close()
