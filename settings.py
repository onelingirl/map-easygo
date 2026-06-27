#! /usr/local/bin/python3
# coding: utf-8
# __author__ = "Brady Hu"
# __date__ = 2017/10/16 16:11

import os

#爬虫参数设置

# 渔网点坐标所在文件
xy_name = "data.txt"

#需要爬取的区域的四个方向点坐标
# 上海海事大学临港校区（上海市浦东新区海港大道1550号）
city_bound_point_A = [121.901, 30.879] #左上角点
city_bound_point_D = [121.901, 30.867] #左下角点
city_bound_point_B = [121.915, 30.879] #右上角点
city_bound_point_C = [121.915, 30.867] #右下角点


#下面设置文件存目录，不要设置在系统盘，不然会出现问题
#当前目录用"."表示，如"./example/"
filepath = r"./example/"
if not os.path.exists(filepath):
	os.makedirs(filepath)
filename = "example"

#爬取的间隔时间
sleeptime = 3600 #单位是秒，7200秒即为2小时
#下面这个设置每个qq号抓取的次数
fre = 80

#每次爬取方格的边长（单位：km）
edge = 2.6


#下面的参数不用设置
lng_delta = 0.01167*edge
lat_delta = 0.009*edge
#是否手动识别验证码，如需手动识别验证码，设置为True，否则设置为False，遇到验证码直接跳过
CAPTCHA_RECOGNIZ = False