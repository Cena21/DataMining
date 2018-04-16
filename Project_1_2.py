# -*- coding: utf-8 -*-
"""
Created on 2018.4.10

@author: Huang-zh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pylab
import statsmodels.api as sm
import scipy.stats as stats

df = pd.read_csv('NFL Play by Play 2009-2017 (v4).csv', low_memory=False)
label_nominal=['GameID',
               'FieldGoalResult',
               'PlayType']
label_nums = ['PosTeamScore',
              'DefTeamScore'
              ]
df_nomi = df[label_nominal]#标称属性
df_nums = df[label_nums]#数值属性

#1.标称属性分析

def Nomi(df):
    df_nomi =df
    nominals = df_nomi.value_counts()#频数
    nominals = pd.DataFrame(nominals)
    nominals.to_csv('result_1.txt',sep=':')
    print("EOF")
    return

#------------------------------------------------------------
    #2.1数值属性分析
    nulltotal = df_nums.isnull().sum().sort_values(ascending=False)
    print('Loss:\n',nulltotal)
    print('Max:\n',df_nums.max())
    print('Min:\n',df_nums.min())
    print('Mean:\n',df_nums.mean())
    print('Median:\n',df_nums.median())
    print('Quantilty:')
    functions = ['25%', '50%', '75%']
    q_up = df_nums.quantile(0.25)
    q_mid = df_nums.quantile(0.5)
    q_down = df_nums.quantile(0.75)
    num_up = pd.DataFrame(q_up)
    num_mid = pd.DataFrame(q_mid)
    num_down = pd.DataFrame(q_down)
    four_num = pd.merge(num_up,num_mid,left_index=True,right_index=True)
    four_num = pd.merge(four_num,num_down,left_index=True,right_index=True)
    print(four_num)
    
    #2.2数据可视化
    dfPTScore = df[['PosTeamScore']]
    dfDTScore = df[['DefTeamScore']]
    #print(dfPTScore)
    dfPTScore.hist(bins = 50)
    plt.show()
    dfPTScore.boxplot()
    plt.show()
    
    dfDTScore.hist(bins = 50)
    plt.show()
    dfDTScore.boxplot()
    plt.show()
    
    #sm.qqplot(df['PosTeamScore'], line='45')
    sm.qqplot(df['DefTeamScore'], line='45')
    pylab.show()
    #stats.probplot(df['Number of Existing Stories'], dist="norm", plot=pylab)
    #pylab.show()

#2.3缺失值处理
def DataProcess(df_data,df_name):
    #原数据
    Draw(df_data)
    
    #滤除缺失数据
    df_1 = df_data.dropna()
    #print("w1")
    df_1=df_1.sort_values(by=df_name)
    #print(df_1)
    Draw(df_1)
    
    #删除取值为0的数据
    df_2 = df_data[(True^df[df_name].isin([0]))]
    df_2 = df_2.dropna()
    df_2 = df_2.sort_values(by=df_name)
    #print(df_2)
    Draw(df_2)
    
    #用均值代替缺失值
    df_3 = df_data.fillna(df_data.mode())
    #print("w3")
    df_3=df_3.sort_values(by=df_name)
    #print(df_1)
    Draw(df_3)

def Draw(df):
    #hist
    df.hist(bins = 50)
    plt.show()
    
    #q-qplot
    sm.qqplot(df,line='45')
    pylab.show()

    #box
    df.boxplot()
    plt.show()

if __name__=='__main__':
    Nomi(df['PlayType'])
    Nomi(df['GameID'])
    Nomi(df['FieldGoalResult'])

    dfPTScore = df[['PosTeamScore']]
    dfDTScore = df[['DefTeamScore']]
    
    print("Data vis:")
    Draw(dfPTScore)
    Draw(dfDTScore)
    
    DataProcess(dfPTScore,'PosTeamScore')
    DataProcess(dfDTScore,'DefTeamScore')

