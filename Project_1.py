# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:47:19 2018

2nd
@author: Huang-zh
"""
import numpy as np
from collections import Counter 
import csv
from matplotlib import pyplot as plt
import scipy.stats as stats
import pandas as pd
#from geneview.gwas import qqplot

with open('Building_Permits.csv','r') as csvfile:
	reader = [each for each in csv.DictReader(csvfile)]#将读取内容转存到列表

#-------- 数据集 2 ------------------------------------------------

	PerNum = [row['Permit Number'] for row in reader]
	PerType = [row['Permit Type'] for row in reader]
	PerTypeDef = [row['Permit Type Definition'] for row in reader]
	SName = [row['Street Name'] for row in reader]
	CurStatus = [row['Current Status'] for row in reader]
	NumExiStos = [row['Number of Existing Stories'] for row in reader]
	ExistUse = [row['Existing Use'] for row in reader]
	PropUse = [row['Proposed Use'] for row in reader]
	SuperDist = [row['Supervisor District'] for row in reader]
	Neighborhoods = [row['Neighborhoods - Analysis Boundaries'] for row in reader]
	Zipcode = [row['Zipcode'] for row in reader]
	Location = [row['Location'] for row in reader]
	ReID = [row['Record ID'] for row in reader]
#--------------------------------------------------------
	EsitCost = [row['Estimated Cost'] for row in reader if row['Estimated Cost']!='']
	RevCost = [row['Revised Cost'] for row in reader if row['Revised Cost']!='']
	PropUnits = [row['Proposed Units'] for row in reader if row['Proposed Units']!='']

#统计各个标称属性元素的个数
def CountNum(args):   
	argset = set(args)
	#for item in argset:
	#    print("%s has %d "%(item,args.count(item)))
	with open('result_2.txt',"a") as f:
		f.write("\n------------------------------------------")
		for item in argset:
			f.write("%s has %d \n"%(item,args.count(item)))
		f.write("--------------------------------------------")
	print('\n////////////////')
	return
	

    #way3 把属性封装成list?? 结合函数来处理？？
#2.对数值属性进行分析
def NumAnalysis(nums,title):
	#nums = [item for item in nums if item!='']#去掉缺失值，当list中有空白值的时候，无法进行类型转化
	#drawHist(nums,title)
	
	numsLen = len(nums)#int 取去掉缺失值后的数据再处理
	nums = [float(item) for item in nums]#用int类型转换报错：ValueError: invalid literal for int() with base 10: '4337.22'
	minNum = min(nums)
	maxNum = max(nums)
	mean = np.mean(nums)
	print("最小值:",minNum,"最大值:",maxNum,"均值：",mean)
	median = get_median(nums,numsLen)
	print("中位数：",median,"缺失值个数：",(198901-numsLen),"\n")
	#typ = type(minNum)
	#print(typ)
def get_median(data,lenght):
	data.sort()
	half = lenght//2
	quant1 = lenght//4
	quant3 = lenght //4 * 3
	print("上四分位数为：",data[quant1],"下四分位数为：",data[quant3])
	return (data[half] + data[~half]) / 2
	
#3.数值属性可视化
#绘制直方图
def drawHist(data,title):
	plt.hist(data,100)
	plt.xlabel("Numbers")
	plt.ylabel('Frequency')
	plt.title(title)
	plt.show()

#缺失值填充
def fillNum(data1,data2):
	data = data1
	for i in range(len(data1)):
		if data[i] ==' ':
			data[i] = data2[i]
	return data

if __name__ == '__main__':
	#---------------------- 标称属性 ------------------------------
	#print("\nPermit Type:")
	CountNum(PerType)
    
	#print("\nPermit Type Definition:")
	CountNum(PerTypeDef)
    
	#print("\nStreet Name:")
	CountNum(SName)
    
	#print("\nCurrent Status:")
	CountNum(PerType)
    
	#print("\nNumber of Existing Stories:")
	CountNum(NumExiStos)
    
	#print("\nExisting Use:")
	CountNum(ExistUse)
    
	#print("\nProposed Use :")
	CountNum(PropUse)
    
	#print("\nSupervisor District:")
	CountNum(SuperDist)
    
	#print("\nNeighborhoods-AB:")
	CountNum(Neighborhoods)
    
	#print("\nZipcode:")
	CountNum(Zipcode)
    
	#print("\nLocation:")
	CountNum(Location)
    
	#print("\n:Record ID")
	CountNum(ReID)
	#------------------- 数值属性 --------------------------------
	print("Estimated Cost")
	NumAnalysis(EsitCost,"Estimated Cost")
	drawHist(EsitCost,"Estimated Cost")
	
	print("Revised Cost:")
	NumAnalysis(RevCost,"Revised Cost")
	drawHist(RevCost,"Revised Cost")
	
	print("Proposed Units:")
	NumAnalysis(PropUnits,"Proposed Units") 

	fill_RecCost=fillNum(RevCost,EsitCost)
	print("Revised Cost_相关关系:")
	drawHist(fill_RecCost,"Revised Cost_fill")
	
	