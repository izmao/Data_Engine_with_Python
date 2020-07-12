#导入库

from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import request
import requests
import numpy as np
import pandas as pd
import random

#从url中获取html内容
def gethtml(url):
    html=urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='lxml')
    return soup

#根据html内容获取列表值
def valueshtml(soup):
    bodydiv = soup.find('div',class_="tslb_b")
    tr_list = bodydiv.find_all('tr')[1:]
    
    valueslist = []
    for tr in tr_list:
        td_list = tr.find_all('td')
        td_text = []
        for tds in td_list:
            td_text.append(tds.text)
        valueslist.append(td_text)
    return valueslist

#主函数
pages = 10
results = []
for i in range(pages):
    url='http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'+str(i)+'.shtml'
    soup = gethtml(url) #调用获取html内容的函数
    results = results+valueshtml(soup) # 调用获取列表值函数

df = pd.DataFrame(results,columns=['投诉编号','投诉品牌','投诉车系','投诉车型','问题简述','典型问题','投诉时间','投诉状态'])
df.to_excel('car_complain.xlsx')
