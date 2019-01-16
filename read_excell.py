# --*-- coding:utf-8 --*--

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


host_path = '/home/ys/桌面/数据/软件开发部-测试店铺账号.xlsx'
web_path = 'https://oa.yuetaosem.com:85/FinancialStatements/1544773114.xlsx'

# 本地读取
data = pd.read_excel(host_path,sheetname ='Sheet1')  

# 网络读取
data = pd.read_excel(web_path,sheetname ='代运营项目管理表')  


def data2pic(url):

	""" 
		1.数据获取
		2.数据处理，提取
		3.数据统计
		4.数据可视化
	""" 

	# 读取数据
	data = pd.read_excel(url,sheetname ='代运营项目管理表')

	# 数据处理
	take_data = (data[['项目类型','续费月']]) # 数据提取

	replace_data = take_data.replace('-','0000-00-00') # 数据填补

	# 数据统计,计数统计
	item_type_count = replace_data['项目类型'].value_counts()
	renewal_month_count = replace_data['续费月'].value_counts()

	# 数据可视化
	x1 = list(renewal_month_count.values)
	tag1 = list(renewal_month_count.index)
	x2 = list(item_type_count.values)
	tag2 = list(item_type_count.index)

	plt.figure(1)
	ax1 = plt.subplot(2,2,1)
	ax2 = plt.subplot(2,2,2)

	plt.sca(ax1)
	plt.bar(range(len(x1)), x1)
	plt.sca(ax2)
	plt.bar(range(len(x2)), x2)
	plt.show()
	

if __name__ == "__main__":


	url = 'https://oa.yuetaosem.com:85/FinancialStatements/1544773114.xlsx'
	data2pic(url)
	
