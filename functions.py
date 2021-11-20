#block warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


import pandas as pd
import numpy as np
import sys
from PANDAS import *
import csv

#All functions 

def Load_data(path):
	path = './data/' + path
	file = open(path)
	csvreader = csv.reader(file)
	data = []
	for row in csvreader:
		data.append(row)
	#data = pd.read_csv(path)
	return data


def Save_file(data, filename):
	path = './data/' + filename
	data.to_csv(path, index=False)
	print("New file is saved at: ",path)

def Missing_col(df):
	#missing_list = df.columns[df.isnull().any()]
	
	missing_list =[]
	for i in range(len(df[0])):
		for j in range(1,len(df)):
			if df[j][i] == '':
				missing_list.append(df[0][i])
				break
	print(len(missing_list))
	return missing_list

def count_missing_row(df):
	count = 0
	for i in range(1,len(df)):	
		for j in range (len(df[0])):
			if df[i][j] == '':
				count +=1
				break
	return count

def Fillna_data_mean(df):
	df1 = df.select_dtypes(np.number)
	df2 = df.select_dtypes(exclude = ['float64','int64'])
	mode = df2.mode()
	df3 = df1.fillna(df.mean())
	df4 = df2.fillna(mode.iloc[0,: ])
	new_df = [df3, df4]
	df5 = pd.concat(new_df, axis = 1)
	new_cols = list(df.columns)
	df6 = df5[new_cols]
	return df6

def Fillna_data_median(df): 
	df1 = df.select_dtypes(np.number)
	df2 = df.select_dtypes(exclude = ['float64','int64'])
	mode = df2.mode()
	df3 = df1.fillna(df.median())
	df4 = df2.fillna(mode.iloc[0,: ])
	new_df = [df3, df4]
	df5 = pd.concat(new_df, axis = 1)
	new_cols = list(df.columns)
	df6 = df5[new_cols]
	return df6

def Drop_row(df, threshold):
	data = df.dropna(how ='any', axis=0, thresh=df.shape[1]*threshold)
	return data

def Drop_col(df, threshold):
	data = df.dropna(how='any', axis=1, thresh=df.shape[0]*threshold)
	return data

def minmaxScaler(df):
	df = df.select_dtypes(np.number)
	X = df.sample(n=1,axis='columns',replace=True)
	X = X.iloc[:,0]
	df1 = []
	for i in range(len(X)):
		df1.append([(X[i] - min(X)) / (max(X) - min(X))])
	return df1

def Z_score(df):
	data_numeric = df.select_dtypes(np.number)
	X = data_numeric.sample(n=1,axis='columns',replace=True)
	X = X.iloc[:,0]
	X_for_zcore = X.to_numpy()
	z_score_formula = (X_for_zcore - np.mean(X_for_zcore, axis=0)) / np.std(X_for_zcore, axis=0)
	return z_score_formula
