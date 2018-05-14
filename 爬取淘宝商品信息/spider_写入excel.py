# _*_ coding:utf-8 _*_
# Author:liu
import requests
import re
import json
import urllib
import xlsxwriter
import os

'''
    获取淘宝商品信息
'''


def write_data():
    # 删除文件
    if os.path.exists('taobaoinfo.xlsx'):
        os.remove('taobaoinfo.xlsx')

    # 创建工作文件
    workbooke = xlsxwriter.Workbook('taobaoinfo.xlsx')
    # 创建工作表
    worksheet = workbooke.add_worksheet()
    # 写标题
    worksheet.write(0, 0, '标题')
    worksheet.write(0, 1, '标价')
    worksheet.write(0, 2, '购买人数')
    worksheet.write(0, 3, '是否包邮')
    worksheet.write(0, 4, '是否天猫')
    worksheet.write(0, 5, '地区')
    worksheet.write(0, 6, '店名')
    worksheet.write(0, 7, '链接')

    return workbooke, worksheet


def main():
    show_info = input("请输入要查询的商品名称：")
    num = int(input("请输入要获取的页数:"))
    show_info = urllib.request.quote(show_info)

    # 创建工作表
    workbooke, worksheet = write_data()

    n = 0

    # 循环页数
    for page in range(num):

        # 拼装地址
        url = "https://s.taobao.com/search?q={}&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180409&ie=utf8&bcoffset={}&ntoffset={}&p4ppushleft=1%2C48&s={}".format(
            show_info, str(6 - (page * 3)), str(6 - (page * 3)), str(page * 44))

        # 发送http请求
        response = requests.get(url)
        # 得到网页源码
        response.encoding = 'utf-8'
        html = response.text
        # print(html)
        # 正则匹配出数据
        content = re.findall(r'g_page_config = (.*?)g_srp_loadCss', html, re.S)[0].strip()[:-1]
        # print(content)
        # 格式化json
        content = json.loads(content)
        # 获取商品信息列表
        data_list = content['mods']['itemlist']['data']['auctions']
        # print(data_list, len(data_list))




if __name__ == '__main__':
    main()
